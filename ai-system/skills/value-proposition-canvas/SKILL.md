---
name: value-proposition-canvas
category: market
description: "Connect specific customer pains and gains to specific product capabilities."
output: "value-proposition.md"
used_by:
  - value-proposition-designer
---

# Value Proposition Canvas

**Category:** `market` · **Output artifact:** `value-proposition.md`

## What this skill does
Connect specific customer pains and gains to specific product capabilities.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `value-proposition-designer`.

## Procedure
1. List the customer's jobs, pains, and gains from evidence.
2. List the product's pain relievers and gain creators.
3. Map each reliever to a named, evidenced pain; unmatched capabilities are scope to cut.
4. Identify pains with no reliever — these are the roadmap.
5. Rate the fit and state where it is weakest.

## Output contract
Write `value-proposition.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** value-proposition-canvas
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
- Unmatched capabilities identified as cuttable
- Unrelieved pains routed to the roadmap
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
