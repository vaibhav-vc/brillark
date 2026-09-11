---
name: effect-size-reporting
category: improvement
description: "Report how much better, not just whether better."
output: "effect-report.md"
used_by:
  - ab-test-runner
---

# Effect Size Reporting

**Category:** `improvement` · **Output artifact:** `effect-report.md`

## What this skill does
Report how much better, not just whether better.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ab-test-runner`.

## Procedure
1. Report the absolute and relative change with the sample size.
2. Report variability, not just the central estimate.
3. State whether the effect is large enough to be worth the churn.
4. Report the cases that got worse alongside those that improved.
5. Avoid claiming significance the sample cannot support.

## Output contract
Write `effect-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** effect-size-reporting
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
- Cases that got worse reported too
- Practical worth stated, not just direction
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
