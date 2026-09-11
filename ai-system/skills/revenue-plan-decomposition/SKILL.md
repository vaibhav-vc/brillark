---
name: revenue-plan-decomposition
category: finance
description: "Break a revenue target into drivers someone can own."
output: "revenue-plan.md"
used_by:
  - chief-revenue-officer-agent
---

# Revenue Plan Decomposition

`finance` · produces `revenue-plan.md` · used by `chief-revenue-officer-agent`

Break a revenue target into drivers someone can own.

## Procedure
1. Decompose the target into volume, conversion, price, and retention.
2. Assign each driver to one owner.
3. Check the implied numbers for plausibility against current performance.
4. Identify the driver requiring the largest improvement — that is the real plan.
5. Set the leading indicator for each driver.

## Output contract
`revenue-plan.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Every driver has one owner
- Implied improvements checked for plausibility
- The output states its confidence grade and names the evidence behind every load-bearing claim.
