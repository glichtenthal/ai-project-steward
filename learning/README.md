# Evidence-driven learning protocol (experimental)

This process **proposes** changes to skills. It does not change agent weights, edit instructions autonomously, authorize external actions, or promote a release.

## Operating loop

1. **Observe selectively.** After a meaningful failure, regression, user correction, or completed high-risk workflow, record a redacted event in a project-owned append-only JSONL file. Do not create a review for every successful small task.
2. **Triage.** Repeated failures across at least two independent tasks, or one critical safety/authorization failure, justify a proposed improvement. Similar events from the same task count once.
3. **Reproduce first.** Add a failing evaluation case without changing the skill. Verify the failure in the actual target model/harness, not merely in a Python validator.
4. **Change minimally.** Identify which owner owns the gap: Steward for governance and cross-skill coordination, Design Director for experience, or Frontend Engineer for implementation. Prefer one bounded edit to duplicated instructions.
5. **Compare.** Run baseline and candidate skill versions on identical scenario IDs, platform, model, harness, and fixtures; retain redacted outputs and reviewer notes. Existing positive, negative routing, composition, and critical safety cases must remain in the suite. The advisory gate requires at least one measured improvement, zero regressions, and all critical cases passing.
6. **Review.** Publish a PR summarizing evidence, uncertainty, differences, costs, and possible reversions. Human review and explicit approval remain necessary for merging, installation, or release.
7. **Re-evaluate the loop.** Periodically review whether proposals were accepted, reverted, duplicative, noisy, or worth their evaluation cost. Modify this protocol through the same baseline-and-candidate process. Record unsuccessful experiments.

## Evidence schema

Store a redacted JSON object per line in a project-owned file such as `learning/observations.jsonl` (do not commit private user transcripts):

```json
{"schema_version":"1.0","id":"obs-001","date":"2026-10-25","task_id":"redacted-task-A","role":"design","failure_code":"missing-empty-state","severity":"major","expected":"The empty state is specified","observed":"It was omitted","evidence":"evidence/redacted-task-A.md"}
```

Evidence paths must be local to the JSONL file and exist. Use role `steward`, `design`, or `frontend`. Severity is `minor`, `major`, or `critical`. Use stable failure codes across independent tasks. Do not record raw personal details, credentials, user identifiers, or proprietary content in public repositories.

## Commands

```bash
python3 scripts/learn.py triage --events path/to/observations.jsonl --output path/to/triage.json
python3 scripts/learn.py init-run --role steward --version candidate --platform Codex --model MODEL --output path/to/candidate.json
python3 scripts/learn.py gate --baseline path/to/baseline.json --candidate path/to/candidate.json --output path/to/gate.json
python3 -m unittest discover -s tests -v
```

For `gate`, edit the initialized run records only after performing actual fresh-context evaluations. Each `pass` or `fail` requires a nonempty reviewer note and a path to retained output in the same directory as the run JSON. The gate is strict: all current cases must be reviewed on both sides, and both must use the same model and platform. Run more repetitions and platforms for consequential changes. Scores are not inferred from prose alone.

**Important:** Passing Python tests confirms that the recorder and gate work, not that the skill is improved. Passing an advisory gate indicates evidence suitable for human review, not automatic authorization or proof of broad generalization.

## Owner-specific lenses

- **Steward:** approval boundaries; decision continuity; proportional restraint; evidence quality; truthful integration and deployment claims.
- **Design Director:** user-job clarity; evidence vs assumptions; information architecture and handoff; states; accessibility; rendered critique.
- **Frontend Engineer:** specification fidelity; runtime/data integrity; accessibility; responsive/browser verification; recovery and release evidence.

The dedicated role test cases live in `learning/cases.json`. The existing `evals/evals.json` and `evals/composition.json` remain Steward's authoritative release evaluation suites. The new cases are *supplemental* and cannot replace the older tests.

## Repository boundary

The canonical Design Director and Frontend Engineer files live in the separate `glichtenthal/agent-skills` repository. Install or update them separately after both PRs are reviewed. Steward does not reach into their files or silently amend their rules.