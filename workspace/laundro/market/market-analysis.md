# Market analysis — linen handling for short-term rental hosts, Manchester

- **Skill:** market-sizing
- **Author agent:** market-researcher
- **Date:** 2026-09-11
- **Confidence:** guessed

```blocks
blocks: [pricing, economics]
reason: >
  Sizing rests on three guessed load-bearing inputs (1-3 property share, stay length, price point).
  A price or a unit-economics model built on this would inherit the guess and hide it behind
  arithmetic.
resolved_by: [source-verifier, data-sourcing-analyst, customer-discovery-interviewer]
```

## Summary

**Confidence is `guessed`, not `estimated`** — the weakest load-bearing input in the evidence table
below is ungraded guesswork, and per the output contract the artifact inherits that. This sizing is
directional only.

Bottom-up, the reachable market is **£70k–£150k of annual revenue**, not a venture-scale
opportunity — it is a dense-route local services business. The headline listing count cannot be
established: three commercial sources give 1,665, 2,453 and 6,951 active listings for the same city,
a 4.2× spread, and none discloses its methodology. The single largest driver of the sizing — what
share of listings belongs to hosts with 1–3 properties — has **no source at all** and is currently a
guess. The sizing should not be used to justify spend until that share is counted.

## Body

### The unit and the count

The buyer unit is a **property under management by a host with 1–3 listings**, not a listing and not
a host. A host with three properties buys one subscription covering three routes; a host with
forty is a commercial account that existing linen hire already serves.

Active listings in Manchester, per three commercial data vendors:

| Source | Figure | Platforms covered | Retrieved |
|---|---|---|---|
| AirDNA | 6,951 | Airbnb + Vrbo + Booking.com | 2026-09-11 |
| Airbtics | 2,453 | Airbnb only | 2026-09-11 |
| AirROI | 1,665 | Airbnb only | 2026-09-11 |

**These are not comparable and must not be averaged.** AirDNA counts three platforms; the other two
count one. That explains part of the gap but not all of it: Airbtics and AirROI both claim
Airbnb-only and differ by 47%. The remaining difference is definitional — what counts as "active" —
and none of the three publishes the definition. Per `comparability-checking`, the honest position is
a **range of 1,665–6,951, not a point estimate**.

All three are commercial vendors selling market-intelligence subscriptions. A larger market figure
serves their product. That is not an accusation of error; it is a reason the grade is capped at
`estimated` absent a disclosed methodology.

### Turnovers per property per year

Reported occupancy is 54%, which is ~197 booked nights. Turnovers depend on average stay length,
which I could not establish:

| Avg stay | Turnovers/year |
|---|---|
| 2 nights | ~99 |
| 3 nights | ~66 |
| 4 nights | ~49 |

I use **66** as the central case. Stay length is a `guessed` input and it swings the answer by 2×.

### Sizing

Revenue per property per year at 66 turnovers × £18 per turnover = **£1,188**.

| Layer | Basis | Figure |
|---|---|---|
| TAM | All Manchester STR listings × £1,188 | £2.0M – £8.3M |
| SAM | Share held by 1–3 property hosts — **GUESSED at 40%** | £0.8M – £3.3M |
| SOM | Properties reachable on one dense van route, two postcode clusters | **£71k – £150k** |

SOM is derived from the route constraint, not from a share of SAM: a single van doing a four-hour
round can serve roughly 60–120 properties weekly at realistic density. That is the binding
constraint, and it is why this is a local operations business rather than a scalable one.

### Why now — not established

The venture brief claims STR supply has grown and cleaner availability has tightened. I found
**contradictory evidence**: one source reports active listings **down 44.1%** year on year while
revenue is up 104.6%. Those two figures are difficult to reconcile and I cannot reconcile them from
the source available. A falling listing count would weaken, not strengthen, the why-now argument.

**The why-now claim is currently unsupported and possibly contradicted.** It should not be repeated
in any investor or planning material until resolved.

### What would falsify this sizing

If hosts with 1–3 properties hold under 15% of listings, SAM collapses below £300k and the
reachable business is too small for the route economics to work.

## Evidence

| Claim | Source | Grade |
|---|---|---|
| Manchester active listings, multi-platform, 6,951 | [AirDNA](https://www.airdna.co/vacation-rental-data/app/gb/north-west-england/manchester/overview) | estimated |
| Manchester active Airbnb listings, 2,453 | [Airbtics](https://airbtics.com/annual-airbnb-revenue-in-manchester-uk/) | estimated |
| Manchester active Airbnb listings, 1,665 | [AirROI](https://www.airroi.com/airbnb-data/united-kingdom/england/manchester) | estimated |
| Occupancy 54%, ADR $141 | AirDNA, via search result | estimated |
| Active listings down 44.1% YoY, revenue up 104.6% | AirDNA, via search result | estimated |
| Share of listings held by 1–3 property hosts | **none — no source found** | guessed |
| Average stay length | **none — no source found** | guessed |
| Price of £18 per turnover | **none — not yet tested with any host** | guessed |
| Van round serves 60–120 properties | **none — not route-tested** | guessed |

Four of nine inputs are `guessed`, and three of those four are load-bearing.

## Open questions

1. What share of Manchester listings belongs to hosts with 1–3 properties? — `data-sourcing-analyst`
2. What is the average stay length? It swings turnover count 2×. — `data-sourcing-analyst`
3. Why do two Airbnb-only sources differ by 47%? — `source-verifier`
4. How can listings fall 44% while revenue doubles? — `source-verifier`
5. What do hosts currently pay for linen handling, and do they see it as a cost? — `customer-discovery-interviewer`

## Next action

**Do not proceed to pricing or unit economics on this sizing.** Commission `source-verifier` to
resolve the 4.2× spread and the listings/revenue contradiction, and `customer-discovery-interviewer`
to establish the 1–3 property share and real willingness to pay. Owner: `business-head`.
