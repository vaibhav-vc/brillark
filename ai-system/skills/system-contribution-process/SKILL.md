---
name: system-contribution-process
category: design
description: "Define how a component enters the system."
output: "contribution-record.md"
used_by:
  - design-system-architect
---

# System Contribution Process

**Category:** `design` · **Output artifact:** `contribution-record.md`

## What this skill does
Define how a component enters the system.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `design-system-architect`.

## Procedure
1. Require evidence the need appeared at least three times.
2. Define the review: accessibility, tokens, states, documentation, and code parity.
3. Assign a maintainer before accepting the contribution.
4. Require a usage example and a migration note for anything it replaces.
5. Publish the addition so consumers discover it rather than rebuilding it.

## Output contract
Write `contribution-record.md` into `workspace/<venture-id>/design/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** system-contribution-process
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
- Three-occurrence evidence required
- Maintainer assigned before acceptance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `design` category
- Designing the showcase case with three tidy items instead of the dense case with real data.
- Treating accessibility as remediation after launch rather than a build requirement.
- Critique that asserts preference where the goal was never stated.
