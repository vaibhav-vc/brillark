---
name: optimisation-drift-detection
category: improvement
description: "Catch the system getting better at its metrics while getting worse at its job."
output: "drift-report.md"
used_by:
  - chief-learning-officer-agent
---

# Optimisation Drift Detection

`improvement` · produces `drift-report.md` · used by `chief-learning-officer-agent`

Catch the system getting better at its metrics while getting worse at its job.

## Procedure
1. Compare metric improvements against real outcomes they are meant to proxy.
2. Look for metrics improving while user or business outcomes do not.
3. Check whether recent changes targeted the measure rather than the goal.
4. Check whether the evaluation set has narrowed toward what we optimise.
5. Report drift and recommend widening the measurement.

## Output contract
`drift-report.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Metrics compared against the outcomes they proxy
- Narrowing evaluation sets flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.
