---
name: contextual-inquiry
category: design
description: "Watch people do the real task in the real place, rather than asking them to describe it."
output: "inquiry-notes.md"
used_by:
  - design-researcher
---

# Contextual Inquiry

**Category:** `design` · **Output artifact:** `inquiry-notes.md`

## What this skill does
Watch people do the real task in the real place, rather than asking them to describe it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-researcher`.

## Procedure
1. Observe the task in its actual environment, with the participant's own data and tools.
2. Ask them to narrate as they work, and interrupt only to understand, never to correct.
3. Record the workarounds — they mark where the current solution fails.
4. Note interruptions, waiting, and context-switching; these rarely appear in interviews.
5. Debrief within the hour, while detail is still recoverable.

## Output contract
Write `inquiry-notes.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** contextual-inquiry
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
- Observation in the real environment with real data
- Workarounds recorded as primary findings
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
