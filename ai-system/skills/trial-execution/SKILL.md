---
name: trial-execution
category: improvement
description: "Run the comparison cleanly."
output: "trial-results.md"
used_by:
  - ab-test-runner
---

# Trial Execution

**Category:** `improvement` · **Output artifact:** `trial-results.md`

## What this skill does
Run the comparison cleanly.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ab-test-runner`.

## Procedure
1. Run baseline and variant on identical cases in identical conditions.
2. Run the full planned sample before looking at results.
3. Record every run, including the failed and the anomalous ones.
4. Compute the effect size and its variability.
5. Re-run any result that would change a decision.

## Output contract
Write `trial-results.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** trial-execution
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
- Full planned sample run before inspection
- Decision-changing results re-run
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
