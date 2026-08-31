# Building Partner Quick Demo

Use this when AI is helping plan or implement a technical build and material choices need to remain visible.

## Input

```text
I want a recurring customer-health workflow that reads HubSpot activity and drafts a private
Slack alert when an account appears at risk. I know the outcome I want, but I do not know
whether this should be a scheduled routine, an event-driven integration, or a small app.
Do not implement anything until we agree on the approach.
```

## Copy-Paste Prompt

```text
Use Building Partner on this request. Compare the realistic approaches, recommend one,
explain what becomes easier now and harder to change later, and identify any approvals
needed before implementation.
```

## Representative Output Shape

```text
Intended outcome
- Detect meaningful customer-risk signals and prepare a private alert without sending or
  changing external data until the workflow has been reviewed.

Options
1. Scheduled routine: simplest setup and easiest to inspect; signals may be delayed.
2. Event-driven integration: faster alerts; more permissions, failure handling, and maintenance.
3. Small custom app: most control; highest build and hosting overhead.

Recommendation
- Start with a scheduled routine using read-only CRM access and a private draft destination.
  This is enough to test whether the risk signals are useful before adding real-time infrastructure.

Easier now
- Fewer moving parts, lower operational cost, simpler manual testing, and a clear rollback path.

Harder later
- Moving to real-time alerts will require a new trigger model and more robust deduplication.

Approval gates
- Ask before connecting HubSpot or Slack, changing permission scope, sending a real alert,
  enabling an automatic schedule, or creating a recurring charge.

Decision record
- After approval, record the selected approach and reconsideration conditions in decisions.md.

Verification
- Dry-run against one healthy account, one genuinely at-risk account, and one account with
  missing activity data. Confirm that no external message is sent during the test.
```

## Natural Next Step

Approve or revise the recommended approach, then ask Building Partner to implement the smallest working version and run the three verification scenarios.
