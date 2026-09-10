---
name: positioning-statement
category: gtm
description: "Decide what the product is in the customer's mind."
output: "positioning.md"
used_by:
  - business-head
  - cmo-agent
  - positioning-messaging-agent
---

# Positioning Statement

**Category:** `gtm` · **Output artifact:** `positioning.md`

## What this skill does
Decide what the product is in the customer's mind.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-head`, `cmo-agent`, `positioning-messaging-agent`.

## Procedure
1. Choose the frame of reference: what category the customer files you under.
2. State for whom, unlike what, and why better.
3. Use the customer's vocabulary from interviews.
4. Check that the claim is provable and the frame is one we can win.
5. Test the statement with real prospects before adopting it.

## Output contract
Write `positioning.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** positioning-statement
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
- Frame of reference chosen deliberately
- Statement tested with real prospects
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
