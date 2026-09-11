---
name: systemic-cause-identification
category: improvement
description: "Find the cause that produces many different failures."
output: "systemic-causes.md"
used_by:
  - failure-miner
---

# Systemic Cause Identification

`improvement` · produces `systemic-causes.md` · used by `failure-miner`

Find the cause that produces many different failures.

## Procedure
1. Look for causes appearing across multiple clusters.
2. Trace each to the artifact or process that permits it.
3. Check whether the cause is structural rather than a repeated mistake.
4. Estimate how many failures would disappear if it were fixed.
5. Propose the fix at the structural level, not per symptom.

## Output contract
`systemic-causes.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Traced to a permitting artifact or process
- Fix proposed structurally, not per symptom
- The output states its confidence grade and names the evidence behind every load-bearing claim.
