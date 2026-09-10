---
name: from-scratch-reconstruction
category: council
description: "Rebuild the plan from the irreducible requirements alone."
output: "reconstruction.md"
used_by:
  - council-first-principles
---

# From Scratch Reconstruction

**Category:** `council` · **Output artifact:** `reconstruction.md`

## What this skill does
Rebuild the plan from the irreducible requirements alone.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-first-principles`.

## Procedure
1. Start from the reduced requirement set, ignoring the existing plan.
2. Design the simplest approach that satisfies all of them.
3. Compare against the proposal and enumerate every difference.
4. For each difference, ask which version is justified.
5. Recommend adopting the differences that survive scrutiny.

## Output contract
Write `reconstruction.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** from-scratch-reconstruction
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
- Built without reference to the existing plan
- Every difference examined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
