Local CRM adapter verification passed with no changes needed.

- Healthy response accepted.
- Empty data rejected.
- Stale data rejected.
- Authentication (401) rejected.
- Rate-limit (429) rejected.

Ran `python3 -m unittest -v test_sync.py`: 5 tests passed. The test server was loopback-only with synthetic fixture data; no real CRM, credentials, customer data, schedules, messages, purchases, or deployment were used.