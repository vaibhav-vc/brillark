---
name: chart-form-selection
category: design
description: "Pick the chart form from the comparison being made."
output: "chart-spec.md"
used_by:
  - data-visualization-designer
---

# Chart Form Selection

`design` · produces `chart-spec.md` · used by `data-visualization-designer`

Pick the chart form from the comparison being made.

## Procedure
1. State the question and the comparison: over time, between categories, part of whole, or relationship.
2. Choose the form that encodes that comparison most directly.
3. Prefer position over area, and area over colour, for quantitative comparison.
4. Reject forms chosen for novelty rather than for the comparison.
5. Check the form still works at the real number of categories.

## Output contract
`chart-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Form follows the stated comparison
- Tested at the real category count
- The output states its confidence grade and names the evidence behind every load-bearing claim.
