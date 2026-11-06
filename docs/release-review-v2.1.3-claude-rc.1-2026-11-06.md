# AI Project Steward 2.1.3 Claude release-candidate preparation review

**Review date:** 2026-11-06
**Disposition:** **HOLD release and installation.** Preparation-only. No release tag, no asset publication, no installation change is authorized by this document.
**Scope:** Claude release candidate `2.1.3-rc.1-claude`. The published Codex stable release [v2.1.3](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.3) is unchanged by this preparation.

## Release scope and boundaries

Promote the existing Codex v2.1.3 instruction payload — SKILL.md SHA-256 `a67245b3797c837d58f94010ce1930352bb15865e514331b8a2dc66a748f9c16` — to the Claude surface, without any instruction-byte changes and without altering the published Codex asset. Package exactly the same eight-file distribution manifest. Replace only `metadata/release.json` with a Claude-scoped candidate variant that declares `status: candidate`, `publication_status: unreleased`, `release_approved: false`, and `installation_approved: false`.

Do **not** incorporate experimental recursive-learning instructions, specialist-skill changes, additional platform-interface files (`agents/anthropic.yaml` is explicitly omitted per the 2026-11-06 decision), new validator rules, or packaging-script changes. Do not imply this release establishes three-platform certification, autonomous learning, or Design Director / Frontend Engineer availability on Claude.

## Evidence reviewed

- **Agent Skills spec compliance.** SKILL.md frontmatter `name: ai-project-steward` (18 chars, lowercase-alphanumeric-hyphens, matches parent directory) and `description` (473 chars) satisfy the published Agent Skills spec (`name` ≤ 64 chars; `description` 1-1024 chars, non-empty, no XML tags). Verified against the current platform.claude.com Agent Skills overview and the agentskills.io specification.
- **Package integrity.** The RC archive `dist/ai-project-steward-2.1.3-rc.1-claude.zip` contains exactly the eight manifest entries. SHA-256: `89fc8c7ec16a2e53073cba3ee4dbb265331e15ca5cc9ec6448641b43a9dc98fc`. Seven shared files (SKILL.md, LICENSE, agents/openai.yaml, assets/icon-small.png, assets/icon-large.svg, learning/README.md, distribution-manifest.txt) are byte-identical to the current source. Archived SKILL.md hash matches the published Codex v2.1.3 payload exactly. Only `metadata/release.json` differs: the RC variant declares Claude candidate scope and no release/installation approval.
- **Source checks.** `python3 scripts/evaluate.py validate` passes. All 42 unit tests pass (`python3 -m unittest discover -s tests -v`). Source tree is unchanged from HEAD `1f98b6f3539498f880d5c37f2595c9842894e79a` except for `decisions.md` additions and the untracked `dist/` artifacts.
- **Install-site survey.** The machine has one existing Claude install at `~/.claude/skills/ai-project-steward/SKILL.md` with SHA-256 `7fa0d8789c4b09ac80d8195e5dd71be25986cba5056962bfa18c2414c0dea57e` — this is the **v2.1.0** instruction payload, dated September 4, 2026. No `metadata/`, `agents/`, or other files are present under that directory. The Codex install at `~/.codex/skills/ai-project-steward/` is the complete published v2.1.3 asset. Design Director and Frontend Engineer are not present under `~/.claude/skills/`.
- **Prior Claude evidence.** Only [v2.1.0 cross-platform probe](../evals/results/v2.1.0-cross-platform-probe.md) exists as retained Claude-specific evaluation: material-decision case passed, ordinary-request case passed, reversible-change case **failed narrow-scope fidelity** (correct label change but unrelated HTML formatting also changed). No v2.1.2 or v2.1.3 Claude-specific evaluation record is retained in this repository.

## Readiness judgment

**Positive.** Zero instruction-byte change; the Codex v2.1.3 behavioral correction (accepted-decision preservation until approved replacement) carries over unchanged. Agent Skills spec compliance confirmed from the current authoritative documentation. Reproducible package build with deterministic timestamps. Source validator and all existing tests pass.

**Open.** No behavioral or routing evaluation has been executed on the RC bytes against any Claude surface. The currently installed Claude `SKILL.md` is v2.1.0 bytes, not the RC bytes; its known narrow-scope reversible-change regression is unresolved. No live claude.ai zip-upload run has been performed. No Claude Code fresh-session routing or restraint evidence exists for the RC. Design Director and Frontend Engineer are absent from `~/.claude/skills/`, so paired-skill composition cannot be exercised on this machine without additional installation decisions.

These limitations do not prove 2.1.3 will regress on Claude, nor do they establish parity. The owner's explicit instruction forbids overwriting the active Claude installation. The Agent Skills spec requires the installed skill directory name to match the `name` frontmatter field, which prevents a sandbox install under a differently named directory without altering the instruction bytes. Behavioral evaluation therefore requires the owner's separate authorization to replace the current v2.1.0 Claude install with the RC bytes (and back it up first).

## Completion plan: five steps

1. **Scope and preparation (this document).** Lock the eight-file manifest, the Claude-scoped `metadata/release.json`, and the `ai-project-steward-2.1.3-rc.1-claude.zip` + checksum. No instruction change, no new validator rule, no new packaging flag.
2. **Pre-install authorization.** Owner explicitly authorizes: (a) backing up `~/.claude/skills/ai-project-steward/SKILL.md` (v2.1.0) and any adjacent files to a dated path outside the active skill-search directory; (b) installing the RC payload bytes (SKILL.md + metadata/release.json + supporting files) into `~/.claude/skills/ai-project-steward/`; (c) accepting that routing and behavior will be observed against the RC bytes. Record hashes before and after.
3. **Fresh-session behavioral evaluation.** Run the ten behavioral cases in `evals/evals.json` across fresh Claude Code CLI conversations against the installed RC. Run the five smoke cases this preparation has already defined (natural routing on technical planning, non-routing on ordinary writing, routine proportionality, unapproved decision preservation, approved replacement with fresh-session continuity). Record outcomes, failure assertions, and evidence hashes in `evals/runs/v2.1.3-rc.1-claude/behavioral.json`. Pay specific attention to the v2.1.0 reversible-change narrow-scope regression.
4. **Package parity re-check and PR update.** Rerun `scripts/evaluate.py validate`, the 42-test unit suite, and parity checks against the staged RC archive. Update this review document, `evals/results/v2.1.3-rc.1-claude.md`, and the draft PR with real evidence. Do not relabel incomplete records as passes.
5. **Owner disposition.** Owner decides whether to publish (new tag or asset addition under v2.1.3, per the 2026-11-06 tag-strategy decision), hold, or iterate. Publication, installation outside this scratch pilot, and any change to the Codex release remain separately authorized.

## Current state

- **Source review:** Complete for packaging and spec-compliance questions.
- **Behavioral evaluation on Claude:** **Not performed.** All ten behavioral and all three composition cases recorded as `not_run` with explicit documentation of why.
- **Installation:** **Not performed.** Existing v2.1.0 Claude install remains in place; Codex v2.1.3 install remains in place.
- **Codex 2.1.3 release and asset:** **Unchanged.**

This report is a preparation checkpoint and does not grant release or installation clearance. Owner authorization is required before Step 2.
