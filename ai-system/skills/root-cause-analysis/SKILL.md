---
name: root-cause-analysis
category: orchestration
description: "Trace a failure back to the cause that can actually be changed."
output: "root-cause-analysis.md"
used_by:
  - retrospective-agent
---

# Root Cause Analysis

`orchestration` · produces `root-cause-analysis.md` · used by `retrospective-agent`

Trace a failure back to the cause that can actually be changed.

## Procedure
1. Establish the factual timeline before interpreting anything.
2. Ask why repeatedly, stopping at the first cause under our control.
3. Distinguish the trigger from the underlying condition that allowed it.
4. Check for multiple contributing causes; single-cause stories are usually incomplete.
5. Propose a change to the condition, not a reminder to be careful.

## Output contract
`root-cause-analysis.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Timeline established before analysis
- Fix targets the enabling condition
- The output states its confidence grade and names the evidence behind every load-bearing claim.
