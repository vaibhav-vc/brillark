---
name: beachhead-selection
category: gtm
description: "Choose the one segment to win first."
output: "beachhead.md"
used_by:
  - gtm-strategist
---

# Beachhead Selection

`gtm` · produces `beachhead.md` · used by `gtm-strategist`

Choose the one segment to win first.

## Procedure
1. Score candidate segments on pain intensity, reachability, budget, and reference value.
2. Prefer a segment small enough to dominate and connected enough to spread.
3. Check that winning it creates a credible path to the next segment.
4. Commit to it explicitly and state what is being deferred.
5. Define what 'won' means before starting.

## Output contract
`beachhead.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Segment small enough to dominate
- Definition of won stated in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
