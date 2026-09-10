---
name: abuse-case-analysis
category: council
description: "Find how the product will be misused."
output: "abuse-cases.md"
used_by:
  - council-red-team
---

# Abuse Case Analysis

**Category:** `council` · **Output artifact:** `abuse-cases.md`

## What this skill does
Find how the product will be misused.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-red-team`.

## Procedure
1. Enumerate the actors who benefit from misusing the system.
2. For each, describe the specific misuse and what it gains them.
3. Assess harm to other users, to third parties, and to the company.
4. Check whether the misuse scales cheaply — that is what makes it serious.
5. Propose detection and prevention for each, with the cost of each control.

## Output contract
Write `abuse-cases.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** abuse-case-analysis
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
- Misuse scalability assessed
- Detection proposed alongside prevention
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
