---
name: co-marketing-planning
category: gtm
description: "Plan joint activity that both parties will actually resource."
output: "co-marketing-plan.md"
used_by:
  - partnership-bd-agent
---

# Co Marketing Planning

**Category:** `gtm` · **Output artifact:** `co-marketing-plan.md`

## What this skill does
Plan joint activity that both parties will actually resource.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `partnership-bd-agent`.

## Procedure
1. Agree the shared audience and the single joint message.
2. Define what each party contributes, with named owners and dates.
3. Set the metrics both parties will judge success on.
4. Agree lead handling and attribution before launch.
5. Schedule the review and the decision to continue or stop.

## Output contract
Write `co-marketing-plan.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** co-marketing-planning
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
- Named owners on both sides
- Attribution agreed before launch
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
