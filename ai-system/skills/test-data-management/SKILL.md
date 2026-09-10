---
name: test-data-management
category: engineering
description: "Make test data predictable and safe."
output: "test-data-standard.md"
used_by:
  - qa-test-strategist
---

# Test Data Management

**Category:** `engineering` · **Output artifact:** `test-data-standard.md`

## What this skill does
Make test data predictable and safe.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `qa-test-strategist`.

## Procedure
1. Define how test data is created, per test rather than shared where possible.
2. Never copy production personal data into test environments.
3. Make data setup explicit in the test, so failures are readable.
4. Clean up deterministically so ordering does not matter.
5. Keep fixtures small enough to understand at a glance.

## Output contract
Write `test-data-standard.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** test-data-management
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
- No production personal data in test environments
- Tests independent of execution order
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
