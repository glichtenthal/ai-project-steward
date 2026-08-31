# Building Partner

A portable operating skill for human-led AI builds.

Building Partner helps people plan and build apps, prototypes, automations, integrations, and other technical workflows while keeping consequential decisions with the person doing the work.

Use it independently whenever AI is helping you build something. It can also follow a judgment workflow, carrying clarified context, tested assumptions, and accepted decisions into implementation with visible trade-offs, explicit approvals, and verification against the real use case.

## Why this exists

AI can move from a plain-language request to working software quickly. That speed is useful, but it can also hide choices about data, cost, permissions, hosting, portability, and maintenance until they are expensive to unwind.

Building Partner makes those choices visible without turning every implementation detail into a meeting. It asks for approval when the stakes warrant it, records material decisions, protects secrets, and checks the working result before describing the build as complete.

## What it does

- translates an ordinary-language goal into a practical implementation
- explains material choices and presents realistic options
- recommends an approach and makes the future trade-offs clear
- pauses before costly, public, destructive, security-sensitive, or difficult-to-reverse actions
- keeps a concise project-level `decisions.md`
- prefers the fewest moving parts that reliably satisfy the request
- runs or renders the result and verifies it against real scenarios

## Good first uses

```text
Help me choose the authentication approach for this prototype before you implement it.
```

```text
Build a small customer-health workflow that reads CRM data and drafts a private alert.
```

```text
Plan this app in ordinary language, explain the material choices, and recommend the simplest reliable architecture.
```

```text
Review this deployment plan and tell me what requires approval or a rollback path.
```

## Install for Claude or ChatGPT

Download `building-partner.skill` from the [latest release](https://github.com/glichtenthal/building-partner/releases/latest), then import it through your Skills settings.

## Install for Codex

Ask Codex:

```text
Install Building Partner v1.0.0 into ~/.agents/skills
```

Or install manually:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo glichtenthal/building-partner \
  --path . \
  --ref v1.0.0 \
  --method download \
  --name building-partner \
  --dest ~/.agents/skills
```

Do not install the skill in more than one user-skills location. Duplicate-name skills can route unpredictably.

## Other skill-capable platforms

Platforms including Town and Replit can import or recreate the root `SKILL.md` as a private custom skill. Keep automatic selection enabled and run both a positive technical-build test and a negative ordinary-work test after installation.

## Try it in three minutes

Start with the [worked quick demo](examples/quick-demo.md). It shows a realistic build request, the expected decision shape, approval boundary, and completion check.

## How it fits with the judgment loop

- **The Briefing Room** organizes messy context.
- **Ground Truth** pressure-tests the plan or assumptions.
- **The Quorum** deliberates consequential decisions.
- **Test Drive** creates the smallest credible test.
- **Building Partner** carries the work into implementation with visible choices, approvals, continuity, and verification.

The other skills are optional. Use Building Partner by itself for an AI-assisted build, or use it after the loop when earlier judgment work should carry into implementation.

## Repo layout

```text
building-partner/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── social-preview.svg
├── evals/
│   └── evals.json
├── examples/
│   └── quick-demo.md
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
