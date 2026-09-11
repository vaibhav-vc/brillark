---
name: design-code-parity-audit
category: design
description: "Check that the design source and the shipped code still agree."
output: "parity-report.md"
used_by:
  - design-system-architect
---

# Design Code Parity Audit

`design` · produces `parity-report.md` · used by `design-system-architect`

Check that the design source and the shipped code still agree.

## Procedure
1. Compare tokens in the design source against the values in code.
2. Compare component states and variants in both.
3. Sample real screens and diff them against their designs.
4. Record every divergence with which side is correct.
5. Fix at the source of truth, not by patching the other side.

## Output contract
`parity-report.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Divergences recorded with the correct side named
- Fixes applied at the source of truth
- The output states its confidence grade and names the evidence behind every load-bearing claim.
