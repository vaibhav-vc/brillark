---
name: first-principles-decomposition
category: council
description: "Strip a plan to what is actually necessary."
output: "first-principles.md"
used_by:
  - council-first-principles
---

# First Principles Decomposition

**Category:** `council` · **Output artifact:** `first-principles.md`

## What this skill does
Strip a plan to what is actually necessary.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-first-principles`.

## Procedure
1. List every element of the plan and what it is meant to achieve.
2. Separate physical, legal, and economic necessities from conventions.
3. Ask of each convention what breaks if it is simply not done.
4. Reduce to the irreducible set of requirements.
5. Present the reduced set for reconstruction.

## Output contract
Write `first-principles.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** first-principles-decomposition
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
- Necessities separated from conventions
- Reduction to an irreducible set
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
