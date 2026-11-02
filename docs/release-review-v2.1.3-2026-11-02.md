# AI Project Steward 2.1.3 bounded release-readiness review

**Review date:** 2026-11-02  
**Disposition:** **HOLD release and installation pending bounded evidence sign-off.**  
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
