---
name: recoverability-classification
category: council
description: "Separate the failures you can come back from."
output: "recoverability-report.md"
used_by:
  - council-risk-and-failure-modes
---

# Recoverability Classification

**Category:** `council` · **Output artifact:** `recoverability-report.md`

## What this skill does
Separate the failures you can come back from.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-risk-and-failure-modes`.

## Procedure
1. Classify each failure as recoverable, costly but survivable, or terminal.
2. For recoverable failures, estimate the recovery cost and time.
3. For terminal failures, verify the classification rigorously.
4. Apply proportionate caution: terminal risks justify slower, safer choices.
5. Ensure no terminal risk is accepted without an explicit decision.

## Output contract
Write `recoverability-report.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** recoverability-classification
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
- Terminal classifications rigorously verified
- No terminal risk accepted implicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
