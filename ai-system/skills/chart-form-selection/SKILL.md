---
name: chart-form-selection
category: design
description: "Pick the chart form from the comparison being made."
output: "chart-spec.md"
used_by:
  - data-visualization-designer
---

# Chart Form Selection

**Category:** `design` · **Output artifact:** `chart-spec.md`

## What this skill does
Pick the chart form from the comparison being made.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-visualization-designer`.

## Procedure
1. State the question and the comparison: over time, between categories, part of whole, or relationship.
2. Choose the form that encodes that comparison most directly.
3. Prefer position over area, and area over colour, for quantitative comparison.
4. Reject forms chosen for novelty rather than for the comparison.
5. Check the form still works at the real number of categories.

## Output contract
Write `chart-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** chart-form-selection
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Form follows the stated comparison
- Tested at the real category count
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
