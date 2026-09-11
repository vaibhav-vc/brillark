---
name: message-hierarchy
category: gtm
description: "Structure the message from headline claim to supporting proof."
output: "message-hierarchy.md"
used_by:
  - positioning-messaging-agent
---

# Message Hierarchy

`gtm` · produces `message-hierarchy.md` · used by `positioning-messaging-agent`

Structure the message from headline claim to supporting proof.

## Procedure
1. State one headline claim; more than one means none will land.
2. Support it with at most three pillars.
3. Attach specific proof under each pillar.
4. Write the version for each audience without changing the spine.
5. Cut anything that does not support the headline.

## Output contract
`message-hierarchy.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Exactly one headline claim
- Proof attached to every pillar
- The output states its confidence grade and names the evidence behind every load-bearing claim.
