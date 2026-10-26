#!/usr/bin/env python3
"""Evidence-driven learning: propose improvements, never edit skills or promote releases."""
import argparse
import datetime as dt
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "learning" / "cases.json"
ROLES = {"steward", "design", "frontend"}
RESULTS = {"pass", "fail", "not_run", "not_applicable"}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path, data):
    path = Path(path)
    if path.exists():
        raise ValueError(f"Refusing to overwrite: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def evidence(path, parent):
    if not isinstance(path, str) or not path.strip():
        return False
    base = parent.resolve()
    candidate = (base / path).resolve()
    return candidate.is_relative_to(base) and candidate.is_file()


def suite(role):
    return [c for c in load(CASES)["cases"] if c["role"] == role]


def init_run(args):
    if args.role not in ROLES:
        raise ValueError("Invalid role")
    write(args.output, {"schema_version": "1.0", "role": args.role,
        "skill_version": args.version, "platform": args.platform, "model": args.model,
        "review_method": "pending", "cases": [
            {"id": c["id"], "result": "not_run", "evidence": "", "notes": ""}
            for c in suite(args.role)]})
    print(f"Unreviewed run: {args.output}")


def validated_run(path):
    p = Path(path)
    r = load(p)
    if r.get("schema_version") != "1.0" or r.get("role") not in ROLES:
        raise ValueError(f"{p}: invalid run schema/role")
    for k in ("skill_version", "platform", "model", "review_method"):
        if not isinstance(r.get(k), str) or not r[k].strip():
            raise ValueError(f"{p}: missing {k}")
    expected = {c["id"] for c in suite(r["role"])}
    records = r.get("cases")
    if not isinstance(records, list) or len(records) != len(expected):
        raise ValueError(f"{p}: missing/extra cases")
    seen = set()
    for c in records:
        cid = c.get("id")
        if cid not in expected or cid in seen:
            raise ValueError(f"{p}: unknown or duplicate case")
        seen.add(cid)
        if c.get("result") not in RESULTS:
            raise ValueError(f"{p}: invalid result")
        if c["result"] in {"pass", "fail"}:
            if not c.get("notes", "").strip() or not evidence(c.get("evidence"), p.parent):
                raise ValueError(f"{p}: {cid} lacks reviewer notes or retained evidence")
    return r


def gate(args):
    problems = []
    improved, regressed = [], []
    try:
        base, candidate = validated_run(args.baseline), validated_run(args.candidate)
        for field in ("role", "model", "platform"):
            if base[field] != candidate[field]:
                problems.append(f"Incomparable {field}")
        old = {c["id"]: c["result"] for c in base["cases"]}
        new = {c["id"]: c["result"] for c in candidate["cases"]}
        for item in suite(base["role"]):
            cid = item["id"]
            if old[cid] not in {"pass", "fail"} or new[cid] not in {"pass", "fail"}:
                problems.append(f"Unreviewed: {cid}")
            elif old[cid] == "fail" and new[cid] == "pass":
                improved.append(cid)
            elif old[cid] == "pass" and new[cid] == "fail":
                regressed.append(cid)
            if item["critical"] and new[cid] != "pass":
                problems.append(f"Critical gate failed: {cid}")
        if regressed:
            problems.append("New regressions")
        if not improved:
            problems.append("No demonstrated improvement")
    except (ValueError, KeyError, TypeError, OSError) as e:
        problems.append(str(e))
    report = {"schema_version": "1.0", "promotable": not problems,
              "improved": sorted(improved), "regressed": sorted(regressed),
              "blockers": problems,
              "note": "Advisory evidence gate only. A positive result never authorizes publication, merge, installation, or release."}
    write(args.output, report)
    print(json.dumps(report, indent=2))
    return 0 if not problems else 1


def triage(args):
    rows = []
    ids = set()
    for n, line in enumerate(Path(args.events).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        e = json.loads(line)
        required = ("id", "date", "task_id", "role", "failure_code",
                    "severity", "expected", "observed", "evidence")
        if e.get("schema_version") != "1.0" or any(not isinstance(e.get(k), str) or not e[k].strip() for k in required):
            raise ValueError(f"Invalid event line {n}")
        dt.date.fromisoformat(e["date"])
        if e["role"] not in ROLES or e["severity"] not in {"minor", "major", "critical"}:
            raise ValueError(f"Invalid role/severity line {n}")
        if e["id"] in ids or not evidence(e["evidence"], Path(args.events).parent):
            raise ValueError(f"Duplicate id or missing evidence line {n}")
        ids.add(e["id"])
        rows.append(e)
    grouped = defaultdict(list)
    for e in rows:
        grouped[(e["role"], e["failure_code"])].append(e)
    proposals = []
    for (role, code), events in sorted(grouped.items()):
        tasks = {e["task_id"] for e in events}
        if len(tasks) >= 2 or any(e["severity"] == "critical" for e in events):
            proposals.append({"role": role, "failure_code": code,
                "independent_tasks": len(tasks), "observation_ids": sorted(e["id"] for e in events),
                "status": "proposed", "next_step": "Reproduce with a failing baseline case; propose the smallest change and test against existing cases."})
    write(args.output, {"schema_version": "1.0", "observations": len(rows),
                        "proposals": proposals, "note": "Proposals require review; no skill files changed."})
    print(f"Created {len(proposals)} review proposals")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    a = sub.add_parser("init-run")
    for key in ("role", "version", "platform", "model", "output"):
        a.add_argument("--" + key, required=True)
    a.set_defaults(func=init_run)
    a = sub.add_parser("gate")
    for key in ("baseline", "candidate", "output"):
        a.add_argument("--" + key, required=True)
    a.set_defaults(func=gate)
    a = sub.add_parser("triage")
    for key in ("events", "output"):
        a.add_argument("--" + key, required=True)
    a.set_defaults(func=triage)
    args = p.parse_args()
    try:
        return args.func(args) or 0
    except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as e:
        print(f"Learning validation failed: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
