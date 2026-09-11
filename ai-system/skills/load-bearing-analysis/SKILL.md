---
name: load-bearing-analysis
category: council
description: "Determine which assumptions the plan cannot survive without."
output: "load-bearing-report.md"
used_by:
  - council-assumption-auditor
---

# Load Bearing Analysis

`council` · produces `load-bearing-report.md` · used by `council-assumption-auditor`

Determine which assumptions the plan cannot survive without.

## Procedure
1. For each assumption, ask what remains true if it is false.
2. Score how much of the plan collapses in each case.
3. Cross-reference the score against the evidence grade.
4. Flag the high-load, low-evidence assumptions as the critical set.
5. Rank the critical set by the cost of being wrong.

## Output contract
`load-bearing-report.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Load cross-referenced against evidence grade
- Critical set explicitly ranked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
