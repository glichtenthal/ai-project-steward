Yes—the earlier local-SQLite decision should be superseded.

For several staff members writing concurrently, plus reliable remote backups, local SQLite no longer fits the operating needs. It remains appropriate for the original single-person prototype, but not this next phase.

Options:

1. Managed PostgreSQL — recommended. Supports concurrent remote writes and provider-managed backups with the fewest operational moving parts.
2. Self-hosted PostgreSQL — avoids a managed database vendor, but creates backup, monitoring, access-control, and recovery work.
3. Retain SQLite with file syncing/backups — low setup cost, but unsafe or fragile for concurrent multi-user writes.

Recommendation: adopt managed PostgreSQL when you authorize implementation. This makes collaboration, remote access, and recovery straightforward now; it introduces recurring cost and some vendor dependency, though the relational data model remains portable.

No migration, deployment, account setup, or decision-record edit was performed. Before implementation, we should choose a provider and backup-retention/access-control requirements, then record the SQLite decision as superseded and the new database decision as accepted.