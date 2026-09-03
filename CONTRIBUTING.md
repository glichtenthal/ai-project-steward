# Contributing

AI Project Steward improves when people contribute realistic build scenarios, routing failures, and examples where important choices became visible too late.

Good contributions include:

- app, prototype, automation, integration, migration, and deployment scenarios with real trade-offs
- examples where the skill asked too many low-impact questions or skipped a material decision
- positive and negative routing cases with clear pass/fail expectations
- failure cases involving secrets, permissions, cost, destructive actions, rollback, or incomplete verification
- redacted live-run evidence that identifies the skill version, platform, model, date, and review method
- composition cases showing cooperation with coding or deployment skills, continuity across fresh sessions, or comparable behavior across platforms

Please keep contributions focused on observable behavior. The goal is more reliable human-led building, not more process for its own sake.

Open an issue with:

1. the build request or scenario
2. the material decision or failure mode
3. the behavior you expected
4. what the skill did instead

Before submitting an evaluation change, run:

```bash
python3 scripts/evaluate.py validate
```

See [evals/README.md](evals/README.md) for the live-run and versioned-results methodology. Never include credentials, private customer data, account identifiers, or unrelated conversation history in an evaluation artifact.
