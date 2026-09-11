---
name: onboarding-design
category: gtm
description: "Get a new customer to their first real value quickly."
output: "onboarding-design.md"
used_by:
  - customer-success-agent
---

# Onboarding Design

`gtm` · produces `onboarding-design.md` · used by `customer-success-agent`

Get a new customer to their first real value quickly.

## Procedure
1. Define first value concretely — the specific moment the customer gets something they wanted.
2. Map every step between signup and that moment.
3. Remove or defer every step that is not required to reach it.
4. Instrument the time to first value and the drop-off per step.
5. Design the recovery path for customers who stall.

## Output contract
`onboarding-design.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- First value defined concretely
- Time to first value instrumented
- The output states its confidence grade and names the evidence behind every load-bearing claim.
