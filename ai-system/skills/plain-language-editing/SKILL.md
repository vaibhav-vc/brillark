---
name: plain-language-editing
category: design
description: "Cut the text down to what people will actually read."
output: "edited-copy.md"
used_by:
  - content-designer
---

# Plain Language Editing

**Category:** `design` · **Output artifact:** `edited-copy.md`

## What this skill does
Cut the text down to what people will actually read.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `content-designer`.

## Procedure
1. Replace jargon with the word a new user would use.
2. Break long sentences into one idea each.
3. Prefer active voice and concrete subjects.
4. Check reading level against the target audience.
5. Re-read for what can be deleted entirely rather than shortened.

## Output contract
Write `edited-copy.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** plain-language-editing
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
- Reading level within target
- Deletion preferred over compression
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
