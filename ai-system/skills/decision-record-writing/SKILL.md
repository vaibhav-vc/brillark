---
name: decision-record-writing
category: orchestration
description: "Capture a decision so a future reader understands why, not just what."
output: "decision-record.md"
used_by:
  - director
---

# Decision Record Writing

`orchestration` · produces `decision-record.md` · used by `director`

Capture a decision so a future reader understands why, not just what.

## Procedure
1. State the decision in one sentence, in the active voice.
2. Describe the context and the constraints in force at the time.
3. List the options considered and why each was rejected.
4. State the consequences accepted, including the bad ones.
5. Name the trigger that should cause this decision to be revisited.

## Output contract
`decision-record.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Rejected options recorded with reasons
- Revisit trigger named
- The output states its confidence grade and names the evidence behind every load-bearing claim.
