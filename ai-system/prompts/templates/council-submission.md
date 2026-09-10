# Council submission

The Council refuses submissions that lack any of these.

```yaml
subject_artifact: art_<id>
requested_decision: |
  <exactly what you want to do if this is approved>
evidence_pack:
  - art_<id>   # every claim's supporting artifact
assumptions:
  - statement: <claim>
    evidence_grade: measured | sourced | benchmarked | estimated | guessed
    load_bearing_score: 1-5
deadline: <ISO-8601>
prior_verdicts: [ver_<id>]
```

You will get back a `council-verdict` with severities, owners, acceptance criteria, and recorded dissent.
