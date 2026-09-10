---
name: simplification-challenge
category: council
description: "Ask what could be removed entirely."
output: "simplification-report.md"
used_by:
  - council-first-principles
---

# Simplification Challenge

**Category:** `council` · **Output artifact:** `simplification-report.md`

## What this skill does
Ask what could be removed entirely.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-first-principles`.

## Procedure
1. List the components, steps, and features in the plan.
2. For each, ask what happens if it is simply removed.
3. Identify elements retained out of habit or completeness.
4. Quantify the cost each element adds.
5. Recommend removals with the risk of each stated.

## Output contract
Write `simplification-report.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** simplification-challenge
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
- Removal tested for every element
- Risk of each removal stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
