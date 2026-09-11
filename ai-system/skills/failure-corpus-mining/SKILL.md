---
name: failure-corpus-mining
category: improvement
description: "Gather everything that went wrong into one place worth analysing."
output: "failure-corpus.md"
used_by:
  - failure-miner
---

# Failure Corpus Mining

**Category:** `improvement` · **Output artifact:** `failure-corpus.md`

## What this skill does
Gather everything that went wrong into one place worth analysing.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `failure-miner`.

## Procedure
1. Collect from incidents, rejected handoffs, Council blockers, escaped defects, and retrospectives.
2. Include the failures nobody filed formally, found in escalations and rework.
3. Normalise into a common record so they can be compared.
4. Record the cost and the stage at which each was caught.
5. Keep the corpus across cycles so patterns become visible.

## Output contract
Write `failure-corpus.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** failure-corpus-mining
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
- Informal failures included, not just filed ones
- Catch stage recorded for each failure
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
