---
name: counter-case-argument
category: council
description: "Argue against the leading option in full."
output: "counter-case.md"
used_by:
  - council-devils-advocate
---

# Counter Case Argument

**Category:** `council` · **Output artifact:** `counter-case.md`

## What this skill does
Argue against the leading option in full.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-devils-advocate`.

## Procedure
1. State the strongest version of the case against, without hedging.
2. Attack the evidence base as well as the reasoning.
3. Show what the recommendation assumes that may not hold.
4. Name what the room may be overlooking because it agrees.
5. Concede explicitly if the case survives; a rubber-stamp adversary is worthless.

## Output contract
Write `counter-case.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** counter-case-argument
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
- Argued without hedging
- Explicit concession when the case survives
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
