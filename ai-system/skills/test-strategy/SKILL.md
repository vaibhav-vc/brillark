---
name: test-strategy
category: engineering
description: "Decide what to test, at what level, and why."
output: "test-strategy.md"
used_by:
  - engineering-head
  - qa-test-strategist
---

# Test Strategy

**Category:** `engineering` · **Output artifact:** `test-strategy.md`

## What this skill does
Decide what to test, at what level, and why.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `engineering-head`, `qa-test-strategist`.

## Procedure
1. Identify the areas where failure would be most costly.
2. Assign each risk to the cheapest level that can catch it.
3. Define what will deliberately not be tested and the risk accepted.
4. Define the gating suite and its maximum runtime.
5. Review after escaped defects to see which level should have caught them.

## Output contract
Write `test-strategy.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** test-strategy
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
- Coverage driven by failure cost
- Untested areas and accepted risk stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
