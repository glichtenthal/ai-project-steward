I recommend a simple internal form feeding a scheduled weekly report.

It’s the lowest-risk way to prove the feedback loop before taking on app maintenance or integration complexity. Keep raw feedback access limited to a small, named group; publish only aggregated themes and anonymized quotes.

★ Insight ─────────────────────────────────────

- “Anonymous” forms can still expose identity through login requirements, timestamps, IP/device metadata, or writing style—privacy design matters more than the form brand.
- A weekly cadence creates a useful review ritual, but it is not suitable for urgent HR, safety, or conduct issues; provide a separate escalation channel.
─────────────────────────────────────────────────

| Option | Best when | Practical trade-offs |
|---|---|---|
| Simple form + scheduled report **(recommended)** | You need a weekly pulse, a small number of question types, and a quick, low-maintenance rollout | Fast, inexpensive, familiar. Less tailored workflow and limited real-time action. |
| Small custom app | You need nuanced anonymity controls, role-based access, case tracking, follow-up, or a bespoke employee experience | Better control and UX, but requires secure development, hosting, maintenance, and ongoing ownership. |
| Event-driven integration | Feedback must trigger immediate routing, alerts, tickets, or actions in HR/Slack/project systems | Powerful automation, but introduces more permissions, failure modes, audit needs, and privacy exposure. |

A practical first version would collect a small set of structured signals (for example: sentiment, topic, optional team) plus one free-text response. Each week, it should produce:

- response count and participation trend;
- recurring themes, split into praise, friction, and requests;
- a small set of carefully anonymized representative comments;
- suggested owners/actions, with human review before sharing.

What this makes easy now: launch quickly, validate whether employees actually use it, and refine questions without committing to infrastructure. What becomes harder later: sophisticated identity protection, two-way case management, and real-time workflows—those are reasons to graduate to a custom app or integration if they become necessary.

I would revisit the choice if any of these become true: feedback needs action within hours, HR/legal requires auditable case handling, anonymity must be technically stronger than a standard internal form can provide, or the weekly process routinely requires manual consolidation across systems.