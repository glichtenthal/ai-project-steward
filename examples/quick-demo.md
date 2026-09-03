# Complete Project Build

This golden-path scenario shows the full operating layer: the prompt, surfaced choices, recommendation, approval boundary, decision record, implementation, and verification.

## Initial request

```text
Build a private customer-health prototype that reads recent CRM activity, identifies accounts
that may need attention, and drafts a private alert. I know the outcome I want, but I do not
know whether this should be a scheduled routine, an event-driven integration, or a small app.
Keep the first version private and do not connect or send anything until we agree on the approach.
```

## Steward response

```text
Intended outcome
- Prove that the selected CRM signals identify useful customer-risk cases and produce a reviewable
  private draft. The first version should not send alerts or modify CRM data.

Material choice
- The implementation model affects permissions, recurring cost, failure handling, portability,
  and maintenance.

Options
1. Scheduled routine: fewest moving parts and easiest to inspect; signals may be delayed.
2. Event-driven integration: faster alerts; broader permissions and more failure handling.
3. Small custom app: most control; highest build, hosting, and maintenance overhead.

Recommendation
- Start with a scheduled local routine using exported or read-only sample CRM data and a private
  draft output. It is enough to test signal quality before connecting live systems.

Easier now
- Lower cost, simpler testing, narrow permissions, and a clear rollback path.

Harder later
- Real-time alerts would require a trigger model, deduplication, and live connector permissions.

Approval boundary
- I can build and test the local version now. I will ask again before connecting HubSpot or Slack,
  storing real customer data, enabling a schedule, sending a message, or creating a recurring charge.
```

## User decision

```text
Approved. Build the local scheduled version with fixture data. Do not connect external accounts
or send messages.
```

## Decision recorded

```markdown
## 2026-09-01 — First customer-health implementation

- **Status:** Accepted
- **Context:** The first version needs to test signal usefulness without live CRM or Slack access.
- **Options considered:** Scheduled routine, event-driven integration, small custom app.
- **Decision:** Build a local scheduled routine using fixture data and private draft output.
- **Rationale:** It tests the core use case with the fewest moving parts and no external permissions.
- **Consequences and reversal difficulty:** Alerts are not real time. Moving later requires trigger,
  connector, and deduplication work, but the risk rules can be reused.
- **Reconsider when:** The signals prove useful and alert delay becomes operationally important.
```

## Implementation handoff

The agent should now build the smallest working version, identify exactly which data is fixture data, and leave instructions that do not depend on the earlier chat.

```text
Implemented
- Added a local input fixture with healthy, at-risk, and missing-activity accounts.
- Added risk evaluation and private draft generation.
- Added a dry-run command; no connector, schedule, or message-sending capability was created.
- Recorded the accepted implementation decision in decisions.md.
```

## Verification

```text
Verified
1. Healthy account: no alert draft created — pass.
2. At-risk account: private draft created with the expected risk reasons — pass.
3. Missing activity: flagged as insufficient data rather than at risk — pass.
4. External-action check: no HubSpot connection, Slack connection, schedule, or send path exists — pass.

Not verified
- Live CRM permissions, live Slack formatting, scheduling reliability, and real-world signal quality
  remain untested because those capabilities were intentionally outside the approved first version.
```

The important behavior is not the exact wording. It is the visible chain from goal to decision to authorized implementation to an honestly bounded verification report.
