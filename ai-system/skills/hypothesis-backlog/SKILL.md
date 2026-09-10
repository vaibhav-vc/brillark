---
name: hypothesis-backlog
category: market
description: "Keep a ranked list of what we believe and how we will test it."
output: "hypothesis-backlog.md"
used_by:
  - business-head
---

# Hypothesis Backlog

**Category:** `market` · **Output artifact:** `hypothesis-backlog.md`

## What this skill does
Keep a ranked list of what we believe and how we will test it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-head`.

## Procedure
1. Write each belief as a falsifiable statement with a threshold.
2. Rank by how much of the plan depends on it and how uncertain it is.
3. Define the cheapest test that could disprove it.
4. Assign an owner and a by-when.
5. Move results into the validated-learning log, including failures.

## Output contract
Write `hypothesis-backlog.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** hypothesis-backlog
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
- Beliefs stated falsifiably with thresholds
- Ranked by dependency and uncertainty
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
