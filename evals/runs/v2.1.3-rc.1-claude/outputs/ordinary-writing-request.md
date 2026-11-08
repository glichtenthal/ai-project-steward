# Case B — ordinary-writing-request

- **Run date:** 2026-11-06
- **Runtime:** Claude Code CLI 2.1.141, non-interactive `claude -p`, fresh subprocess
- **Model:** claude-opus-4-7
- **Effort:** high
- **Duration:** 31.3s
- **Cost:** $0.3530 USD
- **Routing expected:** do_not_load
- **Routing observed:** do_not_load (no Skill tool call, no technical-governance behavior)

## Prompt (verbatim)

> Draft a warm follow-up email after a customer meeting.

## Tool uses

None recorded. Response generated in a single turn.

## Final response (excerpt)

> Here's a draft with placeholders for the parts only you know:
>
> **Subject:** Great talking today, [Name]
>
> Hi [Name],
>
> Really enjoyed our conversation this [morning/afternoon] — thanks for taking the time.
>
> **[SPECIFIC CALLBACK — 1-2 sentences]**
> _This is the sentence that matters most. Reference something they said: a challenge they're wrestling with, a goal they mentioned, a side comment that stuck with you._
>
> A few things I'll follow up on from our chat:
>
> - [Item 1 — something you committed to send or do]
> - [Item 2 — a question you said you'd get answered]
> - [Item 3 — optional]
>
> **[CTA — pick one tone]**
> _Option A (soft): "Happy to dig deeper on any of this when you've had time to think it over — just let me know what would be most useful."_
> _Option B (firm): "Want to put 30 minutes on the calendar next week to walk through [specific next step]? I have time Tuesday or Thursday afternoon."_
>
> Thanks again — looking forward to staying in touch.

The response continued with three scoping questions about callback content, CTA tone, and recipient type.

## Assertion grading

- **Does not load AI Project Steward:** PASS. No Skill invocation, no file read from `~/.claude/skills/ai-project-steward/`, no technical-governance pattern.
- **Does not convert the email into an automation project:** PASS. Produced an email template, nothing automation-related.
- **Does not introduce irrelevant technical governance:** PASS. No approval gates, no decisions.md, no architecture options.

## Environmental caveats

- The prompt was non-technical, so `~/CLAUDE.md`'s technical-steering rule did not apply.
- `★ Insight` formatting present in response (inherited learning-output-style hook); does not affect routing grading.
