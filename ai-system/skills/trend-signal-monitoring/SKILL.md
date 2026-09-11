---
name: trend-signal-monitoring
category: strategy
description: "Watch the small number of indicators that would change the strategy."
output: "signal-watchlist.md"
used_by:
  - chief-strategy-officer-agent
---

# Trend Signal Monitoring

`strategy` · produces `signal-watchlist.md` · used by `chief-strategy-officer-agent`

Watch the small number of indicators that would change the strategy.

## Procedure
1. Derive indicators from the scenarios and the moat thesis.
2. Define the threshold that constitutes a real signal versus noise.
3. Assign a source and a check cadence to each.
4. Review only when a threshold trips, not on a calendar.
5. Retire indicators that have never been informative.

## Output contract
`signal-watchlist.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Thresholds separate signal from noise
- Review triggered by signal, not calendar
- The output states its confidence grade and names the evidence behind every load-bearing claim.
