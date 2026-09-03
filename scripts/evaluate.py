#!/usr/bin/env python3
"""Validate AI Project Steward evaluations and prepare transparent result reports."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVALS_PATH = ROOT / "evals" / "evals.json"
COMPOSITION_PATH = ROOT / "evals" / "composition.json"
ALLOWED_RESULTS = {"pass", "fail", "not_run", "not_applicable"}
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
    "evals/fixtures/local-integration-verification/sync.py",
    "evals/fixtures/local-integration-verification/test_sync.py",
    "examples/README.md",
    "examples/quick-demo.md",
    "examples/fast-reversible-change.md",
    "examples/consequential-deployment.md",
    "examples/false-completion.md",
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
        "schema_version": "1.0",
        "skill_version": args.version,
        "evaluation_date": dt.date.today().isoformat(),
        "platform": args.platform,
        "model": args.model,
        "review_method": "Human review against published assertions",
        "package_validation": "pass",
        "limitations": "Add platform, routing, model-variance, and untested-surface limitations before publishing.",
        "cases": [
            {
                "id": case["id"],
                "routing_expected": case["routing_expected"],
                "routing_result": "not_run",
                "behavior_result": "not_applicable" if case["routing_expected"] == "do_not_load" else "not_run",
                "output_file": "",
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

    cases = run.get("cases")
    if not isinstance(cases, list) or not cases:
        print("Run record must contain a non-empty cases array", file=sys.stderr)
        return 1
    suite_ids = {case["id"] for case in load_json(EVALS_PATH)["evals"]}
    run_ids: set[str] = set()
    errors: list[str] = []
    for case in cases:
        case_id = case.get("id")
        if case_id in run_ids:
            errors.append(f"Duplicate run case: {case_id}")
        run_ids.add(case_id)
        if case_id not in suite_ids:
            errors.append(f"Unknown run case: {case_id}")
        for key in ("routing_result", "behavior_result"):
            if case.get(key) not in ALLOWED_RESULTS:
                errors.append(f"{case_id}: {key} must be one of {', '.join(sorted(ALLOWED_RESULTS))}")
        if (case.get("routing_result") in {"pass", "fail"} or case.get("behavior_result") in {"pass", "fail"}) and not case.get("notes", "").strip():
            errors.append(f"{case_id}: reviewed results require notes")
    if run_ids != suite_ids:
        errors.append("Run record must contain every current evaluation case exactly once")
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

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
        evidence = f"[{case['output_file']}]({case['output_file']})" if case.get("output_file") else "Not retained"
        notes = case.get("notes", "").replace("|", "\\|") or "—"
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
        "schema_version": "1.0",
        "skill_version": args.version,
        "evaluation_date": dt.date.today().isoformat(),
        "platform": args.platform,
        "model": args.model,
        "paired_skills": args.paired_skills,
        "review_method": "Human review against published composition assertions",
        "package_validation": "pass",
        "limitations": "Record activation, platform, paired-skill, cross-session, and cross-platform limitations before publishing.",
        "cases": [
            {
                "id": case["id"],
                "dimension": case["dimension"],
                "result": "not_run",
                "output_file": "",
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

    cases = run.get("cases")
    if not isinstance(cases, list) or not cases:
        print("Composition run record must contain a non-empty cases array", file=sys.stderr)
        return 1
    suite_ids = {case["id"] for case in load_json(COMPOSITION_PATH)["cases"]}
    run_ids: set[str] = set()
    errors: list[str] = []
    for case in cases:
        case_id = case.get("id")
        if case_id in run_ids:
            errors.append(f"Duplicate composition case: {case_id}")
        run_ids.add(case_id)
        if case_id not in suite_ids:
            errors.append(f"Unknown composition case: {case_id}")
        if case.get("result") not in ALLOWED_RESULTS:
            errors.append(f"{case_id}: result must be one of {', '.join(sorted(ALLOWED_RESULTS))}")
        if case.get("result") in {"pass", "fail"} and not case.get("notes", "").strip():
            errors.append(f"{case_id}: reviewed results require notes")
    if run_ids != suite_ids:
        errors.append("Composition run record must contain every current composition case exactly once")
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

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
        evidence = f"[{case['output_file']}]({case['output_file']})" if case.get("output_file") else "Not retained"
        notes = case.get("notes", "").replace("|", "\\|") or "—"
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
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
