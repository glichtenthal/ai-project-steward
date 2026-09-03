For a private customer-portal prototype, I recommend passwordless email links (magic links), assuming customers have reliable access to their work email and the portal is invite-only or limited to known customers.

★ Insight ─────────────────────────────────────

- Authentication is both a UX choice and a long-term security/operations choice.
- Passwordless avoids operating password reset, credential storage, and password-policy flows.
- The main trade-off shifts to email delivery reliability and secure, short-lived link handling.
─────────────────────────────────────────────────

| Option | Best fit | Easier now | Harder later |
|---|---|---|---|
| Passwordless email links — recommended | Known customers accessing a private portal occasionally | Fastest low-friction onboarding; no passwords to store/reset; works regardless of Google account | Requires reliable transactional email, expiration/replay protections, and a path for customers who change email addresses |
| Google sign-in | Customers overwhelmingly use managed Google Workspace accounts | Familiar sign-in and less email-delivery dependence | Excludes non-Google customers or forces a second method; adds Google identity-provider dependency and account-linking edge cases |
| Username/password | A product that needs accounts independent of email providers | Maximum identity-provider independence and supports non-email recovery designs | You own secure password storage, resets, rate limiting, MFA decisions, breach response, and support burden from day one |

What passwordless makes easier later:
- Adding Google sign-in later as an optional convenience, while keeping email identity as the common account key.
- Keeping the prototype simple without creating a password security program.
- Supporting customers from different companies and identity systems.

What it makes harder later:
- Moving away from email as the primary identity/recovery channel if customers require stronger enterprise controls.
- Supporting shared inboxes or customers without dependable email access.
- Meeting enterprise SSO requirements; if that becomes common, SAML/OIDC SSO is the likely next authentication layer.

I would reconsider this recommendation if most customers are already on Google Workspace and explicitly want Google-only access, or if the portal will hold highly sensitive data—in which case enterprise SSO and MFA requirements should drive the choice.

No implementation or decision record was created. If you approve this direction, the next step is to record it as an accepted decision before selecting an authentication provider or building the flow.