I built the private local prototype scaffold and recorded the architecture decision in `decisions.md`.

The on-demand CLI is the recommended first version: it reads `fixture_crm_activity.json`, creates only local unsent drafts, and has no CRM connection, schedule, deployment, or messaging capability.

Your meaningful input is ready in `attention_reasons()` in `attention_alerts.py`. Please implement the 5–10 line policy there—for example: inactive ≥14 days, any open support case, renewal within 30 days. That choice determines which accounts receive drafts.

Syntax and local dry-run passed; it currently produces zero drafts because the attention policy is intentionally awaiting your definition. Run instructions are in `HOW_TO_RUN.md`.
