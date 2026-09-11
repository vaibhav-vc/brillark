---
name: business-continuity-plan
category: risk
description: "Plan for continuing to operate through a serious disruption."
output: "continuity-plan.md"
used_by:
  - chief-risk-officer-agent
---

# Business Continuity Plan

`risk` · produces `continuity-plan.md` · used by `chief-risk-officer-agent`

Plan for continuing to operate through a serious disruption.

## Procedure
1. Identify the functions that must continue and their maximum tolerable downtime.
2. Identify the dependencies each requires: people, systems, and suppliers.
3. Define the alternative arrangement for each dependency.
4. Define activation triggers and who declares them.
5. Test the plan; an untested continuity plan is a document, not a capability.

## Output contract
`continuity-plan.md` → `workspace/<venture-id>/risk/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/risk.tsv`.

## Quality bar
- Maximum tolerable downtime defined per function
- Plan tested, not just written
- The output states its confidence grade and names the evidence behind every load-bearing claim.
