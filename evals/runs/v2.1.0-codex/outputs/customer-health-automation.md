I recommend starting with a scheduled routine that prepares alerts for human review in a private Slack channel. It is the smallest, safest design under the assumption that daily customer-health monitoring is sufficient for one customer-success team.

No workflow, integration, connection, or external resource was created.

## Proposed workflow

1. On weekday mornings, request CRM activity changed since the last successful run using read-only credentials.
2. Normalize relevant signals—such as inactivity, support escalation, renewal proximity, or declining engagement.
3. Apply explicit, versioned health rules.
4. Suppress duplicates using an account-and-reason fingerprint plus a cooldown period.
5. Generate a private alert draft containing:
   - Customer and owner
   - Health concern and severity
   - Specific CRM evidence
   - Suggested next action
   - Link to the CRM record
6. Place the draft in a review queue. After human approval, it may be posted to a restricted Slack channel such as `#customer-health-review`.
7. Record the processing checkpoint, rule version, draft status, and fingerprint—not the complete CRM activity payload.
8. On failure, preserve the last successful checkpoint and notify an operator without advancing it.

Example draft:

> **Customer health review: Acme Corp — High risk**  
> No meaningful activity in 21 days; renewal is in 43 days; two support escalations remain open.  
> Owner: Jordan · Suggested action: confirm an executive check-in this week.  
> Evidence: [CRM record]

## Options compared

| Option | Strengths | Trade-offs | Best fit |
|---|---|---|---|
| Scheduled routine | Fewest components; easy to audit, retry, and disable; no public webhook receiver | Alerts are delayed by the schedule; polling consumes CRM API calls | Daily or hourly monitoring with moderate volume |
| Event-driven integration | Near-real-time alerts; less polling | Requires webhook validation, a reachable endpoint, retries, event ordering, idempotency, and reconciliation for missed events | Risks requiring intervention within minutes |
| Small app | Strong review experience, rule configuration, history, ownership, and access controls | Highest build and maintenance burden; still needs either polling or events underneath | Multiple teams, complex rules, or a substantial approval queue |

A small app is not truly a third triggering method: it is a product layer around a scheduled or event-driven backend.

## Material recommendation

Use a scheduled routine first, with human approval before Slack posting and a private channel rather than individual DMs.

This makes the first version easier to understand, operate, and reverse. Moving later to event-driven processing would require redesigning checkpoints around event IDs, retries, and reconciliation. Adding a full app later is straightforward if review volume or configuration needs justify it.

Before implementation, I would need approval on three consequential choices:

- Is daily monitoring sufficient, or do some conditions require near-real-time alerts?
- Should drafts require human approval, or may qualifying alerts post automatically?
- Should the destination be a restricted team channel or individual DMs?

No `decisions.md` was created because these choices remain proposed rather than accepted.

`★ Insight ─────────────────────────────────────`
The health rules are the real business product; the trigger is infrastructure. Keeping rules deterministic and versioned makes every alert explainable, while deduplication and cooldown controls usually matter more to adoption than faster delivery.
`─────────────────────────────────────────────────`