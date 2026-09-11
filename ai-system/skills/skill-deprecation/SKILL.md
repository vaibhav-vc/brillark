---
name: skill-deprecation
category: improvement
description: "Retire a skill without breaking the agents that name it."
output: "deprecation-record.md"
used_by:
  - skill-refiner
---

# Skill Deprecation

`improvement` · produces `deprecation-record.md` · used by `skill-refiner`

Retire a skill without breaking the agents that name it.

## Procedure
1. Confirm no usage across three cycles and no agent reference remains.
2. Identify the replacement, if any, and the migration.
3. Update every referencing agent in the same change.
4. Run the integrity tests before and after.
5. Record the retirement and its reason.

## Output contract
`deprecation-record.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- All references updated in the same change
- Integrity tests run before and after
- The output states its confidence grade and names the evidence behind every load-bearing claim.
