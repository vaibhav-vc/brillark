---
name: cicd-pipeline-design
category: engineering
description: "Build a pipeline that makes shipping safe and boring."
output: "pipeline.md"
used_by:
  - infra-devops-agent
---

# Cicd Pipeline Design

**Category:** `engineering` · **Output artifact:** `pipeline.md`

## What this skill does
Build a pipeline that makes shipping safe and boring.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `infra-devops-agent`.

## Procedure
1. Define the stages and what each gate proves.
2. Make builds reproducible and artifacts immutable.
3. Run fast checks first so failures surface early.
4. Gate on tests, security scanning, and budget checks.
5. Keep total pipeline time short enough that people do not route around it.

## Output contract
Write `pipeline.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cicd-pipeline-design
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
- Artifacts immutable and reproducible
- Pipeline fast enough to not be bypassed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
