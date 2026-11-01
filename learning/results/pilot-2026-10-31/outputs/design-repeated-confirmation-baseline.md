# Confirmation: design-repeated-confirmation / baseline

Actual synthetic-fixture agent execution. Model gpt-6.1-sol high; Codex CLI 0.166.0-alpha.5.1. Sandbox: read-only. Exit: 0; timeout: False; elapsed: 19.571 seconds.

Instruction SHA-256: c67ec8f590dac213267d8d1b7b6a5010bf1ab74224be631279c767ef7260976f
Prompt SHA-256: da7c89550c0e8888e2d65e8a9b48a5aff6e573adeca3bfe1880edbcab864b890

## Output

Mode: `audit`. Based on your report, two approved handoffs omitted empty-state behavior; I haven’t inspected those artifacts.

`SKILL.md` already requires applicable empty states. The improvement should make state coverage verifiable at handoff, rather than add another reminder or approval step.

Proposed addition to the handoff requirements:

> Before marking a specification `approved`, review state coverage for each in-scope workflow. Explicitly identify applicable states and mark exclusions with a brief reason. For each applicable empty state, specify its trigger, user-facing message, available action, and recovery path. Distinguish first-use emptiness, no matching results, and unavailable data when their meanings or next actions differ. Link these requirements to behavioral acceptance criteria. An omitted state is unresolved, not implicitly out of scope.

Keep this in the existing experience specification. A compact state-coverage table would make omissions easier to spot without creating a separate document.

Validate the proposal by checking whether it exposes both reported omissions, then applying it to the next two handoffs. Success means an engineer can implement the applicable empty states without inventing behavior. That would demonstrate improved handoff completeness, not yet improved user outcomes.

Preserve existing approvals for routine clarifications within the approved direction; use the existing change gate if the correction materially changes workflow or data meaning.

No files were changed. The specific cause of the omissions—and whether this check would have prevented them—remains unverified.
