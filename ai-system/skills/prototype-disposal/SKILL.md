---
name: prototype-disposal
category: design
description: "Retire the prototype instead of letting it become the product."
output: "disposal-note.md"
used_by:
  - prototyper
---

# Prototype Disposal

**Category:** `design` · **Output artifact:** `disposal-note.md`

## What this skill does
Retire the prototype instead of letting it become the product.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `prototyper`.

## Procedure
1. Record the answer the prototype produced.
2. Extract the learnings into the design spec.
3. Archive or delete the artifact rather than extending it.
4. Resist reusing prototype code in production; its shortcuts are invisible later.
5. Note if any part is genuinely production-worthy and why.

## Output contract
Write `disposal-note.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** prototype-disposal
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
- Learnings extracted into the spec
- Prototype not promoted into production
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
