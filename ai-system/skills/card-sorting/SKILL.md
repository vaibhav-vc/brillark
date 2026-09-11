---
name: card-sorting
category: design
description: "Learn how users group and name things, rather than imposing the internal structure."
output: "card-sort-results.md"
used_by:
  - information-architect
---

# Card Sorting

**Category:** `design` · **Output artifact:** `card-sort-results.md`

## What this skill does
Learn how users group and name things, rather than imposing the internal structure.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `information-architect`.

## Procedure
1. Choose open sorting to discover groupings, closed to validate a proposed structure.
2. Use the real item labels, not idealised ones.
3. Run with enough participants that agreement patterns are visible.
4. Analyse for items that participants placed inconsistently — those are the naming problems.
5. Report the groupings users produced, including the ones that surprised you.

## Output contract
Write `card-sort-results.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** card-sorting
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
- Real labels used, not idealised ones
- Inconsistently placed items reported as naming problems
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
