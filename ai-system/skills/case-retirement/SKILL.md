---
name: case-retirement
category: improvement
description: "Remove cases that no longer teach anything."
output: "retirement-log.md"
used_by:
  - benchmark-curator
---

# Case Retirement

`improvement` · produces `retirement-log.md` · used by `benchmark-curator`

Remove cases that no longer teach anything.

## Procedure
1. Identify cases every candidate passes across several cycles.
2. Check the case is not passing because the suite is over-tuned to it.
3. Archive rather than delete, so history remains.
4. Replace retired coverage with a harder case in the same area.
5. Record the retirement and its reason.

## Output contract
`retirement-log.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Over-tuning ruled out before retiring
- Retired coverage replaced
- The output states its confidence grade and names the evidence behind every load-bearing claim.
