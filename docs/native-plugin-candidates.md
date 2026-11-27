# Native plugin candidates

AI Project Steward uses the same reviewed instruction payload for every distribution. This directory's build procedure adds host-specific packaging around the existing stable skill.

## Build

From the repository root, run:

~~~sh
python3 scripts/package_plugins.py
python3 -m unittest discover -s tests -p 'test_plugin_packaging.py' -v
cd dist/plugins
shasum -a 256 -c STEWARD-PLUGIN-SHA256SUMS
~~~

The script derives the instruction version from `metadata/release.json`, verifies the stable skill SHA-256, and builds separate OpenAI and Claude ZIP files. Use `--iteration 2` to increment the packaging candidate version without editing the instruction version. ZIP membership, file bytes, and checksums are verified locally. Existing standalone archives and tags retain their original release scope.

## Installation pilots

Both plugin packages are candidate distributions. The current instruction version is 2.1.3 and the initial plugin version is 2.1.3-plugin.1.

| Distribution | Pilot location | Evidence required |
| --- | --- | --- |
| OpenAI plugin ZIP | ChatGPT private plugin creation and Codex | Account ingestion, plugin discovery, each intended runtime's behavior |
| Claude plugin ZIP | Claude Customize > Plugins, custom plugin upload | Account ingestion, plugin discovery, native Claude and Cowork behavior |
| Unpacked Claude plugin | Claude Code `--plugin-dir` in an isolated workspace | Manifest validation, explicit invocation and behavioral checks |

In OpenAI's Plugin Creator upload the OpenAI ZIP as a private plugin. In Claude's Customize > Plugins upload the Claude ZIP as a custom plugin. For a local Claude Code candidate, extract the Claude archive into an isolated directory and run:

~~~sh
claude plugin validate /path/to/extracted-plugin
claude --plugin-dir /path/to/extracted-plugin
~~~

Check for existing standalone or plugin copies of AI Project Steward and legacy Building Partner before activating a candidate. Use one authoritative copy per test context, preserving the current installation and a verified rollback path. Use explicit invocation when reliable Steward coverage matters.

## Native behavior evaluation

Use the existing [Behavioral Evaluation Suite](../evals/README.md) and [composition cases](../evals/composition/README.md). Begin with fresh, isolated sessions:

- Explicit activation for a customer portal authentication choice.
- Negative routing for an ordinary email draft and CRM explanation.
- A routine, reversible edit with no unrelated changes.
- Material approval, accepted-decision preservation and explicitly approved replacement across fresh sessions.
- Verification of a local fixture integration, including failure handling and accurate completion status.

Retain the exact prompts, responses, routing telemetry where available, modified fixture evidence, and hashes. Record observed behavior separately for ChatGPT, Codex, Claude, Cowork, and Claude Code. Unavailable routing telemetry or unexecuted cases remain unscored. Do not reuse CLI evidence as native chat or Cowork evidence.

At preparation, both packages contained the exact released skill SHA-256 `a67245b3797c837d58f94010ce1930352bb15865e514331b8a2dc66a748f9c16`. Local deterministic packaging and rejection of modified instruction bytes passed, Claude Code 2.1.141 manifest validation passed, and private OpenAI ingestion returned the original skill text. Native behavioral evaluations remain pending. Existing bounded release evidence is documented in the root [README](../README.md). Stable release promotion requires separate review and authorization.
