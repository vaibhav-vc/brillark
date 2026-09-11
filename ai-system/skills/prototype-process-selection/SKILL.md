---
name: prototype-process-selection
category: hardware
description: "Choose how to make the prototype from what it must prove."
output: "prototype-process.md"
used_by:
  - prototyping-fabrication-agent
---

# Prototype Process Selection

`hardware` · produces `prototype-process.md` · used by `prototyping-fabrication-agent`

Choose how to make the prototype from what it must prove.

## Procedure
1. State what the prototype must demonstrate: form, fit, function, or process.
2. Match the process to that: printing for form, machining for fit, tooling for process.
3. Check the process's material properties actually support the conclusion.
4. Balance lead time against fidelity for the question at hand.
5. State explicitly what conclusions this prototype cannot support.

## Output contract
`prototype-process.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Process matched to what must be proven
- Unsupportable conclusions stated explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
