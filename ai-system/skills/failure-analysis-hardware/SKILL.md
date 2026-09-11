---
name: failure-analysis-hardware
category: hardware
description: "Find out why the unit actually failed."
output: "failure-analysis.md"
used_by:
  - hardware-test-engineer
---

# Failure Analysis Hardware

`hardware` · produces `failure-analysis.md` · used by `hardware-test-engineer`

Find out why the unit actually failed.

## Procedure
1. Preserve the failed unit and its context before disturbing anything.
2. Reproduce the failure before theorising about it.
3. Work from symptom to mechanism, using measurement rather than replacement.
4. Confirm the root cause by inducing the failure deliberately.
5. Feed the mechanism into design, test, or process so it cannot recur.

## Output contract
`failure-analysis.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Failure reproduced before diagnosis
- Root cause confirmed by deliberate reproduction
- The output states its confidence grade and names the evidence behind every load-bearing claim.
