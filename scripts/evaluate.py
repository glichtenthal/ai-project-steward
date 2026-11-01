#!/usr/bin/env python3
"""Validate AI Project Steward evaluations and prepare transparent result reports."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
EVALS_PATH = ROOT / "evals" / "evals.json"
COMPOSITION_PATH = ROOT / "evals" / "composition.json"
ALLOWED_RESULTS = {"pass", "fail", "not_run", "not_applicable"}
CONTRACT_FIELDS = ("harness", "tools", "permissions", "fixtures_sha256",
                   "prompts_sha256", "criteria_sha256")


def suite_cases(kind: str) -> list[dict]:
    return load_json(EVALS_PATH)["evals"] if kind == "behavioral" else load_json(COMPOSITION_PATH)["cases"]


def comparison_template(kind: str) -> dict:
    cases = suite_cases(kind)
    def fingerprint(fields):
        return hashlib.sha256(json.dumps([{k: c[k] for k in fields} for c in cases], sort_keys=True).encode()).hexdigest()
    return {"harness": "", "tools": "", "permissions": "", "fixtures_sha256": "",
            "prompts_sha256": fingerprint(("id", "prompt") if kind == "behavioral" else ("id", "turns")),
            "criteria_sha256": fingerprint(("id", "assertions", "routing_expected") if kind == "behavioral" else ("id", "assertions", "dimension"))}


def assertion_template(case: dict) -> list[dict]:
    return [{"assertion": a, "result": "not_run", "notes": ""} for a in case["assertions"]]


def has_review(case: dict, keys: tuple) -> bool:
    assertions = case.get("assertion_results")
    if not isinstance(assertions, list):
        assertions = []
    return any(case.get(k) in ("pass", "fail") for k in keys) or any(
        isinstance(a, dict) and a.get("result") in ("pass", "fail")
        for a in assertions)


def validate_record(record: dict, path: Path, kind: str, strict: bool = False) -> list[str]:
    """Validate records, without inferring a score or upgrading historical evidence."""
    if not isinstance(record, dict):
        return ["Run record must be an object"]
    if record.get("schema_version") not in ("1.0", "1.1"):
        return ["Unsupported run schema_version"]
    if strict and record.get("schema_version") != "1.1":
        return ["Controlled comparison requires schema 1.1; legacy records are historical only"]
    cases = record.get("cases")
    if not isinstance(cases, list) or not cases:
        return ["Run record must contain a non-empty cases array"]
    expected = {c["id"]: c for c in suite_cases(kind)}
    errors, seen = [], set()
    modern = record["schema_version"] == "1.1"
    if modern:
        for key in ("skill_version", "platform", "model", "review_method"):
            if not isinstance(record.get(key), str) or not record[key].strip():
                errors.append(f"Missing {key}")
        if kind == "composition" and (not isinstance(record.get("paired_skills"), str) or not record["paired_skills"].strip()):
            errors.append("Missing paired_skills")
        reviewed = any(isinstance(c, dict) and has_review(c,
                       ("routing_result", "behavior_result") if kind == "behavioral" else ("result",)) for c in cases)
        if reviewed or strict:
            if not isinstance(record.get("review_method"), str) or record.get("review_method", "").strip().lower() == "pending":
                errors.append("Reviewed results require a completed review method; label AI/human review separately")
            contract = record.get("comparison")
            if not isinstance(contract, dict) or any(not isinstance(contract.get(k), str) or not contract[k].strip() for k in CONTRACT_FIELDS):
                errors.append("Reviewed results require controlled comparison metadata")
            else:
                for key in ("fixtures_sha256", "prompts_sha256", "criteria_sha256"):
                    if len(contract[key]) != 64 or any(c not in '0123456789abcdef' for c in contract[key]):
                        errors.append(f"Invalid {key}")
                for key in ("prompts_sha256", "criteria_sha256"):
                    if contract[key] != comparison_template(kind)[key]:
                        errors.append(f"Changed published {key}")
    for case in cases:
        if not isinstance(case, dict):
            errors.append("Each case must be an object")
            continue
        cid = case.get("id")
        if not isinstance(cid, str) or cid not in expected or cid in seen:
            errors.append("Unknown or duplicate case ID")
            continue
        seen.add(cid)
        keys = ("routing_result", "behavior_result") if kind == "behavioral" else ("result",)
        if any(case.get(k) not in tuple(ALLOWED_RESULTS) for k in keys):
            errors.append(f"{cid}: invalid result")
        reviewed = has_review(case, keys)
        if not isinstance(case.get("notes", ""), str):
            errors.append(f"{cid}: notes must be text")
        if reviewed and (not isinstance(case.get("notes"), str) or not case["notes"].strip()):
            errors.append(f"{cid}: reviewed results require notes")
        if not modern:
            continue
        if kind == "behavioral" and case.get("routing_expected") != expected[cid]["routing_expected"]:
            errors.append(f"{cid}: changed routing expectation")
        if kind == "composition" and case.get("dimension") != expected[cid]["dimension"]:
            errors.append(f"{cid}: changed composition dimension")
        if any(case.get(k) == "not_applicable" for k in keys):
            errors.append(f"{cid}: use not_run for unavailable checks; published cases cannot be waived")
        if reviewed:
            name = case.get("output_file")
            evidence = (path.parent / name).resolve() if isinstance(name, str) and name.strip() else None
            if evidence is None or not evidence.is_relative_to(path.parent.resolve()) or not evidence.is_file():
                errors.append(f"{cid}: missing or external retained evidence")
            else:
                data = evidence.read_bytes()
                if not data.strip() or hashlib.sha256(data).hexdigest() != case.get("evidence_sha256"):
                    errors.append(f"{cid}: empty or changed evidence")
        assertions = case.get("assertion_results")
        if not isinstance(assertions, list) or any(not isinstance(a, dict) for a in assertions) or [a.get("assertion") for a in assertions] != expected[cid]["assertions"]:
            errors.append(f"{cid}: missing, reordered or changed assertion reviews")
            continue
        if any(a.get("result") not in ("pass", "fail", "not_run") or
               (a.get("result") in ("pass", "fail") and (not isinstance(a.get("notes"), str) or not a["notes"].strip())) for a in assertions):
            errors.append(f"{cid}: invalid assertion judgment")
            continue
        result = 'not_run' if any(a['result'] == 'not_run' for a in assertions) else 'fail' if any(a['result'] == 'fail' for a in assertions) else 'pass'
        if case.get("behavior_result" if kind == "behavioral" else "result") != result:
            errors.append(f"{cid}: aggregate result contradicts assertion reviews")
    if seen != set(expected):
        errors.append("Run record must contain every published case exactly once")
    return errors


def review_notes(case: dict) -> str:
    assertions = case.get('assertion_results')
    failures = [a.get('assertion', 'unknown') for a in assertions if isinstance(a, dict) and a.get('result') == 'fail'] if isinstance(assertions, list) else []
    return (case.get('notes', '') + (' Known failed assertions: ' + '; '.join(failures) if failures else '')).replace('|', '\\|') or '—'


def evidence_status(record: dict) -> str:
    if record['schema_version'] == '1.0':
        return 'Historical legacy scores; evidence integrity not validated under schema 1.1. Not comparison or promotion approval.'
    return 'Schema 1.1 record consistency checked; execution and review are not authenticated. Coverage completion is not a passing result or promotion approval; human review remains required.'


def evidence_link(case: dict, run_path: Path, report_path: Path) -> str:
    name = case.get("output_file")
    if not name:
        return "Not retained"
    target = run_path.parent / name
    relative = Path(os.path.relpath(target, report_path.parent)).as_posix()
    return f"[Retained output]({quote(relative, safe='/')})"


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "agents/openai.yaml",
    "evals/evals.json",
    "evals/composition.json",
    "evals/README.md",
    "evals/composition/README.md",
    "evals/fixtures/README.md",
    "evals/fixtures/composition-deploy/index.html",
    "evals/fixtures/deployment-storage/index.html",
    "evals/fixtures/deployment-storage/README.md",
    "evals/fixtures/local-integration-verification/sync.py",
    "evals/fixtures/local-integration-verification/test_sync.py",
    "examples/README.md",
    "examples/quick-demo.md",
    "examples/fast-reversible-change.md",
    "examples/consequential-deployment.md",
    "examples/false-completion.md",
    "scripts/package_skill.sh",
    "decisions.md",
    "CHANGELOG.md",
    "LICENSE",
]


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Missing file: {display_path(path)}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {display_path(path)}: {exc}") from exc


def validate_suite() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        if not skill.startswith("---\n"):
            errors.append("SKILL.md must start with YAML frontmatter")
        if "name: ai-project-steward" not in skill:
            errors.append("SKILL.md frontmatter must name ai-project-steward")
        if "description:" not in skill.split("---", 2)[1]:
            errors.append("SKILL.md frontmatter must include a description")

    try:
        suite = load_json(EVALS_PATH)
    except ValueError as exc:
        return errors + [str(exc)]

    if suite.get("skill_name") != "ai-project-steward":
        errors.append("evals.json skill_name must be ai-project-steward")
    if suite.get("suite_name") != "Behavioral Evaluation Suite":
        errors.append("evals.json suite_name must be Behavioral Evaluation Suite")
    if not suite.get("schema_version"):
        errors.append("evals.json must declare schema_version")

    cases = suite.get("evals")
    if not isinstance(cases, list) or not cases:
        return errors + ["evals.json must contain a non-empty evals array"]

    seen: set[str] = set()
    routing_values: set[str] = set()
    required_case_fields = {
        "id",
        "prompt",
        "routing_expected",
        "baseline_expected_failure",
        "expected_output",
        "files",
        "assertions",
    }

    for index, case in enumerate(cases, start=1):
        label = case.get("id", f"case-{index}") if isinstance(case, dict) else f"case-{index}"
        if not isinstance(case, dict):
            errors.append(f"{label}: case must be an object")
            continue
        missing = sorted(required_case_fields - case.keys())
        if missing:
            errors.append(f"{label}: missing fields {', '.join(missing)}")
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{label}: id must be a non-empty string")
        elif case_id in seen:
            errors.append(f"{label}: duplicate id")
        else:
            seen.add(case_id)
        routing = case.get("routing_expected")
        if routing not in {"load", "do_not_load"}:
            errors.append(f"{label}: routing_expected must be load or do_not_load")
        else:
            routing_values.add(routing)
        if not isinstance(case.get("prompt"), str) or not case.get("prompt", "").strip():
            errors.append(f"{label}: prompt must be a non-empty string")
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or len(assertions) < 3:
            errors.append(f"{label}: provide at least three assertions")
        elif any(not isinstance(item, str) or not item.strip() for item in assertions):
            errors.append(f"{label}: assertions must be non-empty strings")
        if not isinstance(case.get("files"), list):
            errors.append(f"{label}: files must be an array")

    if routing_values != {"load", "do_not_load"}:
        errors.append("The suite must include both load and do_not_load routing cases")
    if len(cases) < 8:
        errors.append("The suite must contain at least eight behavioral cases")
    validate_composition_suite(errors)
    return errors


def validate_composition_suite(errors: list[str]) -> None:
    try:
        suite = load_json(COMPOSITION_PATH)
    except ValueError as exc:
        errors.append(str(exc))
        return

    if suite.get("skill_name") != "ai-project-steward":
        errors.append("composition.json skill_name must be ai-project-steward")
    if suite.get("suite_name") != "Harness Composition Evaluation Suite":
        errors.append("composition.json suite_name must be Harness Composition Evaluation Suite")
    if not suite.get("schema_version"):
        errors.append("composition.json must declare schema_version")

    cases = suite.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append("composition.json must contain a non-empty cases array")
        return

    required = {
        "id",
        "dimension",
        "paired_capability",
        "fixture",
        "platform_requirement",
        "turns",
        "expected_output",
        "assertions",
    }
    allowed_dimensions = {"paired_skill", "cross_session", "cross_platform"}
    seen: set[str] = set()
    dimensions: set[str] = set()
    for index, case in enumerate(cases, start=1):
        label = case.get("id", f"composition-{index}") if isinstance(case, dict) else f"composition-{index}"
        if not isinstance(case, dict):
            errors.append(f"{label}: composition case must be an object")
            continue
        missing = sorted(required - case.keys())
        if missing:
            errors.append(f"{label}: missing fields {', '.join(missing)}")
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{label}: id must be a non-empty string")
        elif case_id in seen:
            errors.append(f"{label}: duplicate id")
        else:
            seen.add(case_id)
        dimension = case.get("dimension")
        if dimension not in allowed_dimensions:
            errors.append(f"{label}: unsupported composition dimension")
        else:
            dimensions.add(dimension)
        turns = case.get("turns")
        if not isinstance(turns, list) or not turns or any(not isinstance(turn, str) or not turn.strip() for turn in turns):
            errors.append(f"{label}: turns must be a non-empty array of prompts")
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or len(assertions) < 3:
            errors.append(f"{label}: provide at least three assertions")
        elif any(not isinstance(item, str) or not item.strip() for item in assertions):
            errors.append(f"{label}: assertions must be non-empty strings")

    if dimensions != allowed_dimensions:
        errors.append("The composition suite must cover paired_skill, cross_session, and cross_platform dimensions")


def command_validate(_: argparse.Namespace) -> int:
    errors = validate_suite()
    if errors:
        print("Behavioral Evaluation Suite validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    suite = load_json(EVALS_PATH)
    composition = load_json(COMPOSITION_PATH)
    load_count = sum(case["routing_expected"] == "load" for case in suite["evals"])
    skip_count = len(suite["evals"]) - load_count
    print("Behavioral Evaluation Suite validation passed")
    print(f"- {len(suite['evals'])} cases ({load_count} load, {skip_count} do_not_load)")
    print(f"- {len(composition['cases'])} harness composition cases")
    print("- 4 worked scenarios")
    print("- required package, metadata, evidence, and decision files present")
    return 0


def command_init(args: argparse.Namespace) -> int:
    errors = validate_suite()
    if errors:
        print("Run package validation before creating a live run.", file=sys.stderr)
        return 1
    suite = load_json(EVALS_PATH)
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    if output.exists() and not args.force:
        print(f"Refusing to overwrite existing run: {output}", file=sys.stderr)
        return 1
    record = {
        "schema_version": "1.1",
        "comparison": comparison_template("behavioral"),
        "skill_version": args.version,
        "evaluation_date": dt.date.today().isoformat(),
        "platform": args.platform,
        "model": args.model,
        "review_method": "pending",
        "package_validation": "pass",
        "limitations": "Add platform, routing, model-variance, and untested-surface limitations before publishing.",
        "cases": [
            {
                "id": case["id"],
                "routing_expected": case["routing_expected"],
                "routing_result": "not_run",
                "behavior_result": "not_run",
                "output_file": "",
                "evidence_sha256": "",
                "assertion_results": assertion_template(case),
                "notes": "",
            }
            for case in suite["evals"]
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"Created live-run record: {display_path(output)}")
    return 0


def _count(results: list[dict], key: str, value: str) -> int:
    return sum(case.get(key) == value for case in results)


def command_report(args: argparse.Namespace) -> int:
    run_path = Path(args.run)
    if not run_path.is_absolute():
        run_path = ROOT / run_path
    try:
        run = load_json(run_path)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    errors = validate_record(run, run_path, "behavioral")
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    cases = run["cases"]

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    if output.exists() and not args.force:
        print(f"Refusing to overwrite existing result: {output}", file=sys.stderr)
        return 1

    routing_reviewed = _count(cases, "routing_result", "pass") + _count(cases, "routing_result", "fail")
    behavior_reviewed = _count(cases, "behavior_result", "pass") + _count(cases, "behavior_result", "fail")
    lines = [
        f"# AI Project Steward {run.get('skill_version', 'unknown')} Evaluation Results",
        "",
        f"- **Status:** {'Complete' if all(case['routing_result'] != 'not_run' and case['behavior_result'] != 'not_run' for case in cases) else 'Incomplete'}",
        f"- **Evidence status:** {evidence_status(run)}",
        f"- **Evaluation date:** {run.get('evaluation_date', 'unknown')}",
        f"- **Platform:** {run.get('platform', 'unknown')}",
        f"- **Model:** {run.get('model', 'unknown')}",
        f"- **Review method:** {run.get('review_method', 'unknown')}",
        f"- **Package validation:** {run.get('package_validation', 'unknown')}",
        "",
        "## Summary",
        "",
        f"- Routing: {_count(cases, 'routing_result', 'pass')} passed, {_count(cases, 'routing_result', 'fail')} failed, {len(cases) - routing_reviewed} not run or not applicable.",
        f"- Steward behavior: {_count(cases, 'behavior_result', 'pass')} passed, {_count(cases, 'behavior_result', 'fail')} failed, {len(cases) - behavior_reviewed} not run or not applicable.",
        "",
        "## Case Results",
        "",
        "| Case | Expected routing | Routing | Steward behavior | Evidence | Notes |",
        "|---|---|---|---|---|---|",
    ]
    for case in cases:
        evidence = evidence_link(case, run_path, output)
        notes = review_notes(case)
        lines.append(
            f"| `{case['id']}` | {case.get('routing_expected', 'unknown')} | {case['routing_result']} | "
            f"{case['behavior_result']} | {evidence} | {notes} |"
        )
    lines.extend(
        [
            "",
            "## Limitations",
            "",
            run.get("limitations", "No limitations recorded."),
            "",
            "These results describe observed behavior under the named conditions. They do not guarantee identical routing or responses across every model, platform, context, or future run.",
        ]
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated evaluation result: {display_path(output)}")
    return 0


def command_init_composition(args: argparse.Namespace) -> int:
    errors = validate_suite()
    if errors:
        print("Run package validation before creating a composition run.", file=sys.stderr)
        return 1
    suite = load_json(COMPOSITION_PATH)
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    if output.exists() and not args.force:
        print(f"Refusing to overwrite existing run: {output}", file=sys.stderr)
        return 1
    record = {
        "schema_version": "1.1",
        "comparison": comparison_template("composition"),
        "skill_version": args.version,
        "evaluation_date": dt.date.today().isoformat(),
        "platform": args.platform,
        "model": args.model,
        "paired_skills": args.paired_skills,
        "review_method": "pending",
        "package_validation": "pass",
        "limitations": "Record activation, platform, paired-skill, cross-session, and cross-platform limitations before publishing.",
        "cases": [
            {
                "id": case["id"],
                "dimension": case["dimension"],
                "result": "not_run",
                "output_file": "",
                "evidence_sha256": "",
                "assertion_results": assertion_template(case),
                "notes": "",
            }
            for case in suite["cases"]
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"Created composition-run record: {display_path(output)}")
    return 0


def command_report_composition(args: argparse.Namespace) -> int:
    run_path = Path(args.run)
    if not run_path.is_absolute():
        run_path = ROOT / run_path
    try:
        run = load_json(run_path)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    errors = validate_record(run, run_path, "composition")
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    cases = run["cases"]

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    if output.exists() and not args.force:
        print(f"Refusing to overwrite existing result: {output}", file=sys.stderr)
        return 1

    reviewed = _count(cases, "result", "pass") + _count(cases, "result", "fail")
    lines = [
        f"# AI Project Steward {run.get('skill_version', 'unknown')} Composition Results",
        "",
        f"- **Status:** {'Complete' if all(case['result'] != 'not_run' for case in cases) else 'Incomplete'}",
        f"- **Evidence status:** {evidence_status(run)}",
        f"- **Evaluation date:** {run.get('evaluation_date', 'unknown')}",
        f"- **Platform:** {run.get('platform', 'unknown')}",
        f"- **Model:** {run.get('model', 'unknown')}",
        f"- **Paired skills:** {run.get('paired_skills', 'unknown')}",
        f"- **Review method:** {run.get('review_method', 'unknown')}",
        f"- **Package validation:** {run.get('package_validation', 'unknown')}",
        "",
        "## Summary",
        "",
        f"- Composition: {_count(cases, 'result', 'pass')} passed, {_count(cases, 'result', 'fail')} failed, {len(cases) - reviewed} not run or not applicable.",
        "",
        "## Case Results",
        "",
        "| Case | Dimension | Result | Evidence | Notes |",
        "|---|---|---|---|---|",
    ]
    for case in cases:
        evidence = evidence_link(case, run_path, output)
        notes = review_notes(case)
        lines.append(f"| `{case['id']}` | {case.get('dimension', 'unknown')} | {case['result']} | {evidence} | {notes} |")
    lines.extend(
        [
            "",
            "## Limitations",
            "",
            run.get("limitations", "No limitations recorded."),
            "",
            "These results show observed composition under named conditions. They do not establish deterministic enforcement or guarantee identical behavior across every model, platform, paired skill, or future run.",
        ]
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated composition result: {display_path(output)}")
    return 0


def command_compare(args: argparse.Namespace) -> int:
    """Compare reviewed records; never grant release authority."""
    report = {"ready_for_human_review": False, "promotion_authorized": False,
              "human_review_required": True, "improved": [], "regressed": [], "blockers": [],
              "note": "Advisory comparison only; metadata equality is not execution proof or merge/install/release approval."}
    records = []
    for name in (args.baseline, args.candidate):
        path = Path(name)
        if not path.is_absolute():
            path = ROOT / path
        try:
            record = load_json(path)
            report["blockers"].extend(validate_record(record, path, args.suite, strict=True))
            records.append(record)
        except (ValueError, TypeError, KeyError, OSError) as exc:
            report["blockers"].append(str(exc))
    if not report["blockers"]:
        before, after = records
        for field in ("model", "platform"):
            if before[field] != after[field]:
                report["blockers"].append(f"Incomparable {field}")
        if args.suite == "composition" and before["paired_skills"] != after["paired_skills"]:
            report["blockers"].append("Incomparable paired_skills")
        for field in CONTRACT_FIELDS:
            if before["comparison"][field] != after["comparison"][field]:
                report["blockers"].append(f"Incomparable {field}")
        if not report["blockers"]:
            old = {c['id']: c for c in before['cases']}
            for case in after['cases']:
                cid = case['id']
                for field in (("routing_result", "behavior_result") if args.suite == 'behavioral' else ("result",)):
                    a, b = old[cid][field], case[field]
                    if a not in ('pass', 'fail') or b not in ('pass', 'fail'):
                        report['blockers'].append(f"Incomplete {cid}: {field}")
                    if b == 'fail':
                        report['blockers'].append(f"Candidate failure {cid}: {field}")
                    if a == 'fail' and b == 'pass':
                        report['improved'].append(f"{cid}: {field}")
                    if a == 'pass' and b == 'fail':
                        report['regressed'].append(f"{cid}: {field}")
            if not report['improved']:
                report['blockers'].append('No demonstrated improvement')
            report['ready_for_human_review'] = not report['blockers']
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    if output.exists() and not args.force:
        raise ValueError(f"Refusing to overwrite: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
    return 0 if report['ready_for_human_review'] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="Validate package and evaluation definitions")
    validate.set_defaults(func=command_validate)

    init = subparsers.add_parser("init", help="Create a live-run record")
    init.add_argument("--version", required=True, help="Skill release, for example v2.1.0")
    init.add_argument("--platform", required=True, help="Platform under test")
    init.add_argument("--model", required=True, help="Model under test")
    init.add_argument("--output", required=True, help="Run-record JSON path")
    init.add_argument("--force", action="store_true", help="Overwrite an existing output file")
    init.set_defaults(func=command_init)

    report = subparsers.add_parser("report", help="Generate Markdown from a reviewed run record")
    report.add_argument("--run", required=True, help="Reviewed run-record JSON path")
    report.add_argument("--output", required=True, help="Markdown result path")
    report.add_argument("--force", action="store_true", help="Overwrite an existing output file")
    report.set_defaults(func=command_report)

    init_composition = subparsers.add_parser("init-composition", help="Create a harness-composition run record")
    init_composition.add_argument("--version", required=True, help="Skill release, for example v2.1.0")
    init_composition.add_argument("--platform", required=True, help="Platform or platform set under test")
    init_composition.add_argument("--model", required=True, help="Model or model set under test")
    init_composition.add_argument("--paired-skills", required=True, help="Paired skill names and versions")
    init_composition.add_argument("--output", required=True, help="Composition run-record JSON path")
    init_composition.add_argument("--force", action="store_true", help="Overwrite an existing output file")
    init_composition.set_defaults(func=command_init_composition)

    report_composition = subparsers.add_parser("report-composition", help="Generate Markdown from a reviewed composition run")
    report_composition.add_argument("--run", required=True, help="Reviewed composition run-record JSON path")
    report_composition.add_argument("--output", required=True, help="Markdown result path")
    report_composition.add_argument("--force", action="store_true", help="Overwrite an existing output file")
    report_composition.set_defaults(func=command_report_composition)
    compare = subparsers.add_parser("compare", help="Compare controlled reviewed records; no promotion authority")
    compare.add_argument("--suite", choices=("behavioral", "composition"), required=True)
    for key in ("baseline", "candidate", "output"):
        compare.add_argument("--" + key, required=True)
    compare.add_argument("--force", action="store_true")
    compare.set_defaults(func=command_compare)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f"Evaluation validation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
