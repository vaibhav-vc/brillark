---
name: self-modification-policy
category: improvement
description: "Define what the system may change about itself without human approval."
output: "self-modification-policy.md"
used_by:
  - chief-learning-officer-agent
---

# Self Modification Policy

**Category:** `improvement` · **Output artifact:** `self-modification-policy.md`

## What this skill does
Define what the system may change about itself without human approval.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-learning-officer-agent`.

## Procedure
1. List the artifact classes: prompts, skills, workflows, guardrails, schemas, org shape, evaluation criteria.
2. Permit automatic change only for prompts and skill steps, and only with a passing trial.
3. Require director approval for workflows and agent charters.
4. Require human founder approval for guardrails, schemas, org shape, and evaluation criteria.
5. Log every change with its authorisation level and refuse unauthorised ones.

## Output contract
Write `self-modification-policy.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** self-modification-policy
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
- Evaluation criteria never self-modifiable
- Every change logged with its authorisation level
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
