# Confirmation: design-repeated-confirmation / candidate

Actual synthetic-fixture agent execution. Model gpt-6.1-sol high; Codex CLI 0.166.0-alpha.5.1. Sandbox: read-only. Exit: 0; timeout: False; elapsed: 20.579 seconds.

Instruction SHA-256: 4039da168236b1ca58221a9ea028fbc2cb859ac95b8e9825270ba7febf692e0a
Prompt SHA-256: da7c89550c0e8888e2d65e8a9b48a5aff6e573adeca3bfe1880edbcab864b890

## Output

Recommend adding an explicit state-completeness check to the existing handoff approval gate. The skill already requires empty states; the improvement should make omissions detectable before approval.

**Mode: audit.** I reviewed `SKILL.md` and your report of two omissions. The handoffs themselves were not supplied, so the cause remains unverified.

Proposed wording for a reviewed, versioned update:

> Before marking a handoff `approved`, check each in-scope workflow against the applicable state list. In the existing experience specification, mark each state as specified, not applicable with a reason, or unresolved. For empty states, define the trigger, visible content, available actions, and recovery or next step. Applicable unresolved states leave the handoff incomplete.

Keep this lightweight: use the existing specification and approval step, without adding another document or confirmation round. Check different reasons for emptiness where relevant—first use, no filter matches, or cleared data—because they may require different next actions.

Validate the proposal through the skill’s prescribed learning process: contribute a reproducible case under role `design`, then compare baseline and candidate on identical scenarios. Include both reported failures, a workflow where an empty state is legitimately inapplicable, and a fully specified approved handoff.

Success means applicable empty-state behavior is explicit, exclusions are justified, and complete handoffs retain their existing approval without redundant confirmation. Also check responsive behavior and accessibility.

This is a proposed improvement; no files were changed, comparisons run, or rendered behavior verified.
