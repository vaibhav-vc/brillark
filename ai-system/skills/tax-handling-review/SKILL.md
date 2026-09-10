---
name: tax-handling-review
category: finance
description: "Check that the system applies the tax logic correctly in practice."
output: "tax-review.md"
used_by:
  - billing-systems-designer
---

# Tax Handling Review

**Category:** `finance` · **Output artifact:** `tax-review.md`

## What this skill does
Check that the system applies the tax logic correctly in practice.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `billing-systems-designer`.

## Procedure
1. Sample transactions across jurisdictions and customer types.
2. Recompute the expected treatment independently.
3. Investigate every mismatch, including the ones in our favour.
4. Check that evidence for zero-rating or exemption is actually captured.
5. Report gaps with the specific correction needed.

## Output contract
Write `tax-review.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** tax-handling-review
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
- Sample spans jurisdictions and customer types
- Exemption evidence verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
