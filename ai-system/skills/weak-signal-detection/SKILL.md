---
name: weak-signal-detection
category: research
description: "Notice a change before it is obvious, without inventing one."
output: "signal-report.md"
used_by:
  - horizon-scanner
---

# Weak Signal Detection

`research` · produces `signal-report.md` · used by `horizon-scanner`

Notice a change before it is obvious, without inventing one.

## Procedure
1. Monitor the defined indicators on their cadence.
2. Compare against the threshold, not against your impression.
3. Look for convergence across independent indicators.
4. Resist narrative: three anecdotes is a coincidence until a threshold says otherwise.
5. Report the quiet periods too, so silence carries information.

## Output contract
`signal-report.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Compared against thresholds, not impressions
- Quiet periods reported
- The output states its confidence grade and names the evidence behind every load-bearing claim.
