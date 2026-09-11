---
name: cmf-specification
category: hardware
description: "Specify colour, material, and finish so the factory produces what was designed."
output: "cmf-spec.md"
used_by:
  - industrial-designer
---

# Cmf Specification

`hardware` · produces `cmf-spec.md` · used by `industrial-designer`

Specify colour, material, and finish so the factory produces what was designed.

## Procedure
1. Specify each material by grade and supplier, not by generic name.
2. Specify finish by process and measurable parameter, including texture standard.
3. Specify colour against a physical standard with a stated tolerance.
4. Check every finish for wear, UV, and chemical exposure in real use.
5. Approve against physical samples from the production process.

## Output contract
`cmf-spec.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Colour and texture tied to physical standards
- Approved against production-process samples
- The output states its confidence grade and names the evidence behind every load-bearing claim.
