---
name: root-cause-clustering
category: improvement
description: "Group failures by what actually caused them."
output: "cluster-report.md"
used_by:
  - failure-miner
---

# Root Cause Clustering

**Category:** `improvement` · **Output artifact:** `cluster-report.md`

## What this skill does
Group failures by what actually caused them.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `failure-miner`.

## Procedure
1. Cluster by cause, never by symptom or by reporting domain.
2. Merge clusters that differ only in vocabulary.
3. Require three independent instances before naming a pattern.
4. Distinguish a pattern from several symptoms of one incident.
5. Name each cluster by its cause in one sentence.

## Output contract
Write `cluster-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** root-cause-clustering
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
- Three independent instances required per pattern
- Clustered by cause, not symptom
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
