---
name: self-modification-policy
category: improvement
description: "Define what the system may change about itself without human approval."
output: "self-modification-policy.md"
used_by:
  - chief-learning-officer-agent
---

# Self Modification Policy

`improvement` · produces `self-modification-policy.md` · used by `chief-learning-officer-agent`

Define what the system may change about itself without human approval.

## Procedure
1. List the artifact classes: prompts, skills, workflows, guardrails, schemas, org shape, evaluation criteria.
2. Permit automatic change only for prompts and skill steps, and only with a passing trial.
3. Require director approval for workflows and agent charters.
4. Require human founder approval for guardrails, schemas, org shape, and evaluation criteria.
5. Log every change with its authorisation level and refuse unauthorised ones.

## Output contract
`self-modification-policy.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Evaluation criteria never self-modifiable
- Every change logged with its authorisation level
- The output states its confidence grade and names the evidence behind every load-bearing claim.
