> **2.1.3-rc.1: unreleased Codex-only candidate.** Stable 2.1.2 remains the published release. No tag, release, or installation is authorized by preparing this candidate.

> [Candidate metadata](metadata/release.json) identifies the tested instruction hash and scope. Earlier release reports retain their original version scope and do not certify this candidate. See the [candidate evaluation summary](evals/results/v2.1.3-rc.1-codex.md).

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

**Do not install this candidate until the user separately approves installation.** Source preparation and successful checks do not grant that approval. Publishing a release is also a separate action.

### Codex candidate: private staged installation after approval

The candidate is currently a local, unpublished package. There is no `v2.1.3-rc.1` remote tag or release asset to download. Use the exact staged archive identified in the candidate receipt, not an unpinned checkout of `main` or a command that requests the latest release.

After explicit approval:

1. Verify the staged archive SHA-256 against its receipt, extract it into a temporary directory, and confirm `metadata/release.json` says `2.1.3-rc.1`, `candidate`, and `Codex only`. Confirm the extracted `SKILL.md` SHA-256 matches `skill_sha256`.
2. Locate the existing active Steward directory. Codex's installer defaults to `$CODEX_HOME/skills` (normally `~/.codex/skills`); installations in `~/.agents/skills` may also exist. Update the existing location instead of creating a second active copy. Do not replace Design Director or Frontend Engineer.
3. Back up the entire current Steward directory outside every active skill-search directory, retain its file hashes, and verify the backup before replacement. Keep the published stable package available for rollback.
4. Replace only the approved Steward directory with the verified candidate contents. Do not leave `building-partner`, a second Steward version, or a backup directory active alongside it. Do not remove unrelated skills.
5. In fresh Codex conversations, check positive technical routing, negative ordinary writing, the routine local edit, and unapproved/approved decision replacement. Record the installed hash and the actual results. If a critical check regresses, restore the verified stable backup and report the failure; do not silently declare the candidate promoted.

These are future installation instructions, not actions performed by this candidate preparation. Native routing limitations must remain visible; explicit invocation can verify instructed behavior but cannot establish automatic-selection reliability. The candidate checks reproduced a routine-label source-loading miss in both stable and candidate. Keep that limitation visible when reviewing any explicit-use pilot; do not describe automatic activation as fully verified.

### Published stable version

The published stable version is still **v2.1.2**. Its release asset is `ai-project-steward-2.1.2.zip`, with `STEWARD-SHA256SUMS`; do not assume the obsolete `.skill` asset name exists on that release. Review the [v2.1.2 release](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.2) and verify the downloaded archive against its published digest.

For a separately authorized fresh Codex installation of that stable version, the existing installer can pin the exact v2.1.2 release commit and defaults to the configured Codex skills directory:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo glichtenthal/ai-project-steward \
  --path . \
  --ref 92b2cd704dd4eff339c10001d229403dc75b446c \
  --method download \
  --name ai-project-steward
```

The installer refuses to overwrite an existing skill. Use the verified backup/replacement procedure for an update; do not work around this by installing an overlapping copy elsewhere. The command above is for stable v2.1.2, not this unpublished candidate.

### Other products and platforms

This candidate has no new Claude, ChatGPT, or cross-platform certification. Keep existing stable installations there. A future release must name its actual supported asset format and tested platforms rather than implying that a ZIP is universally importable.

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
