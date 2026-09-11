---
name: rapid-prototyping
category: design
description: "Build the testable artifact fast, without building the product."
output: "prototype"
used_by:
  - prototyper
---

# Rapid Prototyping

**Category:** `design` · **Output artifact:** `prototype`

## What this skill does
Build the testable artifact fast, without building the product.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `prototyper`.

## Procedure
1. Build only the path under test and stub everything else visibly.
2. Use real content and realistic data volumes.
3. Fake the backend rather than building it.
4. Stop as soon as the artifact can answer the question.
5. Note every shortcut so results are not over-read.

## Output contract
Write `prototype` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** rapid-prototyping
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
- Only the tested path built
- Shortcuts documented so results are read correctly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
