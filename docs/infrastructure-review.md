# Infrastructure-only review — November 1, 2026

This extraction is based on main `fa9f0bf`. SKILL.md, agents/openai.yaml, installed-skill policy and metadata/release.json remain byte-identical to that base. No behavioral-gain claim or release/installation approval is made.

Includes the existing schema 1.1 evaluator with optional role suites, separate regression/improvement modes, assertion-level transition reporting, observation-only triage, deterministic tests and an explicit eight-file runtime manifest. It replaces the weaker duplicate gate rather than adding another engine. Role scenarios remain supplemental; nothing invokes models automatically. CI remains push/PR-only and contains no model calls.

An infrastructure change needs deterministic integrity and compatibility evidence, not an invented model-performance gain. Complete comparable passing records can clear regression mode without improvement; incomplete checks and candidate failures still block. All comparison results remain advisory.

The archive includes instructions, license, UI/icon metadata, current release metadata, the optional learning protocol and the manifest. Scripts, test controllers, fixtures, results and private logs stay outside distribution. Evidence remains versioned in the source repository and original behavioral PR. Packaging tests cover exact membership/parity, unsafe/missing/untracked/duplicate/linked entries, preserving an earlier archive on failed validation and repeatable same-environment bytes. Cross-platform ZIP tool/timezone equivalence is not claimed.

The October 31 Frontend rollback assertion regressed pass-to-fail while the aggregate case stayed failed; earlier aggregate-only reporting missed it. The repaired comparator discloses it and blocks clearance. Historical scores and retained model evidence are not rewritten.

Review/merge scope: infrastructure only. Optional behavioral learning instructions remain in [Steward #2](https://github.com/glichtenthal/ai-project-steward/pull/2) and [specialist #5](https://github.com/glichtenthal/agent-skills/pull/5). Merging this PR would not install instructions, publish an archive, create a release, or schedule evaluations. Those remain separate human decisions.
