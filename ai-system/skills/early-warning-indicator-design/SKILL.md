---
name: early-warning-indicator-design
category: council
description: "Define signals that warn before the failure arrives."
output: "early-warning-indicators.md"
used_by:
  - council-risk-and-failure-modes
---

# Early Warning Indicator Design

`council` · produces `early-warning-indicators.md` · used by `council-risk-and-failure-modes`

Define signals that warn before the failure arrives.

## Procedure
1. For each failure mode, identify what changes first.
2. Choose an indicator that is measurable now, not in principle.
3. Set the threshold that distinguishes signal from noise.
4. Assign an owner and a check cadence.
5. Verify the indicator would have fired on a past instance.

## Output contract
`early-warning-indicators.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Indicators measurable today
- Back-tested against a past instance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
