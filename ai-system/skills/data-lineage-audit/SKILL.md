---
name: data-lineage-audit
category: data
description: "Trace a reported number back to where it came from."
output: "lineage-report.md"
used_by:
  - chief-data-officer-agent
---

# Data Lineage Audit

`data` · produces `lineage-report.md` · used by `chief-data-officer-agent`

Trace a reported number back to where it came from.

## Procedure
1. Pick the headline numbers and trace each to its source table.
2. Document every transformation applied along the way.
3. Identify manual steps, which are where errors enter.
4. Verify the same number is computed identically wherever it appears.
5. Fix divergent computations at the source, not in the dashboard.

## Output contract
`lineage-report.md` → `workspace/<venture-id>/data/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/data.tsv`.

## Quality bar
- Manual steps identified
- Divergent computations fixed at source
- The output states its confidence grade and names the evidence behind every load-bearing claim.
