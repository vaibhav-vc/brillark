---
name: deal-structuring
category: gtm
description: "Structure an agreement that is testable before it is binding."
output: "deal-structure.md"
used_by:
  - partnership-bd-agent
---

# Deal Structuring

`gtm` · produces `deal-structure.md` · used by `partnership-bd-agent`

Structure an agreement that is testable before it is binding.

## Procedure
1. Start with the smallest structure that tests the thesis.
2. Define the commitments on both sides concretely.
3. Avoid exclusivity before evidence exists.
4. Set success metrics and a review date inside the agreement.
5. Define the exit and what happens to customers if it ends.

## Output contract
`deal-structure.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- No exclusivity before evidence
- Exit terms defined up front
- The output states its confidence grade and names the evidence behind every load-bearing claim.
