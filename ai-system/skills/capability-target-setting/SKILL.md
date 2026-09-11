---
name: capability-target-setting
category: improvement
description: "Set improvement targets that can be judged."
output: "capability-targets.md"
used_by:
  - chief-learning-officer-agent
---

# Capability Target Setting

`improvement` · produces `capability-targets.md` · used by `chief-learning-officer-agent`

Set improvement targets that can be judged.

## Procedure
1. State the capability in terms of an observable outcome.
2. Set the current baseline from measurement.
3. Set a target and a date.
4. State what evidence would show the target was met.
5. State what would make the target wrong to pursue.

## Output contract
`capability-targets.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Baseline measured, not assumed
- Evidence of success defined in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
