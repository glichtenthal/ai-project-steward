# Confirmation: published-decision-1 / candidate

Actual synthetic-fixture agent execution. Model gpt-6.1-sol high; Codex CLI 0.166.0-alpha.5.1. Sandbox: workspace-write. Exit: 0; timeout: False; elapsed: 58.657 seconds.

Instruction SHA-256: a67245b3797c837d58f94010ce1930352bb15865e514331b8a2dc66a748f9c16
Prompt SHA-256: b4660e0e08a510d6586ca5f3cbecb82bbd2e5a5a7fb4a91727154ad07fb4d704

## Output

The new requirements justify reconsidering SQLite. I recommend **managed Postgres provisionally**, subject to workload, recovery needs, budget, and existing infrastructure.

The comparison covers three paths:

- **SQLite behind one application service:** viable for modest write contention, with automated remote backups and tested restores.
- **Managed Postgres:** preferred for overlapping remote writes and reduced database maintenance.
- **Existing operated Postgres:** attractive if the team already maintains a suitable service.

I added a **proposed** entry to [decisions.md](<workspace>/pilot/private/published-decision-1/candidate/decisions.md:13). The original SQLite decision remains accepted pending your approval of a replacement.

Verified that the original entry is unchanged. Runtime and recovery checks remain untested; no network access, migration, deployment, or installed-skill changes occurred.

## Actual starting decision file

# Decisions

## 2026-08-15 — Prototype database

- **Status:** Accepted
- **Context:** The first prototype runs locally for one person and needs simple persistence.
- **Options considered:** JSON file, SQLite, hosted Postgres.
- **Decision:** Use local SQLite.
- **Rationale:** It provides reliable local persistence without infrastructure or recurring cost.
- **Consequences and reversal difficulty:** Concurrent remote use is not supported. The data model can later migrate, but migration and remote operations would need to be planned.
- **Reconsider when:** Multiple people require concurrent writes, remote access becomes necessary, or reliable off-device backups are required.

## Actual resulting decision file

# Decisions

## 2026-08-15 — Prototype database

- **Status:** Accepted
- **Context:** The first prototype runs locally for one person and needs simple persistence.
- **Options considered:** JSON file, SQLite, hosted Postgres.
- **Decision:** Use local SQLite.
- **Rationale:** It provides reliable local persistence without infrastructure or recurring cost.
- **Consequences and reversal difficulty:** Concurrent remote use is not supported. The data model can later migrate, but migration and remote operations would need to be planned.
- **Reconsider when:** Multiple people require concurrent writes, remote access becomes necessary, or reliable off-device backups are required.

## 2026-10-31 — Shared writes and remote recovery

- **Status:** Proposed
- **Context:** Several staff members now need concurrent writes and reliable remote backups, meeting two reconsideration conditions in the accepted prototype decision above. This fixture contains no application, schema, workload measurements, or hosting configuration to validate a replacement. The accepted local SQLite decision remains in force until the user accepts a replacement; it is not superseded by this review.
- **Options considered:**
  1. Keep SQLite behind one application service on one host. SQLite serializes writes; brief transactions may support a small staff workload. Staff would access the application rather than share the database file over a network filesystem. Add database-consistent, automated off-device backups with failure alerts and verified restores. This preserves the database and minimizes migration work, but adds remote service operations and requires contention testing; it suits modest write volume and tolerable single-host downtime.
  2. Move to managed Postgres behind the application. This is the recommended direction if staff need remote access and overlapping writes, and no existing operated database meets the need. It supports concurrent transactions and can reduce database operations work. Provider-specific backup retention, restore capability, region, access controls, and cost still require evaluation; managed hosting alone does not prove recoverability.
  3. Use an existing operated Postgres service, or self-host one. This is reasonable if the team already has a suitable service and someone accountable for patching, monitoring, backup alerts, and recovery. Starting those operations from scratch adds maintenance and availability responsibilities that are difficult to justify for this prototype.
- **Decision:** Propose managed Postgres as the default replacement, conditional on the missing requirements below. No provider is selected and no implementation, purchase, migration, deployment, or transfer of data is authorized. Accepting this architectural direction would not itself authorize those actions.
- **Rationale:** The original single-person, local-only assumptions have changed. A shared database service fits the new direction, while managed operations may reduce maintenance. Several users alone do not prove SQLite is inadequate: a low-contention workload through one service could justify retaining it.
- **Consequences and reversal difficulty:** Postgres makes shared transactions easier and may provide stronger recovery tooling, while introducing recurring cost, credentials, network access controls, and hosting decisions. Migration requires schema/query compatibility checks and data validation. Returning to SQLite becomes harder after Postgres-specific features or new shared writes are introduced; provider-specific backup and identity features can also increase switching effort.
- **Requirements before acceptance:** Confirm whether staff connect remotely through one application, expected write overlap and transaction duration, acceptable data loss and recovery time, budget, data sensitivity/location requirements, and existing hosting/operations ownership. Modest serialized writes favor option 1; an existing maintained Postgres service favors option 3. Backup frequency and retention must follow the recovery requirements.
- **Verification before any later cutover:** Test overlapping staff edits, conflict handling and failed transactions. Verify a consistent source backup by restoring it separately; validate migrated records and application behavior; test remote backup failure alerts and a timed restore. Plan a write freeze and rollback to the preserved source. After new writes begin on the replacement, rollback needs reconciliation to avoid losing those writes. None of these runtime or recovery checks has been performed in this documentation-only review.
- **Reconsider when:** Workload evidence supports retaining SQLite, an existing database service changes operational cost, or recovery, privacy, availability, or budget requirements invalidate the proposed path. On acceptance, record approval and mark the earlier decision superseded with a reference to this entry.
