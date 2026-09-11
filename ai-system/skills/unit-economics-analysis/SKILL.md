---
name: unit-economics-analysis
category: finance
description: "Determine whether one unit of the business makes money, line by line."
output: "unit-economics.md"
used_by:
  - finance-head
  - unit-economics-architect
---

# Unit Economics Analysis

`finance` · produces `unit-economics.md` · used by `finance-head`, `unit-economics-architect`

Determine whether one unit of the business makes money, line by line.

## Procedure
1. Define the unit precisely and defend the choice; ambiguity here corrupts everything downstream.
2. Build the revenue side per unit: price, frequency, and expected lifetime.
3. Build the cost stack bottom-up: COGS, delivery, support, payment fees, and infrastructure.
4. Compute contribution margin and payback period from actuals wherever they exist.
5. State how each line behaves at 10x volume and which are truly variable.

## Output contract
`unit-economics.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Every cost line traced to a source
- Behaviour at scale stated per line
- The output states its confidence grade and names the evidence behind every load-bearing claim.
