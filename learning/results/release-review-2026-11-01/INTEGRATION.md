# Controlled integration decisions — November 1, 2026

No merge, tag, release, archive publication or installation was performed. No model evaluation was rerun. All conclusions below distinguish source review, distribution inspection and existing behavioral evidence.

## Ready for explicit source merge approval

### Steward infrastructure PR #5

[PR #5](https://github.com/glichtenthal/ai-project-steward/pull/5), reviewed head `2e9d8a819b9be1c740a4ea895e432ac2db6b44c4`, base main `fa9f0bf4958cfe3ccd46df97f202da3a7ec73ebd`.

Final review found no merge-blocking source, security or regression issue within the inspected scope. `SKILL.md`, `agents/openai.yaml`, release metadata, original behavioral/composition definitions and historical results remain byte-identical to main. Instruction SHA-256 is `a67245b3797c837d58f94010ce1930352bb15865e514331b8a2dc66a748f9c16`.

[Exact-head CI](https://github.com/glichtenthal/ai-project-steward/actions/runs/41272762247) passed all 42 deterministic tests, validation and distribution verification. Existing CLI commands and schema-1.0 historical reporting remain supported; default improvement comparisons remain fail-closed. Regression mode does not invent uplift. Assertion pass-to-fail changes block clearance even inside an already failed aggregate case. The observation utility has no separate comparison engine, model execution, installer or approval authority. Composition report headings are clearer; no external undocumented Markdown-heading parser is certified.

The eight-file archive was rebuilt and unpacked into a temporary inspection directory only. Exact members, source-byte parity, metadata instruction hash, YAML entrypoint, icon paths and local instruction/reference links were checked. SHA-256: `80ef35356d8998dd36ba3710e02a3346fcb7027b3132b6be7a0bd624f94fb089`. There are no missing installation-time instruction assets or executable runtime dependencies. A compatible agent host supplies ordinary execution capabilities; Python and evaluator tools are not needed merely to load the skill. Evaluation scripts/cases/results are intentionally source-only, as stated in the optional protocol. The unchanged metadata's `evidence_summary` is a repository-relative informational provenance pointer, not a runtime file requirement; resolve it against the reviewed source revision.

Actual provider installation and post-install model smoke checks were not performed because installation is unapproved. Package completeness is not behavioral release approval. The current main candidate's recorded routing/cross-platform limits remain intact. Infrastructure correctness does not require a fabricated model-performance improvement.

### Design Director-only PR #7

[PR #7](https://github.com/glichtenthal/agent-skills/pull/7), reviewed Design payload `4039da168236b1ca58221a9ea028fbc2cb859ac95b8e9825270ba7febf692e0a`, candidate 1.3.2-rc.1. The existing Design body is an exact prefix; only the validated six-line learning section is appended. Responsibilities, approval gates, UI metadata, immutable references and version-1.0 handoff contract are unchanged. The full Frontend directory equals main/stable 1.3.1, instruction SHA-256 `180c7aa9942bcc94d9dcd066e4b65dd634331e72e847cc4f3d955ed88c1e20f6`.

[Exact-head CI](https://github.com/glichtenthal/agent-skills/actions/runs/41274622942) passed. A temporary candidate Design ZIP was inspected: the same six-file member layout as published product-design-director-1.3.1.zip, source-byte parity, local reference closure and metadata hash/false release/install flags. It was not installed or published. No second canonical Design directory or model-output suite was created.

Existing paired advisory evidence, confirmation and applied handoff/browser evidence are linked from the PR's RELEASE_REVIEW.md at immutable Steward commit `74c834a928d91408768095da9edaa79e55f82490`. Applied implementation used experimental Frontend, so compatibility with stable Frontend here is a targeted check of unchanged contract/references, not a new live model combination test. Native zoom, screen-reader speech and broader cross-browser/device certification remain limitations. Source merge approval does not certify a new release.

Individual Design remains candidate 1.3.2-rc.1. Collection 1.3.2-rc.2 identifies Design-only composition; published stable 1.3.1 assets remain untouched. First merge approved Steward infrastructure so its optional source-review protocol is available on main. Ordinary Design tasks do not require a Steward installation.

## Experimental work retained

### Steward learning PR #2

[PR #2](https://github.com/glichtenthal/ai-project-steward/pull/2) retains optional learning instructions, candidate metadata and all experimental evidence. The following content already matches infrastructure #5 exactly: evaluate.py, observation-only learn.py, packager, manifest, three test modules, validation workflow, learning protocol and role cases. There is no independently diverged comparison implementation.

**Recommendation: narrow this existing PR after infrastructure #5 is actually merged.** Refresh it from actual main using a normal reviewed reconciliation, then verify infrastructure disappears from the remaining diff. Keep only the optional Steward instruction addition, its candidate identity, and retained evidence/documentation. Do not create a replacement PR or delete history merely to hide the shared ancestry. If later behavioral review rejects the addition, close the experiment with an explicit disposition while preserving immutable evidence links. No branch reconciliation against an unmerged future main was fabricated here.

### Frontend-only agent-skills PR #5

[Original PR #5](https://github.com/glichtenthal/agent-skills/pull/5) is narrowed by an append-only split commit to Frontend-only experimentation. Its Design directory is restored to current main; all former mixed commits/evidence remain reachable, including `3347cbfc28b217be421ceeb451013d23c30f1f40`. Frontend instructions stay byte-identical to the tested experimental payload `82a6da544174a6e4486ede5f0594f70bb0dc30a36d569ffedae7a9e23866a01c`. Collection 1.3.2-rc.3 distinguishes this held composition from Design-only rc.2. No source history was rewritten and no evaluator was copied.

Hold the Frontend instruction change because the rollback assertion regressed. Before any later integration, refresh against then-current main, preserve approved Design changes and review collection composition. Never use this held branch as an installation source or blindly merge its old collection metadata over Design's approved source.

## Exact integration order

1. Obtain explicit approval for Steward infrastructure #5 at the reviewed head. Recheck its head/base/checks, then merge only that PR. No release or installation follows automatically.
2. Recheck main CI, unchanged instruction identity and eight-file package. Narrow existing Steward #2 against actual merged main; keep its behavior/evidence experimental. No second engine or maintenance branch is needed.
3. Obtain explicit approval for Design-only #7. Recheck its diff/CI and stable Frontend identity, then merge that source PR. Leave Frontend-only #5 unmerged. `agent-skills` already has legacy GitHub Pages from main `/`; a source merge can trigger the existing catalog rebuild even without visitor-page changes. This is not a new skill release or installation; acknowledge the existing rebuild when approving the merge. No Pages setting was changed.
4. Prepare a separately reviewed release proposal: final version/tag, scope and collection composition, immutable source hashes, intended platforms/activation, package/ZIP contents and checksums, known limitations and rollback artifacts. Keep candidate labels and false release/install flags until that decision is actually authorized. Infrastructure merge alone does not authorize stable Steward 2.1.3 or waive its existing behavioral limits. Design can be published independently of experimental Frontend using the existing standalone ZIP format.
5. Obtain separate publication approval before creating tags/releases/uploading approved artifacts. Preserve existing stable assets; do not publish the held Frontend payload through a combined collection. This step remains blocked by release approval, not infrastructure uplift.
6. Obtain explicit installation approval for an exact approved version and one target location. Verify archive/checksum, snapshot and verify the current installed folder, inspect and stage the approved package, replace only that chosen copy, verify instruction/assets/reference hashes, then start a fresh session for scoped smoke checks. Keep a verified restore copy; do not update both ~/.agents and ~/.codex copies by default. Do not run generic catalog `install.sh --update` for a new Steward version: it currently pins v2.0.0. Review its pin in the release proposal or use the explicitly approved exact-version archive instead. No installer or global PATH was changed here.

## Remaining approval boundaries

No unresolved source/distribution blocker was found for infrastructure #5 or Design-only #7 at the reviewed heads. Human merge approval is pending. Publication versions/tags and installation/smoke checks remain separate, unapproved work. Steward optional behavioral benefit and Frontend rollback remain experimental questions. Existing installed stable versions and repository releases are unchanged.
