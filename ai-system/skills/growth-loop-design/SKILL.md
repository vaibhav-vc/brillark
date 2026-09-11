---
name: growth-loop-design
category: gtm
description: "Design a mechanism where output feeds back into input so growth compounds."
output: "growth-loop.md"
used_by:
  - growth-loop-designer
---

# Growth Loop Design

`gtm` · produces `growth-loop.md` · used by `growth-loop-designer`

Design a mechanism where output feeds back into input so growth compounds.

## Procedure
1. Draw the loop end to end, labelling every step's conversion rate and duration.
2. Compute the amplification factor; below 1.0 it is a funnel, not a loop.
3. Identify the step with the largest drop and the longest delay.
4. Check the loop does not degrade the experience for existing users.
5. State the input required to start the loop and what sustains it.

## Output contract
`growth-loop.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Amplification factor computed, not assumed
- Existing-user impact assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
