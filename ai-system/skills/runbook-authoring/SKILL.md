---
name: runbook-authoring
category: orchestration
description: "Write a procedure another agent can execute without asking questions."
output: "runbook.md"
used_by:
  - coo-agent
---

# Runbook Authoring

`orchestration` · produces `runbook.md` · used by `coo-agent`

Write a procedure another agent can execute without asking questions.

## Procedure
1. State the trigger condition and the expected end state.
2. Write numbered steps with the exact command, query, or decision at each.
3. Include the verification after each step that proves it worked.
4. Cover the failure branches, not only the happy path.
5. Have a different agent execute it once and fix everything they had to ask about.

## Output contract
`runbook.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Tested by a different agent
- Failure branches covered
- The output states its confidence grade and names the evidence behind every load-bearing claim.
