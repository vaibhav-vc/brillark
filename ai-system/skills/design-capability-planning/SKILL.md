---
name: design-capability-planning
category: design
description: "Plan the design capability the roadmap actually needs."
output: "capability-plan.md"
used_by:
  - chief-design-officer-agent
---

# Design Capability Planning

`design` · produces `capability-plan.md` · used by `chief-design-officer-agent`

Plan the design capability the roadmap actually needs.

## Procedure
1. Identify the design work the roadmap requires, by type.
2. Compare against current capability and capacity.
3. Decide what to build, hire, or systematise.
4. Invest in the system where it removes repeated work.
5. Sequence against the roadmap rather than hiring generically.

## Output contract
`capability-plan.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Capability need derived from the roadmap
- System investment weighed against repeated work
- The output states its confidence grade and names the evidence behind every load-bearing claim.
