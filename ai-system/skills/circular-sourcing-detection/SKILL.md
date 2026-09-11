---
name: circular-sourcing-detection
category: research
description: "Spot many sources that are secretly one source."
output: "circularity-report.md"
used_by:
  - source-verifier
---

# Circular Sourcing Detection

`research` · produces `circularity-report.md` · used by `source-verifier`

Spot many sources that are secretly one source.

## Procedure
1. Trace each apparently independent source back toward its origin.
2. Look for a shared press release, single study, or one interview behind the cluster.
3. Count independent origins, not documents.
4. Flag the claim's true evidential weight when the count collapses.
5. Record the cluster so it is not re-counted next time.

## Output contract
`circularity-report.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Independent origins counted, not documents
- Collapsed clusters recorded for reuse
- The output states its confidence grade and names the evidence behind every load-bearing claim.
