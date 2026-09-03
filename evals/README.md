# Behavioral Evaluation Suite

The suite tests whether AI Project Steward changes an agent's behavior in the intended way. It is not a benchmark claiming that every model will produce identical wording.

## What is evaluated

Each case in `evals.json` contains:

- a realistic build or control prompt
- whether the skill should load
- the common failure the skill is intended to prevent
- the expected output shape
- observable assertions used during review

File-dependent cases use the synthetic inputs in [`fixtures/`](fixtures/). Copy a fixture into a clean temporary workspace before running the case so the source remains unchanged.

Results are reported along three separate dimensions:

1. **Package validity** — automated checks for the skill, metadata, examples, and evaluation definitions.
2. **Routing behavior** — whether a platform loaded or skipped the skill appropriately.
3. **Steward behavior** — whether the response demonstrated the expected visibility, guidance, authorization, continuity, restraint, and verification.

The separate [Harness Composition Evaluation Suite](composition/README.md) adds a fourth dimension: whether the skill cooperates with coding and deployment guidance, carries accepted decisions across fresh sessions, and preserves its essential behavior across different platforms.

## Why human review remains part of the process

Keyword matching cannot reliably determine whether a recommendation fits the project, an approval boundary is appropriately scoped, or verification is honest. The runner automates consistency and reporting; a reviewer evaluates the substantive behavior against the published assertions.

## Run package validation

From the repository root:

```bash
python3 scripts/evaluate.py validate
```

This command is dependency-free and is also run in GitHub Actions.

## Prepare a live evaluation run

Create a run record for a specific release, platform, and model:

```bash
python3 scripts/evaluate.py init \
  --version v2.1.0 \
  --platform Codex \
  --model MODEL_NAME \
  --output evals/runs/v2.1.0-codex.json
```

For every case:

1. Start a fresh conversation or equivalent clean context.
2. Submit the prompt exactly as written.
3. Record whether the skill loaded.
4. Save a redacted response when it is safe to publish.
5. Review the response against every assertion.
6. Set `routing_result` and `behavior_result` to `pass`, `fail`, `not_run`, or `not_applicable` and add concise notes.

Routing and behavior are deliberately separate. A platform can fail to select a good skill, and a selected skill can still behave poorly.

## Generate a versioned result

After review:

```bash
python3 scripts/evaluate.py report \
  --run evals/runs/v2.1.0-codex.json \
  --output evals/results/v2.1.0-codex.md
```

The result records the release, platform, model, date, review method, case-level outcomes, limitations, and links to retained outputs. Do not replace failures with reruns that happen to pass; record reruns as additional evidence.

## Release evidence standard

A release result is publishable when:

- package validation passes
- the intended case set was run in clean contexts
- all pass/fail judgments have notes or retained output evidence
- failed or not-run cases remain visible
- the platform, model, date, skill version, evaluator method, and limitations are identified
- no credentials, private customer data, or sensitive account information appear in the artifacts

These results demonstrate observed behavior under named conditions. They are not guarantees for every model, platform router, or future run.
