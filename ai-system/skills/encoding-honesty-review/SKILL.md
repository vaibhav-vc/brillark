---
name: encoding-honesty-review
category: design
description: "Check the chart does not mislead."
output: "encoding-review.md"
used_by:
  - data-visualization-designer
---

# Encoding Honesty Review

**Category:** `design` · **Output artifact:** `encoding-review.md`

## What this skill does
Check the chart does not mislead.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-visualization-designer`.

## Procedure
1. Verify bar charts start at zero and any truncation is impossible to miss.
2. Label non-linear scales explicitly.
3. Check aspect ratio is not exaggerating or flattening a trend.
4. Verify the axis covers the data range without cherry-picking.
5. Check that area and size encodings scale by area, not by radius.

## Output contract
Write `encoding-review.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** encoding-honesty-review
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
- Baselines and scales verified
- Aspect ratio checked for exaggeration
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
