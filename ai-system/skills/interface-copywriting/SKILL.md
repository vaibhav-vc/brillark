---
name: interface-copywriting
category: design
description: "Write the words in the product so they do the explaining."
output: "interface-copy.md"
used_by:
  - content-designer
---

# Interface Copywriting

**Category:** `design` · **Output artifact:** `interface-copy.md`

## What this skill does
Write the words in the product so they do the explaining.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `content-designer`.

## Procedure
1. Write the label for what the user is trying to do, not for what the system does.
2. Front-load the meaningful word so scanning works.
3. Cut every word that does not change the user's next action.
4. Use the vocabulary from research and the glossary.
5. Read it aloud; awkward copy is usually ambiguous copy.

## Output contract
Write `interface-copy.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** interface-copywriting
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
- Labels named for user intent
- Every word changes the next action
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
