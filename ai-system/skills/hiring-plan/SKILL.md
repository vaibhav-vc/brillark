---
name: hiring-plan
category: people
description: "Sequence hiring against the constraint that is actually binding."
output: "hiring-plan.md"
used_by:
  - chro-agent
---

# Hiring Plan

**Category:** `people` · **Output artifact:** `hiring-plan.md`

## What this skill does
Sequence hiring against the constraint that is actually binding.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chro-agent`.

## Procedure
1. Identify the binding constraint on output today.
2. Determine whether hiring is the right fix, or whether process or tooling is.
3. Sequence roles by which constraint each removes.
4. Check the plan against the financial model and runway.
5. Define the trigger for each hire rather than fixed dates.

## Output contract
Write `hiring-plan.md` into `workspace/<venture-id>/people/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** hiring-plan
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
- Binding constraint identified first
- Plan reconciled with the financial model
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `people` category
- Writing a job advertisement before writing the outcomes the role must produce.
- Assessing candidates on different evidence and calling it judgement.
- Hiring to relieve a bottleneck that process or tooling would fix faster.
