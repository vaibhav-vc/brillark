---
name: uncertainty-visualisation
category: design
description: "Show how confident the numbers are."
output: "uncertainty-spec.md"
used_by:
  - data-visualization-designer
---

# Uncertainty Visualisation

`design` · produces `uncertainty-spec.md` · used by `data-visualization-designer`

Show how confident the numbers are.

## Procedure
1. Identify where uncertainty exists: sampling, estimation, or incomplete data.
2. Show intervals or ranges rather than a single confident line.
3. Mark incomplete periods so partial data is not read as a decline.
4. Distinguish measured from forecast values visually.
5. State the sample size where it affects interpretation.

## Output contract
`uncertainty-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Incomplete periods marked
- Forecast visually distinguished from measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.
