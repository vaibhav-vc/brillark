---
name: scalability-stress-review
category: engineering
description: "Find where the architecture breaks before the market finds it."
output: "scalability-review.md"
used_by:
  - cto-agent
  - system-architect
---

# Scalability Stress Review

`engineering` · produces `scalability-review.md` · used by `cto-agent`, `system-architect`

Find where the architecture breaks before the market finds it.

## Procedure
1. Model load at ten and one hundred times current volume.
2. Identify the first component to break at each level.
3. Check data growth separately from request growth.
4. Estimate the cost curve, not just the technical limit.
5. Record the breaking points and the change each would require.

## Output contract
`scalability-review.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- First breaking point identified per level
- Cost curve modelled alongside capacity
- The output states its confidence grade and names the evidence behind every load-bearing claim.
