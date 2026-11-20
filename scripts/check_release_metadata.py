#!/usr/bin/env python3
"""Reject a release archive whose packaged metadata is not a stable, approved release.

Usage:
  python3 scripts/check_release_metadata.py ARCHIVE [ARCHIVE ...] [--expect-version X.Y.Z]
      [--superseded metadata/superseded-assets.json]

Checks each archive's ai-project-steward/metadata/release.json:
  - version is a plain X.Y.Z (no -rc or other pre-release suffix) and matches --expect-version
  - status is "stable"; publication_status, when present, is "stable_release"
  - release_approved is true
  - skill_sha256 equals the SHA-256 of the archived SKILL.md
Archives whose SHA-256 is listed in the superseded file are reported and skipped, so a
corrected release can keep its original asset as an audit record.
Standard library only. Exit status 0 when at least one checked archive passes and none fail.
"""
import argparse
import hashlib
import json
import re
import sys
import zipfile

ROOT = "ai-project-steward/"
VERSION = re.compile(r"^\d+\.\d+\.\d+$")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def problems(archive_path, expect_version=None):
    """Return a list of human-readable problems; empty means the archive passes."""
    try:
        archive = zipfile.ZipFile(archive_path)
    except (OSError, zipfile.BadZipFile) as error:
        return [f"cannot open archive: {error}"]
    with archive:
        names = set(archive.namelist())
        missing = [n for n in (ROOT + "SKILL.md", ROOT + "metadata/release.json") if n not in names]
        if missing:
            return [f"missing {', '.join(missing)}"]
        try:
            meta = json.loads(archive.read(ROOT + "metadata/release.json"))
        except ValueError as error:
            return [f"metadata/release.json is not valid JSON: {error}"]
        skill = sha256(archive.read(ROOT + "SKILL.md"))

    found = []
    version = str(meta.get("version", ""))
    if not VERSION.match(version):
        found.append(f"version {version!r} is not a stable X.Y.Z release")
    elif expect_version and version != expect_version:
        found.append(f"version {version!r} does not match expected {expect_version!r}")
    if meta.get("status") != "stable":
        found.append(f"status is {meta.get('status')!r}, expected 'stable'")
    if "publication_status" in meta and meta["publication_status"] != "stable_release":
        found.append(f"publication_status is {meta['publication_status']!r}, expected 'stable_release'")
    if meta.get("release_approved") is not True:
        found.append(f"release_approved is {meta.get('release_approved')!r}, expected true")
    if meta.get("skill_sha256") != skill:
        found.append(f"skill_sha256 {meta.get('skill_sha256')!r} does not match archived SKILL.md {skill}")
    return found


def load_superseded(path):
    if not path:
        return {}
    with open(path, encoding="utf-8") as handle:
        entries = json.load(handle)
    return {entry["sha256"]: entry for entry in entries}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("archives", nargs="+")
    parser.add_argument("--expect-version")
    parser.add_argument("--superseded", help="JSON list of {sha256, asset, reason, replacement}")
    args = parser.parse_args(argv)
    superseded = load_superseded(args.superseded)
    failed = False
    checked = 0
    for path in args.archives:
        with open(path, "rb") as handle:
            digest = sha256(handle.read())
        if digest in superseded:
            entry = superseded[digest]
            print(f"SKIP {path}: superseded asset {entry.get('asset')} ({entry.get('reason')}); "
                  f"replacement {entry.get('replacement')}")
            continue
        checked += 1
        found = problems(path, args.expect_version)
        if found:
            failed = True
            print(f"FAIL {path} (sha256 {digest})")
            for problem in found:
                print(f"  - {problem}")
        else:
            print(f"PASS {path} (sha256 {digest})")
    if checked == 0:
        print("FAIL: no non-superseded archives were validated")
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
