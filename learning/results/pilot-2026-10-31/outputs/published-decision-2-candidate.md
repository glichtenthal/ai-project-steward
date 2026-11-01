# Confirmation: published-decision-2 / candidate

Actual synthetic-fixture agent execution. Model gpt-6.1-sol high; Codex CLI 0.166.0-alpha.5.1. Sandbox: workspace-write. Exit: 0; timeout: False; elapsed: 56.357 seconds.

Instruction SHA-256: a67245b3797c837d58f94010ce1930352bb15865e514331b8a2dc66a748f9c16
Prompt SHA-256: b4660e0e08a510d6586ca5f3cbecb82bbd2e5a5a7fb4a91727154ad07fb4d704

## Output

The new requirements justify reconsidering SQLite. I recommend managed Postgres if overlapping staff writes will be routine. SQLite behind a shared application remains viable for light writes with tested remote backups; self-managed Postgres adds operational work.

I added a **proposed** decision to [decisions.md](<workspace>/pilot/private/published-decision-2/candidate/decisions.md:13), covering options, trade-offs, missing facts, and future verification. The accepted SQLite decision remains unchanged and in force pending your approval.

Verified that the edit only appends the proposal. No network use, migration, deployment, or installed-skill changes occurred. Concurrency and recovery remain untested.

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

- **Status:** Proposed. The accepted 2026-08-15 SQLite decision remains in force until the user accepts a replacement. This review authorizes no migration, deployment, service purchase, or configuration change.
- **Context:** Several staff members now need concurrent writes and reliable remote backups. These requirements trigger reconsideration of the single-person, local-only prototype decision. Multiple users alone do not rule out SQLite: a central application can queue short writes, but SQLite permits only one writer at a time. Remote backup reliability requires a consistent backup, off-device storage, monitoring, and verified restoration regardless of database choice.
- **Options considered:**
  1. Retain SQLite behind one central application, serialize writes, and add scheduled consistent off-device backups. This minimizes database changes and can suit light write contention; it requires operating the application host and backup process, and write contention or host failure can limit service. Staff should access the application rather than a database file on a shared network drive.
  2. Use managed Postgres behind a shared application, with verified backup and recovery capabilities. This better supports overlapping writes and reduces database operations work; it adds recurring cost, network dependence, access-control configuration, and migration effort. Backup retention, recovery granularity, export access, and restore procedures must be checked for the chosen service and plan.
  3. Operate Postgres and remote backups ourselves. This provides concurrent database access and more infrastructure control, but leaves patching, monitoring, backup verification, and recovery with the project. It is reasonable only if an existing supported platform and operations owner make it simpler than a managed service.
- **Proposed decision and rationale:** Prefer managed Postgres if staff will use a shared remote application and overlapping writes are a continuing requirement, subject to approval of cost, data location, permissions, and recovery capabilities. It addresses the changed usage pattern while avoiding self-managed database operations. If writes are infrequent and can queue, retaining SQLite with a central application and tested remote backups may still be the simpler adequate choice. No provider or plan is selected in this offline review.
- **Consequences and reversal difficulty:** Managed Postgres makes shared writing and database operations easier, but requires application integration and a planned data migration. Provider-specific authentication, backup tooling, or extensions could make replacement harder; standard SQL and tested exports reduce that dependence. A backup does not by itself provide availability during an outage. Returning to local SQLite after shared use would require reconciling writes and losing the shared operating model.
- **Facts needed before acceptance:** Confirm whether staff access one shared application or separate local copies; expected write frequency, overlap, and transaction duration; acceptable data loss and recovery time; uptime and offline-use needs; budget; data sensitivity and residency; and who owns operations. These facts could favor the SQLite path or require additional synchronization design. No application, workload measurements, or backup configuration was available in this fixture.
- **Required evidence before any later cutover:** Separately approve implementation and external actions. Verify an existing backup by restoring it, rehearse migration on a copy, and check row counts, constraints, and key workflows. Test overlapping staff writes for lost updates and lock failures, staff permissions, connection failures, and remote restoration after loss of the primary host. Define the write freeze, verified rollback copy, and rollback procedure; accepting new writes in the replacement database is the point after which rollback needs reconciliation. Nothing in this review verifies those behaviors.
- **Reconsider when:** Workload measurements show queuing is adequate or contention is unacceptable; recovery or availability targets change; costs or residency requirements change; or an existing supported platform changes the operations trade-off.
