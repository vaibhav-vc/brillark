---
name: rubric-writing
category: orchestration
description: "Define scoring criteria that different reviewers apply the same way."
output: "rubric.md"
used_by:
  - evaluation-harness-agent
---

# Rubric Writing

**Category:** `orchestration` · **Output artifact:** `rubric.md`

## What this skill does
Define scoring criteria that different reviewers apply the same way.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `evaluation-harness-agent`.

## Procedure
1. Define the dimensions being scored and keep them independent.
2. Write anchor descriptions for each score level, with examples.
3. Test inter-rater agreement on a sample before adopting it.
4. Remove dimensions where reviewers disagree persistently.
5. Version the rubric and re-test when it changes.

## Output contract
Write `rubric.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** rubric-writing
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
- Anchors have concrete examples
- Inter-rater agreement tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
