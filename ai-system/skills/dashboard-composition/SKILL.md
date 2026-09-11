---
name: dashboard-composition
category: design
description: "Compose a dashboard that answers questions rather than displaying numbers."
output: "dashboard-spec.md"
used_by:
  - data-visualization-designer
---

# Dashboard Composition

`design` · produces `dashboard-spec.md` · used by `data-visualization-designer`

Compose a dashboard that answers questions rather than displaying numbers.

## Procedure
1. Name the question each panel answers, and delete panels with no question.
2. Order panels by the sequence someone would actually investigate.
3. Give the most important comparison the most space.
4. Keep density high enough to compare without scrolling between related panels.
5. Test with a real user doing a real investigation.

## Output contract
`dashboard-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Every panel answers a named question
- Ordering follows real investigation sequence
- The output states its confidence grade and names the evidence behind every load-bearing claim.
