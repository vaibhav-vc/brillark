---
name: simplification-challenge
category: council
description: "Ask what could be removed entirely."
output: "simplification-report.md"
used_by:
  - council-first-principles
---

# Simplification Challenge

`council` · produces `simplification-report.md` · used by `council-first-principles`

Ask what could be removed entirely.

## Procedure
1. List the components, steps, and features in the plan.
2. For each, ask what happens if it is simply removed.
3. Identify elements retained out of habit or completeness.
4. Quantify the cost each element adds.
5. Recommend removals with the risk of each stated.

## Output contract
`simplification-report.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Removal tested for every element
- Risk of each removal stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
