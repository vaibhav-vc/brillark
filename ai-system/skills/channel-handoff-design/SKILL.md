---
name: channel-handoff-design
category: design
description: "Design the moments where the service moves between channels or between machine and human."
output: "handoff-spec.md"
used_by:
  - service-designer
---

# Channel Handoff Design

`design` · produces `handoff-spec.md` · used by `service-designer`

Design the moments where the service moves between channels or between machine and human.

## Procedure
1. Identify every handoff point in the journey.
2. Specify what context travels across, so the customer never repeats themselves.
3. Define who owns the customer at each stage.
4. Design what the customer sees and hears during the transition.
5. Define the fallback when the handoff fails.

## Output contract
`handoff-spec.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Context travels so customers never repeat themselves
- Fallback defined per handoff
- The output states its confidence grade and names the evidence behind every load-bearing claim.
