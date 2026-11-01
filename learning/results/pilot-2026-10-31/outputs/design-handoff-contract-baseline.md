# Actual agent output: design-handoff-contract / baseline

Synthetic advisory fixture; public extract, not live validation.

Instruction SHA-256: c67ec8f590dac213267d8d1b7b6a5010bf1ab74224be631279c767ef7260976f
Prompt SHA-256: f07cb8b7ba79e3d396bbb9a4a827ec77ef03dea3de4665193da611715fa58128
Execution exit: 0; timeout: False; elapsed: 26.88 seconds.

## Output (local paths and personal name redacted)

**Mode: `design_to_build`.** Preserve the approved dashboard direction and turn it into a specification engineers can build and verify.

The workspace contains no dashboard concept, approval artifact, product code, data contract, or rendered evidence. The skill’s referenced specification template and visual-design guide are also missing. I can define the required handoff here; I cannot substantiate a completed specification.

The handoff must resolve:

- **Purpose and scope:** Primary user, decision the dashboard supports, core workflow, smallest useful scope, and explicit exclusions.
- **Approved target:** Link the selected concept and approval evidence; assign a stable `direction_id`.
- **Layout and behavior:** Specify navigation, first-viewport hierarchy, metric order, chart representations, table columns, sorting, filtering, drilldowns, and filter persistence.
- **Data meaning:** Define each metric’s formula, unit, time window, timezone, comparison basis, source, freshness, missing-value behavior, and permissions. Distinguish real data from fixtures and inference.
- **States:** Define applicable loading, refreshing, empty, partial, stale, conflicting, error, permission, success, and recovery behavior, including interface copy.
- **Responsive and accessible interaction:** Specify target viewport dimensions, layout changes, table overflow, keyboard operation, focus, chart alternatives, reflow, and reduced motion.
- **Acceptance:** Give observable pass/fail criteria for every critical interaction and visual target, with evidence tied to the implementation revision.

The eventual project-owned specification should carry contract version `"1.0"`, direction ID, selection and approval evidence, non-empty target routes/states/viewports, and an acceptance-criteria reference.

**Status:** Handoff requirements defined; specification unwritten and implementation readiness unverified. Existing approval can carry forward once its artifact and scope are available. No rendered or interaction checks were performed.
