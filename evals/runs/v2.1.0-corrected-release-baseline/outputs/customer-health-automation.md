A scheduled routine is the best fit to start: it is simpler, easier to audit, and matches “customer health” as a periodic review rather than a real-time emergency. No workflow, integration, or connection was created.

★ Insight ─────────────────────────────────────  
Customer health is usually a derived signal: it needs a defined review window, such as “no meaningful CRM activity in 14 days.” That makes a scheduled check naturally resilient to delayed or incomplete CRM updates.  
─────────────────────────────────────────────────

| Approach | How it works | Strengths | Trade-offs |
|---|---|---|---|
| Scheduled routine | Runs daily or weekly, reads CRM activity, identifies at-risk accounts, drafts a private Slack alert | Fewest moving parts; predictable cost and operations; easy to revise thresholds | Alerts are delayed until the next run |
| Event-driven integration | CRM activity changes trigger immediate evaluation and Slack draft | Near-real-time response; efficient for truly urgent signals | More complex: webhooks, duplicate/out-of-order events, retries, and permission handling |
| Small app | A private app calculates health, shows review queues, and drafts Slack alerts on demand or schedule | Best visibility, approval controls, history, and later expansion | Highest build and maintenance cost; more data storage and access design |

Recommendation: begin with a scheduled routine that produces a private draft for a customer-success owner to review before sending. It makes the core behavior easy to validate without prematurely committing to webhook infrastructure or an application database.

A practical first rule could be: “Each weekday morning, flag active accounts with no logged customer-facing activity in the prior 14 days, excluding accounts with an upcoming meeting.” The private Slack draft should include the account, owner, last activity date, and a short suggested follow-up—without copying unnecessary CRM details.

This choice makes it easy to adjust cadence, thresholds, and alert wording. Moving later to event-driven alerts is feasible if teams need immediate response, but it would require durable event handling and stronger safeguards against noisy duplicates. A small app becomes justified when people need a shared review queue, alert history, overrides, or reporting.

Before creating anything, the material choices needing your approval are:

1. Who receives the private alert: each account owner, a customer-success lead, or a private team channel.
2. What qualifies as unhealthy: inactivity only, or inactivity plus renewal timing, support risk, usage, or other signals.
3. Review model: draft-only for human approval (recommended) or automatically posted private alerts.
4. Cadence: weekday daily (recommended) or weekly.

No `decisions.md` was created because no material option has been selected yet.