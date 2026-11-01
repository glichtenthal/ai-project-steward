# Confirmation: published-decision-1 / baseline

Actual synthetic-fixture agent execution. Model gpt-6.1-sol high; Codex CLI 0.166.0-alpha.5.1. Sandbox: workspace-write. Exit: 0; timeout: False; elapsed: 61.664 seconds.

Instruction SHA-256: e9701b824c6ad04ae8551a1d7cd5d039916bf6be76931074ad933ff60870aac7
Prompt SHA-256: b4660e0e08a510d6586ca5f3cbecb82bbd2e5a5a7fb4a91727154ad07fb4d704

## Output

The earlier decision warrants reconsideration: concurrent staff writes and remote backups both match its explicit reconsideration triggers.

I recommend **managed PostgreSQL**, provisionally. The realistic options are:

- **Centralized SQLite with remote backups:** fewest changes; viable if writes are brief and can queue behind its single writer.
- **Managed PostgreSQL:** better support for concurrent writers and less database administration, with recurring cost and provider dependence.
- **Self-hosted PostgreSQL:** more infrastructure control, but greater maintenance and recovery responsibility.

Write volume, budget, hosting restrictions, and acceptable data loss/recovery time could change that recommendation. Remote backups also need a verified restore procedure regardless of database choice.

I recorded the comparison as **Proposed** in [decisions.md](<<workspace>/pilot/private/published-decision-1/baseline/decisions.md:13>). The original SQLite decision remains **Accepted** pending your decision; it would be marked **Superseded** only after approval.

I checked the document diff and preserved the original entry. No network access, migration, deployment, or installed-skill changes occurred. Workload and backup recovery remain untested.

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

- **Status:** Proposed; approval pending. The 2026-08-15 decision remains Accepted. If this proposal is accepted, mark that earlier decision Superseded and link it to this entry; retain its original rationale.
- **Context:** Several staff members now need concurrent writes and reliable remote backups. Both are explicit reconsideration triggers in the earlier decision. SQLite can serve several users through a central application, but permits only one writer at a time. Staff count alone does not establish whether write contention will be a problem. Local persistence alone does not meet the new recovery requirement.
- **Options considered:**
  1. Keep SQLite behind one central application service, serialize writes with bounded waiting/retries, and add automated, consistent off-device backups with restore checks. This has the fewest database changes and may suit short, infrequent writes. It adds hosting and backup operations; one writer and the application host remain constraints. Staff must use the application rather than directly share a database file across machines.
  2. Use managed PostgreSQL with a backup/restore capability that meets agreed recovery targets. This supports concurrent database writers and can reduce routine database and backup operations. It introduces recurring cost, remote-data permissions, provider dependence, and migration work. Backup retention, restore access, and any point-in-time recovery must be confirmed for the selected service and plan; management alone does not prove recoverability.
  3. Self-host PostgreSQL with automated off-device backups and restore checks. This supports concurrent writers and gives more infrastructure control, but makes the project responsible for patching, availability, monitoring, backup failures, and recovery. Prefer this only if an existing supported environment or a hosting constraint justifies that work.
- **Decision:** Recommend replacing local-only SQLite with managed PostgreSQL, conditional on budget, data-hosting constraints, and recovery requirements. No provider is selected and no implementation is authorized by this proposal. If writes are demonstrably light and serialized access is acceptable, centralized SQLite with verified remote backups remains a realistic smaller alternative.
- **Rationale:** The new scope includes shared operation and recovery after loss of the local machine. A managed concurrent database is the likely best balance if the project has no existing database operator. Changing database engines alone will not prevent conflicting staff edits or prove backups usable; the application also needs explicit transaction and edit-conflict behavior.
- **Consequences and reversal difficulty:** Makes concurrent database writes and centrally managed recovery easier. Adds service cost, networking, access control, and migration responsibilities. Standard PostgreSQL schema and export paths help portability; provider-specific authentication and backup features would make replacement harder. Once staff write to a replacement database, returning to SQLite requires reconciling those writes and checking compatibility, not simply switching a connection setting.
- **Facts needed before acceptance:** Expected simultaneous write load and transaction duration; whether staff use a shared application or separate local copies; existing hosting and operational support; budget and permitted data locations/access; maximum acceptable data loss and recovery time. Light writes favor SQLite; existing operations or hosting restrictions could favor self-hosted PostgreSQL. These facts are not available in this fixture.
- **Verification required before implementation is considered complete:** Exercise simultaneous writes to different records and conflicting edits to the same record; check atomicity on interrupted writes and safe handling of contention/retries. Restore a consistent remote backup into an isolated environment after simulated loss of the original host, verify records and application behavior, and measure data loss and recovery time against agreed targets. Verify backup failure alerts and authorized recovery access. No runtime, workload, or restore validation was performed in this review.
- **Future migration boundary:** Before any migration or deployment, obtain explicit approval of the concrete plan, cost, and access model. Verify a usable source backup, rehearse data conversion and integrity checks on a copy, and define a write-pause/cutover and rollback procedure. Preserve the source; identify the first production write to the replacement as the point after which rollback requires write reconciliation. No migration or deployment is authorized or performed here.
- **Reconsider when:** Measured contention, recovery targets, cost, hosting/privacy constraints, or available operational support change the comparison.
