---
name: boundary-design
category: engineering
description: "Decide where to split the system."
output: "boundary-design.md"
used_by:
  - system-architect
---

# Boundary Design

`engineering` · produces `boundary-design.md` · used by `system-architect`

Decide where to split the system.

## Procedure
1. Group by data ownership and rate of change, not by team structure.
2. Define the contract at each boundary explicitly.
3. Check that a boundary reduces coupling rather than moving it.
4. Assess the cost of crossing: latency, consistency, and debugging.
5. Prefer fewer boundaries until the pain justifies another.

## Output contract
`boundary-design.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Boundaries follow data and change rate
- Crossing cost assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
