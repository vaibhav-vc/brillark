---
name: job-mapping
category: market
description: "Map every step of the job, including the parts our product never touches."
output: "job-map.md"
used_by:
  - jtbd-analyst
---

# Job Mapping

**Category:** `market` · **Output artifact:** `job-map.md`

## What this skill does
Map every step of the job, including the parts our product never touches.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `jtbd-analyst`.

## Procedure
1. List the steps from the customer's first awareness of the need to their final outcome.
2. Mark friction, cost, and time at each step.
3. Identify the steps nobody currently serves well.
4. Check whether the biggest friction is inside or outside our product's scope.
5. Use the map to find where value is unclaimed.

## Output contract
Write `job-map.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** job-mapping
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
- Full job mapped beyond our product boundary
- Friction quantified per step
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
