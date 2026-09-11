---
name: error-message-design
category: design
description: "Write errors that let the user recover."
output: "error-catalogue.md"
used_by:
  - content-designer
---

# Error Message Design

**Category:** `design` · **Output artifact:** `error-catalogue.md`

## What this skill does
Write errors that let the user recover.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `content-designer`.

## Procedure
1. Say what happened in plain language, without codes as the primary message.
2. Say why, when the reason helps the user act.
3. Give the specific next action, and make it doable from where they are.
4. Never blame the user, and never expose internal detail.
5. Keep a reference identifier available but secondary, for support.

## Output contract
Write `error-catalogue.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** error-message-design
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
- Every message offers a doable next action
- No blame and no internal detail exposed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
