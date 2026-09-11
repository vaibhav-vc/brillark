---
name: cache-order-optimisation
category: efficiency
description: "Order the prompt so the stable part stays cacheable."
output: "cache-order.md"
used_by:
  - token-efficiency-analyst
---

# CAChe Order Optimisation

**Category:** `efficiency` · **Output artifact:** `cache-order.md`

## What this skill does
Order the prompt so the stable part stays cacheable.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `token-efficiency-analyst`.

## Procedure
1. Place the most stable content first: base prompt, tier prompt, agent charter.
2. Place skill definitions next, since they change per task but not per turn.
3. Place the context package and the task last, where variability belongs.
4. Never interleave variable content into the stable prefix.
5. Verify cache reuse after any reordering.

## Output contract
Write `cache-order.md` into `workspace/<venture-id>/efficiency/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cache-order-optimisation
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
- No variable content inside the stable prefix
- Cache reuse verified after reordering
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `efficiency` category
- Measuring cost per call instead of cost per completed task.
- Demoting a model tier without checking the hardest cases.
- Trimming context by hand instead of fixing the rule that loaded it.
