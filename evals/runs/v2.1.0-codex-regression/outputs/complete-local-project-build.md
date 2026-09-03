Built and verified a private, local fixture-data prototype.

Recommendation: start with the small local app. It avoids the credentials, security, reliability, and operational overhead of event-driven CRM integration or a scheduled routine while keeping alert review explicit.

Files:

- `attention_alerts.py` — detects blocked activity or 14+ days of inactivity; writes private Markdown drafts only.
- `fixtures/crm_activity.json` — synthetic CRM fixture data.
- `test_attention_alerts.py` — verifies blocked/inactive detection, recent-account exclusion, and unsent drafts.
- `decisions.md` — records the accepted local-first decision.

Run it with:

```bash
python3 attention_alerts.py --as-of 2026-09-01
```

Verified: both tests pass; fixture execution produced two private drafts for the blocked and no-activity accounts. No CRM connection, schedule, real data, sending, deployment, or external account action was used.

Before any future real integration, verify authentication/permissions, privacy and retention, stale or empty data, rate limits, connector failures, and explicit human approval before delivery.
