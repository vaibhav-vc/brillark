---
name: prior-error-lookup
category: memory
description: "Check whether this organisation has already been wrong about this."
output: "prior-error-report.md"
used_by:
  - council-assumption-auditor
---

# Prior Error Lookup

`memory` · produces `prior-error-report.md` · used by `council-assumption-auditor`

Check whether this organisation has already been wrong about this.

## Procedure
1. Extract the assumptions in the current plan.
2. Search memory for previously disproven assumptions on the same subject.
3. Report matches with the evidence that disproved them.
4. Check whether the conditions that made it wrong still hold.
5. Block the plan from repeating an error without an explicit reason why this time differs.

## Output contract
`prior-error-report.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Matches carry the disproving evidence
- Repeat requires an explicit difference
- The output states its confidence grade and names the evidence behind every load-bearing claim.
