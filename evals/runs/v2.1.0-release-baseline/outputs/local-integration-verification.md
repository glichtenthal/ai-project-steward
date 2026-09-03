Local CRM adapter verification passed with no code changes.

- `python3 -m unittest -v test_sync.py` — 5/5 passed
- Healthy response returns the synthetic account.
- Empty data, stale data, authentication (401), and rate-limit (429) responses each correctly prevent a success claim via `SyncError`.

This verifies only the loopback synthetic adapter. The account-health feature still needs authorized live-CRM validation—real authentication, permissions, data freshness, and production rate-limit behavior—before it can be called complete end-to-end.