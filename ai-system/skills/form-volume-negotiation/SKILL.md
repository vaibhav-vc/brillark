---
name: form-volume-negotiation
category: hardware
description: "Settle the internal volume envelope before anyone refines a surface."
output: "volume-envelope.md"
used_by:
  - industrial-designer
---

# Form Volume Negotiation

`hardware` · produces `volume-envelope.md` · used by `industrial-designer`

Settle the internal volume envelope before anyone refines a surface.

## Procedure
1. Collect the space each discipline needs: board, battery, connectors, thermal, and service.
2. Add clearance for tolerances, cable bend radii, and assembly access.
3. Draw the envelope as geometry all disciplines work against.
4. Negotiate conflicts explicitly rather than letting the last person to model win.
5. Freeze the envelope and treat changes to it as decisions with owners.

## Output contract
`volume-envelope.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Clearances and assembly access included
- Envelope frozen as shared geometry
- The output states its confidence grade and names the evidence behind every load-bearing claim.
