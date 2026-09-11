---
name: tech-debt-registry
category: engineering
description: "Record debt with its actual cost."
output: "tech-debt-register.md"
used_by:
  - tech-debt-refactor-agent
---

# Tech Debt Registry

`engineering` · produces `tech-debt-register.md` · used by `tech-debt-refactor-agent`

Record debt with its actual cost.

## Procedure
1. Record each item with its location and the change it makes harder.
2. Estimate the interest: time added to each change in that area.
3. Estimate the cost to fix.
4. Rank by interest rate rather than by size.
5. Review when a roadmap item touches a registered area.

## Output contract
`tech-debt-register.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Interest quantified per item
- Ranked by interest, not size
- The output states its confidence grade and names the evidence behind every load-bearing claim.
