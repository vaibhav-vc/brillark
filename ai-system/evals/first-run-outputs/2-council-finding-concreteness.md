# Red-team attack — dog-walker subscription app

- **Skill:** red-team-attack
- **Author agent:** council-red-team
- **Date:** 2026-09-14
- **Confidence:** estimated

## Summary

The plan's strongest claim — organic word-of-mouth growth to 4,000 subscribers by month nine — is
also its weakest structural point: it has no paid channel to fall back on if word-of-mouth
undershoots, and a funded competitor can buy the same growth curve for cash the incumbent doesn't
have to earn. Two blockers and one major finding below; each has a proposed defence.

## Body

### Attacker 1 — a funded competitor (attacks the strongest claim: word-of-mouth growth)

**Sequence:** A well-capitalised entrant (an existing pet-services platform bolting on walking, or a
funded new entrant) launches at £8/month with a £30 first-walk credit, funded by a marketing budget
this venture does not have. Word-of-mouth growth is a rate, and the competitor's paid acquisition is
also a rate — a faster one. By month four the competitor has out-grown this venture's organic curve
in every city both operate in, because paid CAC beats zero-CAC-but-slow whenever the payback period
tolerates it, and a funded entrant's payback tolerance is by definition higher.

**Severity: blocker.** The plan's entire growth mechanism has no answer to a faster mechanism arriving
from someone with more cash.

**Defence:** Identify one lever word-of-mouth has that paid acquisition cannot buy at any price —
typically trust transferred between neighbours who already know each other, or a geographic density
effect where an early walker becomes locally irreplaceable. If no such lever exists, this is not a
defensible position, only an unexploited one; state that plainly rather than trusting the competitor
not to notice for nine months.

### Attacker 2 — an abusive user (fraud path)

**Sequence:** A subscriber pays £12/month, books walks for a dog that does not exist or is never
collected, and disputes the charge after the walker no-shows to a fabricated address, or the reverse:
a walker claims completed walks that never happened to collect payout. Either scales cheaply — one
person can run this against multiple accounts — and directly consumes contribution margin per
incident.

**Severity: major.** Not existential at nine-months-to-4,000-subscribers scale, but it compounds:
unresolved disputes are also churn events, which directly attacks the growth assumption above.

**Defence:** GPS-stamped walk confirmation and a simple identity check at both subscriber and walker
onboarding. Cheap relative to the fraud it prevents; should be in the MVP, not deferred.

### Attacker 3 — an indifferent market (the break-even assumption)

**Sequence:** Break-even at 4,000 subscribers assumes a stated growth *rate* holds for nine
consecutive months. Word-of-mouth referral rates are not typically linear — they decay as the
easy-to-convert early adopters are exhausted and the remaining market requires more convincing per
conversion. If the rate that got the plan to 1,000 subscribers by month four halves by month seven
(a common pattern, not a worst case), break-even slides past month nine into a runway the plan has
not sized for.

**Severity: major.** This is an arithmetic property of exponential-decay growth curves, not a
speculative risk — it will happen to some degree; the open question is magnitude.

**Defence:** Model break-even against a decaying, not constant, referral rate before committing to
the month-nine date externally. Cheap to do now (a sensitivity table), expensive to discover after
the runway is already spent on that date's assumption.

## Evidence

| Claim | Source | Grade | Load-bearing |
|---|---|---|---|
| Paid CAC generally outcompetes organic growth rate when payback tolerance is high | general marketplace-growth pattern, not this venture's data | estimated | yes |
| Referral rates decay as easy adopters are exhausted | common pattern in consumer subscription growth | estimated | yes |
| GPS/identity verification is standard, low-cost fraud mitigation in gig-marketplace apps | general practice, not vendor-quoted here | estimated | no |

## Open questions

1. What word-of-mouth lever does this specific venture have that a funded competitor cannot buy? —
   owner: `growth-loop-designer`.
2. What does the referral rate actually look like month-over-month in comparable consumer apps, to
   replace the "constant rate" assumption with a real decay curve? — owner: `data-sourcing-analyst`.

## Next action

**Model break-even against a decaying referral rate and name the word-of-mouth moat before this goes
to Council for a spend decision.** Both are cheap to do now and expensive to discover in month seven.
Owner: `business-head`.
