---
name: steelman-construction
category: council
description: "Rebuild a rejected option at its strongest before judging it."
output: "steelman.md"
used_by:
  - council-devils-advocate
  - council-director
---

# Steelman Construction

**Category:** `council` · **Output artifact:** `steelman.md`

## What this skill does
Rebuild a rejected option at its strongest before judging it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-devils-advocate`, `council-director`.

## Procedure
1. State the rejected option in the form its best advocate would use.
2. Identify the conditions under which it would be right.
3. Fix the weaknesses that were incidental rather than fundamental.
4. Compare the strengthened version against the recommendation.
5. State honestly whether the rejection still holds.

## Output contract
Write `steelman.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** steelman-construction
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
- Option restated at its strongest
- Rejection re-tested against the improved version
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
