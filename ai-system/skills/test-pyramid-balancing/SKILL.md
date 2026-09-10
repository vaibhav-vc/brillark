---
name: test-pyramid-balancing
category: engineering
description: "Keep the suite fast and meaningful."
output: "pyramid-report.md"
used_by:
  - qa-test-strategist
---

# Test Pyramid Balancing

**Category:** `engineering` · **Output artifact:** `pyramid-report.md`

## What this skill does
Keep the suite fast and meaningful.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `qa-test-strategist`.

## Procedure
1. Count tests at each level and their runtime contribution.
2. Identify high-level tests that duplicate lower-level coverage.
3. Push coverage down where the same bug can be caught cheaper.
4. Keep end-to-end tests for genuine integration risk only.
5. Track suite runtime as a first-class metric.

## Output contract
Write `pyramid-report.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** test-pyramid-balancing
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
- Duplicated coverage pushed down
- Suite runtime tracked as a metric
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
