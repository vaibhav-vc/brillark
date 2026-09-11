---
name: hypothesis-backlog
category: market
description: "Keep a ranked list of what we believe and how we will test it."
output: "hypothesis-backlog.md"
used_by:
  - business-head
---

# Hypothesis Backlog

`market` · produces `hypothesis-backlog.md` · used by `business-head`

Keep a ranked list of what we believe and how we will test it.

## Procedure
1. Write each belief as a falsifiable statement with a threshold.
2. Rank by how much of the plan depends on it and how uncertain it is.
3. Define the cheapest test that could disprove it.
4. Assign an owner and a by-when.
5. Move results into the validated-learning log, including failures.

## Output contract
`hypothesis-backlog.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Beliefs stated falsifiably with thresholds
- Ranked by dependency and uncertainty
- The output states its confidence grade and names the evidence behind every load-bearing claim.
