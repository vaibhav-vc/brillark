---
name: vendor-risk-review
category: strategy
description: "Assess what a vendor dependency actually exposes us to."
output: "vendor-risk.md"
used_by:
  - cto-agent
---

# Vendor Risk Review

`strategy` · produces `vendor-risk.md` · used by `cto-agent`

Assess what a vendor dependency actually exposes us to.

## Procedure
1. Identify what breaks for customers if the vendor fails or changes terms.
2. Assess concentration: how much depends on this one supplier.
3. Check contractual protections, data portability, and notice periods.
4. Define the exit path and estimate the time and cost to execute it.
5. Set the monitoring signal for vendor deterioration.

## Output contract
`vendor-risk.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Exit path costed, not just identified
- Customer impact of failure assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
