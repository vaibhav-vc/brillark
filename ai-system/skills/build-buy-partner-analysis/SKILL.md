---
name: build-buy-partner-analysis
category: strategy
description: "Decide whether to build a capability, buy it, or partner for it."
output: "build-buy-partner.md"
used_by:
  - cto-agent
---

# Build Buy Partner Analysis

`strategy` · produces `build-buy-partner.md` · used by `cto-agent`

Decide whether to build a capability, buy it, or partner for it.

## Procedure
1. Assess whether the capability is differentiating — customers pay for it — or merely necessary.
2. Estimate the true cost to build, including maintenance for three years.
3. Evaluate the buy option's fit, lock-in, and exit path.
4. Evaluate the partner option's incentive alignment and dependency risk.
5. Decide, and record the condition that would reverse the decision.

## Output contract
`build-buy-partner.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Differentiation assessed first
- Three-year maintenance cost included
- The output states its confidence grade and names the evidence behind every load-bearing claim.
