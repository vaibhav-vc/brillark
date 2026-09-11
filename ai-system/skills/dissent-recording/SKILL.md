---
name: dissent-recording
category: council
description: "Preserve minority positions on the record."
output: "dissent-log.md"
used_by:
  - council-director
  - council-synthesis-arbiter
---

# Dissent Recording

`council` · produces `dissent-log.md` · used by `council-director`, `council-synthesis-arbiter`

Preserve minority positions on the record.

## Procedure
1. Record the dissenting position in the dissenter's own words.
2. Record what evidence would vindicate it.
3. Note who overruled it and on what basis.
4. Keep it attached to the decision permanently.
5. Review dissent when the decision's outcome becomes known.

## Output contract
`dissent-log.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Dissent recorded verbatim
- Vindicating evidence stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
