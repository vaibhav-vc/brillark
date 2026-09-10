---
name: role-scorecard
category: people
description: "Define a role by the outcomes it must produce."
output: "role-scorecard.md"
used_by:
  - chro-agent
---

# Role Scorecard

**Category:** `people` · **Output artifact:** `role-scorecard.md`

## What this skill does
Define a role by the outcomes it must produce.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chro-agent`.

## Procedure
1. State the mission of the role in one sentence.
2. List three to five outcomes with measures and timeframes.
3. List the competencies required to achieve those outcomes.
4. Distinguish must-haves from developable skills.
5. Write it before the job advertisement, and hire against it.

## Output contract
Write `role-scorecard.md` into `workspace/<venture-id>/people/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** role-scorecard
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
- Outcomes measurable with timeframes
- Written before the job advertisement
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `people` category
- Writing a job advertisement before writing the outcomes the role must produce.
- Assessing candidates on different evidence and calling it judgement.
- Hiring to relieve a bottleneck that process or tooling would fix faster.
