---
name: retrospective-facilitation
category: orchestration
description: "Run a cycle review that changes behaviour instead of producing notes."
output: "retrospective.md"
used_by:
  - orchestration-head
  - retrospective-agent
---

# Retrospective Facilitation

`orchestration` · produces `retrospective.md` · used by `orchestration-head`, `retrospective-agent`

Run a cycle review that changes behaviour instead of producing notes.

## Procedure
1. Open by verifying whether last cycle's actions were actually implemented.
2. Establish what happened factually before discussing why.
3. Separate what worked from what did not, with equal rigour on both.
4. Convert each lesson into one specific artifact change with an owner and a date.
5. Close by recording which lessons go to the recurring-flaw register.

## Output contract
`retrospective.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Prior actions verified first
- Every lesson becomes an owned artifact change
- The output states its confidence grade and names the evidence behind every load-bearing claim.
