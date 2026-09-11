---
name: groupthink-detection
category: council
description: "Spot agreement that was assumed rather than earned."
output: "groupthink-check.md"
used_by:
  - council-devils-advocate
---

# Groupthink Detection

`council` · produces `groupthink-check.md` · used by `council-devils-advocate`

Spot agreement that was assumed rather than earned.

## Procedure
1. Check whether any disconfirming test was defined before convergence.
2. Look for whether dissent was voiced and how it was handled.
3. Check whether the alternatives were genuinely explored or listed for form.
4. Ask who would be uncomfortable disagreeing and whether they were asked.
5. Report convergence without evidence as a finding in its own right.

## Output contract
`groupthink-check.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Presence of a disconfirming test verified
- Handling of dissent examined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
