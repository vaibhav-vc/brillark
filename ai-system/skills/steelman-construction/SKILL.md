---
name: steelman-construction
category: council
description: "Rebuild a rejected option at its strongest before judging it."
output: "steelman.md"
used_by:
  - council-devils-advocate
  - council-director
---

# Steelman Construction

`council` · produces `steelman.md` · used by `council-devils-advocate`, `council-director`

Rebuild a rejected option at its strongest before judging it.

## Procedure
1. State the rejected option in the form its best advocate would use.
2. Identify the conditions under which it would be right.
3. Fix the weaknesses that were incidental rather than fundamental.
4. Compare the strengthened version against the recommendation.
5. State honestly whether the rejection still holds.

## Output contract
`steelman.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Option restated at its strongest
- Rejection re-tested against the improved version
- The output states its confidence grade and names the evidence behind every load-bearing claim.
