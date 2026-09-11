---
name: demand-signal-research
category: market
description: "Find evidence that demand exists in behaviour rather than in opinion."
output: "demand-signals.md"
used_by:
  - market-researcher
---

# Demand Signal Research

`market` · produces `demand-signals.md` · used by `market-researcher`

Find evidence that demand exists in behaviour rather than in opinion.

## Procedure
1. Look for money already being spent on the problem, including on workarounds.
2. Examine search behaviour, community discussion, and support forums.
3. Count job postings, tooling adoption, and other proxies for organisational spend.
4. Distinguish curiosity signals from purchase signals.
5. Report the strongest three signals and what would falsify them.

## Output contract
`demand-signals.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Signals are behavioural, not stated intent
- Falsification condition stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
