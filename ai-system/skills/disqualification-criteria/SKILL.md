---
name: disqualification-criteria
category: market
description: "Define who we will not sell to, and stick to it."
output: "disqualification.md"
used_by:
  - icp-persona-builder
---

# Disqualification Criteria

`market` · produces `disqualification.md` · used by `icp-persona-builder`

Define who we will not sell to, and stick to it.

## Procedure
1. Identify the attributes that predicted past failures or churn.
2. Write each as an observable, checkable condition.
3. Distinguish 'not now' from 'never'.
4. Give sellers permission to disqualify and a script for doing it well.
5. Measure how often the criteria are overridden and what happened.

## Output contract
`disqualification.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Criteria observable and checkable
- Override rate measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.
