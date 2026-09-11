---
name: encoding-honesty-review
category: design
description: "Check the chart does not mislead."
output: "encoding-review.md"
used_by:
  - data-visualization-designer
---

# Encoding Honesty Review

`design` · produces `encoding-review.md` · used by `data-visualization-designer`

Check the chart does not mislead.

## Procedure
1. Verify bar charts start at zero and any truncation is impossible to miss.
2. Label non-linear scales explicitly.
3. Check aspect ratio is not exaggerating or flattening a trend.
4. Verify the axis covers the data range without cherry-picking.
5. Check that area and size encodings scale by area, not by radius.

## Output contract
`encoding-review.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Baselines and scales verified
- Aspect ratio checked for exaggeration
- The output states its confidence grade and names the evidence behind every load-bearing claim.
