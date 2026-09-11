---
name: step-concreteness-review
category: improvement
description: "Check every step can actually be followed."
output: "concreteness-review.md"
used_by:
  - skill-refiner
---

# Step Concreteness Review

**Category:** `improvement` · **Output artifact:** `concreteness-review.md`

## What this skill does
Check every step can actually be followed.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `skill-refiner`.

## Procedure
1. Read each step and ask what you would literally do.
2. Flag steps that state a principle rather than an action.
3. Flag steps whose completion cannot be checked.
4. Rewrite flagged steps as observable actions.
5. Verify a different agent can follow the result without asking.

## Output contract
Write `concreteness-review.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** step-concreteness-review
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
- Principles disguised as steps flagged
- Verified by someone who did not write it
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
