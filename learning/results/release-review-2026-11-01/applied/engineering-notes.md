<!-- Public artifact links adjusted to role-specific source snapshots; private agent original retained. -->
# Engineering evidence — saved reports local fixture

Date: 2026-11-01. Mode: `implementation`. Risk: **medium**, because this implements responsive layout, multiple presentation states and a confirmation/recovery flow. Mutations affect only synthetic in-memory membership; there is no authentication or external system.

Release status: **Ready for review**, specifically controller browser review of this local fixture. Browser acceptance and rendered design review are pending. This is neither real-product approval nor production/release/deployment approval.

## Scope and revision

- Implemented file: [index.html](index.html), with inline CSS/JS and system fonts. No dependencies, external resources, persistence, timers, analytics, network API or deployment.
- Reviewed implementation SHA-256: `dd64dd7ba1bdea64aadc1897b5d544cf1884d3b93da39f5a005a5b768c1a9de7`.
- Governing sources read in full: [SKILL.md](frontend-SKILL.md), [release readiness](references/release-readiness.md), [BRIEF.md](BRIEF.md), [experience-spec.md](experience-spec.md). AI Project Steward guidance was also applied.
- Contract frontmatter has supported version `1.0`, approved local-fixture status, stable direction, nonempty states/routes/viewports, selection/approval evidence resolving to the brief and an existing acceptance-criteria section. Authorization is exclusively [the bounded synthetic test](BRIEF.md#authorization-for-this-test-fixture).
- Source spec, brief, skill and release reference were not edited; their SHA-256 values matched before/after implementation. Spec status and implementation/verification references remain untouched. These notes supply implementation evidence separately, without advancing the contract to verified.
- No new material decision, service or data policy was introduced; no `decisions.md` was needed.

Target flow: initial three reports → optional title search → named Archive modal → Cancel/Escape or confirm → persistent per-report feedback → Undo restores exact identity and original seed position.

## Run and recover

Open `index.html` directly in a browser; no setup, install, build or configuration is required. The controller can also expose this same file at `/` with its existing local preview mechanism. The page itself makes no requests. Nothing was served, installed or deployed by this implementation task.

Search is title-only, trimmed and case-insensitive. The demo selector explicitly simulates Normal, Loading, Error and Permission denied; it preserves query and archives. Retry returns to Normal. Loading/Error hide Undo buttons while retaining the visible archive records; blocked mode keeps records readable and disables Archive/Undo. Undo entries have no expiry.

All state is created afresh on load. Reload restores Normal, an empty query, all three seed records and no archive feedback. No migration or stored data exists. Both deliverable files were absent before this task; local rollback is removing these two new files. Capture a before-fix copy before later repairs, as directed by the brief.

## Checks actually executed

Execution used existing Node **v24.15.0**, built-in `node:fs`, `node:vm`, `node:assert/strict`, and system `shasum`. No packages were installed. All checks below exited **0**.

| Check | Evidence/result | Limit |
| --- | --- | --- |
| Inline script parse | Extracted inline script compiled with `new vm.Script(source)` | JavaScript syntax only |
| Static document assertions | Unique static IDs; all `for`, `aria-controls`, `aria-labelledby`, `aria-describedby` targets resolve; one main, H1 and dialog; four exact selector labels; no positive tabindex | Not an HTML conformance validator or accessibility pass |
| Isolation/source scan | No external resource declarations, URL imports/fonts, network APIs, storage/cookies, console logging, transition/animation declarations or smooth scrolling found | Static review, not browser network capture |
| CSS source checks | Balanced delimiters; responsive breakpoints, 1040px workspace, 44px targets and dynamic viewport constraint present | No CSS parser, layout measurement or rendering performed |
| State-logic execution | `node /tmp/saved-report-fixture-check.cjs` passed the scenarios below using a minimal DOM test double | Does not implement native modal, browser focus, scrolling, keyboard default actions or assistive technology |
| Contrast arithmetic | WCAG relative-luminance calculations for configured opaque source colors, below | Actual rendered combinations remain unmeasured |
| Integrity | `shasum -a 256 index.html SKILL.md BRIEF.md experience-spec.md references/release-readiness.md` | File revision evidence only |

The temporary test harness is at `/tmp/saved-report-fixture-check.cjs` (SHA-256 `e42544dca126dc671796d9169650adebbdd3a9bee20b5f5f278e8bffb7fbea0a`); it is not an application dependency or project deliverable and may disappear with temporary-directory cleanup. Run it from this fixture directory while available.

Executed logic scenarios: exact initial seed text/order; `  INVENTORY  ` matching one title; ` operations ` matching no titles; Clear search; all three dialog identities; initial Cancel focus call; cancellation through Cancel, Escape handler and native-cancel event handler; both explicit Tab-wrap handler branches; confirmation removing only captured identity; success announcement; independent persistent archive records; Loading/Error hiding Undo controls; Retry restoring current query and archive membership; blocked actions and mutation guards; selector focus preservation in the test double; restoring a filtered-out item without clearing query; archiving all three; empty state; multiple Undo operations restoring original order; duplicate restoration guard; fresh script execution resetting state.

Configured color calculations (ratios rounded): dark text/white **16.27:1**; secondary text and control border/white **7.58:1**; white/primary blue **6.70:1**; white/hover blue **8.72:1**; secondary/disabled background **6.92:1**; blue focus/white **6.70:1** and blue focus/light background **6.12:1**; secondary/pressed neutral background **6.15:1**. These are source-color calculations, not rendered contrast or accessibility passes. Neutral dividers are decorative; controls use the darker secondary border.

## Controller browser obligations — all pending

No browser was launched or rendered in this task, by the brief's division of work. No browser/version, console review, screenshots, real keyboard checks, screen-reader checks, accessibility pass, zoom pass, viewport pass or independent design-review result is claimed. These are delegated checks, not checks proved unavailable by tooling.

Record implementation hash, browser/version, route/state/viewport, actual observation, screenshot paths and mismatch disposition. Execute `/` at **1280×800**, **768×1024**, **390×844**, **320×800**; also test direct file opening. Screenshot inspection alone is insufficient for interaction/accessibility checks.

| Acceptance | Required controller verification |
| --- | --- |
| AC-01–02 | Exact initial content/order and first-desktop-viewport fit; no fabricated links or network requests; uppercase/trimmed title search; owners/dates excluded; no-match Clear search; no focus movement while typing; count announcements and native search Enter/clear behavior |
| AC-03–05 | Loading named busy region with no row actions; Error and Retry announcing simulated states/recovery; search/selector usable; state/query/archive retention; visible blocked explanation and disabled Archive/Undo; Undo hidden only in Loading/Error |
| AC-06 | Open each native dialog; exact name/description; Cancel initially focused; real Tab and Shift+Tab wrapping; background focus, interaction and scroll prevented; Escape/Cancel preserve data and return to exact opener; backdrop click leaves dialog open |
| AC-07–08 | Confirm targets only captured item, closes dialog and focuses search; persistent named Undo for every archive; original-order restoration without duplicates; focus restored to visible Archive or search if filtered out; all-archived/no-match behavior; reload reset |
| AC-09 | Responsive toolbar/row/metadata/feedback layout at all four sizes; no overflow/clipping; every mobile report dialog's two actions reachable by keyboard and scrolling; repeat at short height, enlarged text and reduced visual viewport/virtual keyboard |
| AC-10 | Accessibility tree: landmarks, heading levels, visible label association, accessible button names, disabled state, DOM/tab order and inert background; non-visual screen-reader announcements without duplication; unobscured focus; actual text/control/focus contrast; 200% text zoom and 400% browser zoom/reflow to 320 CSS px; no motion, including reduced-motion setting |
| AC-11 | Inspect populated, filtered/no-match, loading, error, blocked, dialog, success and restored rendering on desktop/mobile against the spec; capture screenshots; perform rendered design review and record whether reviewer is independent or self-review |

Browser console errors and network activity must be inspected during these flows. Pay particular attention to native dialog behavior across the controller's browser versions, scroll lock, dynamic viewport sizing, focus visibility at short heights and screen-reader live-region delivery. Static intent does not establish those results.

## Mismatch and contract-defect ledger

| Scope | Expected | Observed | Severity/disposition |
| --- | --- | --- | --- |
| Spec Evidence links | Supporting `references/experience-specification.md` and `references/visual-design.md` resolve | Both files are absent from this fixture | Nonblocking provenance defect. The actual handed-off spec contains complete contract fields, visual rules and acceptance criteria; implementation follows those. Recorded without inventing approval or editing source references. |
| `/`, all states/viewports | Rendered fidelity to spec | Not observed; source self-review only | Verification gap, not a pass. Controller must populate actual visual/interaction mismatches and fix/recheck within the bounded direction. |

No other contract defect or intentional design deviation was identified by source review. There was no rendered design assessment, independent review or real-user outcome validation.

## Inapplicable checks and remaining limits

No framework/lint/build configuration, package manifest or existing test suite is present, so no framework build/test command applies. No live integration, credentials, permissions boundary, backend, migration, remote failure, deployment, telemetry vendor, cache policy or rollback service applies to this isolated static demo. Refreshing, partial, stale, conflicting and validation states are explicitly outside the design contract. Simulated Loading/Error/Permission denied are implemented; they are not evidence of real network/security behavior.

Medium-risk browser/keyboard/console/responsive checks and every explicit AC remain required. Automated accessibility, performance instrumentation, visual regression and cross-browser suites were not run; there is no existing harness and no installation was authorized. Cross-browser native-dialog and assistive-technology differences remain unverified. Next action: controller browser verification above, with bounded repairs and evidence tied to the resulting file revision.
