---
name: performance-regression-gating
category: engineering
description: "Stop performance regressions from reaching production."
output: "perf-gate.md"
used_by:
  - performance-engineer
---

# Performance Regression Gating

**Category:** `engineering` · **Output artifact:** `perf-gate.md`

## What this skill does
Stop performance regressions from reaching production.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `performance-engineer`.

## Procedure
1. Establish a stable baseline measurement environment.
2. Run the measurement on every change to critical paths.
3. Set the threshold above measurement noise to avoid false alarms.
4. Fail the build on a real regression and report the contributor.
5. Review the threshold when noise or hardware changes.

## Output contract
Write `perf-gate.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** performance-regression-gating
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
- Threshold set above measurement noise
- Build fails on genuine regressions
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
