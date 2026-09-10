---
name: org-backlog-triage
category: orchestration
description: "Keep one prioritised list for the whole organisation so domains cannot each claim top priority."
output: "org-backlog.md"
used_by:
  - director
---

# Org Backlog Triage

**Category:** `orchestration` · **Output artifact:** `org-backlog.md`

## What this skill does
Keep one prioritised list for the whole organisation so domains cannot each claim top priority.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `director`.

## Procedure
1. Merge domain backlogs into one list with a single ranking.
2. Score each item by strategic value, evidence strength, and cost to learn.
3. Force a strict order — ties are a refusal to decide.
4. Cut items below the funding line explicitly rather than leaving them ambiguous.
5. Publish the line and what sits just below it.

## Output contract
Write `org-backlog.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** org-backlog-triage
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
- Strict order with no ties
- Funding line published
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
