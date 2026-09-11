---
name: touchpoint-instrumentation
category: design
description: "Measure the service where the customer actually experiences it."
output: "instrumentation-plan.md"
used_by:
  - service-designer
---

# Touchpoint Instrumentation

`design` · produces `instrumentation-plan.md` · used by `service-designer`

Measure the service where the customer actually experiences it.

## Procedure
1. Identify the touchpoints that most determine the customer's judgement.
2. Define a measure for each: completion, wait, effort, or resolution.
3. Instrument at the touchpoint rather than inferring from downstream data.
4. Set thresholds that trigger investigation.
5. Review the measures against qualitative feedback so numbers stay grounded.

## Output contract
`instrumentation-plan.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Measured at the touchpoint, not inferred
- Thresholds trigger investigation
- The output states its confidence grade and names the evidence behind every load-bearing claim.
