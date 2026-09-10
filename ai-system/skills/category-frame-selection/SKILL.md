---
name: category-frame-selection
category: gtm
description: "Choose the mental category that sets customer expectations."
output: "category-frame.md"
used_by:
  - positioning-messaging-agent
---

# Category Frame Selection

**Category:** `gtm` · **Output artifact:** `category-frame.md`

## What this skill does
Choose the mental category that sets customer expectations.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `positioning-messaging-agent`.

## Procedure
1. List the categories a buyer might file this under.
2. For each, note the expectations, the comparison set, and the budget line it unlocks.
3. Assess whether we can win the comparison inside that frame.
4. Choose the frame where we compare best and the budget exists.
5. State the expectations the frame creates and confirm we can meet them.

## Output contract
Write `category-frame.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** category-frame-selection
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
- Budget line identified per frame
- Created expectations verified as meetable
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
