---
name: alternative-revival
category: council
description: "Check whether a discarded option deserves reconsideration."
output: "alternative-review.md"
used_by:
  - council-devils-advocate
---

# Alternative Revival

**Category:** `council` · **Output artifact:** `alternative-review.md`

## What this skill does
Check whether a discarded option deserves reconsideration.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-devils-advocate`.

## Procedure
1. Review why each alternative was rejected and when.
2. Check whether the rejecting condition still holds today.
3. Identify alternatives rejected for reasons that have since changed.
4. Re-score the survivors against the current recommendation.
5. Recommend revival only where the evidence genuinely changed.

## Output contract
Write `alternative-review.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** alternative-revival
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
- Rejection reasons re-tested against current facts
- Revival justified by changed evidence
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
