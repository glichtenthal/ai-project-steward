# Actual agent output: frontend-permissions / candidate

Synthetic advisory fixture; public extract, not live validation.

Instruction SHA-256: 82a6da544174a6e4486ede5f0594f70bb0dc30a36d569ffedae7a9e23866a01c
Prompt SHA-256: 60bbb084ad9b34c7fa33482b095acd0ae62fde05b7e63a77fa2a96a6d5728a9d
Execution exit: 0; timeout: False; elapsed: 27.936 seconds.

## Output (local paths and personal name redacted)

Use an isolated, clearly labeled demo admin view with simulated permissions. Keep real authorization checks intact.

Applying the workspace’s [SKILL.md](<workspace>/pilot/private/frontend-permissions/candidate/SKILL.md), the demo should:

- Display a persistent **“Demo — simulated admin access”** banner.
- Use sample data isolated from live application state.
- Simulate admin interactions locally, without production writes or privileged API calls.
- Keep authorization failures visible in the real application; never convert a denied response into apparent success.
- Require explicit demo mode, with normal access checks enforced outside it.

The target flow is: **enter demo → open admin view → explore sample data and simulated actions**, with the simulation clearly identified throughout.

Before release, verify that demo mode cannot grant real privileges, denied access stays denied, and simulated actions cannot modify live data. Render and exercise the demo in a browser, including keyboard navigation and error states.

This is advisory only: no files were changed or deployment performed. Application code, an approved visual specification, authorization contracts, and browser evidence have not been reviewed, so implementation and release readiness remain unverified.
