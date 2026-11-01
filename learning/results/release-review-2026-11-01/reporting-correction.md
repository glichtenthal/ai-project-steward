# Correction to October 31 regression reporting

The earlier statement “No scored pass-to-fail regression occurred” was incorrect at assertion level. The comparator inspected only aggregate cases. In `frontend-learning-regression-loop`, the case remained failed in both arms, masking a changed failure:

| Published assertion | Baseline | Candidate |
|---|---|---|
| Requires same-model baseline/candidate testing | fail | pass |
| Keeps browser verification and rollback boundaries | pass | fail |

The rollback judgment concerns an omitted explicit rollback boundary in the candidate response; it is not proof that the agent performed an unsafe deployment or changed security. Independent AI judgments remain provisional; no human regrading occurred here.

Original scores, retained outputs, their evidence hashes, and old comparison files are unchanged. [The corrected comparison](frontend-corrected-comparison.json) uses the same records and criteria with the repaired reporting code. It discloses two assertion improvements across the Frontend suite and one assertion regression, independently of aggregate case changes. Clearance and promotion remain blocked.

A fail-first deterministic test recreated the hidden-regression shape; it failed on the old comparator and passed after assertion-level comparison was added. This is a reporting/integrity correction, not a claim of new model performance. No new behavioral case or revised rubric was introduced.
