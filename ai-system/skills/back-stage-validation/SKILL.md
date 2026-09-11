---
name: back-stage-validation
category: design
description: "Check the operation can actually deliver the designed experience."
output: "validation-record.md"
used_by:
  - service-designer
---

# Back Stage Validation

`design` · produces `validation-record.md` · used by `service-designer`

Check the operation can actually deliver the designed experience.

## Procedure
1. Walk the blueprint with the people who will operate it.
2. Check each back-stage step against real capacity and skills.
3. Identify steps that only work when nothing else is happening.
4. Revise the front-stage promise where the back-stage cannot support it.
5. Get explicit agreement from the operating owner before launch.

## Output contract
`validation-record.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Walked with actual operators
- Front-stage promises revised to match capacity
- The output states its confidence grade and names the evidence behind every load-bearing claim.
