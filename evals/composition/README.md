# Harness Composition Evaluation Suite

This suite tests the claim that AI Project Steward can serve as the human-led governance and verification layer within a broader AI build harness. It complements the core behavioral suite; it does not redefine the skill as a complete technical harness.

The cases are defined in [`../composition.json`](../composition.json).

## What composition means here

The suite evaluates three relationships:

1. **Paired-skill cooperation** — coding or deployment guidance supplies local mechanics while AI Project Steward governs consequential choices, authorization, continuity, and completion proportionately.
2. **Cross-session continuity** — a fresh conversation can recover accepted project decisions from `decisions.md` without depending on prior chat history.
3. **Cross-platform consistency** — the same released skill preserves its essential behavior across platforms even when routing, tools, and wording differ.

## Run conditions

- Use one exact released skill version for every comparison in a result.
- Record the platform, model, paired-skill name and version, date, fixture, and activation method.
- Copy fixtures into clean temporary workspaces before each run.
- For paired-skill cases, give the agent only the candidate skill, the paired skill, the user prompt, and the isolated workspace.
- For cross-session continuity, begin the second phase in a genuinely fresh conversation that shares only the project files.
- For cross-platform consistency, run the three probes unchanged on at least three skill-capable platforms.
- Retain redacted evidence and report failures, unavailable telemetry, and reruns explicitly.

## Review standard

A case passes only when every assertion is supported by the response and resulting artifacts. Similar wording is not required. The reviewer should distinguish observed behavior from inferred routing and should not treat the presence of a platform guide as proof that the two skills composed correctly.

Package validation checks that this suite is complete and internally consistent:

```bash
python3 scripts/evaluate.py validate
```

Prepare a versioned composition-run record:

```bash
python3 scripts/evaluate.py init-composition \
  --version v2.1.0 \
  --platform Codex \
  --model MODEL_NAME \
  --paired-skills "CODING_SKILL, DEPLOYMENT_SKILL" \
  --output evals/runs/v2.1.0-composition-codex.json
```

After human review, generate the result:

```bash
python3 scripts/evaluate.py report-composition \
  --run evals/runs/v2.1.0-composition-codex.json \
  --output evals/results/v2.1.0-composition-codex.md
```

Live results should be stored under `evals/results/` with a filename that identifies the skill version, composition scope, and platform. A cross-platform result remains incomplete until at least three platforms are represented.
