---
name: repository-reuse-measurement
category: research
description: "Check the research repository is actually an asset."
output: "reuse-report.md"
used_by:
  - research-head
---

# Repository Reuse Measurement

`research` · produces `reuse-report.md` · used by `research-head`

Check the research repository is actually an asset.

## Procedure
1. Count retrievals against new commissions per cycle.
2. Identify questions re-researched despite an existing answer.
3. Diagnose whether misses are retrieval, tagging, or currency failures.
4. Fix the retrieval path rather than telling agents to search harder.
5. Report the reuse rate as a standing metric.

## Output contract
`reuse-report.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Re-researched questions identified
- Fixes target retrieval, not agent effort
- The output states its confidence grade and names the evidence behind every load-bearing claim.
