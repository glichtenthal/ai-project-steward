# Versioned Results

This directory contains published Behavioral Evaluation Suite results organized by skill release and tested platform.

Each result must identify:

- skill release
- platform and model
- evaluation date
- review method
- package-validation status
- case-level routing and behavioral outcomes
- failures, not-run cases, and limitations
- retained redacted output evidence when available

## Current candidate evidence

- [Codex and Claude cross-platform probe](v2.1.0-cross-platform-probe.md) — the identical v2.1.0 instruction payload was exercised on both platforms. Material-decision and ordinary-request controls passed on both; the narrow reversible-change probe passed on Codex and retained a Claude scope-fidelity failure. The formal three-platform case remains incomplete.
- [Corrected Codex release baseline](v2.1.0-corrected-release-baseline.md) — all ten core cases were run against the exact corrected candidate. All eight positive steward-behavior cases passed; both unforced negative controls passed by observed behavior. This is the current release baseline.
- [Final Codex release baseline](v2.1.0-release-baseline.md) — all ten core cases were run against the exact current candidate. Seven of eight positive steward-behavior cases passed; the complete local-project build is retained as a failure because it deferred and did not verify the authorized fixture-data logic. Both unforced negative controls passed by observed behavior.
- [Complete local-build targeted rerun](v2.1.0-complete-local-build-rerun.md) — the narrowly corrected candidate passed the previously failing local-build scenario in a fresh synthetic workspace, including independently verified fixture tests and a dry run. It does not replace the retained baseline failure.
- [Clean Codex regression](v2.1.0-codex-regression.md) — all ten core cases were run against the candidate. Six steward-behavior cases passed, two were retained as failures, and the two unforced negative controls passed by observed behavior.
- [Targeted verification rerun](v2.1.0-verification-rerun.md) — narrow corrections to the local-adapter completion boundary and incomplete-context decision comparison, retested without erasing the earlier misses.
- [Harness composition result](v2.1.0-composition-codex.md) — coding-skill cooperation, deployment-skill cooperation, and fresh-session decision continuity passed on Codex; cross-platform consistency remains unrun.
- [Natural-routing smoke test](v2.1.0-router-smoke.md) — an unforced technical-build prompt selected the currently installed local copy. It is not evidence for the exact candidate package.

No result is backfilled for an earlier release without a retained run record.
