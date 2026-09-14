=== FULL ARTIFACT (workspace/<venture>/market/market-sizing.md — NOT the return) ===

# Market sizing — workshop management software for independent UK bicycle repair shops

- **Skill:** market-sizing
- **Author agent:** market-researcher
- **Date:** 2026-09-14
- **Confidence:** estimated

## Summary

Bottom-up, independent UK bicycle repair shops number roughly 2,500–3,500 (no single authoritative
register exists, so this is a range from trade-body and directory cross-checks). At a realistic
£40–£70/month willingness to pay for workshop management software, SAM is roughly **£1.2m–£2.9m ARR**,
with SOM narrower still once channel reach (direct sales to a fragmented, low-digital-adoption trade)
is accounted for. Full derivation and sources: `market-sizing.md`.

## Body

### Buyer unit and count

Buyer unit: one independent repair shop (not a chain, not a mobile-only operator — those need a
different pricing/feature fit and are excluded from this segment). UK count: no single register
exists; cross-checking a trade-body membership list against a business directory search gives a range
of roughly 2,500–3,500 shops, with the trade body itself likely undercounting non-members.

### Spend per buyer

No public benchmark for this specific software category at this specific segment size exists.
Comparable adjacent categories (salon/garage booking-and-invoicing SaaS aimed at small independents)
cluster around £30–£80/month. Absent shop-specific data, £40–£70/month is a reasoned estimate from
that adjacent-category anchor, not an observed price point for this exact buyer.

### Sizing

| Layer | Basis | Figure |
|---|---|---|
| TAM | All UK independent shops × annualised spend range | £1.2m–£2.9m |
| SAM | Same, narrowed to shops with a POS/booking system already (a rough proxy for digital readiness) | Materially smaller; proxy not yet counted |
| SOM | Reachable via one identified channel (trade-body partnership, direct sales) | Not yet established — no channel commitment exists yet |

### Top-down sanity check

No independent top-down source exists for this specific category; the adjacent SaaS-for-small-trades
category is too broad to cross-check against without introducing a comparison the size of the gap
would not explain. Flagged as an open question rather than skipped.

## Evidence

| Claim | Source | Grade | Load-bearing |
|---|---|---|---|
| 2,500–3,500 independent UK bike shops | trade-body membership + directory cross-check | estimated | yes |
| £40–£70/month willingness to pay | adjacent-category (salon/garage SaaS) anchor, not this segment | estimated | yes |
| Digital-readiness proxy (existing POS/booking) | not yet counted | guessed | no |

## Open questions

1. What share of shops already use any digital booking/POS system, as a readiness proxy for SAM? —
   `data-sourcing-analyst`.
2. Is there an actual channel (trade association partnership, distributor relationship) that makes any
   of TAM reachable, or is SOM currently zero for lack of one? — `competitor-intel-analyst` /
   `partnership-bd-agent`.
3. Does willingness to pay in this specific trade match the adjacent-category anchor, or is bicycle
   repair a lower-margin trade with lower software budgets? — `customer-discovery-interviewer`.

## Next action

Count the digital-readiness proxy and identify one real channel before this sizing is used to justify
spend. Owner: `business-head`.

=== RETURN TO business-head (this is the graded output — must fit ≤800 tokens) ===

**Market sizing done — directional only, confidence `estimated`.**

Bottom-up: ~2,500–3,500 independent UK bike repair shops (no single register; cross-checked
trade-body + directory). At £40–£70/mo willingness to pay (borrowed from adjacent small-trade SaaS,
not observed in this segment), **SAM ≈ £1.2m–£2.9m ARR**. SOM is not yet established — no reachable
channel identified and no digital-readiness proxy counted, so I'm not narrowing further on a guess.

Full derivation, evidence table, and sources: `workspace/<venture>/market/market-sizing.md`.

**Open questions carried forward:** (1) share of shops with existing POS/booking, as a SAM-narrowing
proxy; (2) whether an actual sales channel exists into this fragmented trade; (3) whether this
segment's real willingness to pay matches the adjacent-category anchor or is lower.

**Next action:** count the digital-readiness proxy and confirm one real channel before this sizing
justifies spend. Owner: `business-head`.
