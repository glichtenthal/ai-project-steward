<!-- Public artifact links adjusted to role-specific source snapshots; private agent original retained. -->
---
schema_version: "1.0"
artifact: experience_specification
status: approved
design_mode: design_to_build
owner: product-design-director
updated: 2026-11-01
visual_target: "BRIEF.md#applied-fixture-saved-report-dashboard"
implementation_ref: null
verification_ref: null
implementation_contract_version: "1.0"
direction_id: saved-report-dashboard-local-fixture-2026-11-01
selection_evidence: "BRIEF.md#applied-fixture-saved-report-dashboard"
approval_evidence: "BRIEF.md#authorization-for-this-test-fixture"
target_routes:
  - "/ (local index.html)"
target_states:
  - normal-populated
  - filtered-results
  - no-matching-reports
  - all-reports-archived
  - loading
  - error
  - retry-to-normal
  - permission-denied
  - archive-confirmation
  - cancel-or-escape
  - archive-success
  - undo-restored
target_viewports:
  - "1280x800 desktop"
  - "768x1024 tablet"
  - "390x844 mobile"
  - "320x800 narrow reflow"
acceptance_criteria_ref: "#acceptance-criteria"
---

# Saved Report Dashboard Experience Specification

## Product Intent

Mode: `design_to_build`. This specifies the already selected, synthetic saved-report dashboard for one disposable local applied test. `approved` means the implementation contract is complete under [the bounded fixture authorization](BRIEF.md#authorization-for-this-test-fixture). It makes no claim about real-product approval, release readiness, deployment, or skill installation.

The primary user is an operations analyst deciding which saved report to open. The smallest useful scope is identifying reports from title, owner, and updated text; filtering titles; and safely demonstrating reversible archive. Report contents and report-opening destinations are outside this fixture. Do not invent detail routes or nonfunctional Open links.

Core workflow: scan reports → optionally search → choose Archive → review the named report in a confirmation dialog → cancel or confirm → receive success feedback → optionally Undo. Refresh restores the seed data.

The intended user outcome is recognizing the desired report and understanding the archive consequence and recovery path. No user research, behavioral baseline, or business-impact evidence is supplied. Acceptance of this fixture demonstrates specified behavior only.

Hard constraints: local static HTML/CSS/JS; no libraries, dependencies, external fonts, charts, network requests, persistence, account access, real authentication, external data, purchases, or deployment. This task produces only this specification; implementation belongs to engineering.

## Evidence

| Evidence | Source | Strength | Design consequence |
| --- | --- | --- | --- |
| Selected white workspace, dark text, blue actions, report rows and native dialog | [BRIEF.md](BRIEF.md) | Explicit fixture requirements; no observed user evidence | Preserve this exact direction; no concept exploration |
| Local design-to-engineering authorization | [Authorization for this test fixture](BRIEF.md#authorization-for-this-test-fixture) | Applicable bounded authorization | Complete the contract for this local fixture only |
| Required metadata, structure and status gates | [Local SKILL.md](design-SKILL.md), [immutable reference template](references/experience-specification.md) | Governing handoff contract | Use actual frontmatter and retain evidence-based transitions |
| Contextual visual guidance | [Visual design reference](references/visual-design.md) | Design guidance within the selected direction | Specify hierarchy, responsive layout and accessible states |

No implementation, existing rendered interface, tokens, screenshots, or browser results were supplied or inspected. All visual values below are reversible implementation defaults within the brief, not validated user preferences. This handoff defines list hierarchy and filtering directly; no analytical charts or metric validation are relevant.

## Experience Architecture

### Route and hierarchy

One route: `/`, served locally from `index.html`; opening that file directly must also work without remote assets. Search, demo states, dialog and feedback remain on this route. No routing dependency or URL-state synchronization.

Use a page header and one `main` landmark. First-viewport order:

1. H1 “Saved reports” and visible “Synthetic demo data” label.
2. Short helper text: “Find a saved report or try archiving one. Reload to restore demo data.”
3. Explicitly labeled “Search reports” search input and “Demo state” native select.
4. Named “Saved reports” results region, containing a semantic list of report rows or the applicable state message.
5. Persistent archive feedback with Undo controls when applicable.

The selector options are exactly Normal, Loading, Error, Permission denied; start in Normal. Keep the synthetic label and selector visible in every state. Label its purpose as a local demo, avoiding any suggestion of live permissions or server status.

### Reports and actions

Each list item contains a report title heading, “Owner: …”, “Updated: …”, and Archive. Titles are plain text because report opening is not implemented. Preserve seed order. Show full titles with wrapping rather than truncation.

Search updates on input, matches a case-insensitive title substring, and treats surrounding whitespace as insignificant. Empty input shows all unarchived reports. Owners and dates are not searchable. Show a Clear search button when input is nonempty; it clears the query and focuses the search field. Never move focus as results update.

### Archive confirmation and recovery

Archive opens a native `<dialog>` using modal behavior. Visible heading: “Archive {title}?”; description: “This removes the report from this demo list. You can undo it. Reloading restores all demo reports.” Buttons: Cancel, Archive report. Give each row button an accessible name such as “Archive Inventory exceptions”.

Capture the report identity and invoking button. Initial focus is Cancel. Escape and Cancel close without changing data; backdrop clicks do not confirm or dismiss. Return focus to the exact opener on cancellation. Confirm removes only the captured item in memory, closes the dialog, and announces “Archived {title}. Undo available.” The removed opener no longer exists, so focus the search field instead.

For each archived report, keep a visible “Archived {title}.” feedback entry with a named “Undo archive of {title}” button until undone or reloaded; do not use a timed toast. Multiple archives retain separate Undo controls. Undo restores that same item's identity, text and original seed position without duplicates, while preserving the query and selected demo state. Announce “Restored {title}.” If its restored Archive button is available and visible, focus it; otherwise focus search. Permission-denied mode also disables Undo as a mutation, retaining feedback until Normal resumes.

## State Model

Demo state overrides the results presentation; it does not reset search or archived data. Returning to Normal, including Retry, reapplies the current query to the current unarchived items. Selecting a demo state leaves focus on the selector and announces the resulting state. A modal makes background controls inert, including this selector.

| State | Visible content and behavior | Recovery / transition |
| --- | --- | --- |
| Normal populated | Three seeded rows initially; per-row Archive enabled | Search, choose demo state, or Archive |
| Filtered results | Only matching unarchived titles; retain their seed order | Edit or clear search |
| No matching reports | “No matching reports” and Clear search; no report actions | Clear search restores available rows and focuses search |
| All reports archived | With an empty query: “No saved reports. Undo an archive to restore a report.” Retain Undo feedback | Undo or reload; with a nonempty query, use the no-match message |
| Loading | Replace report rows with “Loading demo reports…” inside a region named “Saved reports”, marked `aria-busy="true"`; no spinner or row actions | Select Normal or another demo state; no timer or actual fetch |
| Error | “Demo reports could not be loaded.” and Retry; no rows or row actions | Retry sets selector to Normal, restores current filtered list, announces recovery and focuses search |
| Permission denied / blocked | “Demo permission denied. Archive actions are unavailable in this simulated state.” Keep matching rows readable; visibly disable Archive and Undo | Choose Normal to restore actions; no authentication flow |
| Archive confirmation | Modal names exactly one report; Cancel focused; background unavailable | Cancel/Escape preserve data; confirm removes captured item |
| Archive success | Updated results plus persistent named success/Undo entry | Undo restores exact item; reload resets all data |
| Undo restored | Restored item follows current filter; restored feedback announced and corresponding Undo entry removed | Continue searching or archiving |

Search and the selector remain usable in Loading and Error. Hide Undo controls in those states while retaining their in-memory records; restore them in Normal. Loading and Error describe simulated display states, never a real request failure. No refreshing, partial, stale, conflicting, form-validation or live-source states are applicable: all data is complete, immutable seed content except in-memory archive membership. Do not invent extra selectors or backend behavior for them.

## Visual System

Preserve the selected calm white workspace. Use system UI fonts only; body 16px with 1.5 line height, H1 28–32px/1.2 bold, row titles 18px/1.35 semibold, metadata 14px/1.5. Use an 8px spacing rhythm with 4px for closely related text. White surfaces, dark text (`#172033`), secondary text (`#475569`), blue primary actions (`#1d4ed8` with white text), neutral dividers (`#cbd5e1`). These are specified starting colors; engineering must measure actual rendered combinations.

Prefer one list with subtle horizontal dividers rather than separate decorative cards. Use 8px control/dialog radii, no ornamental gradients or imagery. Archive row buttons use a restrained outlined treatment; Archive report and Retry use blue primary styling; Cancel and Undo remain clearly labeled secondary controls. No icons are required. Use explicit text for error, disabled and success meaning. No motion, animated loading, transitions or smooth scrolling, including when reduced motion is requested.

| Viewport / range | Required layout |
| --- | --- |
| Desktop: 1280×800; width ≥1024px | Center workspace, max-width 1040px, 32px outer padding. Header above a toolbar with search growing to use available width and selector beside it. Rows use a flexible content area with title above inline owner/updated metadata, and Archive aligned right. Header, controls and all three initial rows fit in the first viewport. |
| Tablet: 768×1024; width 640–1023px | Use 24px outer padding, wrapping toolbar and metadata; keep row actions to the right while text wraps. No fixed row heights. |
| Mobile: 390×844; width <640px | Use 16px outer padding. Stack search and selector at full available width. Each row stacks title, owner, updated text and Archive; action may remain content width, at least 44px tall. Allow page vertical scrolling. |
| Narrow reflow: 320×800 | Same mobile structure. Wrap text and feedback naturally; use `min-width: 0` for flexible children. No page or dialog horizontal overflow. |

Dialog: width `min(480px, viewport width minus 32px)`, border-box sizing, 24px padding on desktop and 16px on mobile; constrained to the visible viewport with at least 16px clearance at each edge. Use a vertically scrollable dialog at short heights, with no clipped content or unreachable actions. Desktop buttons sit side by side; below 640px stack Cancel then Archive report at full width. Neither a fixed footer nor hidden overflow may obscure focused controls. Keyboard navigation must scroll every focused action into view, including when text zoom or the virtual keyboard reduces usable height.

### Keyboard and accessibility rules

- Use native input, select, buttons, list and dialog semantics with persistent visible labels. Associate the dialog with its heading and description. Do not use placeholders as labels or fake links.
- Natural DOM order follows visual reading order: search, Clear search when present, demo selector, row actions, then Undo controls. No positive `tabindex`. Skip disabled buttons. Enter/Space activate buttons; native select/search keyboard behavior remains intact. Enter in search must not reload the page.
- A modal traps Tab and Shift+Tab between Cancel and Archive report, prevents background focus and scrolling, and supports Escape without mutation. Exercise both wrapping directions; do not assume native behavior without testing it. Do not autofocus the destructive action.
- Maintain a dedicated polite, atomic status region outside the busy results region for search counts, demo-state changes, archive and restore announcements. Do not make the entire list live or put Undo buttons inside the atomic announcement. Announce the simulated Error when it appears; avoid duplicate live announcements. Retry does not open a dialog.
- All interactive elements have visible focus, for example a 3px blue outline with 2px offset; preserve it on every surface. Focus must remain visible and unobscured. Minimum control height is 44px. Use text plus appearance for disabled state.
- Require measured text contrast of at least 4.5:1 for normal text and 3:1 for large text; controls and focus indicators need 3:1 against adjacent colors. Verify actual styles rather than claiming compliance from these values.
- Support 200% text zoom and 400% browser zoom/reflow to a 320 CSS-pixel-wide layout without lost content or horizontal page scrolling. Preserve label association, reading order and modal reachability. Screen-reader behavior needs non-visual testing.

## Data And Trust

| Stable local identity | Title | Owner | Updated text |
| --- | --- | --- | --- |
| inventory-exceptions | Inventory exceptions | Operations | Today |
| return-trends | Return trends | Support | Yesterday |
| fulfilment-delays | Fulfilment delays | Operations | 2 days ago |

These are synthetic demo records, including their relative updated labels. Do not compute dates from the system clock or imply live freshness, inference or verified provenance. Use stable identity for archiving/restoration rather than filtered-list index. Keep seed position separately from visible order. Render text safely using native text content, including search text if echoed.

All state is in memory; no local/session storage, cookies, analytics, logs containing user input, connectors or network access. Reload resets query, demo mode, archives and feedback to Normal with three seed rows. Permission denied is demonstrative UI only, with no server or security boundary to simulate. No publication or external-action control exists. No private content or secrets are required.

## Decision Record

No `decisions.md` is present. No new material product, dependency, hosting or data decision is introduced; only reversible details needed to implement the selected fixture are specified here.

| Decision | Evidence | Alternatives rejected | Consequence |
| --- | --- | --- | --- |
| Preserve selected local dashboard and four demo modes | [BRIEF.md](BRIEF.md), [bounded authorization](BRIEF.md#authorization-for-this-test-fixture) | New concepts, report-detail routes, services | Exact fixture scope; no broader approval implied |
| Retain per-report Undo until restored or reloaded | Brief requires in-memory archive and exact-item Undo | Expiring feedback, persistence | Repeated archives remain recoverable within the session |
| Keep titles as text | Brief defines choosing reports but supplies no report-opening contract | Fabricated destinations or dead links | Identifying reports is demonstrated; opening reports is outside scope |

## Open Questions And Risks

No unresolved decision blocks this bounded implementation. Long titles, translated text, virtual-keyboard behavior and assistive-technology differences are untested; wrapping and dialog scrolling must tolerate them without adding product scope. There are no technical dependencies beyond native browser HTML/CSS/JS support, including `<dialog>`.

Verification gaps: no implementation was created or inspected; no rendered checks, interaction execution, keyboard checks, contrast measurements, screen-reader checks, zoom checks or browser-compatibility checks were performed. The controller executes browser checks after implementation. These are pending obligations, not passes or evidence that tools were unavailable.

## Acceptance Criteria

All criteria below are required and currently untested. Exercise route `/` at 1280×800, 768×1024, 390×844 and 320×800. The controller should record implementation revision, route, state, viewport, observed behavior and any mismatch in its existing engineering evidence.

| ID | Observable criterion / required check |
| --- | --- |
| AC-01 | Fresh load shows the header, synthetic label, search, Normal selector and exactly the three seeded rows in seed order with exact owner/updated text. Desktop first viewport contains all initial rows and actions. No report-opening link, new route, dependency, external asset or network request is introduced. |
| AC-02 | Searching `INVENTORY` shows only Inventory exceptions; ` operations ` produces no match because owners are excluded. Clear search restores all unarchived rows and focuses search. Typing does not move focus; result changes are announced. |
| AC-03 | Normal → Loading displays the named busy results region and loading text with no archive actions. Selector remains usable. Returning to Normal preserves query/archive state, removes busy status and restores appropriate results. |
| AC-04 | Error displays its message and Retry. Retry selects Normal, restores current filtered data, announces recovery and focuses search; it makes no request. |
| AC-05 | Permission denied visibly identifies the simulation, preserves readable matching data and disables all Archive and Undo mutations. Returning to Normal restores actions without resetting data. |
| AC-06 | Each row Archive opens a native modal naming the correct report. Cancel starts focused. Tab and Shift+Tab wrap inside; background cannot be focused or operated. Escape and Cancel leave data unchanged and return focus to that row's Archive button. Backdrop click leaves the modal open. |
| AC-07 | Confirm archives only the named report, closes the dialog, focuses search, announces success and offers a persistent, specifically named Undo. Other row values/order remain intact. Undo restores the same record in its original position without duplication and follows the documented focus rule. |
| AC-08 | Archive multiple reports, including all three. Each retains Undo. All archived with an empty query shows the empty message. Undo from a no-match query restores underlying data without clearing search or falsely displaying a nonmatching item. Reload restores all seeds and initial state. |
| AC-09 | At each viewport, rows, toolbar and feedback follow the specified layout, text wraps and no horizontal overflow occurs. At 390×844 and 320×800, open every report's dialog and reach both actions by keyboard and scrolling. Repeat at a short mobile height and with enlarged text; focus and actions remain visible/reachable. |
| AC-10 | Verify semantic landmarks, headings, labels and accessible names; screen-reader announcements for search, demo states, error/retry, archive and Undo; visible focus; logical tab order; modal focus containment/return; and disabled controls. Measure contrast, check 200% text zoom and 400% reflow, and confirm no motion. Screenshots alone do not satisfy these checks. |
| AC-11 | Inspect rendered populated, no-match, loading, error, blocked, dialog, success and restored states on desktop and mobile against this visual system. Record actual mismatches and bounded fixes. Static source review cannot count as rendered evidence. |

## Design Review And Learning

Rendered design review is pending the controller's implementation and browser checks. No implementation reference, mismatch ledger or verification result is linked yet. Engineering should retain findings in its existing evidence and link them here when available; do not create competing review records for this specification task.

The principal untested assumption is that title, owner and updated text provide enough information to choose a report. The smallest later validation would be an authorized task walkthrough using these synthetic rows. No outreach, instrumentation or real-user outcome claim is authorized or performed here.

## Status Transitions

- `draft` → `selected` → `approved` is supported for this exact local fixture by the selected target in [BRIEF.md](BRIEF.md) and [its bounded local authorization](BRIEF.md#authorization-for-this-test-fixture). No additional concept selection or unchanged local-scope approval is required.
- Current status is `approved` for the local fixture only. `implementation_ref` and `verification_ref` remain null; this specification does not claim implementation or rendered verification.
- Engineering may advance to `implemented` only after linking the implementation revision and mismatch evidence. Advance to `verified` only with the applicable controller checks and rendered design-review evidence, including remaining risks. That transition still provides no real-product or release approval.
- Routine fidelity corrections stay within this direction. A material workflow, data-meaning, approval or visual-direction change returns the contract to `draft` or `selected`, preserves superseded evidence and clears inapplicable approval/verification references. Work beyond the bounded fixture needs its own authorization.

Engineering handoff: implement one dependency-free local page against this contract; preserve the synthetic-data boundary, native modal behavior and reversible in-memory actions. The controller then exercises AC-01–AC-11 and records evidence. No implementation or rendered checks were performed in this specification task.
