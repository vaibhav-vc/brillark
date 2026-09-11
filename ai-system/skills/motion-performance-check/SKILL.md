---
name: motion-performance-check
category: design
description: "Confirm the animation does not cost more than it gives."
output: "motion-performance.md"
used_by:
  - motion-designer
---

# Motion Performance Check

**Category:** `design` · **Output artifact:** `motion-performance.md`

## What this skill does
Confirm the animation does not cost more than it gives.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `motion-designer`.

## Procedure
1. Measure frame rate on the slowest supported device.
2. Prefer properties that do not force layout recalculation.
3. Check the animation's cost against the frontend performance budget.
4. Verify behaviour when animations overlap or interrupt.
5. Cut or simplify any animation that cannot hold frame rate.

## Output contract
Write `motion-performance.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** motion-performance-check
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
- Measured on the slowest supported device
- Within the frontend performance budget
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
