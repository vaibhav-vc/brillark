---
name: bottleneck-analysis
category: orchestration
description: "Find the one constraint limiting the whole system's output."
output: "bottleneck-report.md"
used_by:
  - coo-agent
---

# Bottleneck Analysis

`orchestration` · produces `bottleneck-report.md` · used by `coo-agent`

Find the one constraint limiting the whole system's output.

## Procedure
1. Measure queue length and wait time at each stage.
2. Identify the stage where work accumulates fastest.
3. Confirm it is the constraint by checking whether upstream speed-ups help at all.
4. Exploit the constraint before adding capacity elsewhere.
5. Re-measure after the change; the constraint usually moves.

## Output contract
`bottleneck-report.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Constraint confirmed, not assumed
- Re-measured after intervention
- The output states its confidence grade and names the evidence behind every load-bearing claim.
