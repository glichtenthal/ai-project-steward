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
