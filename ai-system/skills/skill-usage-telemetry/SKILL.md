---
name: skill-usage-telemetry
category: improvement
description: "Find out which skills are actually used."
output: "usage-report.md"
used_by:
  - skill-refiner
---

# Skill Usage Telemetry

`improvement` · produces `usage-report.md` · used by `skill-refiner`

Find out which skills are actually used.

## Procedure
1. Count invocations per skill per cycle.
2. Separate skills referenced by agents from skills actually invoked.
3. Identify skills unused across three cycles.
4. Identify skills invoked but producing poor outcomes.
5. Publish usage so refinement targets reality.

## Output contract
`usage-report.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Referenced distinguished from invoked
- Three cycles before declaring a skill unused
- The output states its confidence grade and names the evidence behind every load-bearing claim.
