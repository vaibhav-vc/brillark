---
name: flaky-test-elimination
category: engineering
description: "Remove nondeterminism instead of tolerating it."
output: "flake-report.md"
used_by:
  - qa-test-strategist
---

# Flaky Test Elimination

`engineering` · produces `flake-report.md` · used by `qa-test-strategist`

Remove nondeterminism instead of tolerating it.

## Procedure
1. Detect flakes by re-running the suite on unchanged code.
2. Rank flakes by how often they block the pipeline.
3. Diagnose the actual cause: timing, shared state, ordering, or external dependency.
4. Fix the cause; never quarantine or skip to go green.
5. Track the flake rate as a suite health metric.

## Output contract
`flake-report.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Cause diagnosed, not retried away
- No tests skipped to achieve green
- The output states its confidence grade and names the evidence behind every load-bearing claim.
