---
name: origin-story-development
category: gtm
description: "Capture why the founders started this, credibly."
output: "origin-story.md"
used_by:
  - brand-narrative-agent
---

# Origin Story Development

**Category:** `gtm` · **Output artifact:** `origin-story.md`

## What this skill does
Capture why the founders started this, credibly.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-narrative-agent`.

## Procedure
1. Establish the founder's direct experience of the problem.
2. Describe the specific moment the decision was made.
3. Explain the insight others missed and why the founder saw it.
4. Keep it true — investors and journalists verify these.
5. Compress to a version that survives being retold by others.

## Output contract
Write `origin-story.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** origin-story-development
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
- Verifiably true in every detail
- Compressed to a retellable form
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
