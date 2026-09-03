Outcome: design a workflow that identifies at-risk customers from CRM activity and drafts—not sends—a private Slack alert for human review. Success means it handles no/recent activity correctly, avoids duplicate alerts, keeps customer data private, and leaves the final send decision with a person.

★ Insight ─────────────────────────────────────  
- “Draft” is an important safety boundary: the workflow may prepare a message but must not post automatically.  
- The decisive design factor is how quickly risk must be surfaced: hourly/daily is very different from near-real-time.  
─────────────────────────────────────────────────

| Option | How it works | Strengths | Trade-offs |
|---|---|---|---|
| Scheduled routine | At a set interval, read relevant CRM activity, score/flag accounts, and create reviewable Slack drafts. | Fewest moving parts; easy to audit, retry, and control alert volume. | Alerts are delayed until the next run; needs a reliable way to prevent repeat drafts. |
| Event-driven integration | CRM activity changes trigger an immediate evaluation and draft. | Timely; processes only changed records. | Requires webhook/event permissions, idempotency, retry handling, and careful handling of noisy or out-of-order events. |
| Small app | A lightweight internal app pulls CRM data, applies rules, displays a review queue, and lets a user create Slack drafts. | Best transparency, overrides, and audit trail; rules can evolve safely. | More build and maintenance work; requires hosting and access-control decisions. |

Recommendation: start with a scheduled routine—typically daily for account health, or hourly if the team needs faster follow-up. It is the safest first implementation because it minimizes integration complexity while retaining a clear review boundary. It makes later migration to events straightforward if prompt response becomes demonstrably necessary; switching to a full app later costs more but adds human workflow control.

Proposed initial behavior:

1. On each run, fetch CRM activity for active customers.
2. Apply agreed risk signals, such as no activity in N days, declining engagement, or unresolved support issues.
3. Suppress accounts already drafted/acknowledged within a chosen cooldown period.
4. Produce a concise private Slack draft containing account, reason, relevant activity, and a CRM link.
5. Require a reviewer to approve or post it.

The material choice is the CRM/Slack access model and data exposure. Before any implementation or connection, please approve the architecture direction—my recommendation is the scheduled routine—and specify the required alert freshness (daily, hourly, or near-real-time). That answer could change the recommendation to event-driven.