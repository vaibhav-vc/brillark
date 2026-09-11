---
name: copy-comprehension-testing
category: design
description: "Check that people understand the words before shipping them."
output: "comprehension-results.md"
used_by:
  - content-designer
---

# Copy Comprehension Testing

**Category:** `design` · **Output artifact:** `comprehension-results.md`

## What this skill does
Check that people understand the words before shipping them.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `content-designer`.

## Procedure
1. Show the copy to people outside the team who match the audience.
2. Ask what they think it means and what they would do next.
3. Note every misreading; a single misreading usually predicts many.
4. Rewrite and retest rather than explaining the original.
5. Test the error and empty-state copy too, not just the happy path.

## Output contract
Write `comprehension-results.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** copy-comprehension-testing
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
- Tested with people outside the team
- Misreadings rewritten and retested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
