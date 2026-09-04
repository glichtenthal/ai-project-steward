# AI Project Steward

AI Project Steward provides a clear operating layer for visibility, guidance, approval, continuity, and verification throughout an AI-assisted build.

Use it independently as a portable skill or as the human-led governance and verification layer within a broader AI build harness.

Most AI building workflows help produce the next step. AI Project Steward helps the human and AI manage the build as a whole: it makes consequential choices visible, recommends practical approaches, preserves approval authority, records accepted decisions, and verifies the real result before calling the work complete.

Recommended for people who regularly use AI to build apps, prototypes, automations, integrations, deployments, or other technical projects—especially when the work spans multiple sessions or involves consequential choices.

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

## Install

The repository is the readable source of truth. The release package contains the same skill instructions, metadata, and local assets for import into a compatible AI product. Installing it adds the operating layer described above; it does not create a standalone runtime or complete harness, contain credentials, or connect to external systems by itself.

Before installing, you can review [SKILL.md](SKILL.md), inspect the [latest release](https://github.com/glichtenthal/ai-project-steward/releases/latest), and verify the release digest shown by GitHub.

### Claude or ChatGPT

Download `ai-project-steward.skill` from the [latest release](https://github.com/glichtenthal/ai-project-steward/releases/latest), then import it through your Skills settings.

### Codex

Ask Codex:

```text
Install the latest AI Project Steward release into ~/.agents/skills
```

Or install the current published release manually:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo glichtenthal/ai-project-steward \
  --path . \
  --ref v2.1.1 \
  --method download \
  --name ai-project-steward \
  --dest ~/.agents/skills
```

If `building-partner` is already installed, confirm that `ai-project-steward` passes a positive build test and a negative ordinary-work test before removing the legacy copy. Do not leave both versions active; overlapping skills can route unpredictably.

### Other skill-capable platforms

Other skill-capable platforms can import or recreate the root `SKILL.md` as a private custom skill. Keep automatic selection enabled and run both a positive technical-build test and a negative ordinary-work test after installation.

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

Build and verify the installable archive from the repository's tracked files with:

```bash
./scripts/package_skill.sh
```

The packaging check extracts the archive and compares every packaged file with the tracked source before reporting its SHA-256 digest.

See [evals/README.md](evals/README.md) for the live-run process and [evals/results](evals/results/) for versioned results. Behavioral results identify the platform, model, skill version, date, review method, and limitations; they are not presented as deterministic guarantees across every model or run.

The current Codex composition result verifies cooperation with coding and deployment guidance plus decision continuity across fresh sessions. A separate [two-platform probe](evals/results/v2.1.0-cross-platform-probe.md) compares the identical v2.1.0 instruction payload on Codex and Claude. Material-decision and ordinary-request behavior were consistent; the Claude reversible-change run introduced unrelated formatting. A third verified platform remains unavailable, so the formal cross-platform case remains incomplete rather than inferred.

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
