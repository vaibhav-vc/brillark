---
name: migration-planning
category: engineering
description: "Change a live schema without losing data or availability."
output: "migration-plan.md"
used_by:
  - data-model-designer
---

# Migration Planning

`engineering` · produces `migration-plan.md` · used by `data-model-designer`

Change a live schema without losing data or availability.

## Procedure
1. Define the target state and the intermediate states.
2. Design each step to be backwards compatible with the running code.
3. Plan the backfill separately, with progress tracking and resumability.
4. Define the rollback for each step, or state why it is irreversible.
5. Test on production-shaped data volume before running.

## Output contract
`migration-plan.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Each step backwards compatible
- Rollback defined or irreversibility declared
- The output states its confidence grade and names the evidence behind every load-bearing claim.
