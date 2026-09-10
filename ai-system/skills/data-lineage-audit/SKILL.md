---
name: data-lineage-audit
category: data
description: "Trace a reported number back to where it came from."
output: "lineage-report.md"
used_by:
  - chief-data-officer-agent
---

# Data Lineage Audit

**Category:** `data` · **Output artifact:** `lineage-report.md`

## What this skill does
Trace a reported number back to where it came from.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-data-officer-agent`.

## Procedure
1. Pick the headline numbers and trace each to its source table.
2. Document every transformation applied along the way.
3. Identify manual steps, which are where errors enter.
4. Verify the same number is computed identically wherever it appears.
5. Fix divergent computations at the source, not in the dashboard.

## Output contract
Write `lineage-report.md` into `workspace/<venture-id>/data/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** data-lineage-audit
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
- Manual steps identified
- Divergent computations fixed at source
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `data` category
- Two dashboards reporting the same metric with different definitions.
- Reporting an experiment result that never had the power to detect the effect.
- Collecting a field first and finding a purpose for it later.
