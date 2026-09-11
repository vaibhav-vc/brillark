---
name: typography-system
category: design
description: "Set type so the product can be read comfortably."
output: "type-system.md"
used_by:
  - visual-designer
---

# Typography System

`design` · produces `type-system.md` · used by `visual-designer`

Set type so the product can be read comfortably.

## Procedure
1. Define a scale with enough steps to build hierarchy and few enough to stay consistent.
2. Set line length and line height for reading, not for fitting.
3. Check the smallest text against contrast and size requirements.
4. Define styles semantically — body, caption, heading — not by pixel value.
5. Test with the longest realistic string in every supported language.

## Output contract
`type-system.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Scale defined semantically
- Tested with longest realistic strings
- The output states its confidence grade and names the evidence behind every load-bearing claim.
