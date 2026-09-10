---
name: incident-response-runbook
category: engineering
description: "Prepare so an incident is executed rather than improvised."
output: "incident-runbook.md"
used_by:
  - ciso-agent
---

# Incident Response Runbook

**Category:** `engineering` · **Output artifact:** `incident-runbook.md`

## What this skill does
Prepare so an incident is executed rather than improvised.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ciso-agent`.

## Procedure
1. Define severity levels and what each triggers.
2. Define roles: incident lead, communications, and investigator.
3. Write the first ten minutes as concrete steps.
4. Define customer and regulator communication thresholds and templates.
5. Rehearse it; an untested runbook does not count.

## Output contract
Write `incident-runbook.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** incident-response-runbook
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
- First ten minutes scripted concretely
- Runbook rehearsed, not just written
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
