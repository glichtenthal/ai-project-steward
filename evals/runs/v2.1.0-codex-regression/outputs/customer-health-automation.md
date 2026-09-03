Outcome: a daily scheduled workflow is the best starting design. It minimizes integration complexity while still surfacing accounts whose engagement has deteriorated. Nothing has been created or connected.

Success scenario: each weekday morning, review recent CRM activity, identify customers that meet agreed risk signals, and prepare a private Slack alert for the customer-success owner to review before acting.

| Option | How it works | Strengths | Trade-offs |
|---|---|---|---|
| Scheduled routine | Runs daily/weekly; queries CRM activity, evaluates health rules, drafts a private Slack alert | Simplest, predictable, easy to audit and tune | Alerts are not immediate |
| Event-driven integration | CRM activity changes trigger an immediate assessment and draft | Timely, avoids periodic scanning | More connector permissions, retries, duplicate-event handling, and operational complexity |
| Small app | A purpose-built dashboard/service evaluates health and lets users review drafts | Best control, history, and customization | Highest build, maintenance, hosting, and security burden |

Recommended design: scheduled routine, initially once each weekday.

1. Read only the minimum CRM fields: account owner, last meaningful activity, open support/escalation indicators, renewal date, and agreed usage/engagement metrics.
2. Apply transparent rules such as “no meaningful activity for 21 days” or “renewal within 60 days plus declining usage.” Exact thresholds should be owned by the customer-success team.
3. Produce one private Slack draft per owner or a private digest, including the account, reason it was flagged, relevant dates, and a suggested next step.
4. Require human review before any message is sent or CRM record is changed.
5. Retain only the alert metadata needed for troubleshooting; avoid copying sensitive CRM notes into Slack.

This makes a pilot fast to validate and keeps access limited to read-only CRM data plus private Slack drafting. Moving later to event-driven alerts is feasible, but introduces more failure modes and connector maintenance; building an app is best deferred until the team needs a review queue, analytics, or custom workflows.

Approval boundary: before implementation, you would need to approve the cadence, the health signals/thresholds, which private Slack destination receives drafts, and the read-only CRM/Slack permissions. No `decisions.md` was created because no material choice has been accepted yet.