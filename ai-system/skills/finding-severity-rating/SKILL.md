---
name: finding-severity-rating
category: design
description: "Rate usability findings so the team fixes the right ones first."
output: "severity-ratings.md"
used_by:
  - usability-tester
---

# Finding Severity Rating

**Category:** `design` · **Output artifact:** `severity-ratings.md`

## What this skill does
Rate usability findings so the team fixes the right ones first.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `usability-tester`.

## Procedure
1. Rate by consequence: does it block the task, cost time, or merely annoy?
2. Factor in frequency — how many users hit it, how often.
3. Distinguish comprehension failures from discoverability failures.
4. Rate consistently against prior rounds so trends mean something.
5. Attach the observed evidence to each rating.

## Output contract
Write `severity-ratings.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** finding-severity-rating
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
- Consequence and frequency both factored
- Comprehension separated from discoverability
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
