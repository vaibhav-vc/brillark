---
name: layout-composition
category: design
description: "Arrange the screen so the structure is obvious without explanation."
output: "layout-spec.md"
used_by:
  - visual-designer
---

# Layout Composition

`design` · produces `layout-spec.md` · used by `visual-designer`

Arrange the screen so the structure is obvious without explanation.

## Procedure
1. Establish the grid and the spacing scale, and use them consistently.
2. Group related elements by proximity before adding borders or boxes.
3. Give the primary content the space its importance deserves.
4. Design the dense case with real data volumes, not the showcase case.
5. Check every breakpoint, especially the narrowest supported width.

## Output contract
`layout-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Proximity used before decoration
- Dense realistic case designed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
