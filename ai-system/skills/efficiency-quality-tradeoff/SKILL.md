---
name: efficiency-quality-tradeoff
category: efficiency
description: "Decide whether a saving is worth it."
output: "tradeoff-record.md"
used_by:
  - token-efficiency-analyst
---

# Efficiency Quality Tradeoff

**Category:** `efficiency` · **Output artifact:** `tradeoff-record.md`

## What this skill does
Decide whether a saving is worth it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `token-efficiency-analyst`.

## Procedure
1. Measure the saving per completed task, not per call.
2. Measure quality on the golden cases before and after.
3. Reject any saving that moves quality below the rubric floor.
4. Account for the cost of extra retries the change causes.
5. Record the trade-off and the decision.

## Output contract
Write `tradeoff-record.md` into `workspace/<venture-id>/efficiency/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** efficiency-quality-tradeoff
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
- Retry cost accounted for
- Rubric floor never crossed for savings
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `efficiency` category
- Measuring cost per call instead of cost per completed task.
- Demoting a model tier without checking the hardest cases.
- Trimming context by hand instead of fixing the rule that loaded it.
