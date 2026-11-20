"""Stable-release metadata gate tests; no agent behavior or release is implied."""
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile
from contextlib import redirect_stdout

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_release_metadata as checker  # noqa: E402

SKILL = b"Fixture instructions\n"


def stable_metadata(**overrides):
    meta = {"name": "ai-project-steward", "version": "2.1.3", "status": "stable",
            "publication_status": "stable_release", "release_approved": True,
            "installation_approved": True, "skill_sha256": hashlib.sha256(SKILL).hexdigest()}
    meta.update(overrides)
    return meta


class ReleaseMetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def archive(self, meta, name="package.zip", skill=SKILL, drop=()):
        path = self.root / name
        with zipfile.ZipFile(path, "w") as archive:
            if "SKILL.md" not in drop:
                archive.writestr("ai-project-steward/SKILL.md", skill)
            if "metadata" not in drop:
                archive.writestr("ai-project-steward/metadata/release.json", json.dumps(meta))
        return path

    def run_main(self, *args):
        with redirect_stdout(io.StringIO()) as out:
            code = checker.main([str(a) for a in args])
        return code, out.getvalue()

    def test_stable_approved_archive_passes(self):
        self.assertEqual(checker.problems(self.archive(stable_metadata()), "2.1.3"), [])

    def test_release_candidate_metadata_is_rejected(self):
        # The published v2.1.3-claude asset shipped exactly this shape.
        meta = stable_metadata(version="2.1.3-rc.1-claude", status="candidate",
                               publication_status="unreleased", release_approved=False,
                               installation_approved=False)
        found = checker.problems(self.archive(meta))
        self.assertEqual(len(found), 4, found)

    def test_each_unapproved_field_is_rejected_on_its_own(self):
        for overrides in ({"version": "2.1.3-rc.1"}, {"status": "candidate"},
                          {"publication_status": "unreleased"}, {"release_approved": False},
                          {"release_approved": "true"}, {"skill_sha256": "0" * 64}):
            with self.subTest(overrides=overrides):
                self.assertNotEqual(checker.problems(self.archive(stable_metadata(**overrides))), [])

    def test_expected_version_mismatch_is_rejected(self):
        self.assertNotEqual(checker.problems(self.archive(stable_metadata()), "2.1.4"), [])

    def test_missing_files_and_bad_archives_are_rejected(self):
        self.assertNotEqual(checker.problems(self.archive(stable_metadata(), drop=("metadata",))), [])
        self.assertNotEqual(checker.problems(self.archive(stable_metadata(), drop=("SKILL.md",))), [])
        bad = self.root / "not-a-zip.zip"
        bad.write_bytes(b"not a zip")
        self.assertNotEqual(checker.problems(bad), [])

    def test_only_superseded_assets_fail_closed(self):
        old = self.archive(stable_metadata(status="candidate"), name="old.zip")
        listing = self.root / "superseded.json"
        listing.write_text(json.dumps([{"sha256": hashlib.sha256(old.read_bytes()).hexdigest(),
                                        "asset": "old.zip", "reason": "test", "replacement": "r2.zip"}]))
        code, output = self.run_main(old, "--superseded", listing)
        self.assertEqual(code, 1, output)
        self.assertIn("no non-superseded archives", output)

    def test_superseded_asset_is_skipped_but_others_still_fail(self):
        old = self.archive(stable_metadata(status="candidate"), name="old.zip")
        new = self.archive(stable_metadata(), name="new.zip")
        listing = self.root / "superseded.json"
        listing.write_text(json.dumps([{"sha256": hashlib.sha256(old.read_bytes()).hexdigest(),
                                        "asset": "old.zip", "reason": "test", "replacement": "new.zip"}]))
        code, output = self.run_main(old, new, "--superseded", listing)
        self.assertEqual(code, 0, output)
        self.assertIn("SKIP", output)
        code, output = self.run_main(old, new)
        self.assertEqual(code, 1, output)


if __name__ == "__main__":
    unittest.main()
