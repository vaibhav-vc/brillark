---
name: navigation-design
category: design
description: "Design how people move through the product and know where they are."
output: "navigation-spec.md"
used_by:
  - information-architect
---

# Navigation Design

`design` · produces `navigation-spec.md` · used by `information-architect`

Design how people move through the product and know where they are.

## Procedure
1. Design for the paths users actually take, which usually begin with search.
2. Keep the primary navigation to what most users need most often.
3. Make the current location obvious at every depth.
4. Provide a way back and a way up that always works.
5. Validate with tree testing before committing the structure.

## Output contract
`navigation-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Primary navigation limited to common needs
- Structure validated by tree test
- The output states its confidence grade and names the evidence behind every load-bearing claim.
