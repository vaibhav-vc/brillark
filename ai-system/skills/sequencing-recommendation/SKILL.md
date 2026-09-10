---
name: sequencing-recommendation
category: council
description: "Recommend an order rather than a wish list."
output: "sequence-plan.md"
used_by:
  - council-expansion-scout
---

# Sequencing Recommendation

**Category:** `council` · **Output artifact:** `sequence-plan.md`

## What this skill does
Recommend an order rather than a wish list.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-expansion-scout`.

## Procedure
1. Identify the prerequisites linking the options.
2. Place options that unlock others earlier.
3. Check capacity — a sequence that requires doing everything at once is not a sequence.
4. State what must be true before each step begins.
5. Define the checkpoint between steps.

## Output contract
Write `sequence-plan.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** sequencing-recommendation
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
- Prerequisites drive the order
- Capacity checked against the sequence
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
