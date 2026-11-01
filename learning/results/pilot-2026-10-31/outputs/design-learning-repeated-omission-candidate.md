# Actual agent output: design-learning-repeated-omission / candidate

Synthetic advisory fixture; public extract, not live validation.

Instruction SHA-256: 4039da168236b1ca58221a9ea028fbc2cb859ac95b8e9825270ba7febf692e0a
Prompt SHA-256: da7c89550c0e8888e2d65e8a9b48a5aff6e573adeca3bfe1880edbcab864b890
Execution exit: 0; timeout: False; elapsed: 22.811 seconds.

## Output (local paths and personal name redacted)

Recommend strengthening the **approval check for state coverage**. The skill already requires empty states; the repeated omissions suggest that requirement needs an explicit completeness check.

Proposed wording for a reviewed, versioned update:

> Before marking a handoff `approved`, review each scoped workflow against the applicable state types. Record each state as specified or not applicable, with a brief rationale. For applicable states, define the trigger, displayed content, available actions, and recovery or next step, and link behavioral acceptance criteria. An omitted applicable state leaves the handoff incomplete.

For empty states, explicitly distinguish first use, no matching results, and missing data where relevant. They can require different explanations and actions. Permission failures and loading should retain their own behavior.

Validate the improvement through the skill’s evidence-driven learning protocol: propose a reproducible case for the canonical AI Project Steward learning records, using role `design`. Compare baseline and candidate instructions on identical handoff scenarios, including the two reported failures if their artifacts become available. Check whether applicable empty states are specified before approval, while preserving responsive behavior, accessibility, and existing approval gates.

The evidence currently supports a **reported recurring omission**, not a verified root cause or proven fix: the two handoffs and their approval records were not supplied. This recommendation is a candidate improvement for review; no files or live skills were changed.
