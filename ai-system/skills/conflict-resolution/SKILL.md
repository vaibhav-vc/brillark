---
name: conflict-resolution
category: council
description: "Resolve a direct disagreement between critics."
output: "conflict-resolution.md"
used_by:
  - council-synthesis-arbiter
---

# Conflict Resolution

**Category:** `council` · **Output artifact:** `conflict-resolution.md`

## What this skill does
Resolve a direct disagreement between critics.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-synthesis-arbiter`.

## Procedure
1. State both positions precisely, in their own strongest form.
2. Identify whether they disagree on facts, values, or predictions.
3. For factual disagreements, find the evidence that settles it.
4. For predictive disagreements, define the observation that would settle it later.
5. Decide on evidence, never by averaging or splitting the difference.

## Output contract
Write `conflict-resolution.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** conflict-resolution
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
- Type of disagreement identified
- Decided on evidence, not by compromise
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
