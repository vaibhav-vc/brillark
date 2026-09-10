---
name: sales-playbook
category: gtm
description: "Write down how selling works so someone other than the founder can do it."
output: "sales-playbook.md"
used_by:
  - chief-revenue-officer-agent
  - sales-playbook-agent
---

# Sales Playbook

**Category:** `gtm` · **Output artifact:** `sales-playbook.md`

## What this skill does
Write down how selling works so someone other than the founder can do it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-revenue-officer-agent`, `sales-playbook-agent`.

## Procedure
1. Document the stages, their exit criteria, and the typical duration.
2. Write the discovery script that diagnoses before prescribing.
3. Include the qualification and disqualification rules.
4. Attach the proof asset for each common objection.
5. Test it by having someone new run a real deal with it.

## Output contract
Write `sales-playbook.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** sales-playbook
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
- Exit criteria are buyer actions
- Tested by someone new to the deal
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
