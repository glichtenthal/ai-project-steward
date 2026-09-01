# Decisions

## 2026-08-30 — Public skill architecture and catalog placement

- **Status:** Superseded
- **Context:** Building Partner began as a personal framework distributed across several AI products. Publishing it requires a reusable source of truth and a clear relationship to the existing four-part Judgment Infrastructure loop.
- **Options considered:** Add it as a mandatory fifth loop step; publish it only as an unrelated standalone skill; publish it as a standalone skill and place it first under Applied Judgment Systems with an optional bridge from Test Drive.
- **Decision:** Publish `glichtenthal/building-partner` as the canonical public, platform-neutral skill. Position it first under Applied Judgment Systems and reference it after Test Drive without changing the four-part core loop. Keep private installation status and platform-specific personal adapters outside the public repository.
- **Rationale:** The skill is useful independently and also carries earlier judgment work into implementation. This placement preserves the existing loop, gives Building Partner a clear identity, and creates room for future applied systems.
- **Consequences and trade-offs:** The public repository gains independent releases, evals, and version history. Personal installations must be synchronized from the public policy plus any narrowly scoped private adapter. Moving Building Partner into the core loop later would require catalog and installer changes, but not a skill rewrite.
- **Reconsider when:** Users consistently treat Building Partner as a required fifth loop step, Applied Judgment Systems becomes too broad, or maintaining the public and private layers produces demonstrated drift.
- **Superseded because:** The repository architecture and Applied Judgment Systems placement remain appropriate, but the public name and skill identity were changed to AI Project Steward on August 31, 2026.

## 2026-08-31 — Visual identity and catalog scope

- **Status:** Accepted
- **Context:** The initial dark card used a generic plus mark, while the agent-skills catalog mixed installable skills with a hosted GPT that had no repository, package, or comparable release path.
- **Options considered:** Keep the initial identity and mixed catalog; redesign Building Partner while leaving the hosted GPT; give Building Partner a lighter reusable mark and keep the catalog focused on installable skills.
- **Decision:** Use a light, vector-based Building Partner identity built around two overlapping blocks and a checked decision point. Keep Applied Judgment Systems as the category, present Building Partner as its first entry, and remove Executive Recruiter GPT from the agent-skills catalog until complete applications have a dedicated presentation surface.
- **Rationale:** The mark communicates building and explicit human approval at icon and card sizes. A skills-focused catalog gives every visible entry the same basic contract: source, version, install path, and supporting material.
- **Consequences and trade-offs:** Building Partner gains reusable icon metadata and a clearer public identity. Executive Recruiter GPT loses one discovery link but can return later in a separate applications section without changing the judgment loop or Building Partner.
- **Reconsider when:** Two or more complete applications are ready for a consistent public applications section, or the Building Partner mark does not remain legible in supported skill interfaces.

## 2026-08-31 — Rename to AI Project Steward

- **Status:** Accepted
- **Context:** Building Partner was approachable but described a generic relationship rather than the skill's responsibilities. Creator Steward was more distinctive but could imply writing, design, or content creation. Build Steward was the clearest two-word alternative but is already used for a closely related digital-product governance offering.
- **Options considered:** Keep Building Partner with sharper positioning; rename it Creator Steward; rename it AI Project Steward.
- **Decision:** Rename the public skill, package, repository, and catalog entry to `ai-project-steward` / AI Project Steward. Retain its placement first under Applied Judgment Systems. Preserve a temporary redirect and legacy installer alias for `building-partner`, but do not keep both skills active after migration.
- **Rationale:** The name identifies the technology, the work, and the role. Steward describes an active collaborator that helps the project succeed without taking authority from the user. The public language will consistently emphasize four responsibilities: visible choices, approval boundaries, recorded decisions, and verified results.
- **Consequences and trade-offs:** The new name is more differentiated and faithful to the skill's behavior. “Project” can sound broader than technical builds, so the routing description must continue to exclude ordinary writing, research, summarization, and administrative work. Existing private installations, links, packages, and tests require a coordinated migration. The repository rename and release publication remain paused until the prepared migration is verified and approved.
- **Reconsider when:** Routing begins to activate for ordinary non-build projects, users consistently misunderstand “steward,” or the name develops a material product or trademark conflict.
