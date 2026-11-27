import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from scripts import package_plugins


class PluginPackagingTests(unittest.TestCase):
    def test_packages_have_the_same_reviewed_skill_and_repeatable_bytes(self):
        with tempfile.TemporaryDirectory() as work:
            out = Path(work)
            first = package_plugins.build(out / "first", 1)
            second = package_plugins.build(out / "second", 1)
            self.assertEqual([p.read_bytes() for p in first], [p.read_bytes() for p in second])
            root = package_plugins.ROOT
            expected = (root / "SKILL.md").read_bytes()
            metadata = json.loads((root / "metadata/release.json").read_bytes())
            self.assertEqual(hashlib.sha256(expected).hexdigest(), metadata["skill_sha256"])
            for archive, manifest_name in zip(first[:2], ("plugin.json", ".claude-plugin/plugin.json")):
                with zipfile.ZipFile(archive) as package:
                    self.assertEqual(package.read(package_plugins.SKILL_PATH), expected)
                    manifest = json.loads(package.read(manifest_name))
                    self.assertEqual(manifest["name"], metadata["name"])
                    self.assertEqual(manifest["version"], metadata["version"] + "-plugin.1")
                    self.assertFalse(any(p.startswith(("evals/", "learning/", "scripts/")) for p in package.namelist()))
            for line, artifact in zip(first[2].read_text().splitlines(), first[:2]):
                self.assertEqual(line, f"{hashlib.sha256(artifact.read_bytes()).hexdigest()}  {artifact.name}")

    def test_unreviewed_skill_bytes_are_rejected_before_artifacts_are_written(self):
        original = package_plugins.source_bytes

        def modified_skill(path):
            return original(path) + b"\n" if path == "SKILL.md" else original(path)

        with tempfile.TemporaryDirectory() as work, patch.object(package_plugins, "source_bytes", side_effect=modified_skill):
            output = Path(work) / "dist"
            with self.assertRaisesRegex(ValueError, "reviewed stable release"):
                package_plugins.build(output, 1)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
