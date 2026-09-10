---
name: fundraising-plan
category: finance
description: "Run a raise as a process rather than a scramble."
output: "fundraising-plan.md"
used_by:
  - fundraising-strategist
---

# Fundraising Plan

**Category:** `finance` · **Output artifact:** `fundraising-plan.md`

## What this skill does
Run a raise as a process rather than a scramble.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `fundraising-strategist`.

## Procedure
1. Define the amount, the milestone story, and the use of funds.
2. Build the target investor list by thesis fit and stage.
3. Prepare the data room before any outreach begins.
4. Sequence outreach to create parallel timelines rather than sequential rejections.
5. Prepare honest answers to the three hardest questions about the business.

## Output contract
Write `fundraising-plan.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** fundraising-plan
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
- Data room ready before outreach
- Hard questions answered honestly in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
