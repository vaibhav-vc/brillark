---
name: escalation-rule-design
category: efficiency
description: "Define when a cheaper tier must hand up."
output: "escalation-rules.md"
used_by:
  - model-router-tuner
---

# Escalation Rule Design

`efficiency` · produces `escalation-rules.md` · used by `model-router-tuner`

Define when a cheaper tier must hand up.

## Procedure
1. Identify the conditions the cheaper tier handles badly.
2. Write each as an observable trigger, not a judgement call.
3. Define what the escalating agent passes up.
4. Set the expected escalation frequency and what an excess means.
5. Test the rule fires when it should before relying on it.

## Output contract
`escalation-rules.md` → `workspace/<venture-id>/efficiency/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/efficiency.tsv`.

## Quality bar
- Triggers observable, not judgement calls
- Expected frequency stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
