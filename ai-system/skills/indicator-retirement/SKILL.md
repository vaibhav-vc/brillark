---
name: indicator-retirement
category: research
description: "Stop watching things that never taught you anything."
output: "retirement-log.md"
used_by:
  - horizon-scanner
---

# Indicator Retirement

`research` · produces `retirement-log.md` · used by `horizon-scanner`

Stop watching things that never taught you anything.

## Procedure
1. Review each indicator's history: did it ever fire, and was it right?
2. Identify indicators that fire constantly and are therefore ignored.
3. Identify indicators monitoring a risk that no longer exists.
4. Retire them and record why, rather than accumulating noise.
5. Replace retired coverage where the underlying risk persists.

## Output contract
`retirement-log.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Constant-firing indicators identified
- Retired coverage replaced where risk persists
- The output states its confidence grade and names the evidence behind every load-bearing claim.
