---
name: flaky-test-elimination
category: engineering
description: "Remove nondeterminism instead of tolerating it."
output: "flake-report.md"
used_by:
  - qa-test-strategist
---

# Flaky Test Elimination

**Category:** `engineering` · **Output artifact:** `flake-report.md`

## What this skill does
Remove nondeterminism instead of tolerating it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `qa-test-strategist`.

## Procedure
1. Detect flakes by re-running the suite on unchanged code.
2. Rank flakes by how often they block the pipeline.
3. Diagnose the actual cause: timing, shared state, ordering, or external dependency.
4. Fix the cause; never quarantine or skip to go green.
5. Track the flake rate as a suite health metric.

## Output contract
Write `flake-report.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** flaky-test-elimination
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Cause diagnosed, not retried away
- No tests skipped to achieve green
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
