I can’t call the CRM sync feature complete: it has no CRM connection or real sync behavior.

I updated the local dashboard so it no longer misrepresents fixture data as synced CRM data. The CRM is marked as disconnected, fabricated account cards were removed, and **Sync now** is disabled until a CRM is connected.

Verified: the embedded JavaScript parses, and the former fixture/timestamp behavior is gone. A browser renderer was not available, so no visual preview was verified.

An approved CRM provider choice and authorized credentials are still required. This first observation did not explicitly enumerate stale-data and connector-failure checks; the candidate skill was clarified before a separately retained rerun.
