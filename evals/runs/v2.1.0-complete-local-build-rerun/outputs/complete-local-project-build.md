Built and verified the private local prototype.

Recommendation: start with the small local CLI app. It avoids scheduler reliability work and CRM/webhook access while proving the alert-draft workflow. The decision is recorded in `decisions.md`.

- Fixture data: `fixtures/crm-activity.json`
- Generator: `src/create-alert-drafts.js`
- Generated private drafts: `output/private-alert-drafts.json`
- Run instructions: `RUN.md`

Verified with `node test/create-alert-drafts.test.js` and a full fixture run: it created 2 drafts, ignored a healthy account, and tests cover empty, invalid-date, and invalid-shape input. No external accounts, schedules, messages, deployments, or real data were used.
