---
name: refactoring-planning
category: engineering
description: "Plan a refactor that pays off soon."
output: "refactor-plan.md"
used_by:
  - tech-debt-refactor-agent
---

# Refactoring Planning

`engineering` · produces `refactor-plan.md` · used by `tech-debt-refactor-agent`

Plan a refactor that pays off soon.

## Procedure
1. Justify from delivery pain or defect clustering, not from taste.
2. Refactor along the path of imminent work.
3. Ensure test coverage exists before changing structure.
4. Split into steps that each leave the system working.
5. Define the measurable improvement expected.

## Output contract
`refactor-plan.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Justified by delivery pain
- Each step leaves the system working
- The output states its confidence grade and names the evidence behind every load-bearing claim.
