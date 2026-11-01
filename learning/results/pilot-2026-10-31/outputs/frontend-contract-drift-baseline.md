# Actual agent output: frontend-contract-drift / baseline

Synthetic advisory fixture; public extract, not live validation.

Instruction SHA-256: 180c7aa9942bcc94d9dcd066e4b65dd634331e72e847cc4f3d955ed88c1e20f6
Prompt SHA-256: 55668362df3333d5797b042ed7134250541611182fd6c2c1ae66adddc794d02d
Execution exit: 0; timeout: False; elapsed: 17.732 seconds.

## Output (local paths and personal name redacted)

Changing the approved workflow and data meaning is a material design-contract change. It requires a revised specification and design approval before implementing the affected behavior.

The workspace [SKILL.md](<workspace>/pilot/private/frontend-contract-drift/baseline/SKILL.md) requires: “update the project-owned experience specification and return it to design approval.”

The next step is to prepare a reviewable change proposal:

- Describe the approved behavior, the implementation constraint, and evidence that makes the change necessary.
- Compare an engineering alternative that preserves the contract with the proposed workflow and data changes.
- Specify what each affected field means before and after, including effects on existing records, calculations, permissions, and user expectations.
- Revise the affected flows, states, and acceptance criteria. Preserve historical evidence and clear current approval and verification references that no longer apply.
- Link material decisions to `decisions.md`, when present, and obtain approval for the revised direction.

After approval, implement and verify the revised behavior, including data compatibility and recovery where applicable.

Only `SKILL.md` was reviewed. No specification, implementation constraint, data contract, or test evidence was supplied, so necessity, migration requirements, and correctness remain unverified. No files were changed or checks executed.
