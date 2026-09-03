I recommend passwordless email links for this private customer portal prototype, assuming each customer has a reliable, individual email address.

Why this matters: authentication determines who handles credentials, how customers recover access, and how tightly the portal depends on an external identity provider.

| Option | Advantage now | Cost or constraint later |
|---|---|---|
| Passwordless email links | Simple customer experience; no passwords to store or reset; works across identity providers | Requires dependable transactional email; login depends on email-account security; adding stronger authentication later requires migration work |
| Google sign-in | Fast implementation and mature security; no email delivery system | Excludes or inconveniences customers without suitable Google accounts; creates Google dependency; adding other providers complicates account linking |
| Username/password | Familiar and provider-independent | Highest security and support burden: password storage, resets, abuse prevention, and credential-compromise handling |

The recommendation makes onboarding and account recovery easier now while avoiding Google-only access. It makes email delivery part of the login system, and later additions such as passkeys, multifactor authentication, or enterprise SSO will require careful identity linking.

Reconsider this recommendation if:

- Customers commonly use shared inboxes.
- Sign-in must work during email delivery outages.
- Most customers already use managed Google Workspace accounts.
- The portal will soon handle highly sensitive information requiring stronger authentication.

This is a proposed decision only. I did not implement anything or create `decisions.md`. If you approve passwordless email links, I’ll record the accepted decision before any implementation planning.