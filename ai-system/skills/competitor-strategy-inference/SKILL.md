---
name: competitor-strategy-inference
category: market
description: "Work out what a competitor is trying to do from observable signals."
output: "competitor-strategy.md"
used_by:
  - competitor-intel-analyst
---

# Competitor Strategy Inference

**Category:** `market` · **Output artifact:** `competitor-strategy.md`

## What this skill does
Work out what a competitor is trying to do from observable signals.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `competitor-intel-analyst`.

## Procedure
1. Track hiring, pricing changes, positioning shifts, and product releases.
2. Infer the segment and motion they are optimising for.
3. Identify their constraint — what they cannot easily do.
4. Predict their next two moves and state your confidence.
5. Set watch indicators that would confirm or refute the inference.

## Output contract
Write `competitor-strategy.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** competitor-strategy-inference
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
- Inference supported by observable signals
- Watch indicators defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
