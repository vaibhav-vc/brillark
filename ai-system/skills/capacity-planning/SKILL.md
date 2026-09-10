---
name: capacity-planning
category: engineering
description: "Ensure capacity exists before demand arrives."
output: "capacity-plan.md"
used_by:
  - performance-engineer
---

# Capacity Planning

**Category:** `engineering` · **Output artifact:** `capacity-plan.md`

## What this skill does
Ensure capacity exists before demand arrives.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `performance-engineer`.

## Procedure
1. Project demand from the growth forecast, not from current load.
2. Identify the resource that saturates first.
3. Determine lead time to add capacity for each resource.
4. Set the trigger point that accounts for that lead time.
5. Re-plan when the growth forecast changes materially.

## Output contract
Write `capacity-plan.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** capacity-planning
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
- Lead time built into the trigger point
- First saturating resource identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
