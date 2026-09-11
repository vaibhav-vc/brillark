---
name: improvement-backlog-ranking
category: improvement
description: "Decide what to improve next."
output: "improvement-backlog.md"
used_by:
  - improvement-head
---

# Improvement Backlog Ranking

**Category:** `improvement` · **Output artifact:** `improvement-backlog.md`

## What this skill does
Decide what to improve next.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `improvement-head`.

## Procedure
1. Score each candidate by cost imposed, probability of fix, and effort.
2. Prefer systemic causes over individual symptoms.
3. Prefer changes that can be measured over those that cannot.
4. Fund fewer improvements properly rather than many partially.
5. Publish the ranking and the line.

## Output contract
Write `improvement-backlog.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** improvement-backlog-ranking
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
- Measurable changes preferred
- Systemic causes ranked above symptoms
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
