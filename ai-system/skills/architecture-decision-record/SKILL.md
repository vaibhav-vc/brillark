---
name: architecture-decision-record
category: engineering
description: "Record a technical decision with the alternatives and the trade-offs."
output: "adr.md"
used_by:
  - cto-agent
  - engineering-head
  - system-architect
---

# Architecture Decision Record

**Category:** `engineering` · **Output artifact:** `adr.md`

## What this skill does
Record a technical decision with the alternatives and the trade-offs.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cto-agent`, `engineering-head`, `system-architect`.

## Procedure
1. State the decision and its status in one line.
2. Describe the context: the forces and constraints in play.
3. List the options considered, with the genuine case for each.
4. State the decision and the consequences accepted, including negative ones.
5. Name what would make this decision wrong and worth revisiting.

## Output contract
Write `adr.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** architecture-decision-record
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
- At least two genuine alternatives recorded
- Negative consequences stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
