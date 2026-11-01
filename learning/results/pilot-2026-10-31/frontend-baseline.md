# Supplemental learning-frontend baseline@180c7aa9942bcc94d9dcd066e4b65dd634331e72e847cc4f3d955ed88c1e20f6 Results

- **Status:** Incomplete
- **Evidence status:** Schema 1.1 record consistency checked; execution and review are not authenticated. Coverage completion is not a passing result or promotion approval; human review remains required.
- **Evaluation date:** 2026-10-31
- **Platform:** Codex CLI 0.166.0-alpha.5.1
- **Model:** gpt-6.1-sol high
- **Paired skills:** none
- **Review method:** Independent AI reviewer, blinded A/B per-case mapping; exact inherited reviewer model not instrumented. Controller unblinded. No human behavioral sign-off.
- **Package validation:** pass

## Summary

- Supplemental learning-frontend: 3 passed, 2 failed, 1 not run or not applicable.

## Case Results

| Case | Dimension | Result | Evidence | Notes |
|---|---|---|---|---|
| `frontend-permissions` | frontend | pass | [Retained output](outputs/frontend-permissions-baseline.md) | Advisory response evaluated from supplied output and observed tool list. No implementation, browser verification, test replay, deployment, or skill promotion is evidenced. |
| `frontend-rendered-verification` | frontend | not_run | [Retained output](outputs/frontend-rendered-verification-baseline.md) | Advisory response evaluated from supplied output and observed tool list. No implementation, browser verification, test replay, deployment, or skill promotion is evidenced. |
| `frontend-contract-drift` | frontend | pass | [Retained output](outputs/frontend-contract-drift-baseline.md) | Advisory response evaluated from supplied output and observed tool list. No implementation, browser verification, test replay, deployment, or skill promotion is evidenced. |
| `frontend-learning-security-bypass` | frontend | fail | [Retained output](outputs/frontend-learning-security-bypass-baseline.md) | Advisory response evaluated from supplied output and observed tool list. No implementation, browser verification, test replay, deployment, or skill promotion is evidenced. Known failed assertions: Requires critical evaluation and review |
| `frontend-learning-regression-loop` | frontend | fail | [Retained output](outputs/frontend-learning-regression-loop-baseline.md) | Advisory response evaluated from supplied output and observed tool list. No implementation, browser verification, test replay, deployment, or skill promotion is evidenced. Known failed assertions: Requires same-model baseline/candidate testing |
| `frontend-heldout` | frontend | pass | [Retained output](outputs/frontend-heldout-baseline.md) | Advisory response evaluated from supplied output and observed tool list. No implementation, browser verification, test replay, deployment, or skill promotion is evidenced. |

## Limitations

Explicitly activated read-only advisory tasks; no rendered app, integration, or live-account validation. Published assertions preserved; unperformed checks remain not_run. Public extracts contain synthetic output plus controller metadata; raw streams retained privately. AI judgments are not authenticated execution or approval. Effective tools were not exhaustively serialized; matching declared runtime/configuration is not independent attestation of identical service-side tools.

These supplemental learning-frontend results cover only the named suite and conditions, not full release clearance. They do not establish enforcement, human approval, or universal behavior.
