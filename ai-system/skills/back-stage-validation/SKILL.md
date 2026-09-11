---
name: back-stage-validation
category: design
description: "Check the operation can actually deliver the designed experience."
output: "validation-record.md"
used_by:
  - service-designer
---

# Back Stage Validation

**Category:** `design` · **Output artifact:** `validation-record.md`

## What this skill does
Check the operation can actually deliver the designed experience.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `service-designer`.

## Procedure
1. Walk the blueprint with the people who will operate it.
2. Check each back-stage step against real capacity and skills.
3. Identify steps that only work when nothing else is happening.
4. Revise the front-stage promise where the back-stage cannot support it.
5. Get explicit agreement from the operating owner before launch.

## Output contract
Write `validation-record.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** back-stage-validation
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
- Walked with actual operators
- Front-stage promises revised to match capacity
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
