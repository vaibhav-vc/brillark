---
name: token-accounting
category: efficiency
description: "Know where the tokens actually go."
output: "token-report.md"
used_by:
  - token-efficiency-analyst
---

# Token Accounting

`efficiency` · produces `token-report.md` · used by `token-efficiency-analyst`

Know where the tokens actually go.

## Procedure
1. Record tokens per run, split into system, context, retrieved content, and output.
2. Attribute to agent, skill, and workflow.
3. Compute cost per completed task, not per call.
4. Rank consumers and identify the top few that dominate.
5. Publish the breakdown so optimisation targets reality.

## Output contract
`token-report.md` → `workspace/<venture-id>/efficiency/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/efficiency.tsv`.

## Quality bar
- Cost measured per completed task
- Split by system, context, retrieval, and output
- The output states its confidence grade and names the evidence behind every load-bearing claim.
