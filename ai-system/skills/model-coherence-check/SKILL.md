---
name: model-coherence-check
category: market
description: "Check that the parts of the business model actually fit together."
output: "coherence-check.md"
used_by:
  - business-model-canvas-agent
---

# Model Coherence Check

**Category:** `market` · **Output artifact:** `coherence-check.md`

## What this skill does
Check that the parts of the business model actually fit together.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-model-canvas-agent`.

## Procedure
1. Test whether the channel can reach the stated segment at the stated cost.
2. Test whether the price supports the cost structure and the sales motion.
3. Test whether the key resources exist or can be acquired in time.
4. Test whether the partners have an incentive to participate.
5. Report each incoherence with the two blocks that conflict.

## Output contract
Write `coherence-check.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** model-coherence-check
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
- Conflicts named as specific block pairs
- Motion-to-price fit tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
