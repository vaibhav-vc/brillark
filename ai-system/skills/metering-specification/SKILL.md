---
name: metering-specification
category: finance
description: "Define the billable event precisely enough that nobody disputes the invoice."
output: "metering-spec.md"
used_by:
  - billing-systems-designer
---

# Metering Specification

`finance` · produces `metering-spec.md` · used by `billing-systems-designer`

Define the billable event precisely enough that nobody disputes the invoice.

## Procedure
1. Define the event, its unit, and the exact moment it counts.
2. Specify deduplication and idempotency for retried events.
3. Define late-arriving and out-of-order event handling.
4. Specify aggregation windows and rounding rules.
5. Define the customer-visible usage view so disputes can be self-resolved.

## Output contract
`metering-spec.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Deduplication and late events specified
- Customer-visible usage defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
