---
name: held-out-set-construction
category: improvement
description: "Build a measurement set that stays honest."
output: "held-out-set.md"
used_by:
  - eval-designer
---

# Held Out Set Construction

`improvement` · produces `held-out-set.md` · used by `eval-designer`

Build a measurement set that stays honest.

## Procedure
1. Split before any tuning begins, and record the split.
2. Make the held-out set representative of the real task mix.
3. Keep it large enough to detect the effect you care about.
4. Restrict access so it is not consulted during development.
5. Audit periodically for leakage.

## Output contract
`held-out-set.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Split recorded before tuning begins
- Leakage audited periodically
- The output states its confidence grade and names the evidence behind every load-bearing claim.
