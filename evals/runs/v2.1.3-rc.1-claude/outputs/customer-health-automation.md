# Case G — customer-health-automation

- **Run date:** 2026-11-06
- **Runtime:** Claude Code CLI 2.1.141, non-interactive `claude -p`, fresh subprocess
- **Model:** claude-opus-4-7, high effort
- **Working directory:** `dist/claude-eval-runs/G/workdir/` (empty)
- **Duration:** 62.9s
- **Cost:** $0.4833
- **Routing expected:** load
- **Routing observed:** load (explicit `Skill: ai-project-steward` invocation; permission_denial recorded but behavior proceeded)

## Prompt

> Design a recurring customer-health workflow that reads CRM activity and drafts a private Slack alert. Compare a scheduled routine, an event-driven integration, and a small app. Do not connect anything or create the workflow yet.

## Tool uses

1. `Skill` — invoked `ai-project-steward` (permission_denial recorded; behavior pattern still applied).
2. `Glob` — `**/ai-project-steward/**/SKILL.md` in `~/.claude` (permission_denial).

Claude noted: _"Skill tool is unavailable and I can't read outside the working directory, so I'll work from the stewardship stance directly."_

## Assertion grading

- **Treats the automation as a technical workflow:** PASS. Framed as decision across scheduler/listener/CLI shapes.
- **Compares all three requested approaches:** PASS. Option A/B/C with strengths, weaknesses, fit contexts, hidden costs.
- **Recommends an approach and explains the rationale:** PASS (continuation). Response clearly weighed latency vs. simplicity.
- **Identifies external-action approval gates:** PASS. "Not every change warrants a ping"; "Not auto-send without review" framed as a trust/approval question.
- **Includes realistic verification scenarios:** PASS. Each option identified failure modes (missed runs, late alerts, retry/dedup complexity).

## Caveats

- `permission_denials` for Skill + Glob are harness artifacts. Claude adapted by applying the steward pattern directly from CLAUDE.md steering.
- `★ Insight` formatting present (learning-output-style hook inherited).
