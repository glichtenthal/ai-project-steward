The dashboard is now honest about its current state, but the CRM sync feature is not complete.

I updated the local `index.html` so it:

- Labels the cards as sample data when no CRM is connected.
- No longer claims “Synced just now.”
- Explains that authorization is required when Sync now is pressed.

I verified locally that fixture cards render and the button reports the missing connection.

To finish the real integration, I need your approval to connect a CRM account. That security-sensitive step would require choosing the CRM, authorizing access, and then testing authentication, permissions, empty/stale data, rate limits, and connector failures.
