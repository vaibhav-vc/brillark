---
name: design-token-application
category: design
description: "Use the system's tokens rather than introducing one-off values."
output: "token-usage-report.md"
used_by:
  - visual-designer
---

# Design Token Application

`design` · produces `token-usage-report.md` · used by `visual-designer`

Use the system's tokens rather than introducing one-off values.

## Procedure
1. Look up the semantic token for the intent, not the literal value you want.
2. Propose a token addition when none fits, rather than hard-coding.
3. Check the token works in every theme and mode the product supports.
4. Flag any one-off value remaining, with a reason and a plan to remove it.
5. Verify the applied tokens survive a theme switch.

## Output contract
`token-usage-report.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- No hard-coded values without a recorded reason
- Verified across themes and modes
- The output states its confidence grade and names the evidence behind every load-bearing claim.
