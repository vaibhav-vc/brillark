---
name: council-debate-facilitation
category: council
description: "Run a structured debate that produces a decision."
output: "debate-record.md"
used_by:
  - council-director
---

# Council Debate Facilitation

**Category:** `council` · **Output artifact:** `debate-record.md`

## What this skill does
Run a structured debate that produces a decision.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-director`.

## Procedure
1. Accept the submission only with a stated decision, evidence, and deadline.
2. Assign roles, including at least one critic arguing in favour.
3. Run rounds: claim, challenge, evidence, rebuttal.
4. Cut off arguments that cannot be made falsifiable.
5. Close on time with a verdict, never with an adjournment.

## Output contract
Write `debate-record.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** council-debate-facilitation
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
- Someone assigned to argue in favour
- Closed on time with a verdict
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
