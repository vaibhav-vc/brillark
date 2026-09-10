---
name: onboarding-plan
category: people
description: "Make a new team member productive in their first week."
output: "onboarding-plan.md"
used_by:
  - chro-agent
---

# Onboarding Plan

**Category:** `people` · **Output artifact:** `onboarding-plan.md`

## What this skill does
Make a new team member productive in their first week.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chro-agent`.

## Procedure
1. Define the contribution they should make in week one.
2. Sequence context: mission, customers, system, then codebase or process.
3. Assign an owner responsible for their first two weeks.
4. Give them a real, small piece of work immediately.
5. Collect their questions and fix the documentation they exposed.

## Output contract
Write `onboarding-plan.md` into `workspace/<venture-id>/people/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** onboarding-plan
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
- Week-one contribution defined
- Documentation improved from their questions
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `people` category
- Writing a job advertisement before writing the outcomes the role must produce.
- Assessing candidates on different evidence and calling it judgement.
- Hiring to relieve a bottleneck that process or tooling would fix faster.
