---
name: mvp-scoping
category: product
description: "Find the smallest build that answers the riskiest question."
output: "mvp-scope.md"
used_by:
  - engineering-head
  - mvp-scoper
---

# Mvp Scoping

**Category:** `product` · **Output artifact:** `mvp-scope.md`

## What this skill does
Find the smallest build that answers the riskiest question.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `engineering-head`, `mvp-scoper`.

## Procedure
1. State the riskiest assumption the venture depends on.
2. Design the smallest artifact that could disprove it.
3. Cut everything that does not change what we learn.
4. Prefer a manual step over building automation before demand is proven.
5. Estimate time to first real user and treat it as the binding constraint.

## Output contract
Write `mvp-scope.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** mvp-scoping
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
- Scope tests the riskiest assumption
- Time to first user treated as the constraint
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
