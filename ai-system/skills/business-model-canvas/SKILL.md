---
name: business-model-canvas
category: market
description: "Describe the whole business model on one page with evidence per block."
output: "business-model-canvas.md"
used_by:
  - business-head
  - business-model-canvas-agent
---

# Business Model Canvas

**Category:** `market` · **Output artifact:** `business-model-canvas.md`

## What this skill does
Describe the whole business model on one page with evidence per block.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-head`, `business-model-canvas-agent`.

## Procedure
1. Fill all nine blocks: segments, value proposition, channels, relationships, revenue, resources, activities, partners, costs.
2. Tag each block as measured, sourced, or assumed.
3. Check that the revenue model fits the segment, the channel, and the cost structure.
4. Identify the riskiest block and the test that would validate it.
5. Log what changed since the last version and why.

## Output contract
Write `business-model-canvas.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** business-model-canvas
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
- Every block carries an evidence tag
- Riskiest block identified with a test
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
