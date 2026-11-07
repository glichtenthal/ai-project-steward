# Case I — ordinary-crm-explanation

- **Run date:** 2026-11-06
- **Runtime:** Claude Code CLI 2.1.141, non-interactive `claude -p`, fresh subprocess
- **Model:** claude-opus-4-7, high effort
- **Working directory:** `dist/claude-eval-runs/I/workdir/` (empty)
- **Duration:** 3.9s
- **Cost:** $0.3203
- **Routing expected:** do_not_load
- **Routing observed:** do_not_load (zero tool calls)

## Prompt

> In two or three sentences, explain what a CRM is and why a sales team might use one.

## Response

> A CRM (Customer Relationship Management system) is software that stores and organizes information about a company's prospects and customers — contacts, conversations, deal stages, and account history — in one shared place. Sales teams use one to track every opportunity through the pipeline, remember what was said in prior interactions, and hand off accounts cleanly between reps. It also gives leaders visibility into forecast, activity, and which deals need attention before they slip.

## Assertion grading

- **Does not load AI Project Steward:** PASS. Zero tool calls, zero file reads, zero bash.
- **Answers directly and concisely:** PASS. 3 sentences, exactly as requested.
- **Does not invent a technical build:** PASS. No implementation, no decision record, no architecture framing.

## Note

Fast case: 3.9s. The non-technical framing of the request correctly bypassed `~/CLAUDE.md`'s technical-steering rule.
