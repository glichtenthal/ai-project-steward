"""Synthetic recorder tests. These are not agent evaluations or benefit evidence."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/evaluate.py"
SPEC = importlib.util.spec_from_file_location("evaluation", SCRIPT)
evaluation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(evaluation)


class EvaluationIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                              capture_output=True, text=True)

    def record(self, kind="behavioral", name="run.json"):
        path = self.root / name
        args = ["init" if kind == "behavioral" else "init-composition",
                "--version", "SYNTHETIC UNIT FIXTURE", "--platform", "test harness",
                "--model", "test model", "--output", path, "--force"]
        if kind == "composition":
            args.extend(["--paired-skills", "synthetic role@1"])
        result = self.cli(*args)
        self.assertEqual(result.returncode, 0, result.stderr)
        return path, json.loads(path.read_text())

    def reviewed(self, kind="behavioral", name="run.json"):
        path, record = self.record(kind, name)
        record["review_method"] = "Deterministic synthetic unit fixture; no model or human evaluation"
        record["comparison"].update(harness="synthetic@1", tools="no tools",
                                    permissions="temporary directory only", fixtures_sha256="0" * 64)
        for case in record["cases"]:
            evidence = self.root / f"{case['id']} output.txt"
            evidence.write_text("Synthetic unit fixture, not actual agent output.\n")
            case.update(output_file=evidence.name,
                        evidence_sha256=hashlib.sha256(evidence.read_bytes()).hexdigest(),
                        notes="Synthetic test score only.")
            for assertion in case["assertion_results"]:
                assertion.update(result="pass", notes="Synthetic test score only.")
            if kind == "behavioral":
                case.update(routing_result="pass", behavior_result="pass")
            else:
                case["result"] = "pass"
        return path, record

    def errors(self, record, path, kind="behavioral"):
        return evaluation.validate_record(record, path, kind)

    def assert_rejected(self, record, path, message, kind="behavioral"):
        self.assertTrue(any(message in e for e in self.errors(record, path, kind)),
                        self.errors(record, path, kind))

    def save(self, path, record):
        path.write_text(json.dumps(record))

    def comparison(self, before, after, kind="behavioral"):
        baseline, candidate = self.root / "baseline.json", self.root / "candidate.json"
        self.save(baseline, before)
        self.save(candidate, after)
        output = self.root / "comparison.json"
        result = self.cli("compare", "--suite", kind, "--baseline", baseline,
                          "--candidate", candidate, "--output", output, "--force")
        self.assertTrue(output.is_file(), result.stderr)
        return result, json.loads(output.read_text())

    def improved_pair(self, kind="behavioral"):
        _, after = self.reviewed(kind)
        before = copy.deepcopy(after)
        before["cases"][0]["assertion_results"][0]["result"] = "fail"
        before["cases"][0]["behavior_result" if kind == "behavioral" else "result"] = "fail"
        return before, after

    def test_init_leaves_positive_and_negative_behavior_unreviewed(self):
        path, record = self.record()
        self.assertFalse(self.errors(record, path))
        self.assertTrue(any(c["routing_expected"] == "do_not_load" for c in record["cases"]))
        self.assertTrue(all(c["behavior_result"] == "not_run" for c in record["cases"]))

    def test_composition_and_behavior_review_contracts(self):
        for kind in ("behavioral", "composition"):
            with self.subTest(kind=kind):
                path, record = self.reviewed(kind)
                self.assertEqual(self.errors(record, path, kind), [])

    def test_missing_changed_empty_and_external_evidence(self):
        for fault in ("missing", "changed", "empty", "external", "symlink"):
            with self.subTest(fault=fault):
                path, record = self.reviewed()
                case = record["cases"][0]
                target = self.root / case["output_file"]
                if fault == "missing":
                    target.unlink()
                elif fault in ("changed", "empty"):
                    target.write_text("changed" if fault == "changed" else " \n")
                else:
                    with tempfile.TemporaryDirectory() as external:
                        outside = Path(external) / "output.txt"
                        outside.write_text("Synthetic fixture.")
                        case["evidence_sha256"] = hashlib.sha256(outside.read_bytes()).hexdigest()
                        if fault == "external":
                            case["output_file"] = str(outside)
                        else:
                            target.unlink()
                            target.symlink_to(outside)
                        self.assert_rejected(record, path, "external retained evidence")
                    continue
                self.assertTrue(self.errors(record, path))

    def test_missing_changed_reordered_assertions(self):
        for fault in ("missing", "changed", "reordered"):
            with self.subTest(fault=fault):
                path, record = self.reviewed()
                assertions = record["cases"][0]["assertion_results"]
                if fault == "missing":
                    assertions.pop()
                elif fault == "changed":
                    assertions[0]["assertion"] = "Weakened test"
                else:
                    assertions.reverse()
                self.assert_rejected(record, path, "assertion reviews")

    def test_assertion_notes_required(self):
        path, record = self.reviewed()
        record["cases"][0]["assertion_results"][0]["notes"] = ""
        self.assert_rejected(record, path, "invalid assertion judgment")

    def test_case_notes_required(self):
        path, record = self.reviewed()
        record["cases"][0]["notes"] = ""
        self.assert_rejected(record, path, "require notes")

    def test_pending_review_rejected(self):
        path, record = self.reviewed()
        record["review_method"] = "pending"
        self.assert_rejected(record, path, "completed review method")

    def test_contradictory_aggregate_rejected(self):
        for kind in ("behavioral", "composition"):
            path, record = self.reviewed(kind)
            record["cases"][0]["assertion_results"][0]["result"] = "fail"
            self.assert_rejected(record, path, "contradicts", kind)

    def test_partial_failure_is_visible_and_blocks_comparison(self):
        path, after = self.reviewed()
        before = copy.deepcopy(after)
        case = after["cases"][0]
        case["assertion_results"][0]["result"] = "fail"
        case["assertion_results"][1]["result"] = "not_run"
        case["behavior_result"] = "not_run"
        self.save(path, after)
        output = self.root / "report.md"
        result = self.cli("report", "--run", path, "--output", output)
        self.assertEqual(result.returncode, 0, result.stderr)
        rendered = output.read_text()
        self.assertIn("Incomplete", rendered)
        self.assertIn("Known failed assertions: " + case["assertion_results"][0]["assertion"], rendered)
        result, comparison = self.comparison(before, after)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(comparison["ready_for_human_review"])

    def test_missing_duplicate_and_unknown_cases_rejected(self):
        for fault in ("missing", "duplicate", "unknown"):
            path, record = self.reviewed()
            if fault == "missing":
                record["cases"].pop()
            elif fault == "duplicate":
                record["cases"].append(copy.deepcopy(record["cases"][0]))
            else:
                record["cases"][0]["id"] = "unknown"
            self.assertTrue(self.errors(record, path), fault)

    def test_negative_routing_cannot_waive_behavior(self):
        path, record = self.reviewed()
        negative = next(c for c in record["cases"] if c["routing_expected"] == "do_not_load")
        negative["behavior_result"] = "not_applicable"
        self.assert_rejected(record, path, "cannot be waived")

    def test_routing_expectation_and_dimension_cannot_change(self):
        path, record = self.reviewed()
        record["cases"][0]["routing_expected"] = "do_not_load"
        self.assert_rejected(record, path, "changed routing")
        path, record = self.reviewed("composition")
        record["cases"][0]["dimension"] = "other"
        self.assert_rejected(record, path, "changed composition", "composition")

    def test_metadata_mismatch_blocks_comparison(self):
        for field in ("model", "platform", *evaluation.CONTRACT_FIELDS):
            with self.subTest(field=field):
                before, after = self.improved_pair()
                target = after if field in ("model", "platform") else after["comparison"]
                target[field] = "1" * 64 if field.endswith("sha256") else "different"
                result, report = self.comparison(before, after)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(report["ready_for_human_review"])
                self.assertEqual(report["improved"], [])

    def test_missing_metadata_rejected(self):
        path, record = self.reviewed()
        del record["comparison"]["permissions"]
        self.assert_rejected(record, path, "comparison metadata")

    def test_paired_skill_mismatch_blocks_comparison(self):
        before, after = self.improved_pair("composition")
        after["paired_skills"] = "different role@2"
        _, report = self.comparison(before, after, "composition")
        self.assertIn("Incomparable paired_skills", report["blockers"])

    def test_no_improvement_is_not_success(self):
        _, record = self.reviewed()
        result, report = self.comparison(record, record)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("No demonstrated improvement", report["blockers"])

    def test_regression_blocks_even_with_improvement_elsewhere(self):
        before, after = self.improved_pair()
        after["cases"][1]["routing_result"] = "fail"
        _, report = self.comparison(before, after)
        self.assertTrue(report["improved"])
        self.assertTrue(report["regressed"])
        self.assertFalse(report["ready_for_human_review"])

    def test_success_is_only_advisory(self):
        for kind in ("behavioral", "composition"):
            before, after = self.improved_pair(kind)
            result, report = self.comparison(before, after, kind)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(report["ready_for_human_review"])
            self.assertFalse(report["promotion_authorized"])
            self.assertTrue(report["human_review_required"])

    def test_legacy_report_is_historical_not_comparison_evidence(self):
        path, record = self.reviewed()
        record["schema_version"] = "1.0"
        record.pop("comparison")
        for case in record["cases"]:
            case.pop("assertion_results")
            case.pop("evidence_sha256")
        self.save(path, record)
        output = self.root / "legacy.md"
        result = self.cli("report", "--run", path, "--output", output)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Historical legacy scores", output.read_text())
        _, report = self.comparison(record, record)
        self.assertFalse(report["ready_for_human_review"])

    def test_report_links_resolve_from_report_location(self):
        path, record = self.reviewed()
        self.save(path, record)
        output = self.root / "results" / "report.md"
        result = self.cli("report", "--run", path, "--output", output)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("../" + record["cases"][0]["output_file"].replace(" ", "%20"), output.read_text())

    def test_incomplete_initial_record_reports_without_claiming_success(self):
        path, record = self.record()
        result = self.cli("report", "--run", path, "--output", self.root / "incomplete.md")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Incomplete", (self.root / "incomplete.md").read_text())
        _, report = self.comparison(record, record)
        self.assertFalse(report["ready_for_human_review"])

    def test_existing_outputs_are_not_overwritten(self):
        path, record = self.reviewed()
        self.save(path, record)
        original = path.read_bytes()
        result = self.cli("init", "--version", "x", "--platform", "x", "--model", "x", "--output", path)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(path.read_bytes(), original)
        output = self.root / "report.md"
        output.write_text("Original review")
        result = self.cli("report", "--run", path, "--output", output)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(output.read_text(), "Original review")

    def test_malformed_records_fail_without_tracebacks(self):
        path, original = self.reviewed()
        malformed = [[], {"schema_version": []}, {"schema_version": "1.1", "cases": []}]
        for key, value in (("cases", [None]), ("review_method", [])):
            record = copy.deepcopy(original)
            record[key] = value
            malformed.append(record)
        for key, value in (("id", []), ("notes", {}), ("behavior_result", []), ("assertion_results", [None])):
            record = copy.deepcopy(original)
            record["cases"][0][key] = value
            malformed.append(record)
        for record in malformed:
            self.save(path, record)
            result = self.cli("report", "--run", path, "--output", self.root / "bad.md")
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
