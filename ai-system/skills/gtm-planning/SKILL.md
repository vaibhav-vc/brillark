---
name: gtm-planning
category: gtm
description: "Decide how the product reaches customers and in what order."
output: "gtm-plan.md"
used_by:
  - business-head
  - gtm-strategist
---

# Gtm Planning

**Category:** `gtm` · **Output artifact:** `gtm-plan.md`

## What this skill does
Decide how the product reaches customers and in what order.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-head`, `gtm-strategist`.

## Procedure
1. Choose the motion that matches the price point and the buying process.
2. Select one beachhead segment and state why it is first.
3. Choose at most three channels to test, each with a budget and a kill criterion.
4. Sequence the launch: friendly users, design partners, then public.
5. Define the metrics that would justify scaling each channel.

## Output contract
Write `gtm-plan.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** gtm-planning
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
- Motion matches price point
- Every channel has a kill criterion
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
