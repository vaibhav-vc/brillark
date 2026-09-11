---
name: improvement-return-analysis
category: improvement
description: "Judge whether the improvement effort was worth it."
output: "return-analysis.md"
used_by:
  - chief-learning-officer-agent
---

# Improvement Return Analysis

`improvement` · produces `return-analysis.md` · used by `chief-learning-officer-agent`

Judge whether the improvement effort was worth it.

## Procedure
1. Sum the cost of the improvement work for the period.
2. Sum the measured gains from adopted changes that held.
3. Subtract the cost of changes that were reverted.
4. Report the net honestly, including negative periods.
5. Recommend continuing, refocusing, or reducing the effort.

## Output contract
`return-analysis.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Reverted changes counted as cost
- Negative periods reported honestly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
