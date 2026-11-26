#!/usr/bin/env python3
"""Build deterministic native plugin candidates from the reviewed skill payload."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "ai-project-steward"
TITLE = "AI Project Steward"
REPOSITORY = "https://github.com/glichtenthal/ai-project-steward"
DESCRIPTION = (
    "Guide human-led AI builds through material choices, decision continuity, "
    "approval boundaries, and verification."
)
SKILL_PATH = f"skills/{NAME}/SKILL.md"


def source_bytes(path: str) -> bytes:
    file = ROOT / path
    if file.resolve() != file or not file.is_file():
        raise ValueError(f"Missing or linked source: {path}")
    return file.read_bytes()


def json_bytes(data: dict) -> bytes:
    return (json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode()


def build(output: Path, iteration: int) -> list[Path]:
    metadata = json.loads(source_bytes("metadata/release.json"))
    skill = source_bytes("SKILL.md")
    skill_hash = hashlib.sha256(skill).hexdigest()
    if (
        metadata["name"] != NAME
        or metadata["status"] != "stable"
        or not re.fullmatch(r"\d+\.\d+\.\d+", metadata["version"])
        or skill_hash != metadata["skill_sha256"]
    ):
        raise ValueError("Skill bytes must match the reviewed stable release metadata")
    if iteration < 1:
        raise ValueError("Plugin candidate iteration must be positive")
    version = f'{metadata["version"]}-plugin.{iteration}'
    common = {
        "name": NAME,
        "version": version,
        "description": DESCRIPTION,
        "author": {"name": "Greg Lichtenthal"},
        "homepage": REPOSITORY,
        "repository": REPOSITORY,
        "license": "MIT",
    }
    openai_manifest = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        **common,
        "extensions": {
            "com.openai": {
                "interface": {
                    "displayName": TITLE,
                    "shortDescription": "Human-led AI builds",
                    "longDescription": DESCRIPTION + " Plugin release candidate.",
                    "developerName": "Greg Lichtenthal",
                    "category": "Productivity",
                    "capabilities": ["Interactive"],
                    "defaultPrompt": "Use AI Project Steward to manage this build through verification.",
                    "logo": f"./skills/{NAME}/assets/icon-large.svg",
                    "composerIcon": f"./skills/{NAME}/assets/icon-small.png",
                    "brandColor": "#0E7C70",
                }
            }
        },
    }
    claude_manifest = common.copy()
    shared = {SKILL_PATH: skill, "LICENSE": source_bytes("LICENSE")}
    openai_files = {
        **shared,
        "plugin.json": json_bytes(openai_manifest),
        **{
            f"skills/{NAME}/{path}": source_bytes(path)
            for path in ("agents/openai.yaml", "assets/icon-small.png", "assets/icon-large.svg")
        },
    }
    claude_files = {
        **shared,
        ".claude-plugin/plugin.json": json_bytes(claude_manifest),
    }
    output.mkdir(parents=True, exist_ok=True)
    artifacts = []
    with tempfile.TemporaryDirectory(dir=output) as temporary:
        stage = Path(temporary)
        for platform, files in (("openai", openai_files), ("claude", claude_files)):
            filename = f"{NAME}-{version}-{platform}.zip"
            archive = stage / filename
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
                for path, content in sorted(files.items()):
                    entry = zipfile.ZipInfo(path, date_time=(2000, 1, 1, 0, 0, 0))
                    entry.compress_type = zipfile.ZIP_DEFLATED
                    entry.external_attr = 0o100644 << 16
                    package.writestr(entry, content)
            with zipfile.ZipFile(archive) as package:
                if package.testzip() or sorted(package.namelist()) != sorted(files):
                    raise ValueError(f"Invalid archive membership: {platform}")
                for path, content in files.items():
                    if package.read(path) != content:
                        raise ValueError(f"Archive byte mismatch: {path}")
            artifacts.append(archive)
        sums = stage / "STEWARD-PLUGIN-SHA256SUMS"
        sums.write_text(
            "".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n" for path in artifacts),
            encoding="utf-8",
        )
        for path in (*artifacts, sums):
            path.replace(output / path.name)
    return [output / path.name for path in (*artifacts, sums)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist" / "plugins")
    parser.add_argument("--iteration", type=int, default=1)
    args = parser.parse_args()
    for artifact in build(args.output_dir.resolve(), args.iteration):
        print(artifact)


if __name__ == "__main__":
    main()
