# Building Partner

Describe what you want to build in ordinary language. Building Partner helps the AI surface consequential choices, ask before risky actions, record accepted decisions, and verify the result against the real use case.

Use it for apps, prototypes, automations, integrations, deployments, and other technical workflows. It installs as a portable skill and keeps consequential decisions with the person doing the work.

Building Partner works on its own or after a judgment workflow when clarified context, tested assumptions, and accepted decisions should carry into implementation.

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

See the [worked quick demo](examples/quick-demo.md) for a complete example with realistic options, an approval boundary, a decision record, and verification scenarios.

## Install for Claude or ChatGPT

Download `building-partner.skill` from the [latest release](https://github.com/glichtenthal/building-partner/releases/latest), then import it through your Skills settings.

## Install for Codex

Ask Codex:

```text
Install Building Partner v1.1.0 into ~/.agents/skills
```

Or install manually:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo glichtenthal/building-partner \
  --path . \
  --ref v1.1.0 \
  --method download \
  --name building-partner \
  --dest ~/.agents/skills
```

Do not install the skill in more than one user-skills location. Duplicate-name skills can route unpredictably.

## Other skill-capable platforms

Platforms including Town and Replit can import or recreate the root `SKILL.md` as a private custom skill. Keep automatic selection enabled and run both a positive technical-build test and a negative ordinary-work test after installation.

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
│   ├── icon-large.svg
│   ├── icon-small.png
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
