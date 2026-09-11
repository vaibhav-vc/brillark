---
name: service-blueprinting
category: design
description: "Map the whole service, including everything the customer never sees."
output: "service-blueprint.md"
used_by:
  - service-designer
---

# Service Blueprinting

`design` · produces `service-blueprint.md` · used by `service-designer`

Map the whole service, including everything the customer never sees.

## Procedure
1. Lay out the customer actions across the journey.
2. Add the front-stage touchpoints they interact with.
3. Add the back-stage actions and systems that make each possible.
4. Mark the lines of visibility and internal interaction.
5. Identify where a front-stage promise depends on an unreliable back-stage step.

## Output contract
`service-blueprint.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Back-stage mapped alongside front-stage
- Fragile front-stage promises identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
