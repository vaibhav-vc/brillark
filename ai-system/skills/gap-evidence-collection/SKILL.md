---
name: gap-evidence-collection
category: improvement
description: "Prove the gap is real before proposing to fill it."
output: "gap-evidence.md"
used_by:
  - capability-gap-scout
---

# Gap Evidence Collection

`improvement` · produces `gap-evidence.md` · used by `capability-gap-scout`

Prove the gap is real before proposing to fill it.

## Procedure
1. Collect escalations that found no owner.
2. Collect cases where an agent improvised outside its skills.
3. Collect failures traced to a missing capability.
4. Require at least three independent instances.
5. Estimate what the gap costs per cycle.

## Output contract
`gap-evidence.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Three independent instances required
- Cost of the gap estimated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
