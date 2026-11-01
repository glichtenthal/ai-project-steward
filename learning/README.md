# Evidence-driven learning protocol (experimental)

This process **proposes** changes to skills. It does not change agent weights, edit instructions autonomously, authorize external actions, or promote a release.

## Operating loop

1. **Observe selectively.** After a meaningful failure, regression, user correction, or completed high-risk workflow, record a redacted event in a project-owned append-only JSONL file. Do not create a review for every successful small task.
2. **Triage.** Repeated failures across at least two independent tasks, or one critical safety/authorization failure, justify a proposed improvement. Similar events from the same task count once.
3. **Reproduce first.** Add a failing evaluation case without changing the skill. Verify the failure in the actual target model/harness, not merely in a Python validator.
4. **Change minimally.** Identify which owner owns the gap: Steward for governance and cross-skill coordination, Design Director for experience, or Frontend Engineer for implementation. Prefer one bounded edit to duplicated instructions.
5. **Compare.** Run baseline and candidate skill versions on identical scenario IDs, platform, model, harness, and fixtures; retain redacted outputs and reviewer notes. Existing positive, negative routing, composition, and critical safety cases must remain in the suite. Use regression mode to establish complete passing coverage without inventing a gain. Improvement mode additionally requires an observed improvement. Both reject candidate failures; neither authorizes promotion.
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
python3 scripts/evaluate.py init-learning --role steward --version candidate --platform Codex --model MODEL --output path/to/candidate.json
python3 scripts/evaluate.py report-learning --suite learning-steward --run path/to/candidate.json --output path/to/report.md
python3 scripts/evaluate.py compare --suite learning-steward --mode regression --baseline path/to/baseline.json --candidate path/to/candidate.json --output path/to/regression.json
python3 scripts/evaluate.py compare --suite learning-steward --mode improvement --baseline path/to/baseline.json --candidate path/to/candidate.json --output path/to/improvement.json
python3 -m unittest discover -s tests -v
```

The old `learn.py init-run/gate` commands are removed: `learn.py` only triages observations. All role runs use the existing schema 1.1 validator and comparator in `evaluate.py`. Follow `evals/README.md` for matching harness, tools, permissions, fixture/prompt/criteria fingerprints, evidence hashes, assertion-level reviews, and paired-skill identities. Use `learning-design` and `learning-frontend` for specialists. Incomplete cases block clearance; supplemental results cannot clear the full release suites. Metadata and hashes do not authenticate execution or human approval.

**Important:** Passing Python tests confirms that the recorder and gate work, not that the skill is improved. Passing an advisory gate indicates evidence suitable for human review, not automatic authorization or proof of broad generalization.

## Owner-specific lenses

- **Steward:** approval boundaries; decision continuity; proportional restraint; evidence quality; truthful integration and deployment claims.
- **Design Director:** user-job clarity; evidence vs assumptions; information architecture and handoff; states; accessibility; rendered critique.
- **Frontend Engineer:** specification fidelity; runtime/data integrity; accessibility; responsive/browser verification; recovery and release evidence.

The dedicated role test cases live in `learning/cases.json`. The existing `evals/evals.json` and `evals/composition.json` remain Steward's authoritative release evaluation suites. The new cases are *supplemental* and cannot replace the older tests.

## Repository boundary

The canonical Design Director and Frontend Engineer files live in the separate `glichtenthal/agent-skills` repository. Install or update them separately after both PRs are reviewed. Steward does not reach into their files or silently amend their rules.
## Private evidence and retention

Keep raw event streams outside Git repositories in an access-controlled local review folder. Never retain credentials, auth headers, personal identifiers or private transcripts in public source. Use synthetic fixtures whenever sufficient. Before a PR update, manually inspect public extracts, document redactions, and link each judgment to its actual output. Keep rejected runs and interruption records. Retain private raw pilot evidence until the review decision plus 30 days, then ask before deleting; no automatic deletion is configured. Retain the redacted protocol, source hashes, judgments and disposition for reproducibility. Public extracts must be explicitly reviewed before upload. Repeated reports from one task count once; task IDs and failure codes are operator labels, not independently authenticated recurrence.

## Method review

After a bounded pilot, count actionable proposals, duplicates and false positives, record time/token usage and rejected experiments. Change criteria through review, preserve earlier criteria, and test against held-outs. Do not add a scheduler or model service merely because a manual pilot works.

The recurrence threshold governs automatic triage proposals, not explicitly requested human-led investigations. Keep repeated runs of the same pilot under one task ID. Never relabel retries or model samples as independent real-world failures to satisfy a threshold.
