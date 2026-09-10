---
name: data-room-preparation
category: finance
description: "Assemble everything diligence will ask for, before it is asked for."
output: "data-room-index.md"
used_by:
  - fundraising-strategist
---

# Data Room Preparation

**Category:** `finance` · **Output artifact:** `data-room-index.md`

## What this skill does
Assemble everything diligence will ask for, before it is asked for.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `fundraising-strategist`.

## Procedure
1. Build the index from a standard diligence checklist.
2. Collect corporate, financial, legal, technical, and commercial documents.
3. Reconcile the numbers across documents before anyone else does.
4. Identify the gaps and the issues, and prepare the explanation.
5. Control access and track what each party has seen.

## Output contract
Write `data-room-index.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** data-room-preparation
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
- Cross-document numbers reconciled
- Known issues prepared, not hidden
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
