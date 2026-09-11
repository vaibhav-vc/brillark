---
name: terminology-governance
category: design
description: "Keep one name per concept across every surface."
output: "terminology-record.md"
used_by:
  - content-designer
---

# Terminology Governance

**Category:** `design` · **Output artifact:** `terminology-record.md`

## What this skill does
Keep one name per concept across every surface.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `content-designer`.

## Procedure
1. Check the glossary before introducing any new term.
2. Add new terms with their definition and rejected alternatives.
3. Audit surfaces for drift between the glossary and reality.
4. Coordinate renames across product, docs, marketing, and support together.
5. Record the rename so support can recognise the old term.

## Output contract
Write `terminology-record.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** terminology-governance
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
- Glossary checked before new terms
- Renames coordinated across all surfaces
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
