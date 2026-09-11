---
name: new-agent-justification
category: improvement
description: "Justify a new agent by the accountability nobody currently holds."
output: "agent-proposal.md"
used_by:
  - capability-gap-scout
---

# New Agent Justification

`improvement` · produces `agent-proposal.md` · used by `capability-gap-scout`

Justify a new agent by the accountability nobody currently holds.

## Procedure
1. Name the outcome the new agent would own that no agent owns today.
2. Show why it cannot sit with an existing agent without overloading it.
3. Define its charter, escalation, and definition of done.
4. State the coordination cost it adds.
5. Submit for director approval; the org shape is not self-modifiable.

## Output contract
`agent-proposal.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Unowned outcome named explicitly
- Coordination cost stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
