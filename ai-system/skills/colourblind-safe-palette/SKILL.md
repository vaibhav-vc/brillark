---
name: colourblind-safe-palette
category: design
description: "Build a palette that works for everyone."
output: "palette.md"
used_by:
  - data-visualization-designer
---

# Colourblind Safe Palette

`design` · produces `palette.md` · used by `data-visualization-designer`

Build a palette that works for everyone.

## Procedure
1. Select hues that remain distinguishable under the common deficiencies.
2. Vary lightness as well as hue so greyscale still separates the series.
3. Limit categorical series to a number people can actually match to a legend.
4. Add a redundant encoding — shape, pattern, or direct label.
5. Verify with simulation and in greyscale.

## Output contract
`palette.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Series separable in greyscale
- Redundant encoding beyond colour
- The output states its confidence grade and names the evidence behind every load-bearing claim.
