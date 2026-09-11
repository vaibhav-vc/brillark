---
name: deployment-safety-review
category: engineering
description: "Check a deployment cannot cause irreversible harm."
output: "deployment-review.md"
used_by:
  - infra-devops-agent
---

# Deployment Safety Review

`engineering` · produces `deployment-review.md` · used by `infra-devops-agent`

Check a deployment cannot cause irreversible harm.

## Procedure
1. Verify the change is backwards compatible with the running version.
2. Confirm database changes are separated from code changes.
3. Check the rollback path exists and has been exercised.
4. Confirm monitoring will detect a failure quickly.
5. Verify the blast radius is limited by staged exposure.

## Output contract
`deployment-review.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Rollback exercised, not just documented
- Blast radius limited by staging
- The output states its confidence grade and names the evidence behind every load-bearing claim.
