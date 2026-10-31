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
4. Retain the actual response, relevant tool trace, and resulting artifact evidence in a file beneath the run record's directory. Redact secrets and private data before retention; document redactions and limitations. Never substitute a simulated response for an unavailable execution.
5. Set `output_file` relative to the run record and `evidence_sha256` to the SHA-256 of the retained file. Include or reference all artifacts required to support the judgments. The evaluator rejects missing, empty, changed, or external evidence files, including symlinks escaping that directory.
6. Review every published assertion in `assertion_results`, keeping its original text and order. Assign `pass`, `fail`, or `not_run`, with a reason for each reviewed assertion. Set `behavior_result` to `not_run` while any assertion is unreviewed, otherwise `fail` if any failed, otherwise `pass`. Known failures stay visible even when the aggregate is incomplete.
7. Set `routing_result` independently to `pass`, `fail`, or `not_run`, with case notes supported by routing telemetry. Unavailable telemetry stays `not_run`. Negative routing cases still require ordinary-workflow behavior review. New records cannot waive a published check as `not_applicable`.
8. Replace `review_method: pending` with a clear account of deterministic checks, AI-assisted judgments (including evaluator model and whether blinded), and any completed or pending human review. This is a reviewer declaration, not independently authenticated approval.

Before scoring, fill `comparison.harness`, `tools`, and `permissions` with the exact runtime versions/configuration and effective tool/permission sets. Fill `fixtures_sha256` with the digest of a deterministic manifest of the original fixture paths and their file hashes, sorted by path; retain that manifest with the evidence. Hash starting inputs, not modified outputs. The evaluator supplies the canonical `prompts_sha256` and `criteria_sha256`; changing these fingerprints or the published assertion reviews invalidates a comparison.

These metadata describe the actual executions, not the desired setup. Both arms must use identical initial fixtures, prompts, criteria, model, platform, harness, tools, and permissions, in isolated clean contexts. Preserve immutable source revisions and every attempt in the evidence. Composition records additionally require the same paired skill identities and versions. Metadata equality and content hashes cannot prove that an agent executed a task or that an assertion was judged correctly; inspect the retained traces.

Routing and behavior are deliberately separate. A platform can fail to select a good skill, and a selected skill can still behave poorly.

## Generate a versioned result

After review:

```bash
python3 scripts/evaluate.py report \
  --run evals/runs/v2.1.0-codex.json \
  --output evals/results/v2.1.0-codex.md
```

The result records the release, platform, model, date, review method, case-level outcomes, limitations, and links to retained outputs. Do not replace failures with reruns that happen to pass; record reruns as additional evidence.

New run records use schema `1.1`. Historical schema `1.0` records can still be rendered, explicitly labeled as historical scores without the new integrity validation. Do not convert old records by filling in missing evidence or review fields from assumptions. Re-review retained real evidence or run a new controlled evaluation. `Complete` describes coverage, not success or release authorization.

## Compare reviewed runs

Use the same evaluator, rather than a separate learning framework:

```bash
python3 scripts/evaluate.py compare \
  --suite behavioral \
  --baseline evals/runs/baseline.json \
  --candidate evals/runs/candidate.json \
  --output evals/results/comparison.json
```

Use `--suite composition` for composition records. The advisory check rejects missing or invalid evidence, incomplete reviews, incompatible declared conditions, any candidate failure, and absence of a scored improvement. It never authorizes promotion. A zero exit status means the recorded scores qualify for human inspection, not that real-world benefit, appropriate cost, or release readiness has been established. Run both suites separately, retain failures and repeats, and review ordinary-workflow overhead and safety boundaries before proposing a release. Cross-platform probes must actually include the three platforms specified in the composition case; a pass flag alone is insufficient proof.

This change introduces no execution service, automatic learning, remote data store, or recurring model calls. It hardens manual evidence recording and comparison. Maintain records with the tested source revisions, local hashes, and explicit review limitations; existing stable release metadata continues to describe the published release until a separately approved release updates it.

## Release evidence standard

A release result is publishable when:

- package validation passes
- the intended case set was run in clean contexts
- all pass/fail judgments have retained evidence, matching hashes, and assertion-level review notes under schema `1.1`
- failed or not-run cases remain visible
- the platform, model, date, skill version, evaluator method, and limitations are identified
- no credentials, private customer data, or sensitive account information appear in the artifacts

Publication and production changes still require the user's explicit approval. Deterministic integrity checks establish record consistency; AI-assisted judgments remain provisional until human review. Neither can establish meaningful improvement by itself.

These results demonstrate observed behavior under named conditions. They are not guarantees for every model, platform router, or future run.
