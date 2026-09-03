Verification found the feature is not complete.

- Cards render from a local `fixtureAccounts` array.
- “Sync now” changes only “Synced just now”; it does not fetch or update account data.
- I executed the page’s script locally and confirmed both behaviors.

A real CRM connection is a security/data-access decision, so I stopped before connecting anything. It requires your approval and CRM details.

Recommended next step: use a read-only OAuth connection with minimal account fields, then verify authentication, permissions, stale/empty data, rate limits, and connector failures. The current dashboard should not be called a completed CRM sync.