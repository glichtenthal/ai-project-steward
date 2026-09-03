Built and verified the private, local fixture-data prototype.

Recommendation: start with the local command, not a schedule or event-driven integration. It’s the simplest reliable option: no credentials, external accounts, webhook security, sending, or operational setup. The core can later be reused by either automation path.

Implemented:

- Fixture CRM activity: `fixtures/crm-activity.json`
- Analyzer and private-draft generator: `src/analyze-crm.mjs`
- Decision record: `decisions.md`

Run it with:

```bash
npm test
npm run analyze
```

Verification passed: 2 tests, including stale/missing activity detection and rejection of future-dated activity. The fixture run created 3 unsent, `private-review-only` drafts in `output/alert-drafts.json`.

No external accounts, real customer data, schedule, delivery, deployment, or purchase was used.
