---
name: dashboard-design
category: engineering
description: "Build dashboards that answer a specific question."
output: "dashboard-spec.md"
used_by:
  - observability-agent
---

# Dashboard Design

`engineering` · produces `dashboard-spec.md` · used by `observability-agent`

Build dashboards that answer a specific question.

## Procedure
1. State the one question the dashboard answers before building it.
2. Show the metric, its target, and its trend together.
3. Order panels by the sequence a person would investigate.
4. Remove panels nobody looks at during real incidents.
5. Name the audience and the decision it supports.

## Output contract
`dashboard-spec.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- One named question per dashboard
- Unused panels removed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
