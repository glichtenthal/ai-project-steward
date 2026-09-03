The accepted local-SQLite decision should change: the new requirements exactly match its recorded reconsideration triggers—concurrent writes, remote access, and reliable off-device backups.

Options:

1. Keep local SQLite with a shared/synced file  
   Low effort, but unsafe for multi-user concurrent writes and poor for reliable remote backup/recovery.

2. Use a managed relational database  
   Supports concurrent staff writes and provider-managed remote backups. This is the recommended direction for a staff-facing prototype.

3. Self-host PostgreSQL with managed backups  
   Meets the needs, but adds operational and recovery responsibility; sensible only if you need infrastructure control.

Recommendation: replace local SQLite with a managed relational database, subject to your approval. It makes multi-user operation and backup/recovery simpler now; it creates provider dependence and likely recurring cost, though the relational data model remains portable.

No migration, deployment, service selection, or `decisions.md` change was made. If you approve the direction, the next decision should compare concrete managed-service options based on expected users, data sensitivity, budget, and any existing cloud provider.