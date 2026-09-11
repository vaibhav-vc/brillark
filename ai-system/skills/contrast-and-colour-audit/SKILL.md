---
name: contrast-and-colour-audit
category: design
description: "Check colour works for everyone who has to read it."
output: "contrast-audit.md"
used_by:
  - accessibility-designer
---

# Contrast And Colour Audit

`design` · produces `contrast-audit.md` · used by `accessibility-designer`

Check colour works for everyone who has to read it.

## Procedure
1. Measure contrast for every text and meaningful non-text element.
2. Check against the required ratio for the actual size and weight.
3. Verify no meaning is carried by colour alone.
4. Simulate the common colour vision deficiencies.
5. Check the same in every theme and mode.

## Output contract
`contrast-audit.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Every meaningful element measured
- No meaning carried by colour alone
- The output states its confidence grade and names the evidence behind every load-bearing claim.
