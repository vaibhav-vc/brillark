---
name: recurring-flaw-analysis
category: council
description: "Find the mistakes this organisation keeps making."
output: "recurring-flaws.md"
used_by:
  - council-director
---

# Recurring Flaw Analysis

**Category:** `council` · **Output artifact:** `recurring-flaws.md`

## What this skill does
Find the mistakes this organisation keeps making.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-director`.

## Procedure
1. Group findings across reviews by underlying flaw type.
2. Identify flaws appearing in three or more reviews.
3. Trace each to the agent, skill, or process that permits it.
4. Convert into a guardrail or checklist change at the source.
5. Track whether the flaw rate falls in subsequent reviews.

## Output contract
Write `recurring-flaws.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** recurring-flaw-analysis
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
- Traced to a specific artifact that permits it
- Recurrence rate tracked afterwards
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
