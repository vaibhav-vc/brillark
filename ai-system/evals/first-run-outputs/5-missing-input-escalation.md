# MVP scope — BLOCKED: required input missing

- **Skill:** mvp-scoping
- **Author agent:** mvp-scoper
- **Date:** 2026-09-14
- **Confidence:** guessed

## Summary

**I am not scoping this MVP. The riskiest-assumption analysis is a required input, not a nice-to-have,
and it has not been run.** `mvp-scoping`'s own procedure step 1 is "state the riskiest assumption the
venture depends on" — everything else in the procedure (what to cut, what to defer, what the smallest
disproving build looks like) is derived from that assumption. Without it there is no principled basis
for a scope line, only a guess wearing the shape of one. Escalating to `engineering-head` rather than
inventing an assumption to keep the deadline.

## Body

### Why this blocks rather than merely slows things down

The entire charter of this role is "draws the line between what ships now and what waits, **using
learning value as the only criterion**." Learning value is measured against the riskiest assumption:
a feature earns its place in the MVP only if it changes what the first users teach us about that
assumption. Remove the assumption and the criterion has nothing to point at — any scope line drawn
now would be justified after the fact by whatever assumption seems plausible in the moment, which is
exactly the improvisation this role exists to prevent (base-agent guardrail 5: escalate rather than
guess).

Concretely: if I scoped this MVP right now, I would have to silently pick an assumption to organize
the cuts around. That assumption might not be the one the Council or business-head actually consider
riskiest, and nobody downstream would know a substitution had happened — the scope line would look
authoritative while resting on an invented input.

### What I checked before escalating

- Confirmed no `rat-test.md` or equivalent artifact exists for this venture at the expected path.
- Confirmed this is not a case where the assumption was run and simply not handed to me — the task
  states plainly it "has not been run yet," so this is a sequencing gap, not a missing handoff.

### What happens instead

Per the escalation contract, a missing required input goes to `engineering-head` — either to commission
the riskiest-assumption analysis directly, or to confirm the sequencing (perhaps the analysis is
already scheduled and this scoping request arrived early). I am not producing a placeholder scope
line in the interim, because a placeholder that looks like a real scope line is more dangerous than an
explicit block: someone downstream may build against it.

## Evidence

| Claim | Source | Grade | Load-bearing |
|---|---|---|---|
| Riskiest-assumption analysis has not been run | stated directly in the task | measured | yes |
| No `rat-test.md` artifact exists for this venture | absence checked against expected artifact path | measured | yes |
| MVP scoping requires the riskiest assumption as its first input | `mvp-scoping` skill procedure, step 1 | sourced | yes |

## Open questions

1. Is the riskiest-assumption analysis scheduled, and if so when, or does it need to be commissioned
   now? — owner: `engineering-head`.
2. Once it exists, does the venture's timeline still allow the MVP scope to be built around it, or has
   schedule pressure already made that infeasible? — owner: `engineering-head`.

## Next action

**Escalate to `engineering-head`: commission the riskiest-assumption analysis, or confirm its
schedule, before MVP scoping proceeds.** No scope line is produced in this artifact. Owner:
`engineering-head`.
