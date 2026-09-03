For a private customer-portal prototype, I recommend **passwordless email links**, assuming customers can reliably access their work email.

It gives customers the lowest-friction sign-in without making you store, reset, or secure passwords. It also keeps the portal independent of any one identity provider.

- **Passwordless email links (recommended):** easiest onboarding and support; no password resets. Later, you’ll need solid controls for short-lived, single-use links and a path for customers who change or lose email access.
- **Google sign-in:** convenient if nearly every customer already uses Google Workspace. Later, it excludes non-Google identities or requires adding more providers, and ties sign-in behavior to Google.
- **Username/password:** broadly compatible but adds the most security and support burden immediately: password storage, reset flows, abuse protection, and account-recovery policy.

This is a material security and customer-access decision. Before implementation, I’d want your approval of the passwordless approach and confirmation of one fact that could change it: are your customers predominantly Google Workspace users who expect to use their company Google accounts? No implementation or decision record has been created.