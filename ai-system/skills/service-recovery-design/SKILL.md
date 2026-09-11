---
name: service-recovery-design
category: design
description: "Design what happens when the service fails the customer."
output: "recovery-plan.md"
used_by:
  - service-designer
---

# Service Recovery Design

`design` · produces `recovery-plan.md` · used by `service-designer`

Design what happens when the service fails the customer.

## Procedure
1. List the failure modes the customer will actually experience.
2. Design the acknowledgement: fast, specific, and without blame.
3. Define the remedy and who is empowered to give it without escalation.
4. Design the follow-through so the customer knows it was fixed.
5. Measure recovery satisfaction, not just failure frequency.

## Output contract
`recovery-plan.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Front-line empowered to remedy without escalation
- Recovery satisfaction measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.
