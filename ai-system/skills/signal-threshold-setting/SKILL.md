---
name: signal-threshold-setting
category: research
description: "Define in advance what counts as a signal."
output: "thresholds.md"
used_by:
  - horizon-scanner
---

# Signal Threshold Setting

`research` · produces `thresholds.md` · used by `horizon-scanner`

Define in advance what counts as a signal.

## Procedure
1. Establish the indicator's normal range from historical observation.
2. Set the threshold beyond normal variation.
3. Define the response each crossing triggers, and who acts.
4. Record the threshold before monitoring begins.
5. Review thresholds that never fire and those that fire constantly.

## Output contract
`thresholds.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Threshold set beyond observed normal variation
- Response and owner defined per crossing
- The output states its confidence grade and names the evidence behind every load-bearing claim.
