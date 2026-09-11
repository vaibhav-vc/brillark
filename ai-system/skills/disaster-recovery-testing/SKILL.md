---
name: disaster-recovery-testing
category: engineering
description: "Prove you can actually recover, not just that you have backups."
output: "dr-test-report.md"
used_by:
  - infra-devops-agent
---

# Disaster Recovery Testing

`engineering` · produces `dr-test-report.md` · used by `infra-devops-agent`

Prove you can actually recover, not just that you have backups.

## Procedure
1. Define the recovery time and recovery point objectives.
2. Perform a real restore into a clean environment.
3. Verify data integrity and completeness after restore.
4. Measure the actual time taken against the objective.
5. Fix the gaps and schedule the next test.

## Output contract
`dr-test-report.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Real restore performed and verified
- Actual recovery time measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.
