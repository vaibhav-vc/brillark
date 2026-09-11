---
name: control-framework-design
category: compliance
description: "Build the controls that make compliance demonstrable."
output: "control-framework.md"
used_by:
  - chief-compliance-officer-agent
---

# Control Framework Design

`compliance` · produces `control-framework.md` · used by `chief-compliance-officer-agent`

Build the controls that make compliance demonstrable.

## Procedure
1. Map each applicable requirement to exactly one control.
2. Design the control to be evidenced automatically where possible.
3. Assign an owner and an operating frequency to each control.
4. Define what evidence proves the control operated.
5. Avoid duplicate controls serving the same requirement.

## Output contract
`control-framework.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- One control per requirement
- Evidence definition per control
- The output states its confidence grade and names the evidence behind every load-bearing claim.
