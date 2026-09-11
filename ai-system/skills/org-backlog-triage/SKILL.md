---
name: org-backlog-triage
category: orchestration
description: "Keep one prioritised list for the whole organisation so domains cannot each claim top priority."
output: "org-backlog.md"
used_by:
  - director
---

# Org Backlog Triage

`orchestration` · produces `org-backlog.md` · used by `director`

Keep one prioritised list for the whole organisation so domains cannot each claim top priority.

## Procedure
1. Merge domain backlogs into one list with a single ranking.
2. Score each item by strategic value, evidence strength, and cost to learn.
3. Force a strict order — ties are a refusal to decide.
4. Cut items below the funding line explicitly rather than leaving them ambiguous.
5. Publish the line and what sits just below it.

## Output contract
`org-backlog.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Strict order with no ties
- Funding line published
- The output states its confidence grade and names the evidence behind every load-bearing claim.
