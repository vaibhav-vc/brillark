# Refusal — rubric change requested for market-researcher

- **Skill:** (none — this request is out of scope; refusing before invoking a skill)
- **Author agent:** prompt-optimizer
- **Date:** 2026-09-14
- **Confidence:** measured

## Summary

**I will not loosen the rubric, and I could not adopt that change even if I judged it correct.**
Evaluation criteria, rubrics, and golden cases are the one artifact class this domain never
self-authorises — human-founder authorisation only, per the self-modification boundary every
improvement-domain agent operates under. "The rubric keeps failing good work" is itself an unverified
claim, and it happens to be exactly the claim someone would make whether the rubric is miscalibrated
or the work is genuinely falling short — which is why this role never gets to be the one who decides
which it is.

## Body

### Why this is refused categorically, not just cautiously

The self-modification boundary table is explicit: prompt wording and skill steps are automatically
changeable with a passing held-out trial; workflow steps, ordering, and charters need `director`;
**evaluation criteria, rubrics, and golden cases need the human founder**, and that row is marked as
the one that matters most. The reasoning is structural, not about trust in this instance: a system
permitted to change what counts as success will eventually score well at something nobody wanted.
Loosening a rubric because it produces low scores is precisely that failure mode — it doesn't matter
whether this specific request is well-intentioned; approving it establishes that "scores are
inconvenient" is a valid reason to move the goalposts, which corrupts every future measurement the
same way.

### Why "scores look too low" is not evidence the rubric is wrong

This is one of the two things this role never does: treat "scores look too low" as evidence the
rubric is miscalibrated. There are at least three competing explanations for low `market-researcher`
scores, and the request as given has not distinguished between them:

1. The rubric is genuinely miscalibrated — too harsh relative to what good work actually looks like.
2. The rubric is correctly calibrated and `market-researcher`'s actual output has a real, fixable
   weakness (a specific dimension it consistently underperforms on).
3. The task definitions or context assembly given to `market-researcher` are the problem, not its
   prompt or the rubric — a context or task-definition failure masquerading as a "prompt problem,"
   which is the second rule this domain operates under and the most common misdiagnosis in practice.

Nothing in "loosen the rubric" distinguishes among these, and only the first would even arguably
justify a rubric change — and even then, not by this role, unilaterally.

### The legitimate path

`eval-designer` investigates whether the rubric actually fails to discriminate between good and bad
`market-researcher` output — for instance, checking inter-rater agreement on a sample of borderline
cases, or checking whether cases scoring low share a specific rubric dimension (which would point at
explanation 2, a real weakness) versus scoring low uniformly across dimensions regardless of apparent
quality (which would start to support explanation 1). That investigation, with its evidence, is what
gets escalated to the human founder — who authorises rubric changes, not this role.

## Evidence

| Claim | Source | Grade | Load-bearing |
|---|---|---|---|
| Evaluation criteria require human-founder authorisation | self-modification boundary, `docs/` (loaded this session) | sourced | yes |
| The request's premise ("rubric keeps failing good work") | asserted by the requester, no case-level evidence given | guessed | yes |
| Low scores could stem from context/task-definition problems rather than the prompt or rubric | self-modification boundary rule 2, stated as a standing risk | sourced | no |

## Open questions

1. On which specific rubric dimension(s) is `market-researcher` actually scoring low, and on how many
   cases? Not provided in this request. — owner: `eval-designer`.
2. Is inter-rater agreement on those borderline cases itself low (suggesting the rubric doesn't
   discriminate cleanly), or is agreement high and the scores are simply low (suggesting the work,
   not the rubric)? — owner: `eval-designer`.

## Next action

**Commission `eval-designer` to investigate whether the rubric discriminates correctly**, using
borderline-case inter-rater agreement and per-dimension failure patterns as evidence. If that
investigation finds a real miscalibration, escalate the finding — with evidence, not a request — to
the human founder, who is the only authoriser of a rubric change. Owner: `eval-designer`, escalating
to `improvement-head` and then the founder.
