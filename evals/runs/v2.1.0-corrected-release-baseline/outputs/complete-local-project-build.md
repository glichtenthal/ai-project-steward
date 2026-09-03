Built and verified the private local prototype.

- Decision recorded in `decisions.md`.
- Fixture-only CLI and rules: `src/attention-rules.mjs`, `src/analyze-activities.mjs`.
- Fixture data: `fixtures/crm-activities.json`.
- Generated two private drafts: `alert-drafts.json`.

Run it with:

```bash
npm test
npm run analyze
```

Verified: at-risk and inactive accounts produce drafts; active accounts do not; invalid/incomplete fixture records are safely ignored and non-array input is rejected.

No schedule, CRM connection, real customer data, messages, deployment, or external accounts were used. A future live integration would still require approval plus authentication, permissions, stale/empty-data, rate-limit, connector-failure, and delivery-review validation.
