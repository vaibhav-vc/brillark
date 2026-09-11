---
name: churn-analysis
category: gtm
description: "Understand why customers leave, in categories you can act on."
output: "churn-analysis.md"
used_by:
  - chief-revenue-officer-agent
  - customer-success-agent
---

# Churn Analysis

`gtm` · produces `churn-analysis.md` · used by `chief-revenue-officer-agent`, `customer-success-agent`

Understand why customers leave, in categories you can act on.

## Procedure
1. Capture a reason for every churn, from the customer where possible.
2. Classify into a fixed taxonomy: product gap, value not realised, price, change of need, or service failure.
3. Separate voluntary from involuntary churn — the fixes are different.
4. Compute churn by cohort and segment, not blended.
5. Route each category to the owner who can address it.

## Output contract
`churn-analysis.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Fixed taxonomy applied consistently
- Voluntary and involuntary separated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
