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
