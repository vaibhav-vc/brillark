---
name: ask-framing
category: council
description: "Make a request specific enough to be acted on."
output: "ask.md"
used_by:
  - investor-reporting-agent
---

# Ask Framing

**Category:** `council` · **Output artifact:** `ask.md`

## What this skill does
Make a request specific enough to be acted on.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `investor-reporting-agent`.

## Procedure
1. State exactly what you need: a decision, an introduction, or a resource.
2. Name the person or role who can provide it.
3. State why it matters and what it unblocks.
4. State the deadline and what happens without it.
5. Make it small enough that saying yes is easy.

## Output contract
Write `ask.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** ask-framing
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
- Names the specific person or role
- Deadline and consequence stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
