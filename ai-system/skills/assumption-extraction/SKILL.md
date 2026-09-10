---
name: assumption-extraction
category: council
description: "Surface every assumption, including the invisible ones."
output: "assumption-list.md"
used_by:
  []
---

# Assumption Extraction

**Category:** `council` · **Output artifact:** `assumption-list.md`

## What this skill does
Surface every assumption, including the invisible ones.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: any agent (general-purpose skill).

## Procedure
1. Read the plan for stated assumptions.
2. Extract the unstated ones implied by the numbers, defaults, and structure.
3. Include assumptions about our own capability and speed.
4. Write each as a standalone claim that could be true or false.
5. Pass the list to grading and load-bearing analysis.

## Output contract
Write `assumption-list.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** assumption-extraction
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
- Unstated assumptions surfaced
- Each written as a testable claim
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
