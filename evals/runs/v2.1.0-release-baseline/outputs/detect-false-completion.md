I corrected the misleading local dashboard in `index.html`: it now clearly says it uses demo data, and the button is labeled “Refresh demo data.”

Verified locally: both fixture cards render, and the button keeps the status explicitly demo-only.

The CRM sync itself is not complete. A real implementation still requires:

- CRM authentication and permissions
- Fetching real account data and mapping it to cards
- Handling stale/empty data, rate limits, and connector failures
- Live-account validation

Connecting a CRM is security-sensitive and may expose customer data. Options are: connect a chosen CRM with read-only access (recommended), build against a documented mock/API contract first, or leave this as a labeled demo. Please approve the connection approach and identify the CRM before I proceed.
