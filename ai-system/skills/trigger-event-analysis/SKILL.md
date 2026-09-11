---
name: trigger-event-analysis
category: market
description: "Find the moment that makes a buyer start looking."
output: "trigger-events.md"
used_by:
  - icp-persona-builder
---

# Trigger Event Analysis

`market` · produces `trigger-events.md` · used by `icp-persona-builder`

Find the moment that makes a buyer start looking.

## Procedure
1. Ask every interviewee what changed just before they went looking.
2. Group triggers into types: growth, failure, regulation, personnel change.
3. Assess which triggers are detectable from outside.
4. Design the outreach to arrive shortly after the detectable ones.
5. Measure conversion by trigger type.

## Output contract
`trigger-events.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Triggers grounded in interview evidence
- Detectability assessed per trigger
- The output states its confidence grade and names the evidence behind every load-bearing claim.
