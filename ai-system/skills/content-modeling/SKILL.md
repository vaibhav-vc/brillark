---
name: content-modeling
category: design
description: "Define the content types and their relationships before designing pages."
output: "content-model.md"
used_by:
  - information-architect
---

# Content Modeling

**Category:** `design` · **Output artifact:** `content-model.md`

## What this skill does
Define the content types and their relationships before designing pages.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `information-architect`.

## Procedure
1. Identify the content types and the fields each genuinely needs.
2. Define the relationships between types and their cardinality.
3. Separate content from presentation so it can be reused across surfaces.
4. Define which fields are required and what happens when optional ones are absent.
5. Check the model against every surface that will consume it.

## Output contract
Write `content-model.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** content-modeling
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
- Content separated from presentation
- Absent-optional-field behaviour defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
