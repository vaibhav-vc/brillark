---
name: journey-mapping
category: design
description: "Map the customer's whole path, including the parts the product never sees."
output: "journey-map.md"
used_by:
  - design-researcher
---

# Journey Mapping

`design` · produces `journey-map.md` · used by `design-researcher`

Map the customer's whole path, including the parts the product never sees.

## Procedure
1. Define the journey's start and end from the customer's perspective, not the product's.
2. Lay out the stages with the actions, thoughts, and emotions at each.
3. Mark the pain points and their evidence from research.
4. Include the offline, human, and waiting steps.
5. Identify the two moments that most determine whether the journey succeeds.

## Output contract
`journey-map.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Journey bounded by the customer's goal
- Offline and waiting steps included
- The output states its confidence grade and names the evidence behind every load-bearing claim.
