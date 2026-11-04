# AI Project Steward

**Bring your ideas to life with AI, while your judgment shapes what gets built.**

AI Project Steward helps you navigate consequential technical decisions, preserve choices throughout development, and verify that what gets built works as intended.

Use this portable agent skill to build apps, prototypes, automations, and integrations with AI. It translates goals into practical plans, explains significant tradeoffs in architecture, data, security, cost, and deployment, and keeps accepted decisions available across sessions.

For developers and teams, it brings consistent approval boundaries, project continuity, and meaningful completion checks to existing AI-assisted workflows. Routine, reversible work stays lightweight.

## Why this exists

AI can move from a plain-language request to working software quickly. That speed is useful, but ordinary build conversations can leave important parts of the project implicit:

- architecture, data, cost, permission, hosting, and maintenance choices
- what the user has and has not authorized
- why an earlier decision was made
- whether a polished interface is connected to real behavior
- whether the result was tested against the actual use case

AI Project Steward closes those gaps without turning every implementation detail into a meeting. It applies more structure when a decision is consequential and stays out of the way when a change is low-impact and easy to reverse.

## What changes in the build

AI Project Steward:

- translates the desired outcome into a practical implementation
- explains material choices and compares realistic options in plain English
- recommends an approach and makes present and future trade-offs clear
- pauses before costly, public, destructive, security-sensitive, or difficult-to-reverse actions
- preserves accepted decisions in a concise project-level `decisions.md`
- protects secrets and identifies backup or rollback requirements
- runs or renders the result and checks important success and failure scenarios
- refuses to describe mocked, disconnected, or partially verified behavior as finished

It does **not** require approval or a decision record for every small choice. A reversible local change should remain fast.

## For people building with AI and developers

- **People bringing ideas to life:** Understand the choices that could affect cost, data, privacy, or what can be changed later, without having to direct every implementation detail.
- **Developers and engineering teams:** Keep accepted decisions and approval boundaries clear across sessions, surface hidden assumptions early, and check real functionality instead of relying on a convincing demo.
- **Teams using specialist skills:** Use Steward for project-wide scope, decisions, and completion; Product Design Director for experience design and critique; and Production Frontend Engineer for implementation and technical verification. These roles are complementary, not a bundled or automatically orchestrated multi-agent system.

## How it fits in an AI build harness

A broader AI build harness may include several layers:

- **Model or agent:** reasons, generates, and chooses the next action.
- **Tools and runtime:** read files, write code, run checks, and interact with deployment systems.
- **Project context and memory:** supply requirements, files, prior decisions, and current state.
- **Human-led governance and verification:** keep consequential choices visible, preserve approval authority and continuity, and prove the real result.

AI Project Steward fills the fourth layer. It works alongside coding, deployment, platform, and routine skills rather than replacing them.

It is not a complete technical harness by itself. It does not provide the model, coding runtime, tool permissions, secrets management, observability, sandboxing, or deterministic policy enforcement. Installation adds a portable operating layer that helps the human and AI use those components coherently and responsibly.

## See the range

Four worked scenarios show how the skill adapts to different build conditions:

1. **[Complete project build](examples/quick-demo.md)** — the golden path from an initial request through visible choices, approval, a recorded decision, implementation, and verification.
2. **[Fast reversible change](examples/fast-reversible-change.md)** — progress without unnecessary governance.
3. **[Consequential deployment](examples/consequential-deployment.md)** — authorization, secrets, cost, migration, backup, and rollback boundaries.
4. **[False completion](examples/false-completion.md)** — detecting fixture data or disconnected behavior before declaring success.

The [Behavioral Evaluation Suite](evals/README.md) contains additional routing, restraint, continuity, and completion cases with explicit pass criteria.

## Good first uses

```text
Use AI Project Steward while we build this prototype. Keep consequential choices visible and verify the real result before calling it complete.
```

```text
Help me choose the authentication approach for this app before you implement it.
```

```text
Build a small customer-health workflow that reads CRM data and drafts a private alert.
```

```text
Review this deployment plan and identify what needs an explicit approval, backup, or rollback path.
```

## Release status

**Stable Codex release:** [v2.1.3](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.3), approved with the explicit exceptions in the [bounded clearance review](docs/release-review-v2.1.3-2026-11-02.md#november-3-clearance-addendum). The tested instruction payload is unchanged from 2.1.3-rc.1. Previously accepted decisions stay accepted until the user approves a replacement.

The strict regression gate did **not** pass. The shared routine-label natural-activation miss, mixed runtime/incomplete per-window coverage, inconclusive baseline build and unexecuted cross-platform case remain disclosed. Use explicit invocation when Steward coverage matters. No general speed/cost gain, reliable automatic activation, three-platform certification or autonomous recursive improvement is claimed. [Metadata](metadata/release.json) and the unchanged [candidate evidence](evals/results/v2.1.3-rc.1-codex.md) retain the scope and limitations.

## Install

### Codex 2.1.3

Download `ai-project-steward-2.1.3-codex.zip` and `STEWARD-SHA256SUMS` from the [v2.1.3 release](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.3). Verify the archive's SHA-256 before extracting. Use the release asset rather than a full source checkout or the historical 110-file pilot ZIP.

1. Extract into a temporary directory. Verify `metadata/release.json` names `2.1.3`, `stable`, and `Codex only`, and verify `SKILL.md` against its `skill_sha256`. The archive contains exactly the eight entries in `distribution-manifest.txt`; evaluation tools and evidence remain in the repository.
2. Locate the active Steward directory, normally `~/.codex/skills/ai-project-steward` or the configured Codex skills location. Inspect `~/.agents/skills` and project-local skill sources for overlapping Steward or legacy `building-partner` copies. Update one authoritative target and preserve unrelated skills.
3. Back up the entire current Steward directory and relevant configuration outside active skill-search directories. Record hashes and verify the backup before replacement. If updating a private pilot, back up that current pilot rather than assuming an older stable backup represents today's state.
4. Replace only the selected Steward directory with the verified `ai-project-steward/` archive contents. Do not install source evaluation files, retain active backup copies, or replace Design Director or Frontend Engineer.
5. In fresh Codex conversations, test positive technical routing, negative ordinary writing, proportional routine edits, unapproved decision preservation and explicitly approved replacement with fresh-session continuity. Keep the known natural routine-edit loading miss visible; explicit use does not prove automatic selection. Restore the verified backup if a critical check regresses.

The skill will be available on the next turn. Restart a conversation when checking fresh-session behavior. Installing Steward does not authorize the systems it helps you build to publish, spend money, expose data or bypass approval boundaries.

### Other products and platforms

Version 2.1.3 clearance is Codex-only. Keep existing stable Claude/ChatGPT installations unchanged; this release does not establish new certification for them. The earlier [v2.1.2 release](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.2) remains available for its historical scope and rollback needs.

## How it fits with the judgment loop

- **The Briefing Room** organizes messy context.
- **Ground Truth** pressure-tests the plan or assumptions.
- **The Quorum** deliberates consequential decisions.
- **Test Drive** creates the smallest credible test.
- **AI Project Steward** carries the work into implementation with visible choices, approval boundaries, decision continuity, and verification.

The other skills are optional. Use AI Project Steward independently for an AI-assisted build, or after the loop when earlier judgment work should carry into implementation.

## Evidence and evaluation

The evaluation system separates three questions:

1. **Package validity:** Are the skill, metadata, examples, and evaluation definitions complete and internally consistent?
2. **Routing behavior:** Does the platform activate the skill for relevant builds and leave it inactive for unrelated work?
3. **Steward behavior:** Once active, does it exhibit the expected guidance, authorization, continuity, restraint, and verification behaviors?
4. **Composition behavior:** Can it work alongside coding or deployment guidance, preserve decisions across fresh sessions, and exhibit the same essential safeguards across platforms?

Run the dependency-free package validation with:

```bash
python3 scripts/evaluate.py validate
```

Build and verify the installable archive from the explicit distribution manifest with:

```bash
./scripts/package_skill.sh
```

The packaging check uses `distribution-manifest.txt`, verifies exact archive membership and source-byte parity, and excludes evaluation evidence/controllers. See `learning/README.md` for source-only evaluation tooling.

See [evals/README.md](evals/README.md) for the live-run process and [evals/results](evals/results/) for versioned results. Behavioral results identify the platform, model, skill version, date, review method, and limitations; they are not presented as deterministic guarantees across every model or run.

The historical v2.1.0 Codex composition result verifies cooperation with coding and deployment guidance plus decision continuity across fresh sessions. A separate [two-platform probe](evals/results/v2.1.0-cross-platform-probe.md) compares the identical v2.1.0 instruction payload on Codex and Claude. Material-decision and ordinary-request behavior were consistent; the Claude reversible-change run introduced unrelated formatting. A third verified platform remains unavailable, so the formal cross-platform case remains incomplete rather than inferred.

## Repo layout

```text
ai-project-steward/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
├── evals/
│   ├── evals.json
│   ├── composition.json
│   ├── composition/
│   ├── README.md
│   ├── runs/
│   └── results/
├── examples/
├── scripts/
│   ├── evaluate.py
│   └── package_skill.sh
├── .github/workflows/
│   └── validate.yml
├── README.md
├── decisions.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── LICENSE
```

## Version history

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT. See [LICENSE](LICENSE).

## More judgment infrastructure

Browse [Judgment Infrastructure for Human-Led AI](https://glichtenthal.github.io/agent-skills/) for portable skills and applied systems that help people think and build without outsourcing judgment.
