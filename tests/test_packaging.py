"""Distribution boundary tests; no agent behavior or release is implied."""
import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import zipfile

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/package_skill.sh"


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "scripts").mkdir()
        shutil.copy2(SCRIPT, self.root / "scripts/package_skill.sh")
        (self.root / "SKILL.md").write_text("Fixture instructions\n")
        (self.root / "private-evidence.txt").write_text("Must stay out of distribution\n")
        (self.root / "distribution-manifest.txt").write_text("SKILL.md\ndistribution-manifest.txt\n")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)

    def package(self, name="package.skill"):
        return subprocess.run(["bash", str(self.root / "scripts/package_skill.sh"),
                               str(self.root / name)], text=True, capture_output=True)

    def test_only_manifest_files_ship_and_contents_match(self):
        result = self.package()
        self.assertEqual(result.returncode, 0, result.stderr)
        with zipfile.ZipFile(self.root / "package.skill") as archive:
            self.assertEqual(set(archive.namelist()), {"ai-project-steward/SKILL.md",
                                                      "ai-project-steward/distribution-manifest.txt"})
            self.assertEqual(archive.read("ai-project-steward/SKILL.md"),
                             (self.root / "SKILL.md").read_bytes())

    def test_missing_duplicate_escape_and_untracked_entries_fail(self):
        for entry in ("missing.txt", "SKILL.md\nSKILL.md", "../outside", "/tmp/outside", "untracked.txt"):
            with self.subTest(entry=entry):
                (self.root / "untracked.txt").write_text("not tracked")
                (self.root / "distribution-manifest.txt").write_text(entry + "\n")
                self.assertNotEqual(self.package().returncode, 0)

    def test_symlink_entries_fail(self):
        (self.root / "link.txt").symlink_to(self.root / "private-evidence.txt")
        subprocess.run(["git", "-C", str(self.root), "add", "link.txt"], check=True)
        (self.root / "distribution-manifest.txt").write_text("link.txt\n")
        self.assertNotEqual(self.package().returncode, 0)

    def test_linked_parent_directory_fails(self):
        nested = self.root / "nested"
        nested.mkdir()
        (nested / "file.txt").write_text("fixture")
        subprocess.run(["git", "-C", str(self.root), "add", "nested/file.txt"], check=True)
        nested.rename(self.root / "moved")
        nested.symlink_to(self.root / "moved", target_is_directory=True)
        (self.root / "distribution-manifest.txt").write_text("nested/file.txt\n")
        self.assertNotEqual(self.package().returncode, 0)

    def test_failed_validation_preserves_prior_artifact(self):
        self.assertEqual(self.package().returncode, 0)
        original = (self.root / "package.skill").read_bytes()
        (self.root / "distribution-manifest.txt").write_text("missing.txt\n")
        self.assertNotEqual(self.package().returncode, 0)
        self.assertEqual((self.root / "package.skill").read_bytes(), original)

    def test_same_inputs_produce_same_archive(self):
        self.assertEqual(self.package("first.skill").returncode, 0)
        self.assertEqual(self.package("second.skill").returncode, 0)
        self.assertEqual(hashlib.sha256((self.root / "first.skill").read_bytes()).hexdigest(),
                         hashlib.sha256((self.root / "second.skill").read_bytes()).hexdigest())
