---
name: model-change-logging
category: market
description: "Record how the business model evolved and what caused each change."
output: "model-change-log.md"
used_by:
  - business-model-canvas-agent
---

# Model Change Logging

**Category:** `market` · **Output artifact:** `model-change-log.md`

## What this skill does
Record how the business model evolved and what caused each change.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-model-canvas-agent`.

## Procedure
1. Record the previous state, the new state, and the date.
2. State the evidence or event that triggered the change.
3. Note which blocks were affected downstream.
4. Record what the change invalidates in existing plans.
5. Keep the history readable so the pattern of pivots is visible.

## Output contract
Write `model-change-log.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** model-change-logging
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
- Trigger evidence recorded per change
- Downstream invalidations noted
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
