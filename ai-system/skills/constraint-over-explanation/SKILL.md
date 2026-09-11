---
name: constraint-over-explanation
category: improvement
description: "Write rules agents follow rather than rationale they interpret."
output: "rule-text.md"
used_by:
  - knowledge-distiller
---

# Constraint Over Explanation

`improvement` · produces `rule-text.md` · used by `knowledge-distiller`

Write rules agents follow rather than rationale they interpret.

## Procedure
1. State the rule as a directive, not as background.
2. Make the condition for applying it unambiguous.
3. State what to do when the rule cannot be followed.
4. Avoid hedged language that invites improvisation.
5. Keep the rationale separate and shorter than the rule.

## Output contract
`rule-text.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Rule stated as an unambiguous directive
- Cannot-follow case specified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
