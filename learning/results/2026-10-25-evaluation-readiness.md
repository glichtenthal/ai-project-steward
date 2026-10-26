# Candidate evaluation gate: 2026-10-25

## Status: BLOCKED, NOT A MODEL-EVALUATION PASS

Scope: [Steward PR #2](https://github.com/glichtenthal/ai-project-steward/pull/2) and [paired Design/Frontend PR #5](https://github.com/glichtenthal/agent-skills/pull/5).

### Verified

- Existing GitHub Actions run on initial Steward learning branch completed successfully: package validation, learning-engine unit tests, archive integrity.
- The comparison gate requires evidence-backed and reviewed results, matching models/platforms, and zero observed regressions.
- The candidate adds **six direct recursive-learning pressure and restraint cases** (two per role) to distinguish the new improvement behavior from existing general build checks.
- The latest edits to those tests require a fresh GitHub Actions check.

### Not performed

- No authenticated agent harness was available from this execution environment. No isolated baseline and candidate model runs were executed.
- No retained paired model outputs, run records with human-verified assertions, cross-harness reproducibility data, or runtime cost measurements exist for these two PRs.
- The prior Python unit tests are structural tests of the learning system, **not evidence of agent improvement**.

### Release recommendation

**Do not merge these PRs as an evidence-validated behavioral improvement yet.** Maintain them in draft. Execute baseline and candidate skill instructions in clean, equivalent contexts on a named model and harness; retain outputs, score each assertion, and run the learning gate for each role. Re-run existing Steward behavioral and composition suites and the specialist release checks on affected flows. Distinguish unchanged critical safeguards, new improvements, and any regressions. Review evidence and approve the eventual merge separately.

### How to complete

1. Choose an authorized, instrumented agent runtime able to load an exact skill revision into a clean context. Use the same model, tools, permissions, fixtures, prompt, and scoring criteria for baseline and candidate. Existing positive/negative routing and tool-use cases also need unforced activation trials.
2. Run each scenario from `learning/cases.json` with each skill's current main-branch instructions and the PR candidate. Repeat changed or borderline cases; preserve raw redacted outputs outside the public repo if sensitive.
3. Produce `init-run` JSON records for each role and version, assign pass/fail only after reviewing retained evidence against the published assertions, then invoke `scripts/learn.py gate`.
4. Record any errors, missing tool access, and incomplete evidence as incomplete. Do not replace failed attempts with successful reruns without retaining both.
5. Only after the reports demonstrate the value of each proposed modification, complete PR review and merge with the user's authorization under existing release procedures.

This document is intentionally a negative evidence record, not an invented result.