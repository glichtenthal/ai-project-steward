Switching the project back to local SQLite would conflict with the accepted decision and current requirements.

The local `decisions.md` says SQLite was superseded specifically because several staff members need concurrent writes and reliable off-device backups. Those requirements have not been documented as changed.

Realistic options:

- Keep managed PostgreSQL for both the demo and eventual operation. Best continuity, but requires enough service setup to run the demo.
- Use SQLite only as an isolated, disposable demo mode. Reasonable if the demo is single-user, contains no canonical data, requires no synchronization, and is clearly not evidence that production requirements are satisfied.
- Reverse the accepted decision and restore SQLite project-wide. Not justified unless concurrent staff access and remote-backup requirements have genuinely disappeared.

Recommendation: preserve managed PostgreSQL as the accepted target. Consider SQLite only as a tightly scoped demo convenience—not as a reversal—provided it will not create database-specific behavior or a second implementation that must be maintained.

A demo-only SQLite path makes immediate setup easier, but introduces two risks: the demo may not exercise PostgreSQL-specific behavior, and data/schema differences may create later rework. I could not assess that implementation cost because this workspace contains only `decisions.md`, with no application code or separate requirements files.

No files, data, accounts, services, or deployments were changed.
