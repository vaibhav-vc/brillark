---
name: discovery-call-script
category: gtm
description: "Structure the first call to diagnose rather than pitch."
output: "discovery-script.md"
used_by:
  - sales-playbook-agent
---

# Discovery Call Script

**Category:** `gtm` · **Output artifact:** `discovery-script.md`

## What this skill does
Structure the first call to diagnose rather than pitch.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `sales-playbook-agent`.

## Procedure
1. Open by establishing the agenda and the time available.
2. Ask about the current situation and the trigger that prompted the call.
3. Quantify the problem in the customer's own metrics.
4. Confirm the decision process and who else is involved.
5. Close with a specific, agreed next step — never 'I'll follow up'.

## Output contract
Write `discovery-script.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** discovery-call-script
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
- Problem quantified in customer metrics
- Specific next step agreed on the call
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
