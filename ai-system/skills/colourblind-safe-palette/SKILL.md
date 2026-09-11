---
name: colourblind-safe-palette
category: design
description: "Build a palette that works for everyone."
output: "palette.md"
used_by:
  - data-visualization-designer
---

# Colourblind Safe Palette

**Category:** `design` · **Output artifact:** `palette.md`

## What this skill does
Build a palette that works for everyone.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-visualization-designer`.

## Procedure
1. Select hues that remain distinguishable under the common deficiencies.
2. Vary lightness as well as hue so greyscale still separates the series.
3. Limit categorical series to a number people can actually match to a legend.
4. Add a redundant encoding — shape, pattern, or direct label.
5. Verify with simulation and in greyscale.

## Output contract
Write `palette.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** colourblind-safe-palette
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
- Series separable in greyscale
- Redundant encoding beyond colour
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
