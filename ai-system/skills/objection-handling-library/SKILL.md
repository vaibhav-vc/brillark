---
name: objection-handling-library
category: gtm
description: "Build evidenced answers to the objections that actually lose deals."
output: "objection-library.md"
used_by:
  - sales-playbook-agent
---

# Objection Handling Library

**Category:** `gtm` · **Output artifact:** `objection-library.md`

## What this skill does
Build evidenced answers to the objections that actually lose deals.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `sales-playbook-agent`.

## Procedure
1. Collect objections from lost-deal records, not from imagination.
2. Rank by frequency and by how often they end the deal.
3. Write the answer for each, grounded in proof rather than reassurance.
4. Attach the specific asset — data, case study, or reference.
5. Review quarterly and retire objections the product has fixed.

## Output contract
Write `objection-library.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** objection-handling-library
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
- Objections sourced from lost deals
- Each answer carries a proof asset
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
