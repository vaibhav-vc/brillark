---
name: transaction-design
category: engineering
description: "Decide the consistency guarantee each operation actually offers."
output: "transaction-design.md"
used_by:
  - backend-implementation-agent
---

# Transaction Design

**Category:** `engineering` · **Output artifact:** `transaction-design.md`

## What this skill does
Decide the consistency guarantee each operation actually offers.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `backend-implementation-agent`.

## Procedure
1. Identify the invariants that must never be violated.
2. Determine the smallest transactional boundary that protects them.
3. Decide the guarantee for operations that cross boundaries.
4. Document the guarantee offered to callers explicitly.
5. Test the concurrent case, not just the sequential one.

## Output contract
Write `transaction-design.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** transaction-design
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
- Invariants identified before boundaries
- Concurrent behaviour tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
