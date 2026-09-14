# Council verdict — laundro business model, stage gate: business-model

- **Skill:** verdict-writing
- **Author agent:** council-director
- **Date:** 2026-09-11
- **Confidence:** estimated

## Summary

**Verdict: reject.** The Council was convened to review a business model and found that no business
model exists to review: five of the seven preceding steps are blocked and the sizing step has been
invalidated. The venture's stated market gap — that commercial linen hire cannot serve a host with
one to three properties — is contradicted by advertised Manchester offers, and the venture brief
itself records `why_us: "Nothing yet"`. Rejection here is not a judgement that the idea is dead; it
is a refusal to let a stage gate be passed by a run that never completed, and it names the three
things that would let the founder resubmit.

## Body

### What the Council was actually handed

| Step | State |
|---|---|
| `size` | **invalidated** — completed, then contradicted by `competition` |
| `competition` | done |
| `jobs`, `value`, `model` | blocked by `competition` |
| `pricing`, `economics` | blocked by `size`, which is itself invalidated |

Two of eight steps produced an artifact. One of those two has been superseded. The `requested_decision`
attached to this review is a spend authorisation against `success_looks_like` in `venture.yaml`.

The orchestrator handed this state to the Council as mandatory input. That is worth recording,
because the first version of this system would have offered the Council the final step of a broken
run with no indication that anything was wrong.

### Where the ten critics landed

**`council-first-principles`** — strip it back and the venture is: buy linen, wash it, drive it
around a postcode cluster. There is no step in that chain that a competitor cannot also perform, and
at least one Manchester competitor already performs all of it. What is necessary here is a reason the
founder wins a route-density race against an incumbent who already has the vans.

**`council-economics-skeptic`** — the sizing's revenue layers all scale linearly with a £18
per-turnover figure that no host has been asked about and that sits roughly 2.7× above an
incumbent's advertised pack price. Note the arithmetic hazard: the two figures are not directly
comparable (packs per turnover is unestablished), so the honest statement is not "the price is
wrong" but "the price now has a market reference point and nobody has computed the conversion."
Until someone does, every number downstream is unfalsifiable rather than merely uncertain.

**`council-assumption-auditor`** — the load-bearing unstated assumption is not about price. It is
that *laundry is the host's problem*. The brief asserts two hours per turnover and treats removing
it as obviously valuable. That assumption has never been put to a host, and the incumbents' existence
suggests hosts who feel it already have somewhere to go.

**`council-red-team`** — the competitive response is trivial. An incumbent with existing routes can
match any price this venture sets, at lower marginal cost, on the day it notices. A one-founder,
part-time, £15k operation entering a route-density business against a firm that already owns the
density is attacking the strongest point of the strongest defender.

**`council-risk-and-failure-modes`** — pre-mortem, twelve months out: the founder signed 8–12
properties at an introductory price, discovered the van round is 40% deadhead at that density, raised
the price, and lost the properties to the incumbent who was already passing the door. Runway is 9
months; the density flywheel needs longer than that to spin up. The kill criterion in `venture.yaml`
(3 of 15 hosts above the cost floor, by 2026-10-15) is well specified and has not been run — it is
the cheapest thing in this whole plan and it is still outstanding.

**`council-legal-and-regulatory-critic`** — nothing blocking at this stage. Flagged for later:
commercial laundering of bed linen carries hygiene obligations, and the non-negotiable "no commercial
laundry facility in year one" implies subcontracting, which moves those obligations onto a third
party the venture does not control. Minor now, major at MVP.

**`council-ethics-and-responsibility`** — `venture.yaml` names cleaners whose income includes laundry
time as an affected group and then never returns to them. The plan's efficiency gain is partly a
transfer away from the people currently paid for that time. This does not block, but a plan that
lists an affected group and does not address it has not finished thinking.

**`council-devils-advocate`** — against the room: "the whitespace is occupied" is the Council's own
consensus and it is thinly evidenced. The competitive map rests on advertising copy retrieved through
a search index, not on a single conversation with a provider or a host. Advertised terms are not
accepted terms; several of these firms may in practice decline a single-property host in an outer
postcode. The Council should not let a search result close a market it has not called.
**This dissent is recorded and not resolved.**

**`council-expansion-scout`** — the constructive read. If incumbents already run linen, the
unoccupied position is the *coordination* layer: check-outs move, cleaners cancel, and the linen
round is weekly while turnovers are not. Nobody in the map sells schedule certainty. That is an
asset-light software-shaped business rather than a van business, it fits a part-time founder with
£15k far better than vans do, and it does not require the density bet. It is speculative and is
recorded as an option, not a recommendation.

**`council-synthesis-arbiter`** — three findings block; two are major. The blockers are all
resolvable for under £500 and inside three weeks, which is why the verdict is reject-and-resubmit
rather than a recommendation to abandon.

### The machine-readable verdict

```council-verdict
id: ver_laundro-business-model-01
subject_artifact: laundro/market/competitive-map.md
requested_decision: >
  Authorise spend against the business model and proceed to MVP definition.
verdict: reject
issued_by: council-director
issued_at: "2026-09-11T09:30:00Z"
deadline_met: true
findings:
  - id: F1
    severity: blocker
    finding: >
      The venture's stated market gap does not exist as described. Manchester providers advertise
      weekly Airbnb linen rounds organised by changeover day and postcode, and UK providers advertise
      pay-as-you-go with no contract, against a brief that says commercial linen hire cannot serve a
      one-to-three-property host.
    failure_scenario: >
      The founder spends the 15k budget acquiring linen stock and a van round on the belief that no
      alternative exists for small hosts, then discovers at first sales contact that prospects are
      already served, have a price anchor 2-3x below the plan, and see no reason to switch. The money
      is in depreciating linen and the runway is gone.
    raised_by: [council-first-principles, council-red-team, competitor-intel-analyst]
    remedy: >
      Call three Manchester providers as a prospective one-property host and record what they
      actually quote and accept. Advertised terms are not accepted terms; this establishes which.
    owner: source-verifier
    acceptance_criterion: >
      Three provider quotes on record for a single-property host, with stated minimums, or three
      refusals on record. Either outcome settles the premise.
  - id: F2
    severity: blocker
    finding: >
      The price that every revenue figure rests on has never been tested with a host, and the kill
      criterion written to test it has not been run.
    failure_scenario: >
      TAM, SAM and SOM all scale linearly with 18 pounds per turnover. If real willingness to pay is
      10 pounds, the reachable business is 40k a year before costs and the route never reaches
      contribution margin. The plan proceeds because nobody ran the 15 conversations that would have
      shown this in a fortnight.
    raised_by: [council-economics-skeptic, council-assumption-auditor]
    remedy: >
      Run the kill criterion already specified in venture.yaml: 15 qualifying hosts, price stated
      above the cost floor by at least 3.
    owner: customer-discovery-interviewer
    acceptance_criterion: >
      15 host conversations logged against the 2026-10-15 deadline, with the 3-of-15 threshold
      resolved either way.
  - id: F3
    severity: blocker
    finding: >
      No differentiation exists. venture.yaml records why_us as "Nothing yet" and the competitive map
      could not construct a reason for a host to switch.
    failure_scenario: >
      The venture launches as a second, smaller, later copy of an incumbent with existing routes. The
      incumbent matches price at lower marginal cost the week it notices, and the venture has no
      position to retreat to.
    raised_by: [council-red-team, council-devils-advocate, council-synthesis-arbiter]
    remedy: >
      State a defensible position, or adopt the coordination-layer option below, or stop. A price
      that is merely lower is not a position.
    owner: business-head
    acceptance_criterion: >
      A written why_us that survives the question "what stops the incumbent doing this next week?"
  - id: F4
    severity: major
    finding: >
      The pack-to-turnover conversion ratio is unestablished, which makes incumbent pricing and this
      venture's pricing non-comparable and leaves the central cost question open.
    failure_scenario: >
      The founder compares 18 pounds per turnover against 6.65 pounds per pack, concludes there is a
      large margin, and builds a cost model on a unit mismatch that overstates gross margin by the
      number of packs a turnover consumes.
    raised_by: [council-economics-skeptic]
    remedy: >
      Establish packs per turnover for a typical one- and two-bedroom property before any unit
      economics work begins.
    owner: data-sourcing-analyst
  - id: F5
    severity: major
    finding: >
      The why-now claim in venture.yaml is unsupported and possibly contradicted by the source data
      carried forward from the invalidated sizing step.
    failure_scenario: >
      The claim is repeated in any material shown to a lender or partner, and is contradicted by the
      first person who checks a listings trend. Credibility is spent on a claim the venture did not
      need to make.
    raised_by: [council-assumption-auditor, source-verifier]
    remedy: >
      Resolve the listings-down-44-percent versus revenue-up-104-percent contradiction, or delete the
      why-now claim from the brief.
    owner: source-verifier
  - id: F6
    severity: minor
    finding: >
      Cleaners whose income includes laundry time are named as an affected group and never addressed.
    failure_scenario: >
      The venture's route depends on cleaners cooperating at handover while removing part of their
      billable time. Cleaners decline to cooperate and the operating model loses its cheapest
      distribution channel.
    raised_by: [council-ethics-and-responsibility]
    remedy: >
      Decide whether cleaners are a channel or a displaced party, and design for the answer.
  - id: F7
    severity: minor
    finding: >
      Subcontracted laundering moves hygiene obligations to a party the venture does not control,
      given the non-negotiable against a commercial facility in year one.
    failure_scenario: >
      A hygiene failure at the subcontractor reaches a guest, and the venture carries the reputational
      and contractual consequence without having had any control over the process.
    raised_by: [council-legal-and-regulatory-critic]
    remedy: >
      Carry this to the MVP gate as a supplier-qualification requirement.
expansion_options:
  - >
    Sell schedule certainty rather than clean linen. Incumbents run weekly rounds; turnovers are not
    weekly. Nobody in the competitive map sells coordination against moving check-outs. Asset-light,
    fits a part-time founder with 15k, and does not require winning the density race.
  - >
    Sell to the cleaners rather than the hosts. Cleaners already absorb laundry time across multiple
    properties and aggregate density the venture would otherwise have to build.
dissent:
  - agent: council-devils-advocate
    position: >
      The rejection rests on advertising copy retrieved through a search index, not on one
      conversation with a provider or a host. Advertised coverage is routinely broader than accepted
      intake, and an outer-postcode single-property host may well be declined by every firm in that
      table. The Council has closed a market it has not called. I would have held the verdict at
      approve_with_conditions pending F1, rather than reject, because a reject signals to the founder
      that the premise is settled when what we actually have is one round of desk research.
  - agent: council-expansion-scout
    position: >
      Rejecting the venture and rejecting the founder's read of the market are being conflated. The
      observation that incumbents run weekly rounds while turnovers are irregular is the most
      valuable thing this run produced, and it arrived as a by-product of a rejection. Recorded so it
      is not lost with the plan it came attached to.
```

## Evidence

| Claim | Source | Grade | Load-bearing |
|---|---|---|---|
| Five steps blocked, `size` invalidated | `workspace/laundro/run.json` | measured | yes |
| Manchester incumbents advertise Airbnb linen rounds by postcode | `competitive-map.md` | estimated | yes |
| Incumbent pack prices £6.65–£19.69 | `competitive-map.md` | estimated | yes |
| `why_us` is "Nothing yet" | `venture.yaml`, founder's own words | sourced | yes |
| Kill criterion specified and not yet run | `venture.yaml` + absence of any discovery artifact | measured | yes |
| £18 per turnover is untested | `market-analysis.md` evidence table | estimated | yes |
| Packs per turnover | none — not established | guessed | no |
| Advertised terms equal accepted terms | none — explicitly contested by `council-devils-advocate` | guessed | no |
| Incumbent marginal cost is below a new entrant's | inference from existing route density | guessed | no |

The verdict rests on the run's own state and on the founder's own `why_us`, both of which are
`measured` or `sourced`. It does not rest on the price comparison or on the assumption that
advertised terms are accepted terms — that is precisely the recorded dissent, and F1 exists to settle
it.

## Open questions

1. Do Manchester providers actually accept a single-property host in an outer postcode? — `source-verifier` (F1, and the substance of the recorded dissent)
2. What will 15 qualifying hosts state as a price? — `customer-discovery-interviewer` (F2)
3. How many packs does one turnover consume? — `data-sourcing-analyst` (F4)
4. Is the coordination gap real, and is anyone paid to close it today? — `jtbd-analyst`
5. Carried unresolved from `market-analysis.md`: the 1–3 property share, average stay length, the 4.2× listing-count spread, and the listings/revenue contradiction.

## Next action

**Run F1 and F2 before anything else — together they cost under £500 and about three weeks, and
either one can end the venture.** Do not redo the sizing step first: sizing a market whose premise is
unsettled repeats the error that invalidated it. Owner: `business-head`, reporting to the founder as
`decision_maker`.
