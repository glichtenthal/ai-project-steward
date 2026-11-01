# Supervised learning pilot — October 31, 2026

## Decision

Keep all three candidates **unreleased and uninstalled**. Recommend **revise** for Steward PR #2 and agent-skills PR #5: the consolidated infrastructure is useful, but the full comparison gates do not clear. No additional state-coverage rule or autonomous learning service is justified by this pilot.

## What actually ran

48 completed real-agent executions, zero timeouts: 38 main advisory runs (19 paired scenarios across three roles), four explicit decision-control runs, four exact published decision-regression runs, and two design confirmation runs. Model: gpt-6.1-sol, high reasoning; Codex CLI 0.166.0-alpha.5.1 throughout. Runtime flags and source loading match within each pair, but the full effective service-side tool inventory was not serialized, so declared metadata is not independent tool-equivalence attestation. Every recorded execution includes an observed SKILL.md source read. **Source distinction:** main Steward learning runs use candidate `b488980` (instruction hash `801be5dc…`); the eight historical decision-control/published-fixture executions compare stable against `fa9f0bf` (hash `a67245b3…`), the narrower merged candidate **without** the learning section. Those control results do not validate the learning instructions. Design confirmation uses the same frozen specialist payloads as its main pair. Main cases and explicit controls used read-only permissions; the four historical published-fixture runs used isolated workspace-write permissions. No production resources or accounts were involved.

[Protocol](protocol.json), [exact input prompts](inputs/), [input hashes](inputs-manifest.json), [source revisions](source-refs.json), [execution manifest](execution-manifest.json), and [accounting](execution-accounting.json) identify the conditions. The three held-outs were fixed before any main evaluation. Confirmation repeats were declared later, before their executions, with unchanged instructions; they are not additional held-outs.

These are real agents answering synthetic advisory scenarios. They do **not** establish actual rendered design quality, live integrations, native routing, or ordinary implementation speed. The original assertions remain unchanged; unavailable execution checks remain not_run rather than being redefined as advisory successes.

## Baseline versus candidate

| Role | Baseline assertion pass / fail / not_run | Candidate assertion pass / fail / not_run | Observed difference |
|---|---|---|---|
| Steward | 19 / 0 / 2 | 19 / 0 / 2 | No scored gain |
| Design | 15 / 1 / 2 | 16 / 0 / 2 | Candidate explicitly proposes controlled baseline reproduction |
| Frontend | 14 / 2 / 2 | 15 / 1 / 2 | Candidate explicitly requires evaluation/review before a lasting change; rollback coverage still misses one rubric |

Each role's held-out assertions passed in both arms. No scored pass-to-fail regression occurred. All full role comparisons remain blocked: Steward lacks performed edit/verification, Design lacks an actual completed responsive handoff, and Frontend lacks rendered checks and retains a rubric failure. The targeted differences are procedural response improvements, not proof of better user outcomes. A missing explicit review or rollback statement is not evidence that an agent actually weakened security.

Independent AI reviewers used per-case blinded A/B labels, with alternating arm assignments. The controller was unblinded. Reviewer models inherited the parent configuration and were not separately instrumented; no human behavioral approval is claimed. See the [baseline/candidate reports and scored records](.) and [confirmation judgments](confirmations.json). Hashes establish retained content consistency, not authenticated execution or correct grading.

## Genuine learning cycle and disposition

1. **Observe:** The original public PR #3 history reported premature supersession of an accepted decision. Its private original trace was unavailable. In this pilot, the stable design answer also proposed a lasting rule without the predefined controlled baseline-reproduction step; the actual response is retained.
2. **Diagnose:** Distinguish a missing improvement-validation procedure from a missing design-state rule. Both stable and candidate already require empty states. The two omitted handoffs mentioned by the synthetic prompt were not supplied and are not established real incidents.
3. **Reproduce:** The design omission recurred in a separate unchanged stable run. Candidate included controlled baseline comparison in both the initial and confirmation outputs. The historical Steward decision-status failure did **not** recur in either the two explicit-control pairs or the two exact published-fixture pairs. Actual before/after decision files preserve Accepted and append Proposed alternatives.
4. **Propose:** Test the existing minimal learning-section candidate; add no new design-state rule. This candidate was authored before this pilot and frozen before scoring; it was not tuned against the held-outs. The pilot is a retrospective validation cycle, not a claim that this session autonomously invented the candidate after observing the failure.
5. **Evaluate:** Compare actual stable/candidate outputs under matching conditions; preserve all outcomes. Same-pilot repeats are not independent production incidents.
6. **Review:** Blinded independent AI judgments support the narrow design procedural difference; the unblinded controller reviewed retained text and writable-fixture postconditions. Human sign-off remains pending.
7. **Retain or reject:** Retain the small design learning addition only as a candidate for review. Reject further state-coverage wording expansion and any claim of newly demonstrated Steward decision benefit. Hold promotion of all roles while declared release checks remain incomplete.

[Observation records](observations.jsonl) produce [zero automatic proposals](triage.json): the two design samples share one task ID. This is intentional restraint. The user explicitly authorized the pilot; no recurrence threshold was manipulated. Synthetic triage unit tests separately cover two distinct tasks and a critical incident; they do not prove semantic incident classification.

## Framework assessment

Consolidation removes the weaker independent gate. Schema 1.1 is reused for role cases, with hashed retained evidence, frozen assertions, declared harness/fixture conditions and advisory approval boundaries. `--mode regression` can clear identical complete passing coverage without inventing improvement; default improvement mode still requires a gain. No incomplete or failing candidate clears either gate.

A further iteration is worthwhile **only to improve evaluation fitness**: provide actual handoff/app fixtures for the unperformed checks, and clarify rubric semantics before new runs. Do not weaken the current criteria after seeing failures or add global rules to satisfy keywords. The strict rubric identified an omission in a 250-word advisory response; it cannot establish a production security defect. Held-outs and independent review help but do not eliminate score overfitting.

## Time, cost and failed attempts

Recorded executions total 1,196.377 aggregate seconds (parallel, not wall-clock), 3,007,460 input tokens including 2,371,456 cached input tokens, and 30,551 output tokens; the runtime separately reports 8,240 reasoning-output tokens. Do not sum potentially overlapping usage categories into a billing estimate. Dollar cost is unavailable. Reviewer usage and the initial probe/controller attempts are excluded from these totals.

Median main-run elapsed seconds, baseline/candidate: Steward 23.108/18.766; Design 18.901/20.282; Frontend 19.930/21.215. Small mixed tasks, concurrent execution and source-loading differences prevent broad latency claims.

One initial runtime attempt failed host permissions; an authorized retry succeeded. A controller compatibility failure affected three initial attempts; their evidence remains private, outside scored comparisons. Automatic approval review rejected an inadequately scoped confirmation command before execution; the corrected controller explicitly listed six jobs and was approved. No rejected attempt was silently counted as a pass.

## Reproduction and safeguards

Use a project-local Python environment and the existing standard-library evaluator; no dependencies or services are needed. Retrieve skill files at [source-refs.json](source-refs.json) revisions and verify their recorded SHA-256 values. Copy each exact input into a new isolated workspace as prompt.txt, copy the correct arm's instructions as SKILL.md, and include decisions.md only where the input manifest specifies it. Run the installed Codex version with the model/reasoning/sandbox flags recorded in execution-manifest.json, saving actual JSONL events and final output. Reuse the shared init-learning/report-learning/compare commands described in ../../README.md. Never substitute a model plan for execution evidence.

[controller.rb](controller.rb) is the archived main-run controller snapshot: it dynamically discovers prepared directories, always uses read-only permissions, and has no global job cap. It is **not a safe turnkey replay command** or a scheduled service. [confirmation-controller.rb](confirmation-controller.rb) is the separately scoped six-job snapshot, using workspace-write only for the published decision fixtures. Inspect the explicit execution manifest and prepare only an authorized bounded job list before any replay. Main-role fixtures are advisory; reproducing actual visual/implementation checks needs a new reviewed fixture contract, not altered scores for this run.

Raw streams remain outside Git. Public files contain controller-inspected synthetic final outputs, prompt/source hashes, judgment notes and redacted postconditions; local paths and personal name are redacted, and trailing whitespace is normalized in public Markdown extracts. Raw-output digests in execution-manifest.json identify the privately retained originals. Preserve failures and private raw evidence until review disposition plus 30 days, then ask before deletion. No deletion or periodic model execution is scheduled. CI checks record/package integrity only, and release/install flags remain false.
