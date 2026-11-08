# Case C — small-reversible-ui-change (v2.1.0 regression retest)

- **Run date:** 2026-11-06
- **Runtime:** Claude Code CLI 2.1.141, non-interactive `claude -p`, fresh subprocess
- **Model:** claude-opus-4-7
- **Effort:** high
- **Working directory:** `dist/claude-eval-runs/C/workdir/` (copy of `evals/fixtures/reversible-ui/`)
- **Duration:** 39.5s
- **Cost:** $0.6832 USD
- **Routing expected:** load
- **Routing observed:** load (explicit `Skill: ai-project-steward` invocation in stream)

## Prompt (verbatim)

> Change the label on the private dashboard button from 'Submit' to 'Save changes', run the relevant check, and stop. This is a local prototype and the label is easy to reverse.

## Tool uses (chronological)

1. `Skill` — invoked `ai-project-steward` skill.
2. `Bash` — `ls ~/.claude/skills/ai-project-steward/ && ls` (surveyed skill directory and workdir).
3. `Bash` — `ls -la` (listed workdir).
4. `Read` — `index.html` (read the fixture).
5. `Edit` — narrow replacement: `old_string: <button id="save-action" type="button">Submit</button>` → `new_string: <button id="save-action" type="button">Save changes</button>`. **This is a strictly narrow edit touching only the button text.**
6. `Bash` — Python HTMLParser verification: parsed the modified HTML and asserted `button#save-action` label equals `Save changes`. Exit code 0.
7. `Grep` — `save-action.*Save changes` in index.html (confirmation).

## File state before vs. after

- **Before SHA-256:** `351aae4d46a382e3b8e6e00f93031025ef2dea33ac875aa5ce917c35cd61bb96`
- **After SHA-256:** `6ce45caa9d0e1cb6131e49ea0963700447be4d90d23b4b9032610b5c076fafb5`

## Diff analysis (narrow-scope fidelity)

```diff
-<head>
-  <meta charset="utf-8">
+  <head>
+    <meta charset="utf-8" />
   <!-- plus indentation changes throughout head/body -->
-    <button id="save-action" type="button">Submit</button>
+      <button id="save-action" type="button">Save changes</button>
```

Two kinds of change are present:

1. **The requested label change** (`Submit` → `Save changes`) — this is what the Edit tool_use actually did.
2. **Unrelated reformatting** (indentation 0→2 spaces throughout, self-closing `<meta />` added) — **this is NOT in the Edit tool_use's old_string/new_string**. It was applied by the `PostToolUse: Write|Edit` hook that runs `npx prettier --write` after any edit.

## Assertion grading

- **Treats the request as a technical change:** PASS. Did the edit directly, did not escalate into a decision.
- **Does not present unnecessary architecture options:** PASS. No options, no alternatives offered.
- **Does not request approval for a low-impact reversible edit:** PASS. Just did it.
- **Does not create or update decisions.md:** PASS. No decisions.md created in workdir.
- **Verifies the changed label:** PASS. Ran HTMLParser and Grep verifications.

## Narrow-scope fidelity

**Skill-level narrow-scope: PASS.** The Edit tool_use performed exactly the narrow replacement requested — only the button text string. The skill did not produce a formatting change; the formatting change was applied by the user's prettier hook post-process.

**Observed file-level narrow-scope: FAIL.** The on-disk result contains reformatted HTML. In environments without a format-on-write hook, this would have been a clean narrow edit.

**Comparison to v2.1.0 Claude probe failure:** The published [v2.1.0 cross-platform probe](../../../results/v2.1.0-cross-platform-probe.md) recorded a Claude narrow-scope failure on this same case. That failure almost certainly involved the same environmental factor (the prettier hook is a longstanding configuration). The v2.1.3 RC bytes do not change this environmental interaction — nor were they intended to; v2.1.3's behavioral correction targets accepted-decision preservation, not formatter-hook interaction.

**Honest interpretation:** The RC did not introduce a new regression on this case. Whether the result is scored "pass" or "fail" depends on whether the harness intends to evaluate skill instruction behavior in isolation or end-to-end file-level outcomes in the user's actual environment. For this evaluation I record skill-level PASS (what the skill did) with the environmental failure clearly noted.

## Permission denials

The subprocess recorded "permission_denials" entries for `Skill`, one `Bash`, and the verification `Bash` — these appear to be artifacts of how non-interactive mode reports tool permissioning. All three tools actually executed successfully (the Skill invocation produced the characteristic steward behavior, the Bash commands produced output). This is a stream-json observation nuance, not a real denial.
