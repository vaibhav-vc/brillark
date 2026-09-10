---
name: benchmark-comparison
category: council
description: "Compare our numbers to observed reality and demand a reason for every gap."
output: "benchmark-comparison.md"
used_by:
  - council-economics-skeptic
---

# Benchmark Comparison

**Category:** `council` · **Output artifact:** `benchmark-comparison.md`

## What this skill does
Compare our numbers to observed reality and demand a reason for every gap.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-economics-skeptic`.

## Procedure
1. Collect benchmarks from sources with a stated methodology and sample.
2. Match on stage, model, and market — mismatched benchmarks mislead.
3. Compare our conversion, CAC, churn, growth, and margin against the range.
4. Flag every figure outside the range, especially the favourable ones.
5. Require an explanation for each gap or correct the number.

## Output contract
Write `benchmark-comparison.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** benchmark-comparison
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
- Benchmarks matched on stage and model
- Favourable outliers challenged too
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
