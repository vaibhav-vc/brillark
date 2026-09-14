# Unit economics — CAC $400, retention ~2 years, $99/month

- **Skill:** unit-economics-analysis
- **Author agent:** unit-economics-architect
- **Date:** 2026-09-14
- **Confidence:** guessed

## Summary

**I can show you the arithmetic, but not a defensible answer on pricing.** Both inputs — CAC $400 and
"about two years" retention — are stated as approximations with no source given, and "about two
years" is a stated assumption, not an observed cohort curve. A ratio computed from two ungraded
inputs is itself ungraded, whatever it comes out to. I am not issuing a pricing recommendation on
this evidence; I am telling you what would need to exist before one could be issued responsibly.

## Body

### The numbers as given, graded

| Input | As stated | Grade | Why |
|---|---|---|---|
| CAC | "around $400" | **guessed** | No source: not stated as computed from actual spend ÷ actual customers acquired, including salaries |
| Monthly price | $99 | sourced | This is presumably the actual, set price — the only solid input here |
| Customer lifetime | "about two years" | **guessed** | This is an assumed horizon, not an observed cohort retention curve. "About" concedes it is not measured. |

### What the arithmetic says, with the caveat load-bearing throughout

If CAC is really $400 and average lifetime is really 24 months at $99/month: naive LTV = $99 × 24 =
$2,376, giving LTV:CAC ≈ 5.9:1 and payback in roughly 4 months. **This number is fully computable and
almost entirely uninformative**, because both of its inputs are guesses dressed as figures. A 5.9:1
ratio built on a guessed retention assumption is not evidence the business is healthy — it is a
demonstration that the assumption, if true, would be good news. Per this organisation's standard, a
`guessed` input may never be load-bearing at a stage gate, and a pricing decision is a stage gate.

The specific failure this masks: an assumed two-year lifetime almost always overstates real retention,
because real cohort curves have early churn (the first 1–3 months, where most subscription attrition
concentrates) that a flat "about two years" average erases. If even a third of customers churn inside
month three and the rest genuinely stay two years, blended LTV drops well below the naive figure
above, and payback period lengthens accordingly — in a direction that would argue against a price
increase, not for one.

### On raising prices

**I am not recommending a price change from this evidence.** A pricing decision made on an assumed
lifetime is a decision made on a number nobody has actually observed. Raising price without knowing
the real retention curve risks accelerating churn among exactly the price-sensitive customers whose
departure would most damage a lifetime figure that is already unmeasured.

## Evidence

| Claim | Source | Grade | Load-bearing |
|---|---|---|---|
| CAC "around $400" | stated by requester, no computation shown | guessed | yes |
| Customer lifetime "about two years" | stated by requester, no cohort data shown | guessed | yes |
| Price $99/month | stated by requester (presumed actual, set price) | sourced | yes |
| Naive LTV:CAC ≈ 5.9:1 | arithmetic on the two guessed inputs above | guessed | no |

## Open questions

1. What is the actual acquisition spend and actual number of customers acquired in the period it
   covers, fully loaded (including salaries)? This replaces the CAC guess. — owner: `financial-model-builder`.
2. What does the real cohort retention curve look like, month by month, for at least the earliest
   cohorts with enough history? This replaces the lifetime guess and is the harder, more important
   number to get. — owner: `revenue-forecaster` / `cohort-retention-analysis`.
3. Where does early (month 1–3) churn concentrate, and is it already reflected in "about two years,"
   or is that an average across survivors only? — owner: same cohort analysis.

## Next action

**Run `cohort-retention-analysis` on actual customer data before any pricing decision is considered.**
The CAC figure also needs replacing with a computed value from actual spend and actual acquisitions.
Until both exist, this is not a unit-economics analysis the organisation can act on — it is a
demonstration of what the analysis would look like if the inputs were real. Owner: `finance-head`.
