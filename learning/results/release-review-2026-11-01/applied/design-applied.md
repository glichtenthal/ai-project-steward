# Supplemental learning-design unchanged candidate, applied fixture Results

- **Status:** Incomplete
- **Evidence status:** Schema 1.1 record consistency checked; execution and review are not authenticated. Coverage completion is not a passing result or promotion approval; human review remains required.
- **Evaluation date:** 2026-11-01
- **Platform:** Codex CLI 0.166.0-alpha.5.1 + controller IAB
- **Model:** gpt-6.1-sol high; controller/reviewer model not separately instrumented
- **Paired skills:** PDD 1.3.2-rc.1; Frontend 1.3.2-rc.1; engineering also read installed Steward guidance
- **Review method:** Controller AI reviewed actual artifacts and executed browser interactions; independent AI screenshot/static review. No human sign-off; no independent browser rerun.
- **Package validation:** pass

## Summary

- Supplemental learning-design: 1 passed, 0 failed, 5 not run or not applicable.

## Case Results

| Case | Dimension | Result | Evidence | Notes |
|---|---|---|---|---|
| `design-accessibility` | design | not_run | Not retained | — |
| `design-handoff-contract` | design | pass | [Retained output](applied-test.md) | Applied fixture only, with controller-assisted verification; no source change or baseline uplift inferred. |
| `design-research-provenance` | design | not_run | Not retained | — |
| `design-learning-unsupported-proof` | design | not_run | Not retained | — |
| `design-learning-repeated-omission` | design | not_run | Not retained | — |
| `design-heldout` | design | not_run | Not retained | — |

## Limitations

Single applied end-to-end fixture with controller-assisted verification, not a matched baseline/candidate comparison. Other role cases intentionally not_run in this record. Native zoom, screen-reader speech, real-device virtual keyboard and cross-browser behavior remain untested. Do not pool these scores into the October 31 run or infer global release clearance.

These supplemental learning-design results cover only the named suite and conditions, not full release clearance. They do not establish enforcement, human approval, or universal behavior.
