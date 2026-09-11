---
name: golden-case-curation
category: orchestration
description: "Maintain the reference examples that define good output."
output: "golden-cases.md"
used_by:
  - benchmark-curator
  - evaluation-harness-agent
---

# Golden Case Curation

**Category:** `orchestration` · **Output artifact:** `golden-cases.md`

## What this skill does
Maintain the reference examples that define good output.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `benchmark-curator`, `evaluation-harness-agent`.

## Procedure
1. Choose cases that discriminate — a case everything passes teaches nothing.
2. Include at least one historical failure per agent.
3. Record why each case's expected output is correct.
4. Review annually and retire cases that no longer discriminate.
5. Keep the set small enough to run on every change.

## Output contract
Write `golden-cases.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** golden-case-curation
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
- Every case discriminates
- Historical failures represented
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
