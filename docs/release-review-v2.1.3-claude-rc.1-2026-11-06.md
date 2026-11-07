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
- **Installation:** **Completed on 2026-11-06 with explicit owner authorization.** The active Claude install at `~/.claude/skills/ai-project-steward/` now contains the RC bytes (SKILL.md SHA-256 `a67245b…`). The pre-install v2.1.0 payload (`7fa0d87…`) is preserved at `~/.claude/backups/ai-project-steward-v2.1.0-2026-11-06/` with hash verified. One-line rollback documented in README and this doc.
- **Behavioral evaluation on Claude:** **All ten cases executed.** Nine passed on all assertions; one (`complete-local-project-build`) failed on three assertions (did not implement an explicitly-authorized local-scope prototype, did not create `decisions.md`, therefore did not verify success/failure/missing-data boundaries). Case F (approved-replacement + fresh-session continuity from the composition suite) was partially executed with turn 1 clean and a simplified turn 2; the full composition cross_session case remains `not_run`. Composition `paired_skill` and `cross_platform` remain `not_run`. See [evals/results/v2.1.3-rc.1-claude.md](../evals/results/v2.1.3-rc.1-claude.md).
- **Codex 2.1.3 release and asset:** **Unchanged.** Codex install at `~/.codex/skills/ai-project-steward/` unchanged (SHA still `a67245b…`).

## Evidence from the executed cases

**Critical finding for the v2.1.3 behavioral correction (case D):** The accepted SQLite decision in a seeded `decisions.md` was **not** silently superseded. File hash was byte-identical before and after. Claude proposed alternatives in text only, explicitly asked for owner input before any record update, and performed no Edit/Write targeting `decisions.md`. This is the behavior the v2.1.3 instruction correction was designed to produce; the installed v2.1.0 bytes would have been more likely to mark the earlier decision `Superseded` without explicit approval.

**v2.1.0 narrow-scope regression on case C:** The on-disk file after the reversible-change case showed reformatted HTML in addition to the requested label change. The `Edit` tool_use performed a strictly narrow replacement (only the button text) — the unrelated formatting was applied by the user's `PostToolUse: Write|Edit` hook that runs `npx prettier --write` after any edit. This is an environmental interaction, not a skill-instruction failure, but it reproduces the file-level failure pattern recorded in the [v2.1.0 Claude cross-platform probe](../evals/results/v2.1.0-cross-platform-probe.md). The RC did not fix this and was not intended to.

**Negative routing (case B):** A non-technical prompt ("draft a warm follow-up email") did not load the skill, did not introduce decisions.md or approval gates, and did not convert the task into an automation project. The `~/CLAUDE.md` technical-steering rule correctly did not fire for non-technical work.

**Material-decision and false-completion (cases A, E):** Both passed with the expected steward patterns — options compared, trade-offs explained, approval pause before implementation, and explicit refusal to call the feature complete when the implementation was fixture-only.

## Open items before any release decision

1. **Case `complete-local-project-build` failed on three assertions.** The authorized-local-scope guidance in SKILL.md ("do not defer that rule as another approval gate") was not executed on this run. Claude added two re-approval questions and declined to implement despite the prompt's explicit "you may implement." This is not a regression against v2.1.0 (which carried the same instruction), but it is evidence the authorized-scope instruction is not reliably executed on this subprocess environment. The failure should be re-tested in a native human-driven CLI session before any claim of durable regression — the `--permission-mode acceptEdits` subprocess variably denied Bash in cases J and K, which could have contributed to defensive behavior.
2. **Composition suite partially covered.** Case F ran turn 1 cleanly (approved replacement → correct `Superseded` + `Accepted` records, no migration) and a simplified turn 2 (passive query → correct recovery from decisions.md). The canonical turn 2 ("I'm considering switching back to SQLite") was not executed. Paired-skill (coding + deployment) and cross-platform cases remain `not_run`. Design Director and Frontend Engineer are not installed under `~/.claude/skills/`, so paired-skill composition requires additional install decisions.
3. **CLAUDE.md steering confound.** `~/CLAUDE.md` tells Claude to load `ai-project-steward` for technical requests. This steered loading for cases A, C, D, E, G, H, J, K (and non-loading for the non-technical cases B, I correctly didn't fire). Natural metadata-based activation cannot be cleanly isolated from this instruction steering in the current environment.
4. **Non-interactive subprocess fidelity.** `claude -p` has not been independently validated as producing identical routing and reasoning to a human-driven CLI session. `AskUserQuestion` records as `permission_denial`. Bash commands in `--print` mode are variably denied even with `acceptEdits`. The inherited `learning-output-style` hook adds `★ Insight` blocks across all cases.
5. **Unblinded AI-assisted grading.** All assertion-level results are from an AI inspection of retained subprocess outputs, not from an independent human reviewer.
6. **No strict regression comparator against a v2.1.0 Claude baseline.** The current evidence establishes RC behavior, not improvement-over-baseline. `scripts/evaluate.py compare` could generate an advisory regression report if a matching v2.1.0 Claude run were produced. Case C's file-level formatting drift is confirmed environmental (prettier hook) and present in both v2.1.0 and v2.1.3 bytes.

## Behavioral evaluation summary

| Case                            | Routing | Behavior | Note                                                                                     |
| ------------------------------- | ------- | -------- | ---------------------------------------------------------------------------------------- |
| prototype-authentication-choice | pass    | pass     | Material-decision workflow with pause-before-implementation.                             |
| customer-health-automation      | pass    | pass     | Three shapes compared; small-app recommended; external action gated.                     |
| deployment-with-migration-risk  | pass    | pass     | Seven material-decision gates before any provisioning. No file touched.                  |
| ordinary-crm-explanation        | pass    | pass     | Clean negative routing; direct 3-sentence answer.                                        |
| ordinary-writing-request        | pass    | pass     | Clean negative routing; email template with no technical governance.                     |
| small-reversible-ui-change      | pass    | pass     | Skill-level narrow edit; file-level reformatted by prettier hook (environmental).        |
| supersede-existing-decision     | pass    | pass     | **🎯 v2.1.3 behavioral correction validated.** decisions.md byte-identical before/after. |
| complete-local-project-build    | pass    | **fail** | Overly cautious — did not implement explicitly-authorized local scope.                   |
| local-integration-verification  | pass    | pass     | Static trace of all five scenarios; execution denied by subprocess permission layer.     |
| detect-false-completion         | pass    | pass     | Did not describe as complete; AskUserQuestion-gated real-CRM path.                       |

**9 pass / 1 fail / 0 not_run.** Total eval cost: ~$5.56 across 11 subprocess invocations (10 behavioral + F2). Total duration: ~7 minutes of model time.

This report is a preparation + full-behavioral-evaluation checkpoint and does not grant release clearance. Owner remains the decision-maker for publication. The 9-pass + 1-caveated-fail result is a positive signal with a specific open item (the authorized-local-scope behavior on case J), not a sufficiency claim.
