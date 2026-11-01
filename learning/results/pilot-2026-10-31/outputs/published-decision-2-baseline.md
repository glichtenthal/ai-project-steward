# Confirmation: published-decision-2 / baseline

Actual synthetic-fixture agent execution. Model gpt-6.1-sol high; Codex CLI 0.166.0-alpha.5.1. Sandbox: workspace-write. Exit: 0; timeout: False; elapsed: 59.616 seconds.

Instruction SHA-256: e9701b824c6ad04ae8551a1d7cd5d039916bf6be76931074ad933ff60870aac7
Prompt SHA-256: b4660e0e08a510d6586ca5f3cbecb82bbd2e5a5a7fb4a91727154ad07fb4d704

## Output

The new requirements justify reconsidering SQLite: both match triggers in the accepted decision.

I recommend **managed PostgreSQL** for staff writing concurrently from separate machines. Two alternatives remain viable:

- **Centralized SQLite:** simpler for light, brief writes, with consistent remote backups and tested restores.
- **Self-hosted PostgreSQL:** appropriate if existing infrastructure and an operator can support it.

The recommendation depends on write volume, hosting, budget, and acceptable data loss and recovery time.

I added a **Proposed** entry to [decisions.md](<<workspace>/pilot/private/published-decision-2/baseline/decisions.md:13>). The original remains **Accepted** pending your decision; acceptance of a replacement should mark it **Superseded**.

Verified the diff preserves the original entry. Concurrency and recovery remain untested. No network access, migration, deployment, or installed-skill changes occurred.

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

## 2026-10-31 — Shared writes and remote backups

- **Status:** Proposed
- **Context:** Several staff members now need concurrent writes and reliable remote backups. Both requirements trigger reconsideration of the prototype database decision above. This fixture contains no application, workload measurements, hosting configuration, or backup evidence, so this is an architecture review rather than a validated implementation plan.
- **Options considered:**
  1. Keep SQLite behind one application server, serialize writes, and add consistent off-device backups. This retains the existing database and can suit short, infrequent writes, but requires centralized application hosting, contention handling, backup monitoring, and restore testing. Do not share the database file across staff machines or a synced/network folder.
  2. Use managed PostgreSQL through the application. This is the recommended direction for staff working from separate machines with overlapping writes. It supports concurrent database writers and reduces database operations work, but introduces recurring cost, network dependence, access configuration, and a planned migration. Backup retention and recovery capabilities must be confirmed for the chosen service and plan; hosting alone does not establish reliable recovery.
  3. Self-host PostgreSQL and maintain remote backups. This offers infrastructure control and the same database concurrency model, but makes the project responsible for patching, availability, monitoring, and recovery. Consider it if existing infrastructure and an accountable operator make that burden reasonable.
- **Decision:** Recommend replacing local SQLite with managed PostgreSQL, conditional on confirming deployment topology, write workload, budget, and recovery requirements. No replacement has been approved. The 2026-08-15 decision remains Accepted for the current prototype. If a replacement is accepted, mark that earlier decision Superseded and link it to the accepted successor; do not erase the original rationale.
- **Rationale:** The earlier choice was appropriate for one local user. Shared writes and off-device recovery change that operating model. Managed PostgreSQL is the preferred default for shared remote use; centralized SQLite remains a reasonable smaller change if writes are brief and contention is demonstrably low. Staff count alone does not prove SQLite is unsuitable.
- **Consequences and reversal difficulty:** Managed PostgreSQL makes shared writes and database operations easier, while adding ongoing cost and provider dependencies around backups, access, and hosting. Standard PostgreSQL limits database-engine lock-in, but changing providers still requires data transfer and recovery planning. Returning to SQLite becomes harder after schema changes or new production writes. Choosing centralized SQLite avoids an engine migration now but retains a single-writer limit and application-server operations.
- **Open facts that could change the recommendation:** Whether all writes can pass through one server; overlapping write frequency and transaction duration; offline requirements; available hosting and operational ownership; acceptable recurring cost; maximum acceptable data loss and restore time; backup retention and privacy requirements. A light centralized workload favors SQLite; substantial overlap favors PostgreSQL; offline operation requires a separate synchronization design.
- **Validation required before implementation approval:** Define measurable write and recovery targets. Exercise representative simultaneous staff edits, including edits to the same record, to check contention and prevent silent lost updates. Define safe behavior during network/database outages and failed writes. Verify consistent backups during writes, alerting on missed backups, and restoration into an isolated environment within the agreed recovery targets. None of these checks has been run in this fixture.
- **Migration and authorization boundary:** Review only is authorized. Before any future migration or deployment, obtain approval for the concrete service, costs, access model, and cutover plan. Identify and verify a restorable source backup, data/schema checks, a write-freeze or reconciliation strategy, and a rollback path. Preserve the source database. Once the destination accepts new writes, restoring the old database alone would lose those writes; rollback then requires reconciliation. No migration, deployment, purchase, or external access was performed for this review.
- **Reconsider when:** Workload measurements favor a simpler path; recovery targets exceed the selected backup capability; costs or operational ownership change; offline use becomes necessary; or portability, privacy, or availability requirements change.
