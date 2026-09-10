---
name: churn-analysis
category: gtm
description: "Understand why customers leave, in categories you can act on."
output: "churn-analysis.md"
used_by:
  - chief-revenue-officer-agent
  - customer-success-agent
---

# Churn Analysis

**Category:** `gtm` · **Output artifact:** `churn-analysis.md`

## What this skill does
Understand why customers leave, in categories you can act on.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-revenue-officer-agent`, `customer-success-agent`.

## Procedure
1. Capture a reason for every churn, from the customer where possible.
2. Classify into a fixed taxonomy: product gap, value not realised, price, change of need, or service failure.
3. Separate voluntary from involuntary churn — the fixes are different.
4. Compute churn by cohort and segment, not blended.
5. Route each category to the owner who can address it.

## Output contract
Write `churn-analysis.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** churn-analysis
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
- Fixed taxonomy applied consistently
- Voluntary and involuntary separated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
