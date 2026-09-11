---
name: release-quality-reporting
category: engineering
description: "Report quality as a signal with known limits."
output: "quality-report.md"
used_by:
  - qa-test-strategist
---

# Release Quality Reporting

`engineering` · produces `quality-report.md` · used by `qa-test-strategist`

Report quality as a signal with known limits.

## Procedure
1. Report coverage of risk areas, not just line coverage.
2. Report known defects and their severity, including the ones being accepted.
3. State what was not tested and why.
4. Compare against previous releases to show the trend.
5. Avoid single percentages that imply more certainty than exists.

## Output contract
`quality-report.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Untested areas stated explicitly
- Accepted defects disclosed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
