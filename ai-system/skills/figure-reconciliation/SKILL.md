---
name: figure-reconciliation
category: finance
description: "Trace every externally reported number to its source before it leaves the building."
output: "reconciliation-trail.md"
used_by:
  - investor-reporting-agent
---

# Figure Reconciliation

`finance` · produces `reconciliation-trail.md` · used by `investor-reporting-agent`

Trace every externally reported number to its source before it leaves the building.

## Procedure
1. List every figure appearing in the external document.
2. Trace each to its source system or calculation.
3. Recompute independently and compare.
4. Resolve any difference before publication, not after.
5. Record the reconciliation trail so the figure can be defended later.

## Output contract
`reconciliation-trail.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Every external figure traced
- Differences resolved before publication
- The output states its confidence grade and names the evidence behind every load-bearing claim.
