# Claude Code 2.1.3 packaging correction — November 21, 2026

Use [ai-project-steward-2.1.3-claude-r2.zip](https://github.com/glichtenthal/ai-project-steward/releases/download/v2.1.3-claude/ai-project-steward-2.1.3-claude-r2.zip) with [STEWARD-CLAUDE-R2-SHA256SUMS](https://github.com/glichtenthal/ai-project-steward/releases/download/v2.1.3-claude/STEWARD-CLAUDE-R2-SHA256SUMS) from the existing [v2.1.3-claude release](https://github.com/glichtenthal/ai-project-steward/releases/tag/v2.1.3-claude).

The original `ai-project-steward-2.1.3-claude.zip` contained release-candidate `metadata/release.json` (`2.1.3-rc.1-claude`, candidate/unreleased) because the distribution allowlist did not ship the separate canonical `metadata/release-claude.json`. Instructions were unaffected.

The prepared r2 archive changes only `metadata/release.json`, making it byte-identical to [the approved Claude Code record at the original tag](https://github.com/glichtenthal/ai-project-steward/blob/v2.1.3-claude/metadata/release-claude.json): version 2.1.3, stable, Claude Code scope. All seven other runtime files are unchanged. r2 is a packaging revision, not another skill version or release tag.

- Corrected ZIP SHA-256: `37456b38e018af03fc333c2a5940f4dd36de0d55190068a435f12d05861d88ea`.
- Unchanged SKILL.md SHA-256: `a67245b3797c837d58f94010ce1930352bb15865e514331b8a2dc66a748f9c16`.
- Eight-file inventory: LICENSE, SKILL.md, agents/openai.yaml, assets/icon-large.svg, assets/icon-small.png, distribution-manifest.txt, learning/README.md, metadata/release.json.

The existing [original archive](https://github.com/glichtenthal/ai-project-steward/releases/download/v2.1.3-claude/ai-project-steward-2.1.3-claude.zip) (SHA-256 `89fc8c7ec16a2e53073cba3ee4dbb265331e15ca5cc9ec6448641b43a9dc98fc`), [original checksum](https://github.com/glichtenthal/ai-project-steward/releases/download/v2.1.3-claude/STEWARD-CLAUDE-SHA256SUMS), release tag and evaluation history remain intact for audit. They are not the recommended Claude Code installation package.

Verification compared the exact prepared archive and checksum with independent downloads from the published release, checked all four asset hashes and confirmed the seven unchanged members and canonical metadata bytes. [PR #10](https://github.com/glichtenthal/ai-project-steward/pull/10) supplies the stable-metadata gate; the [hosted release-assets validation](https://github.com/glichtenthal/ai-project-steward/actions/runs/44942257978) passed, checking r2 and identifying the original by its exact superseded digest. No gate was bypassed and no archive was rebuilt for publication.

Support is bounded to the recorded **Claude Code CLI** evaluation and its accepted exceptions. Native claude.ai support is unverified. This correction does not rerun behavioral evaluations, demonstrate an incremental quality benefit over ordinary Codex, authorize another system's actions or update existing installations. Follow the backup and verification instructions in the [installation guide](../README.md#claude-code-213).
