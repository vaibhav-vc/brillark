---
name: improvement-queue-ranking
category: improvement
description: "Rank candidate fixes by what they are actually worth."
output: "improvement-queue.md"
used_by:
  - agent-performance-analyst
---

# Improvement Queue Ranking

**Category:** `improvement` · **Output artifact:** `improvement-queue.md`

## What this skill does
Rank candidate fixes by what they are actually worth.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `agent-performance-analyst`.

## Procedure
1. Estimate the cost each problem imposes per cycle.
2. Estimate the probability a proposed fix works.
3. Estimate the effort and the risk of the fix.
4. Rank by expected value, not by how recently it was raised.
5. Publish the queue and what sits below the line.

## Output contract
Write `improvement-queue.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** improvement-queue-ranking
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
- Ranked by expected value, not recency
- Below-the-line items published
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
