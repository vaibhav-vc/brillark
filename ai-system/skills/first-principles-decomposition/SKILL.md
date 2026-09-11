---
name: first-principles-decomposition
category: council
description: "Strip a plan to what is actually necessary."
output: "first-principles.md"
used_by:
  - council-first-principles
---

# First Principles Decomposition

`council` · produces `first-principles.md` · used by `council-first-principles`

Strip a plan to what is actually necessary.

## Procedure
1. List every element of the plan and what it is meant to achieve.
2. Separate physical, legal, and economic necessities from conventions.
3. Ask of each convention what breaks if it is simply not done.
4. Reduce to the irreducible set of requirements.
5. Present the reduced set for reconstruction.

## Output contract
`first-principles.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Necessities separated from conventions
- Reduction to an irreducible set
- The output states its confidence grade and names the evidence behind every load-bearing claim.
