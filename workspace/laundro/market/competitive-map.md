# Competitive map — linen handling for short-term rental hosts, Manchester

- **Skill:** competitive-landscape-mapping
- **Author agent:** competitor-intel-analyst
- **Date:** 2026-09-11
- **Confidence:** estimated

```blocks
blocks: [size, jobs, value, model]
reason: >
  The venture premise is contradicted. `venture.yaml` states that commercial linen hire "is built
  for hotels: pallet volumes, contracts, and minimums that a three-property host cannot meet". A
  Manchester-based provider runs weekly linen rounds for Airbnb hosts, organised by changeover day
  and postcode, from GBP 6.65 per pack, and at least two UK providers advertise pay-as-you-go with
  no contract. The whitespace this venture was pointed at is occupied. The sizing artifact also
  assumes GBP 18 per turnover, roughly 2.7x the incumbent's advertised pack price, so the SOM range
  is built on a price the market appears already to undercut.
resolved_by: [source-verifier, customer-discovery-interviewer, business-head]
```

## Summary

**There is no whitespace.** The business the venture brief proposes to build already exists in
Manchester, sold to the same buyer, on the same weekly-round operating model the brief treats as its
insight. The brief's stated gap — that commercial linen hire cannot serve a 1–3 property host — is
contradicted by advertised offers from at least one Manchester provider and several UK-wide ones,
including pay-as-you-go with no contract. Separately, the incumbent's advertised price (from £6.65
per pack) sits far below the £18 per turnover the sizing artifact assumed, which means the sizing's
revenue figures and the `size` step that produced them must be revisited before anything is built on
them.

## Body

### The map

| Who | What they sell | Segment | Model | Evidence of 1–3 property access |
|---|---|---|---|---|
| **Doing it yourself** (status quo) | Host's own time + own linen stock | All hosts | £0 cash, ~2h per turnover | This is the real incumbent |
| **The cleaner who also launders** | Turnover clean with laundry time billed in | 1–3 property hosts | Per-turnover fee | Advertised by Manchester cleaning firms as "linen support" included |
| **The Textile Service** (Stockport) | Linen hire + collection/return, weekly round | Airbnb, holiday lets, serviced apartments | Per-pack weekly exchange, from £6.65 | Explicitly markets to Airbnb hosts by postcode round |
| **Linen Host** | Linen hire + laundry | Individual hosts and property managers | Packs from £10.99; pay-as-you-use | Explicitly targets individuals hosting alongside other work |
| **BNB Laundry** | Airbnb laundry | Hosts | Pay-as-you-go, no contract | No-contract offer stated |
| **Airlinen / 1st Class Linen / Laundryheap** | Linen hire | Hosts, letting agencies | £10.30–£19.69 per set | London-weighted, but the model is not hotel-only |
| **Traditional commercial linen hire** | Pallet-volume contracts | Hotels | Annual contract, minimums | This is the only competitor the brief actually described |

### The whitespace test

The skill's quality bar requires checking whether the whitespace is empty *for a good reason*. The
finding is stronger than that: **it is not empty at all.** The brief mapped one competitor class
(hotel linen hire) and concluded from its absence at the low end that the low end was unserved. It
is served, by a different competitor class the brief did not look for — small and mid-size linen
hire firms that already organise by changeover day and postcode, which is precisely the "density
bet" the venture describes as its own idea.

This is the failure mode the skill exists to catch: a competitive set defined by the shape of the
proposed solution rather than by where the buyer's budget actually goes.

### What the brief got right

The status quo — the host doing it themselves — is genuinely the largest competitor by volume, and
none of the incumbents removes the host's coordination burden entirely. If there is a business here
it is in that coordination gap, not in the washing.

### Effect on the sizing

`market-analysis.md` priced a turnover at £18 and graded that input `guessed`. Advertised incumbent
pricing is £6.65–£19.69 *per pack*, with packs exchanged weekly rather than per turnover. The two
are not directly comparable (a pack may cover one bed; a turnover may need several), but the gap is
large enough that the £18 figure can no longer be treated as a neutral placeholder — it now has a
market reference point that may sit below it. Every revenue layer in the sizing (TAM, SAM, SOM)
scales linearly with that figure.

### Differentiation — stated as a reason to switch

I cannot state one. A host switching from The Textile Service to this venture would be switching
between two weekly linen rounds, one of which exists and has vans. `venture.yaml` already records
`why_us: "Nothing yet"`. The competitive map confirms that as the binding problem rather than a
formality to fill in later.

## Evidence

| Claim | Source | Grade | Load-bearing |
|---|---|---|---|
| Manchester provider runs weekly Airbnb linen rounds by changeover day and postcode | [The Textile Service](https://www.thetextileservice.co.uk/airbnb-linen-hire-manchester) (via search result; site not directly fetchable from this environment) | estimated | yes |
| Packs from £6.65 | The Textile Service, via search result | estimated | yes |
| Packs from £10.99; pay-as-you-use; targets individual hosts | [Linen Host](https://linenhost.co.uk/) | estimated | yes |
| Pay-as-you-go, no contract | [BNB Laundry](https://bnblaundry.co.uk/) | estimated | yes |
| Sets £13.29–£19.69 | [Airlinen](https://www.airlinen.co.uk/pricing) | estimated | no |
| Single bed pack £10.30 + VAT | [1st Class Linen](http://www.1stclasslinenhire.co.uk/Airbnb-linen-hire-London.asp) | estimated | no |
| Manchester cleaning firms advertise linen support within turnover cleans | [BritsMaid](https://www.britsmaid.co.uk/), [Brit Polish](https://britpolish.co.uk/) | estimated | yes |
| Host self-service costs ~2h per turnover | `venture.yaml`, founder's own statement | guessed | no |
| Pack-to-turnover conversion ratio | none — not established | guessed | no |

The conclusion — *the whitespace is occupied* — rests only on the `estimated` rows. It does not rest
on the £18-vs-£6.65 comparison, which is why this artifact is graded `estimated` and not `guessed`:
the pack/turnover ratio is flagged as an open question rather than used to draw the conclusion.

## Open questions

1. How many packs does one turnover consume, and what does a two-bedroom turnover actually cost at
   incumbent list prices? — `data-sourcing-analyst`
2. Do the Manchester incumbents actually accept a single-property host, or is the marketing broader
   than the intake? Advertised terms are not accepted terms. — `source-verifier`
3. What do hosts already using one of these services pay in total, and why did they choose it? —
   `customer-discovery-interviewer`
4. Is there a coordination gap (scheduling against unpredictable check-outs) that none of the
   incumbents closes? — `jtbd-analyst`
5. Carried from `market-analysis.md`, unresolved: the 1–3 property share, average stay length, the
   4.2× listing-count spread, and the listings-down-44%/revenue-up-104% contradiction.

## Next action

**Stop the business-model workflow and put the premise to the founder.** The brief's stated gap does
not exist as described; continuing to design a value proposition and a canvas on top of it produces
a plan for a market position that is already taken. Owner: `business-head`, escalating to the
founder as `decision_maker` per `venture.yaml`.
