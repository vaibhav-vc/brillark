---
name: red-team-attack
category: council
description: "Attack a plan the way a competitor or bad actor would."
output: "red-team-report.md"
used_by:
  - council-red-team
---

# Red Team Attack

**Category:** `council` · **Output artifact:** `red-team-report.md`

## What this skill does
Attack a plan the way a competitor or bad actor would.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-red-team`.

## Procedure
1. Attack the plan's strongest claim first; weak points are already known.
2. Model three attackers: a funded competitor, an abusive user, and an indifferent market.
3. Write each attack as a concrete sequence of events, not an adjective.
4. Rank by damage multiplied by plausibility and drop what cannot be made concrete.
5. Propose the cheapest defence for each surviving attack.

## Output contract
Write `red-team-report.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** red-team-attack
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
- Attacks written as concrete sequences
- A defence proposed for each surviving attack
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
