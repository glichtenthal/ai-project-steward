# Decisions

## 2026-08-30 — Public skill architecture and catalog placement

- **Status:** Accepted
- **Context:** Building Partner began as a personal framework distributed across several AI products. Publishing it requires a reusable source of truth and a clear relationship to the existing four-part Judgment Infrastructure loop.
- **Options considered:** Add it as a mandatory fifth loop step; publish it only as an unrelated standalone skill; publish it as a standalone skill and place it first under Applied Judgment Systems with an optional bridge from Test Drive.
- **Decision:** Publish `glichtenthal/building-partner` as the canonical public, platform-neutral skill. Position it first under Applied Judgment Systems and reference it after Test Drive without changing the four-part core loop. Keep private installation status and platform-specific personal adapters outside the public repository.
- **Rationale:** The skill is useful independently and also carries earlier judgment work into implementation. This placement preserves the existing loop, gives Building Partner a clear identity, and creates room for future applied systems.
- **Consequences and trade-offs:** The public repository gains independent releases, evals, and version history. Personal installations must be synchronized from the public policy plus any narrowly scoped private adapter. Moving Building Partner into the core loop later would require catalog and installer changes, but not a skill rewrite.
- **Reconsider when:** Users consistently treat Building Partner as a required fifth loop step, Applied Judgment Systems becomes too broad, or maintaining the public and private layers produces demonstrated drift.
