---
name: figure-with-limits-reporting
category: research
description: "Report a number with everything needed to use it responsibly."
output: "figure-report.md"
used_by:
  - data-sourcing-analyst
---

# Figure With Limits Reporting

`research` · produces `figure-report.md` · used by `data-sourcing-analyst`

Report a number with everything needed to use it responsibly.

## Procedure
1. State the figure with its unit, date, and geography.
2. State the range or confidence, not a bare point estimate.
3. State the source, its grade, and its methodology in one line.
4. State what the figure does not cover.
5. Refuse to supply a bare number when the decision needs the caveats.

## Output contract
`figure-report.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Range reported, not a bare point estimate
- Coverage gaps stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
