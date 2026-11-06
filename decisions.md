# Product Decisions

This public record contains decisions that shape the skill, package, and public catalog. Private installation status, account-specific routers, and cross-platform distribution history are maintained in the separate private distribution guide.

## 2026-08-30 — Standalone skill and catalog placement

- **Status:** Accepted
- **Context:** The operating framework is useful independently and can also carry prior judgment work into implementation.
- **Options considered:** Add it as a mandatory fifth step in the core judgment loop; publish it as an unrelated standalone skill; publish it as a standalone skill under Applied Judgment Systems with an optional bridge from Test Drive.
- **Decision:** Publish the framework as a standalone, platform-neutral skill and place it first under Applied Judgment Systems. Reference it after Test Drive without changing the four-part core loop.
- **Rationale:** This preserves the complete judgment loop while giving the build-focused operating layer a clear identity and independent installation path.
- **Consequences and reversal difficulty:** The skill has its own repository, releases, examples, and evaluations. Moving it into the core loop later would require catalog and installer changes, but not a skill rewrite.
- **Reconsider when:** Users consistently treat the skill as a required fifth loop step or the Applied Judgment Systems category no longer describes the portfolio.

## 2026-08-31 — Visual identity and catalog scope

- **Status:** Accepted
- **Context:** The initial identity used a generic mark, while the catalog mixed installable skills with a hosted application that had no comparable package or release path.
- **Options considered:** Keep the initial identity and mixed catalog; redesign the identity while retaining the hosted application; use a distinctive build-and-check mark and keep this catalog focused on installable skills.
- **Decision:** Use a light visual identity built around overlapping blocks and a checked decision point. Keep the catalog focused on installable skills until complete applications have a dedicated presentation surface.
- **Rationale:** The mark communicates building plus explicit verification, and a skills-focused catalog gives every entry the same source, version, installation, and evidence contract.
- **Consequences and reversal difficulty:** The skill has reusable icon metadata and a clearer public identity. A separate applications section can be introduced later without changing the skill architecture.
- **Reconsider when:** Multiple complete applications are ready for a consistent public section or the mark does not remain legible in supported interfaces.

## 2026-08-31 — AI Project Steward name and role

- **Status:** Accepted
- **Context:** Building Partner was approachable but generic. Creator Steward was distinctive but could imply content creation rather than project development.
- **Options considered:** Keep Building Partner with sharper positioning; rename it Creator Steward; rename it AI Project Steward.
- **Decision:** Use `ai-project-steward` / AI Project Steward for the skill, package, repository, and catalog entry.
- **Rationale:** The name identifies the technology, the work, and the role. “Steward” describes an active collaborator that helps a project succeed without taking authority from the user.
- **Consequences and reversal difficulty:** The name is differentiated and faithful to the behavior. “Project” is broad, so routing must continue to exclude ordinary writing, research, summarization, and administrative work.
- **Reconsider when:** Routing begins to activate for ordinary non-build projects, users consistently misunderstand “steward,” or the name develops a material product or trademark conflict.

## 2026-09-01 — Hybrid behavioral evidence system

- **Status:** Accepted
- **Context:** Declarative prompt cases describe intended behavior but do not, by themselves, show that a released skill produced the behavior. Fully automated semantic scoring would add model cost and could mistake keyword matching for good stewardship.
- **Options considered:** Keep declarative cases only; add fully automated model calls and grading; combine automated package validation with repeatable live runs and explicit human review.
- **Decision:** Use a hybrid Behavioral Evaluation Suite. Automate package and case-definition validation, use a repeatable runner to prepare and summarize live runs, and publish versioned human-reviewed results with retained, redacted outputs where appropriate.
- **Rationale:** The hybrid approach makes evidence reproducible without hiding judgment behind a brittle score. It also distinguishes package validity, routing behavior, and steward behavior.
- **Consequences and reversal difficulty:** The repository gains a small dependency-free runner, a CI validation workflow, four public scenarios, and versioned result files. Live model runs still require platform access and must identify their model, date, method, and limitations. The structure can later move to a shared portfolio harness if several skills adopt it.
- **Reconsider when:** Three or more skill repositories duplicate the runner, a stable cross-platform evaluation API becomes available, or human review becomes the primary bottleneck.

## 2026-09-01 — Secondary AI build harness positioning

- **Status:** Accepted
- **Context:** AI Project Steward already functions as an operating layer around AI-assisted builds. Industry discussion of harness engineering offers a useful architectural frame, but calling the skill a complete harness would imply runtime orchestration, tool enforcement, observability, and persistent state that it does not provide.
- **Options considered:** Keep all harness language out of the product; describe the skill as one layer within a broader AI build harness; reposition the product primarily as an AI harness.
- **Decision:** Keep “portable operating skill” and the existing value proposition primary. Add secondary language explaining that AI Project Steward can serve as the human-led governance and verification layer within a broader AI build harness.
- **Rationale:** This makes the product legible within current AI architecture without weakening its plain-language value or overstating technical enforcement.
- **Consequences and reversal difficulty:** The repository, product page, catalog, packaging explanation, and evidence methodology gain a consistent layer model. The skill name, routing metadata, and `.skill` distribution remain unchanged. Removing the secondary framing later would be easy; making harness the primary category would require stronger runtime and enforcement capabilities.
- **Reconsider when:** Users mistake the skill for a complete technical harness, the term loses practical meaning, or the product adds native state, enforced gates, tool interception, and automated verification sufficient to support a primary harness category.

## 2026-09-01 — Expanded behavioral evidence scope

- **Status:** Accepted
- **Context:** The first release evidence established core steward behavior, deployment-skill cooperation, and decision continuity. It did not directly exercise a local integration's important failure paths or a naturally selected positive routing case.
- **Options considered:** Keep the original core suite; add only more happy-path prompts; add local, observable evaluation cases for routing, approval boundaries, decision reversals, integration verification, and skill composition.
- **Decision:** Extend the evidence plan with an explicit local integration-verification case and separate natural-routing and coding-composition probes. Retain the existing approval-boundary and decision-reversal cases as their authoritative core checks.
- **Rationale:** This adds observable coverage of the gap the skill is meant to close without substituting a mock adapter for a live account or overstating what one platform router proves.
- **Consequences and reversal difficulty:** Results can make more specific claims about safe local verification and composition. A real-account test remains separately approval-gated and cannot be inferred from the local adapter. The additional cases are easy to revise as real integrations and platform access become available.
- **Reconsider when:** A supported cross-platform evaluation interface provides reliable routing telemetry, or a controlled test account and explicit authorization make a real-connector evaluation appropriate.

## 2026-09-18 — Prepare Steward 2.1.2 stable release

- **Status:** Accepted for publication on 2026-09-18.
- **Context:** Promote the tested September 17 candidate unchanged; preserve the separate older hardening experiment.
- **Options:** Keep candidates only; publish the tested instructions unchanged; add further speculative instructions.
- **Recommendation:** Prepare the tested instructions unchanged, with version metadata and bounded evidence.
- **Consequences:** Preserves tested behavior; source publication and installation remain separate steps. Local changes can be discarded before publication.
- **Reconsider when:** Review finds a source conflict or repeated real-world failures justify a focused instruction change.

## 2026-11-01 — Minimal distribution and separate infrastructure review

- **Status:** Accepted for implementation by the November 1 quality request; merge, release and installation remain unapproved.
- **Context/options:** Ship every tracked source file; maintain parallel runtime/evidence archives; or ship one explicit runtime allowlist and retain evidence in versioned source.
- **Decision:** Use one reviewed distribution manifest, reject unsafe/missing/untracked/linked entries, and verify exact membership and byte parity. Keep evaluation tooling and evidence in Git. Prepare infrastructure independently of behavioral instruction promotion.
- **Rationale:** Smaller portable instructions and one source evidence system; no new services, dependencies or evaluation engine.
- **Consequences:** Source-based tooling must run in its reviewed checkout, not inside installed skills. Stable releases and instruction hashes are unchanged. Reverting the packaging change is straightforward before any release; no installed archive is replaced here.
- **Reconsider when:** A required runtime reference is missing, platform consumers require another asset, or source-retained evidence cannot reproduce a result.

## 2026-11-06 — Prepare Claude 2.1.3 release candidate from shared source

- **Status:** Accepted for release-candidate preparation on 2026-11-06. Publication, tag creation, and installation remain unapproved.
- **Context:** The published v2.1.3 Codex-only release preserves the tested instruction bytes. Users want Claude support without maintaining a separate skill or weakening the existing instructions. The Agent Skills spec (`name` ≤ 64 chars, `description` ≤ 1024 chars, non-empty) is already satisfied by the current `SKILL.md` (473-char description, compliant identifier). Prior Claude evidence exists only on v2.1.0 (material-decision and ordinary-request passed; narrow-scope reversible-change failed on unrelated HTML formatting).
- **Options considered:** (A) Minimal RC: build a Claude-scoped archive from the existing 8-file manifest with a Claude-targeted `metadata/release.json`, leave the Codex release and source files otherwise untouched. (B) Parametric packaging: add `--scope` to `scripts/package_skill.sh`, produce per-platform archives, and introduce `agents/anthropic.yaml`. (C) Universal scope: update the shared metadata to declare "Codex and Claude" scope in one shared archive.
- **Decision:** Use (A) for the RC. Keep (C) as the follow-up state once Claude evaluation evidence supports broadening scope. Reject (B) for this RC because the added packaging surface is not required by the Agent Skills spec and increases the maintained manifest.
- **Rationale:** Smallest reversible change; preserves the published Codex 2.1.3 asset and tag unchanged; keeps one canonical `SKILL.md` instruction payload across platforms; defers the shared-scope metadata change until Claude evaluation evidence exists.
- **Consequences and reversal difficulty:** The RC produces a separately labeled `ai-project-steward-2.1.3-rc.1-claude.zip` with Claude-scoped release metadata. Reversible by deleting the staged `dist/` artifact and the branch. Final move to (C) requires owner approval after evaluation and would update `metadata/release.json` and the README install section.
- **Reconsider when:** Claude evaluation introduces instruction-level requirements that cannot be served by the current SKILL.md bytes, the Agent Skills spec changes materially, or a new Claude UI layer requires platform-specific interface metadata.

## 2026-11-06 — Defer Claude release tag until publication

- **Status:** Accepted for preparation on 2026-11-06.
- **Context:** The published `v2.1.3` tag is pinned to the Codex-only release. A Claude release could extend v2.1.3 (asset addition) or ship as a new tag (e.g. v2.1.4) once evidence clears.
- **Options considered:** Pre-commit to a v2.1.4 tag; pre-commit to extending v2.1.3 via asset addition; defer the tag decision until publication time.
- **Decision:** Stay as an RC during preparation. Owner selects the final tag approach when publication is authorized, based on the Claude evaluation record and scope-change acceptability.
- **Rationale:** Keeps the preparation reversible, avoids committing to a tag name that the evaluation outcome might contradict, and preserves the immutability of the current v2.1.3 release.
- **Consequences and reversal difficulty:** No new tag is created during preparation. No asset is uploaded. Reverting the branch is sufficient to cancel.
- **Reconsider when:** The Claude evaluation clears and the owner is ready to publish; or a stakeholder requires a pre-committed version plan before evaluation proceeds.

## 2026-11-06 — Omit agents/anthropic.yaml for the Claude 2.1.3 RC

- **Status:** Accepted on 2026-11-06.
- **Context:** `agents/openai.yaml` supplies Codex-specific interface metadata (short description, icons, brand color, implicit-invocation policy). claude.ai and Claude Code do not consume an equivalent file today.
- **Options considered:** Include an `agents/anthropic.yaml` mirroring `openai.yaml` for parity; omit it for this RC and reconsider if a Claude surface introduces an interface-metadata contract.
- **Decision:** Omit `agents/anthropic.yaml` from the Claude RC distribution. The existing `agents/openai.yaml` remains in the archive and is documented as Codex-only interface metadata.
- **Rationale:** No consumer exists today; adding the file creates manifest and validator surface that must be maintained without a current purpose.
- **Consequences and reversal difficulty:** Smaller archive, no new validator rule. Reversible by adding the file and extending the distribution manifest if a Claude UI contract appears.
- **Reconsider when:** claude.ai, Claude Code, or a managed-agent surface publishes an interface-metadata contract analogous to Codex's `agents/openai.yaml`.

## 2026-11-03 — Codex-only 2.1.3 release exception

- **Status:** Accepted by explicit owner instruction on November 3; package finalization, publication, current-pilot backup, installation and smoke checks authorized.
- **Context/options:** Hold pending a complete strict matrix, remediate routing before release, or release the already tested narrow correction under disclosed Codex-only exceptions.
- **Decision:** Release unchanged tested instructions under the exact exceptions in the [clearance review](docs/release-review-v2.1.3-2026-11-02.md#november-3-clearance-addendum). Preserve the failed strict gate and original results.
- **Rationale/consequences:** Retained evidence supports the accepted-decision correction without more model evaluation. Automatic routine-edit activation remains unreliable; use explicit invocation when coverage matters. No broad performance or cross-platform claim is authorized.
- **Reversal and review triggers:** Verify published package integrity and current-pilot backup; restore that backup on a critical installation/smoke regression. Reconsider release clearance if instruction bytes change, evidence integrity fails or a material regression emerges. Other skills and experimental PRs remain unchanged.
