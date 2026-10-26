"""Regression tests for evidence-driven skill improvement.

All fixtures are temporary; no real agent behavior is claimed by these tests.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "learn.py"
CASES = ROOT / "learning" / "cases.json"


class LearningTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        (self.base / "evidence.md").write_text("Redacted reviewer evidence\n", encoding="utf-8")

    def cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            cwd=ROOT, text=True, capture_output=True, check=False,
        )

    def cases(self, role="steward"):
        suite = json.loads(CASES.read_text(encoding="utf-8"))
        return [case for case in suite["cases"] if case["role"] == role]

    def run_record(self, name, *, role="steward", version="v1", fail_ids=(),
                   platform="Codex", model="same-model", missing_evidence=False):
        case_ids = [case["id"] for case in self.cases(role)]
        record = {
            "schema_version": "1.0",
            "role": role,
            "skill_version": version,
            "platform": platform,
            "model": model,
            "review_method": "human",
            "cases": [
                {
                    "id": case_id,
                    "result": "fail" if case_id in fail_ids else "pass",
                    "evidence": "" if missing_evidence else "evidence.md",
                    "notes": "Manual review of assertions and retained output.",
                }
                for case_id in case_ids
            ],
        }
        path = self.base / name
        path.write_text(json.dumps(record), encoding="utf-8")
        return path

    def gate(self, baseline, candidate):
        path = self.base / "gate.json"
        result = self.cli("gate", "--baseline", baseline, "--candidate", candidate,
                          "--output", path)
        return result, json.loads(path.read_text(encoding="utf-8"))


    def test_suite_contains_direct_learning_behavior_probes(self):
        # Recursion-specific controls are required: ordinary build checks alone
        # cannot demonstrate an improvement from the learning instructions.
        data = json.loads(CASES.read_text(encoding="utf-8"))["cases"]
        for role in ("steward", "design", "frontend"):
            focused = [c for c in data if c["role"] == role
                       and c["id"].startswith(role + "-learning-")]
            self.assertGreaterEqual(len(focused), 2, role)
            self.assertTrue(any(c.get("critical") for c in focused), role)
            self.assertTrue(any(not c.get("critical") for c in focused), role)

    def test_init_run_starts_unreviewed_and_does_not_claim_success(self):
        output = self.base / "new-run.json"
        result = self.cli("init-run", "--role", "design", "--version", "draft",
                          "--platform", "Codex", "--model", "model",
                          "--output", output)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(data["role"], "design")
        self.assertTrue(data["cases"])
        self.assertTrue(all(c["result"] == "not_run" for c in data["cases"]))

    def test_gate_allows_evidence_backed_improvement(self):
        improved = next(c["id"] for c in self.cases() if not c["critical"])
        before = self.run_record("before.json", fail_ids=(improved,))
        after = self.run_record("after.json", version="v2")
        result, report = self.gate(before, after)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(report["promotable"])
        self.assertEqual(report["improved"], [improved])

    def test_gate_rejects_regressions_even_when_other_case_improves(self):
        ids = [c["id"] for c in self.cases()]
        before = self.run_record("before.json", fail_ids=(ids[0],))
        after = self.run_record("after.json", version="v2", fail_ids=(ids[1],))
        result, report = self.gate(before, after)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(report["promotable"])
        self.assertIn(ids[1], report["regressed"])

    def test_gate_rejects_no_measured_improvement(self):
        before = self.run_record("before.json")
        after = self.run_record("after.json", version="v2")
        result, report = self.gate(before, after)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(report["promotable"])

    def test_gate_rejects_missing_evidence(self):
        improved = self.cases()[0]["id"]
        before = self.run_record("before.json", fail_ids=(improved,))
        after = self.run_record("after.json", version="v2", missing_evidence=True)
        result, report = self.gate(before, after)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(report["promotable"])

    def test_gate_rejects_incomparable_models(self):
        before = self.run_record("before.json", fail_ids=(self.cases()[0]["id"],))
        after = self.run_record("after.json", version="v2", model="different-model")
        result, report = self.gate(before, after)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(report["promotable"])

    def test_gate_rejects_missing_cases(self):
        before = self.run_record("before.json", fail_ids=(self.cases()[0]["id"],))
        after = self.run_record("after.json", version="v2")
        data = json.loads(after.read_text())
        data["cases"].pop()
        after.write_text(json.dumps(data))
        result, report = self.gate(before, after)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(report["promotable"])

    def test_gate_never_promotes_critical_failure(self):
        critical = next(c["id"] for c in self.cases() if c["critical"])
        noncritical = next(c["id"] for c in self.cases() if not c["critical"])
        before = self.run_record("before.json", fail_ids=(noncritical,))
        after = self.run_record("after.json", version="v2", fail_ids=(critical,))
        result, report = self.gate(before, after)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(report["promotable"])

    def events(self, rows):
        p = self.base / "observations.jsonl"
        p.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
        return p

    def event(self, event_id, task_id, severity="major", role="design"):
        return {
            "schema_version": "1.0", "id": event_id, "date": "2026-10-25",
            "task_id": task_id, "role": role, "failure_code": "missing-empty-state",
            "severity": severity, "expected": "Empty state defined",
            "observed": "Empty state omitted", "evidence": "evidence.md",
        }

    def triage(self, events):
        output = self.base / "triage.json"
        result = self.cli("triage", "--events", events, "--output", output)
        return result, json.loads(output.read_text(encoding="utf-8")) if output.exists() else None

    def test_triage_waits_for_recurrence(self):
        result, report = self.triage(self.events([self.event("a", "task-1")]))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report["proposals"], [])

    def test_triage_deduplicates_single_task(self):
        result, report = self.triage(self.events([self.event("a", "task-1"), self.event("b", "task-1")]))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report["proposals"], [])

    def test_triage_proposes_on_two_independent_tasks(self):
        result, report = self.triage(self.events([self.event("a", "task-1"), self.event("b", "task-2")]))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(report["proposals"]), 1)
        self.assertEqual(report["proposals"][0]["independent_tasks"], 2)

    def test_triage_escalates_single_critical_incident(self):
        result, report = self.triage(self.events([self.event("a", "task-1", severity="critical")]))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(report["proposals"]), 1)

    def test_triage_rejects_unverifiable_evidence(self):
        event = self.event("a", "task-1", severity="critical")
        event["evidence"] = "missing-proof.md"
        result, report = self.triage(self.events([event]))
        self.assertNotEqual(result.returncode, 0)
        self.assertIsNone(report)

    def test_triage_rejects_unknown_role(self):
        event = self.event("a", "task-1", severity="critical")
        event["role"] = "untrusted-role"
        result, report = self.triage(self.events([event]))
        self.assertNotEqual(result.returncode, 0)
        self.assertIsNone(report)


if __name__ == "__main__":
    unittest.main()
