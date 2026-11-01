# Final quality and release decisions — November 1, 2026

## Recommendation

| Review unit | Recommendation | Basis |
|---|---|---|
| [Steward infrastructure extraction #5](https://github.com/glichtenthal/ai-project-steward/pull/5) | **Safe to merge after human source review**; no release/install implied | One stronger evaluator; assertion regression disclosure; observation-only triage; explicit distribution manifest; 42 deterministic tests and hosted CI. SKILL.md, UI invocation policy and release metadata are byte-identical to main fa9f0bf. Infrastructure does not need artificial model uplift. |
| [Steward #2](https://github.com/glichtenthal/ai-project-steward/pull/2) | **Keep behavioral instructions experimental**; merge infrastructure via #5 first | Original scored Steward advisory results were unchanged. Applied specialist work is not evidence of a new Steward learning benefit. Preserve the candidate and stable identities pending targeted benefit/approval. |
| Design portion of [agent-skills #5](https://github.com/glichtenthal/agent-skills/pull/5) | **Eligible for independent design-only source approval**, if separated from Frontend | Repeated narrow procedural difference plus an actual complete handoff and scoped responsive implementation. AI-reviewed, one synthetic fixture; no broad performance or accessibility certification. |
| Frontend portion of agent-skills #5 | **Hold experimental instruction promotion**; do not merge the mixed PR wholesale | The October 31 rollback assertion regressed despite an aggregate case already failing. The applied fixture demonstrates execution/recovery capability but neither erases that score nor proves the lasting instruction change improves it. |

No source instruction, stable version, release approval, installation approval or installed skill changed in this final-quality pass. New material packaging choices were recorded in decisions.md. No model scheduler, service or second evaluator was introduced.

## Reporting correction

[Correction and unchanged evidence links](reporting-correction.md) and [new comparison output](frontend-corrected-comparison.json). The comparator now reports assertion transitions even within failed cases. The prior no-regression claim was too broad; all original October 31 scored records/output digests and old comparison files are preserved. No rubric was regraded or weakened to obtain a pass.

## Distribution

[distribution-manifest.txt](../../../distribution-manifest.txt) is the literal eight-file allowlist: SKILL.md, LICENSE, agents/openai.yaml, two icons, metadata/release.json, optional learning/README.md, and the manifest itself. No scripts, tests, pilot outputs, fixtures or model controllers ship. All reproducibility material stays in versioned source; evaluation tools run from the matching reviewed checkout, not an installed skill folder.

The former runtime archive contained 222 tracked files. The new packager verifies the exact eight names and byte parity, rejects missing/untracked/duplicate/unsafe/linked entries, and preserves an earlier artifact if validation fails. Same-environment reproducible bytes are tested; identical ZIP bytes across tools/timezones are not claimed. Published release assets are untouched. [Packaging receipt](packaging-receipt.txt).

## Applied test

[Applied report](applied/applied-test.md), [actual handoff](applied/experience-spec.md), [implementation](applied/index.html), [browser observations](applied/browser-checks.json), [screenshots](applied/), [execution provenance](applied/executions.json), and [artifact digests](applied/artifact-manifest.json).

Two actual gpt-6.1-sol/high CLI tasks produced the specification and HTML implementation. Controller browser actions then exercised the existing handoff/rendered-verification requirements. Nineteen observation groups cover desktop/mobile, recovery, modal focus/Escape, confirmation/Undo, repeated archives, reload and tablet/narrow/short layouts. One mobile-only typography repair and two restored handoff reference copies are recorded separately from agent output. An independent AI screenshot/static review found no material mismatch against the bounded brief; it did not rerun browser interactions.

The six assertions in the existing design-handoff-contract/frontend-rendered-verification cases have scoped applied evidence in the shared schema 1.1 reports. Other cases are intentionally not_run in those new records. Do not pool them into the earlier comparison or claim that all role/release suites clear. No suite case or skill rule was added to make this test pass.

Native zoom, screen-reader speech, physical virtual keyboard, cross-browser/device coverage and exhaustive accessibility remain untested. The app's permission/error states are explicitly synthetic. No live data, real authorization or deployment was tested. Source color calculations and DOM-test-double checks are separate from actual browser evidence.

## Checks and cost

42 local deterministic tests pass on the approved project-local Python 3.14.7. Hosted infrastructure CI uses Python 3.12 and runs suite validation, the same tests, and package verification: [run 41272762247](https://github.com/glichtenthal/ai-project-steward/actions/runs/41272762247). Fail-first tests demonstrated the prior hidden-regression and source-wide-packaging defects before their fixes.

The two applied agent executions report 588,034 input tokens, including 516,352 cached input tokens, and 19,111 output tokens. Reviewer/controller usage and exact dollar charges are not independently metered; no billing estimate is invented. No future model execution is scheduled.

Raw event streams remain outside Git; source and fixture artifacts contain synthetic data. Retention remains review disposition plus 30 days, followed by a deletion approval request, without an automatic deletion job. Historical failures, limits and private originals remain retained. The temporary loopback server is stopped after verification; open the self-contained HTML directly to reproduce the fixture.

## Next decision

Approve infrastructure independently if its source/CI evidence is satisfactory. Do not add more framework machinery or extra behavioral wording now. Review the Frontend rollback omission with the unchanged rubric and evidence before deciding whether a targeted instruction change or explicit scope-limited human acceptance is justified. Design can be reviewed separately rather than held hostage by the mixed specialist PR. Merge, release, publication and installation remain separate human actions; none was performed here.
