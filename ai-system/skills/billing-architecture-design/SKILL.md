---
name: billing-architecture-design
category: finance
description: "Design the plumbing that turns pricing into collected cash."
output: "billing-architecture.md"
used_by:
  - billing-systems-designer
---

# Billing Architecture Design

`finance` · produces `billing-architecture.md` · used by `billing-systems-designer`

Design the plumbing that turns pricing into collected cash.

## Procedure
1. Model the pricing in the billing data model before writing any code.
2. Define plans, entitlements, and the metering source of truth.
3. Design proration, upgrades, downgrades, and refunds explicitly.
4. Specify the tax determination path per jurisdiction.
5. Define reconciliation between billing and the ledger, and alarm on drift.

## Output contract
`billing-architecture.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Proration and refunds specified up front
- Automated reconciliation defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
