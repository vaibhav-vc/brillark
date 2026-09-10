---
name: groupthink-detection
category: council
description: "Spot agreement that was assumed rather than earned."
output: "groupthink-check.md"
used_by:
  - council-devils-advocate
---

# Groupthink Detection

**Category:** `council` · **Output artifact:** `groupthink-check.md`

## What this skill does
Spot agreement that was assumed rather than earned.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-devils-advocate`.

## Procedure
1. Check whether any disconfirming test was defined before convergence.
2. Look for whether dissent was voiced and how it was handled.
3. Check whether the alternatives were genuinely explored or listed for form.
4. Ask who would be uncomfortable disagreeing and whether they were asked.
5. Report convergence without evidence as a finding in its own right.

## Output contract
Write `groupthink-check.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** groupthink-detection
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
- Presence of a disconfirming test verified
- Handling of dissent examined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
