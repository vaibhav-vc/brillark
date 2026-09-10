---
name: release-quality-reporting
category: engineering
description: "Report quality as a signal with known limits."
output: "quality-report.md"
used_by:
  - qa-test-strategist
---

# Release Quality Reporting

**Category:** `engineering` · **Output artifact:** `quality-report.md`

## What this skill does
Report quality as a signal with known limits.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `qa-test-strategist`.

## Procedure
1. Report coverage of risk areas, not just line coverage.
2. Report known defects and their severity, including the ones being accepted.
3. State what was not tested and why.
4. Compare against previous releases to show the trend.
5. Avoid single percentages that imply more certainty than exists.

## Output contract
Write `quality-report.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** release-quality-reporting
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
- Untested areas stated explicitly
- Accepted defects disclosed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
