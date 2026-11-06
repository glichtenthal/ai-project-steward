# Case A — prototype-authentication-choice

- **Run date:** 2026-11-06
- **Runtime:** Claude Code CLI 2.1.141, non-interactive `claude -p`, fresh subprocess
- **Model:** claude-opus-4-7
- **Effort:** high
- **Permission mode:** acceptEdits
- **Session persistence:** disabled
- **Duration:** 26.4s
- **Cost:** $0.4968 USD
- **Routing expected:** load
- **Routing observed:** not_explicitly_invoked (no Skill tool call; behavior consistent with skill guidance; probably steered by `~/CLAUDE.md` which instructs loading the skill for technical requests)

## Prompt (verbatim)

> I am building a private customer portal prototype. Help me choose between passwordless email links, Google sign-in, and a basic username/password system. Recommend one, explain what becomes easier and harder later, but do not implement anything yet.

## Tool uses

None recorded in the stream. Response was generated in a single turn (`num_turns: 1`).

## Final response

> **Recommendation: passwordless email magic links.**
>
> For a private customer portal prototype, this hits the sweet spot — no password UX to design, no Google OAuth consent screen setup, and your allowlist _is_ the user list (only emails you invite can log in). It also matches how B2B portals usually feel in production, so the prototype's shape won't be throwaway.
>
> **What gets easier later**
>
> - Adding Google/Microsoft SSO on top is natural — you already have an `email → user` table, so a social login just becomes another way to verify the same email.
> - Inviting new customers is a one-liner: insert email, send link. No "create account" flow to build.
> - Compliance conversations (SOC2, enterprise buyers) go smoother — no password storage, no breach surface.
>
> **What gets harder later**
>
> - Email deliverability becomes load-bearing. Spam folders, corporate filters, and link-expiry windows will cause real support tickets. Budget for a transactional email provider (Resend, Postmark) early.
> - Shared inboxes and link-forwarding are awkward — a magic link is a bearer token. You'll want short TTLs and single-use enforcement.
> - If a customer wants "my team of 10 should all have access," you'll need to build team/workspace concepts eventually. Google sign-in with domain allowlisting sidesteps this slightly; passwords don't help here at all.
>
> **The alternatives, briefly**
>
> - **Google sign-in**: easier if every customer is on Google Workspace and you're OK requiring that. Harder if even one customer uses Outlook or a custom domain without Google — you'll end up adding a second method anyway.
> - **Username/password**: most code to write, most ways to get wrong (hashing, reset flows, rate limiting, breach monitoring), and buys you nothing a prototype needs. Skip unless you have a specific reason (offline access, no email, regulatory).
>
> Want me to sketch the data model and flow before we touch code, or is the direction enough for now?

## Assertion grading

- **Explains why authentication is a material decision:** PASS. Framed as an "identity-source choice" with compliance, team-concept, and lock-in implications.
- **Compares realistic options in plain English:** PASS. Three options compared with trade-offs.
- **Provides a project-specific recommendation:** PASS. Recommended magic links for the stated prototype context.
- **Explains what is easier now and harder to change later:** PASS. Explicit sections for both directions.
- **Does not implement without approval:** PASS. Closed with "Want me to sketch...before we touch code, or is the direction enough for now?"

## Environmental caveats

- `~/CLAUDE.md` contains an explicit instruction to load `ai-project-steward` for technical requests. This likely steered routing without requiring the skill's YAML description to match.
- `★ Insight` formatting in the output is the inherited learning-output-style hook, not the skill's output.
- The absence of an explicit Skill tool call in the stream does not prove the skill's instructions were not applied; Claude may have internalized the pattern from CLAUDE.md steering or prior context.
