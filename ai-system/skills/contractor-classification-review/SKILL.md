---
name: contractor-classification-review
category: finance
description: "Check that contractors are genuinely contractors."
output: "classification-review.md"
used_by:
  - tax-and-compliance-finance
---

# Contractor Classification Review

**Category:** `finance` · **Output artifact:** `classification-review.md`

## What this skill does
Check that contractors are genuinely contractors.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `tax-and-compliance-finance`.

## Procedure
1. List every non-employee engagement and its working arrangement.
2. Assess control, integration, substitution rights, and financial risk.
3. Compare against the tests used in the relevant jurisdiction.
4. Flag high-risk engagements with the specific factor that creates the risk.
5. Escalate anything uncertain to qualified advice rather than deciding internally.

## Output contract
Write `classification-review.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** contractor-classification-review
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
- Assessed against jurisdiction-specific tests
- Uncertain cases escalated to advice
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
