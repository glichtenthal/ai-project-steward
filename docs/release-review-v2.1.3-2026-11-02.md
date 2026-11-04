# AI Project Steward 2.1.3 bounded release-readiness review

**Review date:** 2026-11-02  
**Original disposition (November 2):** **HOLD release and installation pending bounded evidence sign-off.** See the November 3 clearance addendum below for the current disposition.
**Scope:** Codex-only candidate 2.1.3-rc.1. The published stable release remains [v2.1.2](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.2).

## Release scope and boundaries

Promote only the already-merged Steward instruction correction: accepted project decisions stay accepted until the user explicitly approves a replacement. Include the existing evaluator integrity hardening, assertion-level regression comparisons, triage tooling and reviewed eight-file distribution manifest. The candidate's recorded instruction SHA-256 is `a67245b3797c837d58f94010ce1930352bb15865e514331b8a2dc66a748f9c16`.

Do **not** incorporate experimental recursive-learning instructions from [Steward PR #2](https://github.com/glichtenthal/ai-project-steward/pull/2), the held Frontend Engineer experiment, or any change to Design Director. Do not imply this release creates autonomous skill learning or a packaged multi-agent runtime.

## Evidence reviewed

- [Merged Steward PR #3](https://github.com/glichtenthal/ai-project-steward/pull/3) shows exactly one material `SKILL.md` paragraph correction, focused approved-versus-unapproved decision tests, added evidence integrity tests, and a restored deployment fixture.
- [Merged infrastructure PR #5](https://github.com/glichtenthal/ai-project-steward/pull/5) added schema 1.1 validation, assertion-level regression checks, minimal allowlisted packaging, and deterministic test coverage without changing the instruction payload.
- [Codex 2.1.3-rc.1 evaluation](../evals/results/v2.1.3-rc.1-codex.md) records 30 controller case executions, 29 completed. The candidate completed its scored runs; the baseline local build timed out. A routine-label natural-loading case missed expected skill source reads in **both** baseline and candidate. No general speed or routing improvement is demonstrated.
- Codex execution was spread across two CLI runtime versions; the full strict advisory comparison did **not** pass. Its published record explicitly keeps missing coverage, not-run checks, and limitations visible.
- [Package/CI checks](https://github.com/glichtenthal/ai-project-steward/actions) passed on the latest main commit reviewed on 2026-11-02. These validate source/package integrity and deterministic tests, not independent behavioral outcomes.
- The detailed raw traces, assertion reviews, and immutable candidate archive receipt are described as retained in a **private local** `codex-2.1.3-rc.1` packet. They were not available for independent review during this repository-only assessment.

## Readiness judgment

**Positive:** Small and comprehensible instruction change; observed focused improvement in preserving unapproved decisions; no new regression reported in completed paired comparisons; deployment/integration safeguards maintained; deterministic packaging and validator CI successful.

**Open:** Full advisory gate blocked; one baseline timeout and mixed runtime windows prevent a complete controlled claim; an existing natural-loading miss remains; human inspection of the private raw evidence has not been confirmed; production installation and fresh post-install activation have not occurred.

These limitations do not prove 2.1.3 is worse, and a bounded Codex-only release could disclose known routing limits. However, an unresolved advisory gate and unavailable raw evidence must not be silently recast as clearance or full human review. The user authorized a **conditional** five-step release workflow, not an invented pass or automatic bypass of recorded requirements.

## Completion plan: five steps

1. **Scope:** Keep the change set above. No experimental learning or specialist skill changes.
2. **Focused sign-off:** In the existing local Codex review workspace, inspect the retained baseline/candidate outputs, hashes, notes, decision-control runs, and interruptions; verify no unreported critical pass-to-fail assertion. Run only the missing, decision-relevant probes in one pinned current runtime if their evidence remains insufficient. Clearly document whether the shared routing miss and baseline timeout are accepted **known limitations**, or whether the current release gate demands remediation; do not claim strict regression clearance if it remains blocked. Record an explicit reviewer disposition and reviewed evidence locations without publishing private data.
3. **Release preparation:** Only after Step 2 is cleared or a specific scoped exception is explicitly approved, finalize v2.1.3 release metadata and the README/changelog. Retain the tested instruction bytes. Package exactly the reviewed manifest entries; run validation, deterministic tests, archive exact-membership/parity and SHA-256 checks. Record the source commit and artifact digest.
4. **Publication:** Use an authenticated GitHub release-capable environment to create the `v2.1.3` tag and release with the verified ZIP, checksum and bounded Codex-only release notes. Verify the actual published asset and links. Do not claim three-platform certification or autonomous recursive improvement.
5. **Local installation:** Only after a published, verifiable asset exists, inspect duplicate Steward sources in the user's active Codex configuration, back up the selected existing skill and configuration, install into one authoritative target, and test fresh-session positive/negative routing, decision replacement, and neighboring Design Director/Frontend Engineer availability. Restore the verified backup on failure.

## Current state

- **Source review:** Completed from publicly accessible repository evidence.
- **Focused evidence sign-off:** **Blocked** pending private local packet inspection and decision on known gate limitations.
- **Stable packaging and release:** **Not performed**; stable v2.1.2 remains the only published Steward release.
- **New installation:** **Not performed**; existing Codex, Design Director, Frontend Engineer, and Claude installations are unchanged by this review.

This report is a review checkpoint and does not itself grant release or installation clearance.

## November 3 clearance addendum

**Disposition: GO WITH EXPLICIT EXCEPTION REQUIRED.** The private evidence audit is complete for the narrow Codex-only instruction correction. No newly identified critical candidate regression was found in the inspected evidence. The strict regression gate **has not passed**. Publication and installation remain unauthorized by this review; the exception below requires the owner's explicit acceptance.

### Independently checked

The reviewer inspected the private original `codex-2.1.3-rc.1` packet, the merged review packet, actual baseline/candidate responses, command/event traces, saved decision artifacts, assertion judgments, timeout/interruption receipts, and the later limited-installation receipts. This is a fresh AI-assisted audit of retained executions, not independent human behavioral approval or a new model benchmark. Historical judgments and raw results were preserved unchanged.

- Source reviewed: main at `b696f3245e24415d979145cd59170660867b6e32`. Its `SKILL.md` matches the tested candidate, merged instruction commit `85a52d0`, and retained candidate packages: SHA-256 `a67245b3797c837d58f94010ce1930352bb15865e514331b8a2dc66a748f9c16`. Against stable `92b2cd7`, the instruction diff is exactly the accepted-decision paragraph correction.
- All **762** original manifest entries, **91** selected review copies and their originals, and **30** assertion-evidence file hashes verified. Original private bundle SHA-256: `cc4838fa7a5c4c0c3fea918d72adee734ec99a576985251c19bcffad68a69c00`; merged review bundle: `4b7ca4d9bf45cfbeff3ead18a7c9a03435363b6343e658c2d20a6b5b97089a4e`. Both ZIP CRC checks passed. These hashes establish retained byte identity, not independent execution provenance or human approval. Private traces and account-specific paths are not published here.
- For all **15** controller-recorded baseline/candidate pairs, prompts and initial project fixtures matched; runtime, model, reasoning, time limits, mounted companion instructions, browser adapter and workspace restrictions were comparable within each pair. The intended Steward instruction difference was retained. Runtime windows remain separate.
- The records contain **66 baseline** and **73 candidate** passing assertion judgments across **29 completed executions**. One baseline build is incomplete; missing cases remain `not_run`. Completed reviewed assertions showed no pass-to-fail candidate regression. This does not establish results for unexecuted cases or attribute safeguards solely to the skill: fixture instructions also prohibited external actions.

### Behavioral findings

| Question | Actual retained result |
| --- | --- |
| Unapproved replacement | In focused explicit-use repeat 22 on CLI 0.165, baseline marked SQLite **Superseded** while its replacement was still **Proposed**; candidate kept SQLite **Accepted** and the alternative **Proposed**. Candidate passed both focused repeats; baseline passed the other. Later native repeats passed in both arms. The narrow observed correction is supported; elimination of the failure is not established. |
| Approved replacement and continuity | Both arms on CLI 0.166 accepted explicitly approved PostgreSQL, superseded SQLite, and preserved that decision in a distinct fresh conversation. Only the decision record changed; architecture approval did not authorize migration, spending, connection or deployment. |
| Natural activation/nonactivation | Positive technical planning loaded Steward; ordinary CRM explanation and email writing did not. Routine-label natural activation failed in **both** arms on both runtime windows. The successful edit does not turn that routing failure into a pass. |
| Routine proportionality | Natural label edits changed only `index.html` and passed real local render/click checks without added approval gates or decision records. A separate explicitly activated pair also stayed proportional; skipped source loading alone is not evidence of active-skill overhead. |
| Safety and verification | Inspected migration, deployment, local-adapter and false-completion traces preserve external-action boundaries, secrets handling, backup/restore and rollback planning, and the distinction between synthetic checks and live completion. The five adapter conditions actually ran. Candidate local build retained eleven passing tests and desktop/mobile checks. No newly identified critical regression; no production or real-account verification is inferred. |

The baseline local build hit its declared **240-second** limit (exit `-15`, no retained final response); partial implementation is not scored as a completed pass or behavioral failure. The candidate completed, but this cannot support a general speed claim. Two separate false-completion attempts remain host-interrupted/incomparable: baseline events show browser-broker connection refusal; candidate has a completion event without the controller completion/snapshot receipts. Their recovered pair is separate, and neither interrupted attempt was promoted into the scores.

The instruction correction is the behavioral change. Schema/assertion validation, triage, regression reporting, evidence integrity and the eight-file allowlist are infrastructure improvements; their deterministic passes do not demonstrate better Steward behavior, recursive learning, or specialist improvements. No critical case in the 30 recorded executions was silently omitted from the audit; the timeout and unexecuted runtime/platform cases remain incomplete. Held experimental learning/security cases are outside this candidate's instruction delta and receive no clearance here.

### Additional checks and evaluation restraint

No additional model executions were necessary: the retained paired decision probes, approved-replacement/fresh-session case, explicit routine edit, natural positive/negative routing and safety traces answer the decision-relevant questions. Repeating them would not resolve the known routing failure or create a complete single-runtime matrix. No suite rerun or new evaluation framework was introduced.

Fresh checks on the reviewed checkout with Python **3.9.6**: source/suite validation passed; all **42** existing unit tests passed; package build verified exactly **eight** manifest files, CRC, membership and source-byte parity. The local **RC integrity-check artifact**, not a stable release artifact, has SHA-256 `80ef35356d8998dd36ba3710e02a3346fcb7027b3132b6be7a0bd624f94fb089`. The older 110-file private pilot ZIP remains historical evidence and must not be substituted for the current eight-file distribution.

The current comparator was also run in **regression mode** against all four retained runtime/suite combinations. All four returned blocked (`regression_clear: false`); all reported empty assertion-regression lists. Behavioral blockers remain the shared routing failure and incomplete per-window coverage/baseline build; composition also retains the unexecuted three-platform case. No records were pooled, routing expectations weakened, or gate failures relabeled as passes.

**Correction to the repository-only account above:** private receipts show an explicitly approved limited Codex pilot installation on October 31, followed by six smoke cases in seven fresh CLI conversations (28 provisional assertion passes; the native routine-routing miss remained). All **139** pilot evidence-manifest hashes verified, and all **110** files currently in that installed pilot match its receipt. Current Design Director and Frontend Engineer files also match the retained specialist hashes. That private pilot approval was not stable-release approval; it does not validate a future eight-file stable installation or desktop activation. No installation or specialist modification occurred in this clearance review.

### Exact exception and remaining work

The proposed exception is: **accept this one Codex-only 2.1.3 release on the inspected bounded evidence despite the blocked full-suite regression gate, specifically the shared routine-label natural-activation failure, mixed runtime/incomplete per-window matrix, inconclusive baseline build, and unexecuted cross-platform case.** Use explicit invocation when Steward coverage matters. Do not claim reliable automatic activation, full current-runtime or three-platform certification, general speed/cost gains, or proven elimination of decision-replacement errors. The evidence review is AI-assisted and unblinded; the owner still supplies the human release judgment. This exception waives no safety, approval or verification boundary and authorizes no instruction expansion.

Before publication: obtain explicit owner acceptance of that exception and separate release authorization; retain the tested instruction bytes; finalize stable version/status, README/changelog and bounded release notes; rerun the existing validation/tests and eight-file exact-membership/parity checks on that final source commit; record its artifact digest. Then, only when authorized, publish the tag/release and verify the downloaded asset/checksum. No additional behavioral suite is required unless source instructions change or a material regression emerges.

Before any stable installation: obtain its separate authorization, inspect active/duplicate sources, verify a fresh backup of the **currently installed pilot** and relevant configuration, install the verified published eight-file asset into one authoritative target, and run fresh-session positive/negative routing, explicit decision-control and neighboring-skill smoke checks. Preserve the disclosed native routine-edit limitation and restore the backup on a critical failure. The old stable backup is historical, not automatically the correct rollback for today's pilot state.

**Stopped after clearance.** Only this redacted review document is updated. No stable release metadata, tag, release, installation, experimental PR, Design Director or Frontend Engineer was changed.

## Owner authorization after clearance — November 3

The owner explicitly accepted the documented Codex-only exceptions and authorized final package verification, stable publication, backup of the current pilot, installation and smoke checks. This supersedes the earlier lack of authorization; it does not change the failed strict gate, historical test results or scope. No other skills or experimental PRs are authorized to change. Execution completion must be verified separately from this authorization.

## Authorized publication and installation completed — November 3

The accepted-exception Codex-only release is published as [v2.1.3](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.3), targeting source commit `ac43773b8fdfcca993ff5449ee87cf16fb3ad581`. The published `ai-project-steward-2.1.3-codex.zip` has SHA-256 `89c417673beb4d35805642d9ff75a11f0a75d9c7e2077dd0fcf57a59e13790b7`. The tag, both asset downloads, ZIP CRC, exact eight-file membership and every payload hash were independently checked against the final source and published checksum. The tested instruction hash remains unchanged. Final source validation and all 42 existing local tests passed; [hosted validation](https://github.com/glichtenthal/ai-project-steward/actions/runs/41767861103) also succeeded. The tag remains pinned to the final package source; this later execution addendum does not change that asset.

The current 110-file private pilot was fully backed up and hash-verified outside active skill locations, with a separate private configuration backup, before replacing one authoritative Steward directory with the downloaded published eight-file package. All 60 files in the other local installed-skill directories still match their pre-update hashes. Design Director and Frontend Engineer remain present and unchanged; their specialist behavior was not re-evaluated. No overlapping Steward or legacy Building Partner source was found in the checked global and project-ancestor skill locations. Rollback was not needed; both a verified pilot backup archive and the original retired directory are retained privately.

### Actual installed-surface smoke results

Reused the existing case definitions and controlled execution adapter in fresh ephemeral CLI sessions against the actual installed directory, with no repository-local Steward copy. All six executions completed in one CLI `0.166.0-alpha.5.1` window on `gpt-6.1-sol`, high reasoning. Seven distinct conversations include the two-phase continuity case. Apps/plugins/web/memory were disabled for these synthetic sessions; neighboring specialists were disabled only within each invocation, with their installed files untouched. Restricted local Chrome `156.0.8078.81` supplied actual render/click evidence.

| Smoke case | Observed result |
| --- | --- |
| Ordinary writing, natural selection | Direct email draft; no Steward source read, tools or file changes; 3 assertion passes. |
| Authentication choice, natural selection | Installed Steward read; conditional options/recommendation and permission boundaries; no implementation; 5 passes. |
| Routine label edit, natural selection | Installed Steward read in this sample; only the label changed, real browser/click check passed, no governance overhead; 5 passes. |
| Routine label edit, explicit invocation | Installed source read; only `index.html` changed; label and existing click behavior verified; 5 passes. |
| Unapproved decision replacement | Original SQLite Accepted entry stayed unchanged; alternative appended as Proposed; no external action; 5 passes. |
| Approved replacement, then fresh conversation | PostgreSQL Accepted and SQLite Superseded only after explicit approval; fresh conversation recovered the decision without reverting it or authorizing implementation; 5 passes. |

**Total: 28 passing, zero failing assertion judgments; no newly identified critical regression.** Reviews are unblinded AI-assisted inspections of actual events, outputs and artifacts, not independent human grading or a new baseline/candidate benchmark. The native routine-edit activation success in this single smoke does **not** erase the historical shared misses or prove automatic activation is reliable. The strict regression gate remains failed, and all accepted release limitations remain in force. Desktop UI activation and specialist behavior were not certified by these CLI checks.

A preparation-only attempt failed on a browser-adapter filename before any model call; it was retained and fresh run identifiers were used after correction. The CLI also automatically registered six scratch project paths as trusted despite the ignore-user-config flag. Only those exact entries were removed after testing; the original configuration was restored byte for byte and the transient snapshot retained privately. No unrelated configuration change was overwritten.

Private raw smoke traces, assertion notes, evidence hashes, backup and installation receipts remain local. Historical evaluation records were not rewritten. Steward experimental PR #2 and specialist experimental PR #5 remain open, draft and unmerged; their heads and last-update metadata remain from before this release work. No other installed skills or experimental PRs were changed.
