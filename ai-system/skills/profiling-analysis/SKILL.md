---
name: profiling-analysis
category: engineering
description: "Find where time and resources actually go."
output: "profile-report.md"
used_by:
  - performance-engineer
---

# Profiling Analysis

**Category:** `engineering` · **Output artifact:** `profile-report.md`

## What this skill does
Find where time and resources actually go.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `performance-engineer`.

## Procedure
1. Reproduce the slow case reliably before profiling.
2. Profile the real workload rather than a synthetic loop.
3. Identify the largest contributor, not the most interesting one.
4. Verify the hypothesis by changing one thing and re-measuring.
5. Stop when the budget is met; further optimisation is unpaid work.

## Output contract
Write `profile-report.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** profiling-analysis
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
- Real workload profiled
- Hypothesis verified by re-measurement
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
