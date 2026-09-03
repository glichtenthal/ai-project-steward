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
