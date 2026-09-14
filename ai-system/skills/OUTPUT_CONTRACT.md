# Skill output contract

The shape every skill output takes. It lives here, once, instead of being repeated in 590 skill
files — which is roughly 100,000 tokens of duplication removed from the library, and one file in the
cacheable prefix instead of a block in every skill an agent loads.

Load this once per session. Every `SKILL.md` points here rather than restating it.

## Where it goes

`workspace/<venture-id>/<category>/<output>` — then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory rather than a loose file.

## Required structure

```markdown
# <title>
- **Skill:** <skill-name>
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer — a reader who stops here must still have the answer>

## Body
<the substance produced by the skill's procedure>

## Evidence
| Claim | Source | Grade | Load-bearing |
|---|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Rules

1. **Summary first, and it must stand alone.** Most readers — human and agent — stop after it. An
   artifact whose summary defers to the body has no summary.
2. **Every load-bearing claim appears in the evidence table** with a source and a grade. A claim
   graded `guessed` may never be load-bearing at a stage gate.
3. **Open questions are carried, not dropped.** They travel through handoffs unedited; tidying them
   away is how organisations lose the thread.
4. **One next action, with one owner.** A list of five possible next steps is not a next action.
5. **The confidence grade is the artifact's, not the author's mood.** It is the weakest grade among
   the claims the conclusion actually rests on.
6. **Say which claims the conclusion rests on.** Context you gathered but did not lean on still
   belongs in the table — dropping it to protect your grade is the failure this rule prevents.
   Mark such a row in one of exactly two ways, and the orchestrator will exclude it from rule 5:

   - a `Load-bearing` column holding `no`, or
   - the literal text `(not load-bearing)` inside the **claim cell** or the **grade cell**.

   The marker is not read from the Source cell, so prose there never switches the check off by
   accident. An unmarked row counts as load-bearing. Marking a row you did lean on is the one way
   to defeat rule 5, and it is a lie the next reader will find in your Body.

   ```markdown
   | Claim | Source | Grade | Load-bearing |
   |---|---|---|---|
   | Manchester listing count 1,665-6,951 | three vendors | estimated | yes |
   | Host spends ~2h per turnover | founder's recollection | guessed | no |
   ```

## The standing quality bar

Every skill's own quality bar adds to this one, which applies to all of them:

> The output states its confidence grade and names the evidence behind every load-bearing claim.
