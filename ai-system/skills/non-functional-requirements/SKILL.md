---
name: non-functional-requirements
category: product
description: "State the qualities the system must have, not just its behaviour."
output: "nfr.md"
used_by:
  - product-requirements-agent
---

# Non Functional Requirements

`product` · produces `nfr.md` · used by `product-requirements-agent`

State the qualities the system must have, not just its behaviour.

## Procedure
1. Specify latency and throughput targets for the critical journeys.
2. Specify availability and the acceptable failure behaviour.
3. Specify security, privacy, and data retention requirements.
4. Specify accessibility and browser or device support.
5. Make each testable; an untestable requirement is a wish.

## Output contract
`nfr.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Every requirement testable
- Failure behaviour specified, not just uptime
- The output states its confidence grade and names the evidence behind every load-bearing claim.
