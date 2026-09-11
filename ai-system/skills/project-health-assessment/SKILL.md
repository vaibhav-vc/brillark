---
name: project-health-assessment
category: research
description: "Check whether the thing will still exist in three years."
output: "health-assessment.md"
used_by:
  - technology-evaluator
---

# Project Health Assessment

`research` · produces `health-assessment.md` · used by `technology-evaluator`

Check whether the thing will still exist in three years.

## Procedure
1. Check release cadence, issue response time, and open-issue trend.
2. Check contributor count and concentration — a one-maintainer project is a risk.
3. Check funding, governance, and commercial backing.
4. Check the deprecation and breaking-change record.
5. State the risk and what we would do if the project stopped.

## Output contract
`health-assessment.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Contributor concentration assessed
- Contingency stated if the project stops
- The output states its confidence grade and names the evidence behind every load-bearing claim.
