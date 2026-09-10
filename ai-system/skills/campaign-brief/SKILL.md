---
name: campaign-brief
category: gtm
description: "Define a campaign tightly enough that it can be judged afterwards."
output: "campaign-brief.md"
used_by:
  - cmo-agent
---

# Campaign Brief

**Category:** `gtm` · **Output artifact:** `campaign-brief.md`

## What this skill does
Define a campaign tightly enough that it can be judged afterwards.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cmo-agent`.

## Procedure
1. State the audience, the single message, and the action requested.
2. Set the budget, the duration, and the success metric.
3. Define attribution before launch.
4. List the assets required and their owners.
5. State the kill criterion and the review date.

## Output contract
Write `campaign-brief.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** campaign-brief
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
- One message, one requested action
- Success metric and kill criterion defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
