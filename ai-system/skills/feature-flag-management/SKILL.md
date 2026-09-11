---
name: feature-flag-management
category: engineering
description: "Use flags without creating a permanent maze."
output: "flag-registry.md"
used_by:
  - release-manager
---

# Feature Flag Management

`engineering` · produces `flag-registry.md` · used by `release-manager`

Use flags without creating a permanent maze.

## Procedure
1. Give every flag an owner, a purpose, and an expiry date.
2. Distinguish release flags from operational toggles from experiments.
3. Keep flag logic out of deep code paths.
4. Remove flags promptly after full rollout.
5. Audit flags regularly and delete the abandoned ones.

## Output contract
`flag-registry.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Every flag has an owner and expiry
- Stale flags removed, not accumulated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
