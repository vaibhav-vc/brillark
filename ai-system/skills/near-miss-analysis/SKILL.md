---
name: near-miss-analysis
category: risk
description: "Learn from the failures that almost happened."
output: "near-miss-log.md"
used_by:
  - chief-risk-officer-agent
---

# Near Miss Analysis

`risk` · produces `near-miss-log.md` · used by `chief-risk-officer-agent`

Learn from the failures that almost happened.

## Procedure
1. Capture near misses deliberately; they are rarely reported unprompted.
2. Analyse what stopped the failure — design or luck.
3. Treat luck-stopped near misses as failures for analysis purposes.
4. Identify the control that would make the outcome reliable.
5. Track near-miss frequency as a leading indicator.

## Output contract
`near-miss-log.md` → `workspace/<venture-id>/risk/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/risk.tsv`.

## Quality bar
- Luck distinguished from design
- Frequency tracked as a leading indicator
- The output states its confidence grade and names the evidence behind every load-bearing claim.
