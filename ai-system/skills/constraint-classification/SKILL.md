---
name: constraint-classification
category: council
description: "Sort real constraints from assumed ones."
output: "constraint-analysis.md"
used_by:
  - council-first-principles
---

# Constraint Classification

`council` · produces `constraint-analysis.md` · used by `council-first-principles`

Sort real constraints from assumed ones.

## Procedure
1. List every constraint the plan treats as fixed.
2. Classify each: physical, legal, contractual, economic, or habitual.
3. For each non-physical constraint, identify who could change it.
4. Test whether anyone has actually tried.
5. Report constraints that are choices nobody owns as findings.

## Output contract
`constraint-analysis.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Owner identified per changeable constraint
- Unowned assumed constraints flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.
