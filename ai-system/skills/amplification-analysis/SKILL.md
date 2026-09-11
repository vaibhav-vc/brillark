---
name: amplification-analysis
category: gtm
description: "Determine whether a loop actually compounds."
output: "amplification-analysis.md"
used_by:
  - growth-loop-designer
---

# Amplification Analysis

`gtm` · produces `amplification-analysis.md` · used by `growth-loop-designer`

Determine whether a loop actually compounds.

## Procedure
1. Compute how many new inputs each output generates.
2. Measure the cycle time from input to new input.
3. Project growth from amplification and cycle time together.
4. Identify whether amplification is stable, decaying, or saturating.
5. State the level at which the loop stalls and why.

## Output contract
`amplification-analysis.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Cycle time included in the projection
- Saturation point identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
