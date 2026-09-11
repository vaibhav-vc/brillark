---
name: loop-instrumentation
category: gtm
description: "Measure a growth loop so optimisation is not guesswork."
output: "loop-instrumentation.md"
used_by:
  - growth-loop-designer
---

# Loop Instrumentation

`gtm` · produces `loop-instrumentation.md` · used by `growth-loop-designer`

Measure a growth loop so optimisation is not guesswork.

## Procedure
1. Define an event for every step of the loop.
2. Instrument step conversion and step duration separately.
3. Attribute new users back to the loop step that produced them.
4. Build the dashboard that shows amplification over time.
5. Verify the instrumentation against a known cohort before trusting it.

## Output contract
`loop-instrumentation.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Duration measured alongside conversion
- Instrumentation validated against a known cohort
- The output states its confidence grade and names the evidence behind every load-bearing claim.
