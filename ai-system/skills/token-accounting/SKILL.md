---
name: token-accounting
category: efficiency
description: "Know where the tokens actually go."
output: "token-report.md"
used_by:
  - token-efficiency-analyst
---

# Token Accounting

**Category:** `efficiency` · **Output artifact:** `token-report.md`

## What this skill does
Know where the tokens actually go.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `token-efficiency-analyst`.

## Procedure
1. Record tokens per run, split into system, context, retrieved content, and output.
2. Attribute to agent, skill, and workflow.
3. Compute cost per completed task, not per call.
4. Rank consumers and identify the top few that dominate.
5. Publish the breakdown so optimisation targets reality.

## Output contract
Write `token-report.md` into `workspace/<venture-id>/efficiency/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** token-accounting
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
- Cost measured per completed task
- Split by system, context, retrieval, and output
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `efficiency` category
- Measuring cost per call instead of cost per completed task.
- Demoting a model tier without checking the hardest cases.
- Trimming context by hand instead of fixing the rule that loaded it.
