---
name: win-loss-analysis
category: gtm
description: "Find out why deals were actually won and lost."
output: "win-loss-report.md"
used_by:
  - chief-revenue-officer-agent
  - sales-playbook-agent
---

# Win Loss Analysis

`gtm` · produces `win-loss-report.md` · used by `chief-revenue-officer-agent`, `sales-playbook-agent`

Find out why deals were actually won and lost.

## Procedure
1. Interview the buyer, not only the seller — their accounts differ.
2. Record the decisive factor, not the polite reason.
3. Classify losses: product gap, price, timing, trust, or process failure.
4. Count patterns across deals rather than reacting to the last loss.
5. Route product-caused losses to product with evidence.

## Output contract
`win-loss-report.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Buyer interviewed, not just the seller
- Losses classified and counted
- The output states its confidence grade and names the evidence behind every load-bearing claim.
