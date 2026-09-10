---
name: dependency-failure-analysis
category: engineering
description: "Decide what happens when each external dependency fails."
output: "dependency-failure-plan.md"
used_by:
  - system-architect
---

# Dependency Failure Analysis

**Category:** `engineering` · **Output artifact:** `dependency-failure-plan.md`

## What this skill does
Decide what happens when each external dependency fails.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `system-architect`.

## Procedure
1. List every external dependency and what it provides.
2. For each, define the behaviour when it is slow, wrong, or absent.
3. Choose a strategy: fail fast, degrade, cache, or queue.
4. Set timeouts and retry policy deliberately, with backoff.
5. Test the failure behaviour rather than assuming it.

## Output contract
Write `dependency-failure-plan.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** dependency-failure-analysis
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
- Behaviour defined for slow as well as absent
- Failure behaviour actually tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
