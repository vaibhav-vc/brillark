---
name: riskiest-assumption-testing
category: product
description: "Test the belief that would hurt most if wrong, first."
output: "rat-test.md"
used_by:
  - mvp-scoper
---

# Riskiest Assumption Testing

**Category:** `product` · **Output artifact:** `rat-test.md`

## What this skill does
Test the belief that would hurt most if wrong, first.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `mvp-scoper`.

## Procedure
1. Rank assumptions by how much of the plan collapses if each is false.
2. Take the top one and define what evidence would disprove it.
3. Design the cheapest test that could produce that evidence.
4. Set the decision threshold before running it.
5. Act on the result, including when it is inconvenient.

## Output contract
Write `rat-test.md` into `workspace/<venture-id>/product/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** riskiest-assumption-testing
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
- Threshold set before the test runs
- Result acted on regardless of convenience
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `product` category
- Writing a requirement that starts with a solution instead of an evidenced problem.
- Shipping without defining, in advance, what would show it worked.
- Treating the roadmap as a promise rather than a current best sequence.
