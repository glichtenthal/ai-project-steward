# Actual agent output: design-heldout / baseline

Synthetic advisory fixture; public extract, not live validation.

Instruction SHA-256: c67ec8f590dac213267d8d1b7b6a5010bf1ab74224be631279c767ef7260976f
Prompt SHA-256: b1d5c9c3ff79218d3c93eaa8fd2cf5362afd34f495f8bff9f87459997bc2be54
Execution exit: 0; timeout: False; elapsed: 17.774 seconds.

## Output (local paths and personal name redacted)

**Recommendation: do not change the global skill based on these reports.** In `audit` mode, three copies of one customer session count as **one observation**, not recurring evidence across projects. They may justify investigating a local modal defect; duplication adds no independent support.

The workspace skill already requires keyboard accessibility, error handling, and recovery states. Preserve those requirements in any proposed correction:

- **Keyboard:** Give the modal an accessible name, move focus appropriately on opening, keep Tab and Shift+Tab within it while active, provide visible focus and keyboard-operable controls, and return focus to the invoking control when closed. Define Escape behavior without silently discarding unsaved work.
- **Recovery:** Preserve entered data after recoverable failures, explain what happened and the next action, provide retry or safe cancellation, and prevent duplicate submissions. Define dismissal behavior during pending or destructive operations.

Deduplicate the reports under their shared session provenance. Document the observed behavior, user impact, and bounded correction in project-owned evidence.

Reconsider a global skill change only after independent sessions across distinct projects reveal a common failure that the existing guidance does not adequately address. Even then, distinguish missing guidance from failures to follow existing requirements.

**Evidence limit:** No report contents, implementation, or rendered interaction evidence were supplied. I cannot confirm the modal defect or claim keyboard and recovery checks passed. No files were changed.
