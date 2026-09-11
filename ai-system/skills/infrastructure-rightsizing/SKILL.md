---
name: infrastructure-rightsizing
category: engineering
description: "Match provisioned capacity to actual demand."
output: "rightsizing-report.md"
used_by:
  - cost-optimization-analyst
  - infra-devops-agent
---

# Infrastructure Rightsizing

`engineering` · produces `rightsizing-report.md` · used by `cost-optimization-analyst`, `infra-devops-agent`

Match provisioned capacity to actual demand.

## Procedure
1. Measure actual utilisation over a representative period, including peaks.
2. Identify idle, over-provisioned, and orphaned resources.
3. Distinguish waste from headroom deliberately held for spikes.
4. Resize incrementally and verify performance after each change.
5. Set alerts so drift is caught before it accumulates.

## Output contract
`rightsizing-report.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Headroom distinguished from waste
- Performance verified after each change
- The output states its confidence grade and names the evidence behind every load-bearing claim.
