---
name: visual-hierarchy-design
category: design
description: "Make the order things are read match the order they matter."
output: "hierarchy-spec.md"
used_by:
  - visual-designer
---

# Visual Hierarchy Design

`design` · produces `hierarchy-spec.md` · used by `visual-designer`

Make the order things are read match the order they matter.

## Procedure
1. Decide what must be read first, second, and not at all.
2. Create the hierarchy with size, weight, and space before reaching for colour.
3. Check the hierarchy by squinting or blurring — the structure should survive.
4. Ensure the primary action is unambiguous on every screen.
5. Verify with real content, where competing elements actually compete.

## Output contract
`hierarchy-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Hierarchy holds when blurred
- Primary action unambiguous per screen
- The output states its confidence grade and names the evidence behind every load-bearing claim.
