---
name: narrative-one-pager
category: strategy
description: "Compress the whole company onto one page a new person could absorb."
output: "one-pager.md"
used_by:
  - ceo-agent
---

# Narrative One Pager

**Category:** `strategy` · **Output artifact:** `one-pager.md`

## What this skill does
Compress the whole company onto one page a new person could absorb.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ceo-agent`.

## Procedure
1. State who we serve, what problem, and why it matters.
2. State what we do and why it is different.
3. Include the current stage and the next milestone.
4. Include the numbers that matter most, current as of a stated date.
5. Test it on someone unfamiliar and fix what they misunderstand.

## Output contract
Write `one-pager.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** narrative-one-pager
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
- Tested on an unfamiliar reader
- Numbers dated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
