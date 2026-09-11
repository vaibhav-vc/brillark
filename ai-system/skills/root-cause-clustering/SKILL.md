---
name: root-cause-clustering
category: improvement
description: "Group failures by what actually caused them."
output: "cluster-report.md"
used_by:
  - failure-miner
---

# Root Cause Clustering

`improvement` · produces `cluster-report.md` · used by `failure-miner`

Group failures by what actually caused them.

## Procedure
1. Cluster by cause, never by symptom or by reporting domain.
2. Merge clusters that differ only in vocabulary.
3. Require three independent instances before naming a pattern.
4. Distinguish a pattern from several symptoms of one incident.
5. Name each cluster by its cause in one sentence.

## Output contract
`cluster-report.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Three independent instances required per pattern
- Clustered by cause, not symptom
- The output states its confidence grade and names the evidence behind every load-bearing claim.
