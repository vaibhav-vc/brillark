---
name: severity-normalisation
category: council
description: "Make severity consistent across different critics."
output: "normalised-severities.md"
used_by:
  - council-synthesis-arbiter
---

# Severity Normalisation

`council` · produces `normalised-severities.md` · used by `council-synthesis-arbiter`

Make severity consistent across different critics.

## Procedure
1. Collect the ratings from every critic.
2. Compare findings of similar consequence rated differently.
3. Re-anchor against the scale definitions and prior verdicts.
4. Adjust outliers and record the adjustment.
5. Report persistent disagreement rather than averaging it away.

## Output contract
`normalised-severities.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Outliers re-anchored to the scale
- Persistent disagreement reported, not averaged
- The output states its confidence grade and names the evidence behind every load-bearing claim.
