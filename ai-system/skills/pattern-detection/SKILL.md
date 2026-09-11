---
name: pattern-detection
category: orchestration
description: "Find repeating structures in outcomes, failures, or requests."
output: "pattern-report.md"
used_by:
  - retrospective-agent
---

# Pattern Detection

`orchestration` · produces `pattern-report.md` · used by `retrospective-agent`

Find repeating structures in outcomes, failures, or requests.

## Procedure
1. Collect events over at least three cycles; two points are not a pattern.
2. Group by cause and by structure rather than by label.
3. Test whether the pattern predicts anything, or is coincidence.
4. Quantify frequency and cost.
5. Recommend a systemic change proportional to the cost.

## Output contract
`pattern-report.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- At least three cycles of data
- Pattern shown to be predictive
- The output states its confidence grade and names the evidence behind every load-bearing claim.
