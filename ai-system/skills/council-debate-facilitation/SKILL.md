---
name: council-debate-facilitation
category: council
description: "Run a structured debate that produces a decision."
output: "debate-record.md"
used_by:
  - council-director
---

# Council Debate Facilitation

`council` · produces `debate-record.md` · used by `council-director`

Run a structured debate that produces a decision.

## Procedure
1. Accept the submission only with a stated decision, evidence, and deadline.
2. Assign roles, including at least one critic arguing in favour.
3. Run rounds: claim, challenge, evidence, rebuttal.
4. Cut off arguments that cannot be made falsifiable.
5. Close on time with a verdict, never with an adjournment.

## Output contract
`debate-record.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Someone assigned to argue in favour
- Closed on time with a verdict
- The output states its confidence grade and names the evidence behind every load-bearing claim.
