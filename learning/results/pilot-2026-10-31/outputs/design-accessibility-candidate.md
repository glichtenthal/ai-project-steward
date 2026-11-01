# Actual agent output: design-accessibility / candidate

Synthetic advisory fixture; public extract, not live validation.

Instruction SHA-256: 4039da168236b1ca58221a9ea028fbc2cb859ac95b8e9825270ba7febf692e0a
Prompt SHA-256: ed39be045bd8ef9ccd44dfcb8aca05aeb32b37a42968bd8e05401f932ada9170
Execution exit: 0; timeout: False; elapsed: 26.169 seconds.

## Output (local paths and personal name redacted)

Mode: **concept**. Assumption: account owners need to change preferences and manage deletion safely. No existing interface, design system, referenced templates, or rendered evidence was supplied; this is an untested design proposal.

Three directions:

- **Category pages — recommended:** Profile, Security, Notifications, and Account navigation; each page opens with current settings. Edit → Save → confirmation. Familiar and scannable, with more navigation.
- **Single settings page:** Section links above a compact form; review changes → Save all. Efficient for frequent editors, but long pages and shared save behavior increase cognitive load.
- **Task hub:** Start with “Update preferences,” “Secure account,” or “Close account”; each opens a focused sequence. Clear for occasional users, with more steps for experts.

For the recommended direction:

- Use labeled native controls, clear headings, and an explicit Save button. Show unsaved changes, saving, saved, validation errors, and permission restrictions.
- Place destructive actions in a distinct, plainly labeled Account section. Explain scope, affected data, and actual recovery options before confirmation.
- Open an accessible confirmation dialog naming the target and consequences. Label the action specifically: “Delete account.” Initially focus **Cancel**; require target-name entry only when the consequences justify added friction.
- Keep Tab and Shift+Tab inside the dialog. Escape cancels before submission. Return focus to the trigger after cancellation; after deletion, move to a meaningful destination.
- Prevent duplicate submissions; announce progress and failures. Preserve recoverable input.
- Maintain logical focus order, visible unobscured focus, sufficient contrast, and reflow on narrow screens.

Validate keyboard completion, cancellation, failure recovery, screen-reader announcements, and zoom before approval. No accessibility pass is claimed.
