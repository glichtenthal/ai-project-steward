# Bounded applied design-to-engineering test

## Scope and result

One synthetic saved-reports dashboard was designed by the unchanged candidate Design Director and implemented by the unchanged candidate Frontend Engineer, then exercised in the actual in-app browser by the controller. Both CLI tasks completed using gpt-6.1-sol/high and Codex CLI 0.166.0-alpha.5.1. Source digests and usage are in executions.json. The fixture authorization is synthetic setup under the human's November 1 test request, not approval for a real product or release.

This exercises the existing `design-handoff-contract` and `frontend-rendered-verification` assertions. No behavioral suite case, rubric or runtime skill instruction was added. Original October 31 not_run scores and the rollback regression remain unchanged. This is capability evidence for this applied pipeline, not matched baseline/candidate uplift or proof of unattended browser verification by the CLI agents.

## Evidence

- Actual [design handoff](experience-spec.md) has versioned frontmatter, fixture-only approval provenance, explicit states/viewports, keyboard/recovery rules and acceptance criteria. The controller did not advance its status or manufacture real-product approval.
- Actual [agent-original implementation](index.agent-original.html), [controller-tested implementation](index.html), [engineering notes](engineering-notes.md), [source snapshots](design-SKILL.md), [execution provenance](executions.json) and [browser observations](browser-checks.json) are retained.
- Actual screenshots: [desktop](desktop.jpg), [mobile](mobile.jpg), [mobile dialog](mobile-dialog.jpg), [tablet](tablet.jpg), [narrow](narrow.jpg), [loading](mobile-loading.jpg), [error](mobile-error.jpg), [permission denied](mobile-permission-denied.jpg), [no match](mobile-no-match.jpg), [all archived](mobile-all-archived.jpg).

## Checks performed

- 1280×800 desktop, 390×844 mobile, 768×1024 tablet, 320×800 narrow layout, and a 390×320 short dialog viewport. Numeric page widths matched scroll widths; screenshots inspected. Mobile lists intentionally scroll vertically.
- Case-insensitive title filtering, owner-only no-match, Clear recovery and focus, loading/busy semantics, error/Retry, and explicitly simulated disabled archive actions.
- Native modal name and Cancel initial focus; Tab/Shift+Tab wrapping; Escape and Cancel preserve data and return focus to the correct opener.
- Confirm removes only the selected report, displays persistent named Undo and success status; Undo restores identity/order. Repeated archives, all-archived recovery, Undo while a no-match filter remains active, and reload reset were exercised.
- No warning/error entries appeared in the browser dev log. No external script/style resource declarations were present. These checks are not a complete network-security audit.
- Engineering separately ran syntax/static assertions, DOM-test-double logic scenarios and source-color calculations, with no dependency installation. Those checks alone were not counted as browser evidence.

## Repairs and review

The controller preserved the original HTML and made one mobile-only heading change (24px to 20px) to remove an awkward final-word wrap, then reloaded and rechecked affected mobile views. No JavaScript or state behavior changed. The controller also restored the two missing immutable design reference files for handoff provenance; original engineering notes retain the observed gap. Public artifact links were adjusted to role-specific skill snapshots, while private originals remain retained.

An independent AI reviewer inspected the handoff, source and actual desktop/mobile/dialog screenshots and found no material mismatch against the bounded brief. It did not independently execute browser interactions. This is AI artifact review and controller-assisted execution, not human approval.

## Limits and disposition

Screen-reader speech/live-region delivery, native 200% text and 400% browser zoom, physical virtual-keyboard behavior, backdrop/background-inert interaction, and exhaustive cross-browser/device coverage were not run. Static contrast calculations do not establish a full measured accessibility pass. Extra stress requirements generated in the fixture specification were not adopted as new permanent suite gates.

The actual handoff, responsive rendering and core interaction/recovery checks now have applied evidence. Their six existing assertions are recorded in the shared schema 1.1 reports for this fixture; other cases remain not_run. This does not erase the Frontend rollback regression or establish full release clearance. Keep all source/release/install decisions separate.

To reproduce: open index.html directly, or serve this directory on loopback using an approved local runtime. Follow BRIEF.md and browser-checks.json at the recorded viewports. No libraries, build, external accounts, persistent data or service are required. Reload is the fixture reset; index.agent-original.html is the before-repair snapshot. Raw event streams remain private under the earlier retention policy.
