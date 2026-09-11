---
name: tooling-design-review
category: hardware
description: "Review the tool before it is cut."
output: "tool-review.md"
used_by:
  - dfm-engineer
---

# Tooling Design Review

`hardware` · produces `tool-review.md` · used by `dfm-engineer`

Review the tool before it is cut.

## Procedure
1. Review parting line, gate, and ejection against the part design.
2. Check for witness marks and cosmetic consequences on visible surfaces.
3. Confirm shrinkage assumptions for the specified material.
4. Agree the trial and sampling plan before the tool is made.
5. Confirm the design is frozen; never cut a tool on a moving design.

## Output contract
`tool-review.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Cosmetic consequences of gating agreed
- Design confirmed frozen before cutting
- The output states its confidence grade and names the evidence behind every load-bearing claim.
