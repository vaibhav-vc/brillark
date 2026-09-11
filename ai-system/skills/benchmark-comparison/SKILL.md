---
name: benchmark-comparison
category: council
description: "Compare our numbers to observed reality and demand a reason for every gap."
output: "benchmark-comparison.md"
used_by:
  - council-economics-skeptic
---

# Benchmark Comparison

`council` · produces `benchmark-comparison.md` · used by `council-economics-skeptic`

Compare our numbers to observed reality and demand a reason for every gap.

## Procedure
1. Collect benchmarks from sources with a stated methodology and sample.
2. Match on stage, model, and market — mismatched benchmarks mislead.
3. Compare our conversion, CAC, churn, growth, and margin against the range.
4. Flag every figure outside the range, especially the favourable ones.
5. Require an explanation for each gap or correct the number.

## Output contract
`benchmark-comparison.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Benchmarks matched on stage and model
- Favourable outliers challenged too
- The output states its confidence grade and names the evidence behind every load-bearing claim.
