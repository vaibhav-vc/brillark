---
name: post-release-review
category: engineering
description: "Learn from every release, not just the bad ones."
output: "post-release-review.md"
used_by:
  - release-manager
---

# Post Release Review

`engineering` · produces `post-release-review.md` · used by `release-manager`

Learn from every release, not just the bad ones.

## Procedure
1. Compare the actual rollout against the plan.
2. Record what surprised the team, however small.
3. Check whether monitoring detected issues before users did.
4. Identify the one change that would have made this smoother.
5. Feed the change into the process, not into a memo.

## Output contract
`post-release-review.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Surprises recorded even without incident
- One concrete process change identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
