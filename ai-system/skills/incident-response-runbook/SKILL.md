---
name: incident-response-runbook
category: engineering
description: "Prepare so an incident is executed rather than improvised."
output: "incident-runbook.md"
used_by:
  - ciso-agent
---

# Incident Response Runbook

`engineering` · produces `incident-runbook.md` · used by `ciso-agent`

Prepare so an incident is executed rather than improvised.

## Procedure
1. Define severity levels and what each triggers.
2. Define roles: incident lead, communications, and investigator.
3. Write the first ten minutes as concrete steps.
4. Define customer and regulator communication thresholds and templates.
5. Rehearse it; an untested runbook does not count.

## Output contract
`incident-runbook.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- First ten minutes scripted concretely
- Runbook rehearsed, not just written
- The output states its confidence grade and names the evidence behind every load-bearing claim.
