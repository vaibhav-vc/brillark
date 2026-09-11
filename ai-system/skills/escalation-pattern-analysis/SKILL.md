---
name: escalation-pattern-analysis
category: orchestration
description: "Find the process defects behind repeated escalations."
output: "escalation-pattern-report.md"
used_by:
  - escalation-manager
---

# Escalation Pattern Analysis

`orchestration` · produces `escalation-pattern-report.md` · used by `escalation-manager`

Find the process defects behind repeated escalations.

## Procedure
1. Group escalations by root cause rather than by symptom or reporter.
2. Identify causes appearing three or more times.
3. Trace each recurring cause to the process step that permits it.
4. Propose a process change, not a reminder to try harder.
5. Verify next cycle whether the pattern actually stopped.

## Output contract
`escalation-pattern-report.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Grouping by cause, not symptom
- Fix targets the process, not individual effort
- The output states its confidence grade and names the evidence behind every load-bearing claim.
