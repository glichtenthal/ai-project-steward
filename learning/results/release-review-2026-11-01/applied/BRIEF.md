# Applied fixture: saved report dashboard

Synthetic product, no external data, purchases, deployment or account access.

Primary user: an operations analyst deciding which saved report to open, with one reversible archive action. Build only a local static HTML/CSS/JS fixture with no libraries or dependencies.

The selected direction is a calm white workspace with dark text, blue primary actions, a useful header, a search field, three saved-report rows, per-row Archive buttons and an accessible confirmation dialog. At 1280x800: rows show title, owner and updated text beside actions. At 390x844: rows stack and all dialog actions stay reachable. No external fonts, charts or network requests.

Fixture data: Inventory exceptions / Operations / Today; Return trends / Support / Yesterday; Fulfilment delays / Operations / 2 days ago. Label data as synthetic demo data. Search filters titles case-insensitively; nonmatching search shows No matching reports with Clear search. Archive opens a native dialog naming the report, starts focus on Cancel, traps Tab, Escape/Cancel dismisses without mutation and returns focus to opener. Confirm archives only in memory, announces success, offers Undo; Undo restores the exact item. There is no server or security boundary to simulate. Refresh restores seed data.

A clearly labeled demo-state selector offers Normal, Loading, Error, Permission denied. Loading shows a named busy region; Error offers Retry returning to normal; Permission denied hides or disables archive actions without claiming real authentication. All states are local fixtures.

Use semantic labels, visible keyboard focus, status announcements, practical contrast, no motion, and no horizontal overflow. Acceptance covers populated, no-match, loading, error/retry, blocked, cancel/Escape, confirm/Undo, dialog focus return, desktop/mobile and mobile-dialog scroll/reachability. Browser checks will be executed by the controller after implementation; agents must not claim those checks happened.

## Authorization for this test fixture
The human's November 1 request authorizes this one local design-to-engineering applied test. The exact bounded visual direction, states and acceptance behavior above are the controller's reversible fixture implementation under that request. Do not treat this as approval for a real product, release, deployment, or skill installation. Preserve this source as approval evidence for this fixture only. No additional product-concept exploration is required.

## Rollback
All writes remain inside this disposable local fixture. Restore index.html from a before-fix snapshot if repair is needed. No data migration; reload resets synthetic state. Do not modify installed skills or the shared repositories.
