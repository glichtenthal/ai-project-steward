# Decisions

## 2026-08-15 — Prototype database

- **Status:** Accepted
- **Context:** The first prototype runs locally for one person and needs simple persistence.
- **Options considered:** JSON file, SQLite, hosted Postgres.
- **Decision:** Use local SQLite.
- **Rationale:** It provides reliable local persistence without infrastructure or recurring cost.
- **Consequences and reversal difficulty:** Concurrent remote use is not supported. The data model can later migrate, but migration and remote operations would need to be planned.
- **Reconsider when:** Multiple people require concurrent writes, remote access becomes necessary, or reliable off-device backups are required.
