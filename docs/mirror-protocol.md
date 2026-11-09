# Codex → Claude Mirror Protocol

How to mirror a published Codex release into a parallel Claude Code release (and, when applicable, claude.ai) using the same instruction bytes.

## Goal

Publish a Claude Code release that carries **the identical skill instruction payload** as the corresponding Codex release, with evidence of behavior on Claude surfaces and explicit owner authorization.

## Invariant

**The skill bytes are shared across surfaces; the validation records are not.**

- `SKILL.md` and the installable `ai-project-steward/` payload have one SHA-256 per version. Every per-surface release (`vX.Y.Z` for Codex, `vX.Y.Z-claude` for Claude Code) references this same hash.
- Each surface gets its own release metadata file (`metadata/release.json` for Codex, `metadata/release-claude.json` for Claude Code), its own evidence record under `evals/results/`, and its own GitHub tag + release.
- The `instruction_bytes_identical_to_codex_vX_Y_Z: true` claim in `metadata/release-claude.json` is independently verifiable by comparing the SHA; if it is ever false, treat that as a packaging bug and fix before proceeding.

This is why one repo serves multiple releases: shared bytes, per-surface audit trails.

## Trigger

A new Codex release (`vX.Y.Z`) ships on GitHub with:

- An annotated tag `vX.Y.Z`
- A GitHub release with `ai-project-steward-X.Y.Z-codex.zip` + `STEWARD-SHA256SUMS`
- `metadata/release.json` updated to reflect the new release
- The instruction bytes committed at some `instruction_commit` SHA

## The Seven-Step Sequence

### Step 1 — Verify byte-identity before anything else

```bash
# Pull the latest main
git checkout main && git pull origin main

# Verify the SKILL.md on main matches the Codex release's published skill_sha256
jq -r '.skill_sha256' metadata/release.json
shasum -a 256 SKILL.md
# These must match. If they don't, the Codex release is misaligned with main; stop and investigate.
```

### Step 2 — Create the RC branch and update the RC metadata

```bash
git checkout -b prepare/claude-X.Y.Z-rc.1

# Update the installed RC metadata at ~/.claude/skills/ai-project-steward/metadata/release.json
# to point at the new instruction commit + Codex stable release.
```

The RC `release.json` fields that need updating each cycle:

- `version`: `X.Y.Z-rc.1-claude`
- `date`: today's date
- `source.base_commit` / `source.instruction_commit`: the Codex instruction commit
- `source.codex_stable_release`: `vX.Y.Z`
- `source.codex_stable_commit`: the Codex release commit SHA
- `skill_sha256`: the shared hash
- `release_approved` / `installation_approved`: both `false` at RC stage

### Step 3 — Run the behavioral suite on Claude Code

Ten cases live in `evals/evals.json`. Run them against the RC bytes via a mix of:

- Fresh `claude -p` subprocesses for the eight cases that don't require native interaction
- Native interactive CLI runs for cases that fail or produce `permission_denial` under `--print` (historically case J; may evolve)

Record each case's output to `evals/runs/vX.Y.Z-rc.1-claude/outputs/<case>.md` and the aggregate to `evals/runs/vX.Y.Z-rc.1-claude/behavioral.json`.

### Step 4 — Run the composition suite on Claude Code

Four cases live in `evals/composition.json`:

- `coding-skill-collaboration` — pair with `production-frontend-engineer`; native CLI session
- `cross-session-decision-continuity` — two turns in separate fresh native CLI sessions; reset the workdir fixture to the seed before turn 1
- `deployment-skill-collaboration` — pair with a deployment skill if installed, else `production-frontend-engineer` under a documented loosened interpretation; native CLI session
- `cross-platform-essential-behavior` — requires identical bytes on at least three skill-capable platforms

**Workdir discipline for native-CLI runs:** use a one-line launcher script with `cd ~/path || exit 1` to make the working directory a hard gate. Multi-line pastes split under terminal auto-wrap and silently drop the `cd`, causing Claude to attach to the home directory and real user projects. This has happened twice in historical runs; both required cleanup.

Record each case to `evals/runs/vX.Y.Z-rc.1-claude/outputs/<case>.md` and the aggregate to `evals/runs/vX.Y.Z-rc.1-claude/composition.json`.

### Step 5 — Open the evidence PR into main

Draft the PR body with:

- Behavioral aggregate (`X pass / Y fail / Z not_run`)
- Composition aggregate (`X pass / Y fail / Z not_run`)
- Links to each evidence file
- Per-case bounded exceptions (grading caveats that reviewers must accept or reject before authorization)
- The `skill_sha256` claim

Reviewer confirms gradings and accepts any bounded exceptions in writing in the PR body or a review comment.

### Step 6 — Squash-merge, write authorization metadata, commit

After PR approval:

```bash
gh pr merge <N> --squash --delete-branch
git checkout main && git pull origin main
```

Write `metadata/release-claude.json` (new file per release, or update if this is a repeat-authorization for the same version) mirroring the structure of the previous Claude release. Key fields that change each cycle:

- `version`, `date`, `skill_sha256`
- `source.instruction_commit`, `source.codex_stable_release`, `source.claude_evidence_merge_commit`
- `validation_scope`: short prose summary of what was run
- `tested_runtimes`: Claude Code CLI version
- `known_limitations`: the bounded exceptions
- `exception_acceptance`: dated owner acceptance statement

Commit with a message that enumerates the exceptions and names the merge commit of the evidence PR.

### Step 7 — Tag and cut the GitHub release

```bash
# Copy the RC-named zip to the stable name (byte-identical)
cp dist/ai-project-steward-X.Y.Z-rc.1-claude.zip dist/ai-project-steward-X.Y.Z-claude.zip
(cd dist && shasum -a 256 ai-project-steward-X.Y.Z-claude.zip > STEWARD-CLAUDE-SHA256SUMS)

# Annotated tag
git tag -a vX.Y.Z-claude -m "AI Project Steward X.Y.Z — Claude Code"
git push origin vX.Y.Z-claude

# GitHub release with the two assets and a release-note body that mirrors
# the Codex v2.1.3 release body pattern.
gh release create vX.Y.Z-claude \
  dist/ai-project-steward-X.Y.Z-claude.zip \
  dist/STEWARD-CLAUDE-SHA256SUMS \
  --title "AI Project Steward X.Y.Z — Claude Code" \
  --notes "$(cat <<'EOF'
# Release notes body — mirror the v2.1.3-claude pattern
EOF
)"
```

## When claude.ai is added as a third surface

Mirror the same seven-step pattern with:

- Evidence directory: `evals/runs/vX.Y.Z-rc.1-claude-web/`
- Metadata file: `metadata/release-claude-web.json`
- Tag: `vX.Y.Z-claude-web`
- GitHub release asset name: `ai-project-steward-X.Y.Z-claude-web.zip`

Each surface's authorization is independently revocable; adding one does not implicitly authorize another.

## Division of labor (when an AI assistant helps)

An assistant can own, end-to-end:

- Byte-identity verification (Step 1)
- RC branch creation and metadata update (Step 2)
- Behavioral subprocess runs (Step 3, subprocess-safe cases)
- Evidence file authoring from a known-good transcript
- PR authorship + merge (Step 5–6, with explicit owner authorization at merge)
- Tag and release creation (Step 7, with explicit owner authorization)

What requires the human partner at the terminal:

- Native interactive CLI runs for composition cases
- Multi-platform runs for `cross-platform-essential-behavior`
- Explicit acceptance of bounded exceptions before authorization is written

The historical pattern: assistant prepares the launcher script, the human pastes `sh /tmp/run-<case>-eval.sh` and the canonical prompt, then pastes the transcript back for grading and evidence-file authoring.

## References

- First published Claude Code release following this pattern: [`v2.1.3-claude`](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.3-claude)
- Corresponding Codex release: [`v2.1.3`](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.3)
- Evidence PR for the first Claude Code release: [#8](https://github.com/glichtenthal/ai-project-steward/pull/8)
- Release review document: [`docs/release-review-v2.1.3-claude-rc.1-2026-11-06.md`](release-review-v2.1.3-claude-rc.1-2026-11-06.md)
