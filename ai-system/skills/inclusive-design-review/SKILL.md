---
name: inclusive-design-review
category: design
description: "Review the design for who it excludes before it is built."
output: "inclusive-review.md"
used_by:
  - accessibility-designer
---

# Inclusive Design Review

`design` · produces `inclusive-review.md` · used by `accessibility-designer`

Review the design for who it excludes before it is built.

## Procedure
1. List the ways people might differ: ability, device, connection, language, literacy, context.
2. Walk the flow as each, and note where it fails.
3. Check assumptions about steady hands, full attention, and fast connections.
4. Prioritise findings by how many are excluded and how completely.
5. Propose the change that removes the exclusion, not a parallel path.

## Output contract
`inclusive-review.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Exclusions identified before build
- Fixes remove exclusion rather than adding a side path
- The output states its confidence grade and names the evidence behind every load-bearing claim.
