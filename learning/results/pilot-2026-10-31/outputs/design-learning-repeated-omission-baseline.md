# Actual agent output: design-learning-repeated-omission / baseline

Synthetic advisory fixture; public extract, not live validation.

Instruction SHA-256: c67ec8f590dac213267d8d1b7b6a5010bf1ab74224be631279c767ef7260976f
Prompt SHA-256: da7c89550c0e8888e2d65e8a9b48a5aff6e573adeca3bfe1880edbcab864b890
Execution exit: 0; timeout: False; elapsed: 20.029 seconds.

## Output (local paths and personal name redacted)

The skill already requires empty states. Two approved handoffs omitting them suggest a gap in the approval check; another reminder would add little.

Recommend a **state-coverage check before approval**, recorded in the existing experience specification. Apply it across relevant states so the improvement generalizes beyond empty states.

Proposed wording for “Approval And Change Gates”:

> Before marking a handoff `approved`, review each in-scope route or workflow against the applicable state list. Record each state as specified, not applicable with a reason, or unresolved. For applicable states, link the expected behavior and acceptance criteria. Unresolved behavior keeps the handoff in `draft`.
>
> For empty states, distinguish first use, no matching results, and data removed or cleared where relevant. Specify the trigger, user-facing explanation, available next action, and behavior when the user lacks permission to take that action.

Keep this proportionate: a compact table in the existing specification is sufficient. No new document, tool, or approval stage is needed.

Validate the proposal by replaying the check against both omitted handoffs, then using it on the next applicable handoff. Success means it exposes the missing behavior before approval and gives engineering enough detail to implement without guessing.

**Evidence limit:** I reviewed SKILL.md and your report, not the two handoffs. The proposal addresses a plausible enforcement gap; its effectiveness remains untested. No files were changed.
