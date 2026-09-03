For a private customer-portal prototype, I recommend **passwordless email links**.

Assumption: each customer already has a reliable, unique email address. If every intended customer is known to use Google Workspace, Google sign-in could become the better fit.

| Option | Best when | Easier now | Harder later |
|---|---|---|---|
| Passwordless email links — recommended | Known customers, low-friction access | No passwords or reset flow; works without requiring Google | Email delivery, short-lived secure links, and account-linking rules need care |
| Google sign-in | Nearly all customers use Google | Fast familiar sign-in; provider handles identity proof | Excludes non-Google users; creates provider dependency and later account-merging concerns |
| Username/password | You need independent credentials or offline-style access | Works for anyone with no identity provider | Password hashing, resets, breach protection, MFA, and greater support/security responsibility |

Passwordless is the smallest, most inclusive prototype path: customers prove control of the email address you already associate with them, without introducing a password-management system. It also preserves the option to add Google sign-in later and link it to the same customer account.

★ Insight ─────────────────────────────────────  
Authentication method and customer identity are separate choices. Keep a stable internal customer ID, with sign-in methods attached to it; that makes adding Google later much less disruptive.  
The main future cost of magic links is reliable email delivery—not the login screen itself.  
─────────────────────────────────────────────────

This is a material security and portability decision, so I’m treating it as **proposed**, not accepted. If you approve it, I can record the decision in `decisions.md`; I will not implement authentication unless you explicitly ask.