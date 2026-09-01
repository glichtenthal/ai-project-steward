# Decisions

## 2026-08-30 — Public skill architecture and catalog placement

- **Status:** Accepted
- **Context:** Building Partner began as a personal framework distributed across several AI products. Publishing it requires a reusable source of truth and a clear relationship to the existing four-part Judgment Infrastructure loop.
- **Options considered:** Add it as a mandatory fifth loop step; publish it only as an unrelated standalone skill; publish it as a standalone skill and place it first under Applied Judgment Systems with an optional bridge from Test Drive.
- **Decision:** Publish `glichtenthal/building-partner` as the canonical public, platform-neutral skill. Position it first under Applied Judgment Systems and reference it after Test Drive without changing the four-part core loop. Keep private installation status and platform-specific personal adapters outside the public repository.
- **Rationale:** The skill is useful independently and also carries earlier judgment work into implementation. This placement preserves the existing loop, gives Building Partner a clear identity, and creates room for future applied systems.
- **Consequences and trade-offs:** The public repository gains independent releases, evals, and version history. Personal installations must be synchronized from the public policy plus any narrowly scoped private adapter. Moving Building Partner into the core loop later would require catalog and installer changes, but not a skill rewrite.
- **Reconsider when:** Users consistently treat Building Partner as a required fifth loop step, Applied Judgment Systems becomes too broad, or maintaining the public and private layers produces demonstrated drift.

## 2026-08-31 — Visual identity and catalog scope

- **Status:** Accepted
- **Context:** The initial dark card used a generic plus mark, while the agent-skills catalog mixed installable skills with a hosted GPT that had no repository, package, or comparable release path.
- **Options considered:** Keep the initial identity and mixed catalog; redesign Building Partner while leaving the hosted GPT; give Building Partner a lighter reusable mark and keep the catalog focused on installable skills.
- **Decision:** Use a light, vector-based Building Partner identity built around two overlapping blocks and a checked decision point. Keep Applied Judgment Systems as the category, present Building Partner as its first entry, and remove Executive Recruiter GPT from the agent-skills catalog until complete applications have a dedicated presentation surface.
- **Rationale:** The mark communicates building and explicit human approval at icon and card sizes. A skills-focused catalog gives every visible entry the same basic contract: source, version, install path, and supporting material.
- **Consequences and trade-offs:** Building Partner gains reusable icon metadata and a clearer public identity. Executive Recruiter GPT loses one discovery link but can return later in a separate applications section without changing the judgment loop or Building Partner.
- **Reconsider when:** Two or more complete applications are ready for a consistent public applications section, or the Building Partner mark does not remain legible in supported skill interfaces.
