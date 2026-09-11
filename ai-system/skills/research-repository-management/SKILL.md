---
name: research-repository-management
category: design
description: "Keep past research findable so the next project does not re-run it."
output: "repository-entry.md"
used_by:
  - design-researcher
---

# Research Repository Management

**Category:** `design` · **Output artifact:** `repository-entry.md`

## What this skill does
Keep past research findable so the next project does not re-run it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-researcher`.

## Procedure
1. Tag every finding by topic, segment, product area, and date.
2. Store the evidence alongside the conclusion, not just the conclusion.
3. Record the study's method and limits so reuse is judged fairly.
4. Check the repository before commissioning new research.
5. Expire findings whose conditions have changed rather than leaving them to mislead.

## Output contract
Write `repository-entry.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** research-repository-management
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
- Evidence stored with each conclusion
- Repository checked before new research is commissioned
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
