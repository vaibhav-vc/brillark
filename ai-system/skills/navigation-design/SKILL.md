---
name: navigation-design
category: design
description: "Design how people move through the product and know where they are."
output: "navigation-spec.md"
used_by:
  - information-architect
---

# Navigation Design

**Category:** `design` · **Output artifact:** `navigation-spec.md`

## What this skill does
Design how people move through the product and know where they are.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `information-architect`.

## Procedure
1. Design for the paths users actually take, which usually begin with search.
2. Keep the primary navigation to what most users need most often.
3. Make the current location obvious at every depth.
4. Provide a way back and a way up that always works.
5. Validate with tree testing before committing the structure.

## Output contract
Write `navigation-spec.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** navigation-design
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
- Primary navigation limited to common needs
- Structure validated by tree test
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
