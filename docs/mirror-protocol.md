# Multi-Surface Release Protocol

How to validate the AI Project Steward skill on multiple surfaces (Codex CLI, Claude Code, claude.ai) using the same instruction bytes, and record each surface's authorization inside a single GitHub release.

## Goal

Publish **one release per instruction-payload version**, with explicit per-surface validation evidence and owner authorization listed in release metadata and release notes.

Earlier terminology called this a "mirror protocol" because the first Claude Code release (`v2.1.3-claude`) was cut as a separate tag that mirrored the Codex release. Starting with v2.1.4, we consolidate.

## Deprecation note: the 2.1.3 per-surface-release pattern

The v2.1.3 cycle used **separate tags per surface**: `v2.1.3` (Codex only) and `v2.1.3-claude` (Claude Code). Each had its own metadata file (`metadata/release.json` and `metadata/release-claude.json`) and its own GitHub release. Both remain in the repo as the audit trail of that cycle; nothing about them is retroactively edited.

Reasons we moved away from it:

- Users see two "AI Project Steward 2.1.3" releases for identical bytes, which is confusing.
- The release count doubles over time; most of the duplicated content is boilerplate.
- Per-surface revocable authorization isn't a requirement for an open-source publication — a single release listing validated surfaces is honest enough.

**Starting with v2.1.4**, use the single-release model described below.

## Invariant

The skill bytes are shared across surfaces; the validation records are not.

- `SKILL.md` and the installable `ai-project-steward/` payload have one SHA-256 per version. The release references this hash.
- Each surface produces its own evidence record under `evals/results/` and its own entry in `metadata/release.json`'s `validated_surfaces` array.
- The release can grow over time: surfaces are added to the same release as their evidence lands.

## Trigger

A new instruction-payload version is ready to be published. The usual pattern:

- First surface (currently Codex) ships their evaluation evidence and opens a release PR
- The `vX.Y.Z` tag is cut and the GitHub release is published with the first surface validated
- Additional surfaces (currently Claude Code, later claude.ai) add their evidence to the same release over time

A surface's SHA check is Step 1 every time, to prove the bytes haven't drifted.

## The Sequence (per surface adding validation)

### Step 1 — Verify byte-identity before anything else

```bash
git checkout main && git pull origin main

# The release metadata's claimed SKILL.md hash:
jq -r '.skill_sha256' metadata/release.json

# The hash of the SKILL.md file on disk:
shasum -a 256 SKILL.md
```

These must match. If they don't, the release is misaligned with `main`; stop and investigate before running any eval.

If this is a doc-only Codex push with unchanged skill bytes, **no new release is needed and no new validation is required.** Just leave the latest release in place.

### Step 2 — Create the surface RC branch and update RC metadata

```bash
git checkout -b prepare/<surface>-X.Y.Z-rc.1
```

Update the installed RC metadata at `~/.claude/skills/ai-project-steward/metadata/release.json` (or the equivalent for other surfaces) to point at this version. Fields that change each cycle:

- `version`: `X.Y.Z-rc.1-<surface>`
- `date`: today's date
- `source.instruction_commit`: the commit where the SKILL.md bytes were authored
- `skill_sha256`: the shared hash
- `release_approved` / `installation_approved`: both `false` while RC is pending

### Step 3 — Run the behavioral suite on this surface

Ten cases live in `evals/evals.json`. Run them against the RC bytes via:

- Fresh `claude -p` / equivalent subprocess calls for cases that work non-interactively
- Native interactive CLI runs for cases that fail or return `permission_denial` under `--print`-equivalent modes (historically case J on Claude Code)

Record each case's output to `evals/runs/vX.Y.Z-rc.1-<surface>/outputs/<case>.md` and the aggregate to `evals/runs/vX.Y.Z-rc.1-<surface>/behavioral.json`.

### Step 4 — Run the composition suite on this surface

Four cases live in `evals/composition.json`:

- `coding-skill-collaboration` — pair with the surface's installed coding/frontend skill in a native CLI session
- `cross-session-decision-continuity` — two turns in separate fresh native CLI sessions; reset the workdir fixture to the seed before turn 1
- `deployment-skill-collaboration` — pair with a dedicated deployment skill if available, else a scope-adjacent skill (document the loosened interpretation if so)
- `cross-platform-essential-behavior` — requires identical bytes on at least three skill-capable platforms; typically graded by combining per-surface records across releases

**Workdir discipline for native-CLI runs:** use a one-line launcher script with `cd ~/path || exit 1` to make the working directory a hard gate. Multi-line pastes split under terminal auto-wrap and silently drop the `cd`, causing the agent to attach to the home directory and real user projects. This has happened twice in historical runs; both required cleanup.

Record each case to `evals/runs/vX.Y.Z-rc.1-<surface>/outputs/<case>.md` and the aggregate to `evals/runs/vX.Y.Z-rc.1-<surface>/composition.json`.

### Step 5 — Open the evidence PR into main

Draft the PR body with:

- Behavioral aggregate (`X pass / Y fail / Z not_run`)
- Composition aggregate (`X pass / Y fail / Z not_run`)
- Links to each evidence file
- Per-case bounded exceptions (grading caveats that require explicit owner acceptance)
- The `skill_sha256` claim

Owner confirms gradings and accepts any bounded exceptions in writing in the PR body or a review comment before merge.

### Step 6 — Squash-merge, update release.json's validated_surfaces array

After PR approval:

```bash
gh pr merge <N> --squash --delete-branch
git checkout main && git pull origin main
```

Open `metadata/release.json`. If `validated_surfaces` doesn't exist yet, add it as an empty array. Append a new surface entry:

```json
{
  "surface": "<surface name>",
  "status": "approved_with_bounded_exceptions",
  "date": "<YYYY-MM-DD>",
  "tested_runtimes": ["<runtime and version>"],
  "evidence_summary": "evals/results/vX.Y.Z-rc.1-<surface>.md",
  "release_review": "docs/release-review-vX.Y.Z-<surface>-rc.1-<date>.md",
  "known_limitations": ["<bounded exception 1>", "..."],
  "exception_acceptance": "Owner explicitly accepted ... on <date> ...",
  "evidence_merge_commit": "<short SHA from Step 5>"
}
```

Commit with a message naming the surface, the merge commit of the evidence PR, and enumerating the bounded exceptions.

### Step 7 — Update the release notes and (if needed) the release artifacts

**If this is the first surface validation for this version** (and the release hasn't been cut yet):

```bash
git tag -a vX.Y.Z -m "AI Project Steward X.Y.Z"
git push origin vX.Y.Z
gh release create vX.Y.Z \
  dist/ai-project-steward-X.Y.Z.zip \
  dist/STEWARD-SHA256SUMS \
  --title "AI Project Steward X.Y.Z" \
  --notes "<body listing the currently validated surface>"
```

**If the release already exists** (because a different surface validated first), edit the release notes to add this surface:

```bash
gh release edit vX.Y.Z --notes "<updated body listing all validated surfaces>"
```

The release body's "Validated surfaces" section should list each surface, its validation date, its evidence pointer, and its bounded exceptions.

### Note on release-artifact naming

Starting with v2.1.4, the stable zip is named `ai-project-steward-X.Y.Z.zip` (no `-codex` or `-claude` suffix), since the zip is the same bytes regardless of which surface validated. Historical per-surface-suffixed artifacts (`ai-project-steward-2.1.3-codex.zip`, `ai-project-steward-2.1.3-claude.zip`) remain in their releases as published; new releases drop the suffix.

## Division of labor (when an AI assistant helps with a surface validation)

An assistant can own, end-to-end:

- Byte-identity verification (Step 1)
- RC branch creation and metadata update (Step 2)
- Behavioral subprocess runs (Step 3, subprocess-safe cases)
- Evidence file authoring from a known-good transcript
- PR authorship + merge (Step 5–6, with explicit owner authorization at merge)
- `release.json` updates and release-note editing (Step 7, with explicit owner authorization)

What requires the human partner at the terminal:

- Native interactive CLI runs for composition cases
- Multi-platform runs for `cross-platform-essential-behavior`
- Explicit acceptance of bounded exceptions before authorization is written

The historical pattern: assistant prepares the launcher script, the human pastes `sh /tmp/run-<case>-eval.sh` and the canonical prompt, then pastes the transcript back for grading and evidence-file authoring.

## References

- First release using the single-release multi-surface pattern: `v2.1.4` (pending)
- Last release using the per-surface pattern (historical reference): [`v2.1.3`](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.3) (Codex), [`v2.1.3-claude`](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.3-claude) (Claude Code)
- First Claude Code evidence PR: [#8](https://github.com/glichtenthal/ai-project-steward/pull/8)
- Release review document for the Claude 2.1.3 cycle: [`docs/release-review-v2.1.3-claude-rc.1-2026-11-06.md`](release-review-v2.1.3-claude-rc.1-2026-11-06.md)
