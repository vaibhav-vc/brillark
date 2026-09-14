"""Tests for the runtime: memory store and workflow orchestrator.

Every test here exists because running the system for real exposed the gap it covers. They are not
hypothetical: each one failed before the fix it guards.

    python3 ai-system/tests/test_runtime.py
"""
from __future__ import annotations

import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import memory  # noqa: E402
import run_workflow as rw  # noqa: E402
import validate as schema_validate  # noqa: E402
from loader import Organisation  # noqa: E402


def artifact(confidence: str, rows: list[tuple[str, str]], blocks: str = "") -> str:
    table = "\n".join(f"| {claim} | src | {grade} |" for claim, grade in rows)
    return f"""# Test artifact
- **Skill:** market-sizing
- **Confidence:** {confidence}
{blocks}
## Summary
A summary long enough to clear the minimum-length check that rejects stubs pretending to be work.

## Body
Body text.

## Evidence
| Claim | Source | Grade |
|---|---|---|
{table}

## Open questions
Something unresolved.

## Next action
Someone does something.
"""


class TestConfidenceEnforcement(unittest.TestCase):
    """The contract said confidence is the weakest load-bearing grade. Nothing enforced it, and a
    real artifact shipped claiming 'estimated' over four guessed inputs."""

    def check(self, body: str) -> list[str]:
        problems = []
        import re
        declared = re.search(r"\*\*Confidence:\*\*\s*([a-z]+)", body)
        stated = declared.group(1)
        evidence = rw.parse_evidence_grades(body)
        load_bearing = [(c, g) for c, g, lb in evidence if lb]
        if load_bearing:
            weakest = min(load_bearing, key=lambda cg: rw.GRADES.index(cg[1]))[1]
            if rw.GRADES.index(stated) > rw.GRADES.index(weakest):
                problems.append(f"overstates: {stated} over {weakest}")
        return problems

    def test_an_overclaim_is_caught(self):
        body = artifact("estimated", [("solid claim", "sourced"), ("weak claim", "guessed")])
        self.assertTrue(self.check(body), "confidence above the weakest load-bearing grade must fail")

    def test_an_honest_grade_passes(self):
        body = artifact("guessed", [("solid claim", "sourced"), ("weak claim", "guessed")])
        self.assertEqual(self.check(body), [])

    def test_understating_confidence_is_allowed(self):
        """Claiming less than the evidence supports is caution, not a contract breach."""
        body = artifact("estimated", [("a", "measured"), ("b", "sourced")])
        self.assertEqual(self.check(body), [])

    def test_rows_marked_not_load_bearing_do_not_cap_confidence(self):
        body = artifact("sourced", [("a", "sourced"), ("colour of the logo (not load-bearing)", "guessed")])
        self.assertEqual(self.check(body), [])

    def test_grades_are_parsed_from_the_evidence_table(self):
        rows = rw.parse_evidence_grades(artifact("guessed", [("a", "measured"), ("b", "guessed")]))
        self.assertEqual([g for _, g, _ in rows], ["measured", "guessed"])


class TestWorkflowBlocking(unittest.TestCase):
    """The orchestrator advanced regardless of what a step found. An artifact saying 'do not
    proceed to pricing' was followed by the runner offering pricing."""

    def test_an_artifact_can_block_later_steps(self):
        body = artifact("guessed", [("a", "guessed")], blocks="""
```blocks
blocks: [pricing, economics]
reason: inputs are guessed
resolved_by: [source-verifier]
```
""")
        declared = rw.parse_blocks(body)
        self.assertIsNotNone(declared)
        self.assertEqual(declared["blocks"], ["pricing", "economics"])
        self.assertEqual(declared["resolved_by"], ["source-verifier"])

    def test_an_artifact_without_a_block_declares_none(self):
        self.assertIsNone(rw.parse_blocks(artifact("guessed", [("a", "guessed")])))

    def test_malformed_block_declarations_are_ignored_not_crashed(self):
        body = artifact("guessed", [("a", "guessed")], blocks="```blocks\nnot: valid: yaml: here\n```")
        self.assertIsNone(rw.parse_blocks(body))

    def test_an_empty_block_list_is_not_a_block(self):
        body = artifact("guessed", [("a", "guessed")], blocks="```blocks\nblocks: []\n```")
        self.assertIsNone(rw.parse_blocks(body))


class TestMemoryContract(unittest.TestCase):
    def test_provenance_is_mandatory(self):
        problems = memory.validate({"type": "semantic", "claim": "A standalone claim about things.",
                                    "scope": "org.x"})
        self.assertTrue(any("provenance" in p for p in problems))

    def test_a_strong_grade_must_name_a_source(self):
        """'measured' asserts an external source exists. Make it say which."""
        problems = memory.validate({
            "type": "semantic", "claim": "A standalone claim about things.", "scope": "org.x",
            "provenance": {"author_agent": "a", "evidence_grade": "measured"}})
        self.assertTrue(any("source_artifacts" in p for p in problems))

    def test_a_guess_does_not_need_a_source(self):
        problems = memory.validate({
            "type": "semantic", "claim": "A standalone claim about things.", "scope": "org.x",
            "provenance": {"author_agent": "a", "evidence_grade": "guessed"}})
        self.assertEqual(problems, [])

    def test_a_fragment_is_rejected(self):
        problems = memory.validate({
            "type": "semantic", "claim": "yes", "scope": "org.x",
            "provenance": {"author_agent": "a", "evidence_grade": "guessed"}})
        self.assertTrue(any("standalone" in p for p in problems))

    def test_contradicting_numbers_on_the_same_subject_are_detected(self):
        existing = [{"claim": "Manchester has 6951 active short-term rental listings.",
                     "scope": "v.x", "status": "active",
                     "provenance": {"evidence_grade": "estimated", "created_at": "2026-01-01T00:00:00+00:00"}}]
        new = {"claim": "Manchester has 1665 active short-term rental listings.", "scope": "v.x"}
        self.assertTrue(memory.find_contradictions(new, existing))

    def test_a_different_scope_is_not_a_contradiction(self):
        existing = [{"claim": "Manchester has 6951 active short-term rental listings.",
                     "scope": "v.other", "status": "active",
                     "provenance": {"evidence_grade": "estimated"}}]
        new = {"claim": "Manchester has 1665 active short-term rental listings.", "scope": "v.x"}
        self.assertEqual(memory.find_contradictions(new, existing), [])

    def test_superseded_claims_do_not_re_trigger(self):
        existing = [{"claim": "Manchester has 6951 active short-term rental listings.",
                     "scope": "v.x", "status": "superseded",
                     "provenance": {"evidence_grade": "estimated"}}]
        new = {"claim": "Manchester has 1665 active short-term rental listings.", "scope": "v.x"}
        self.assertEqual(memory.find_contradictions(new, existing), [])


class TestAttributedDisagreement(unittest.TestCase):
    """Two sources disagreeing is a finding to preserve. Memory contradicting itself is a conflict
    to resolve. Conflating them made the memory store fight the research doctrine."""

    def test_attribution_is_recognised(self):
        self.assertEqual(memory._attribution("AirDNA reported 6951 listings in Manchester."), "AirDNA")
        self.assertEqual(memory._attribution("AirROI estimates 1665 listings."), "AirROI")

    def test_an_unattributed_claim_has_no_attribution(self):
        self.assertIsNone(memory._attribution("Manchester has 6951 active listings."))

    def test_differently_attributed_claims_are_distinguishable(self):
        a = memory._attribution("AirDNA reported 6951 listings in Manchester.")
        b = memory._attribution("AirROI reported 1665 listings in Manchester.")
        self.assertNotEqual(a, b)
        self.assertTrue(a and b, "both must be attributed for this to be disagreement, not conflict")

    def test_contested_records_stay_retrievable(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = memory.WORKSPACE
            try:
                memory.WORKSPACE = pathlib.Path(tmp)
                rec = {"type": "episodic",
                       "claim": "AirROI reported 1665 active listings in Manchester.",
                       "scope": "v.x",
                       "provenance": {"author_agent": "market-researcher",
                                      "evidence_grade": "estimated"}}
                memory.contest("v", rec, "mem_other", "different platform coverage")
                stored = memory.load_all("v")
                self.assertEqual(len(stored), 1)
                self.assertEqual(stored[0]["status"], "contested")
                self.assertIn("mem_other", stored[0]["contested_with"])
                self.assertTrue(stored[0]["contest_note"])
            finally:
                memory.WORKSPACE = original

    def test_contest_requires_a_note(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = memory.WORKSPACE
            try:
                memory.WORKSPACE = pathlib.Path(tmp)
                rec = {"type": "episodic", "claim": "X reported 1 thing about the market.",
                       "scope": "v.x",
                       "provenance": {"author_agent": "a", "evidence_grade": "estimated"}}
                self.assertEqual(memory.contest("v", rec, "mem_other", ""), 1,
                                 "recording a disagreement without saying why teaches nothing")
            finally:
                memory.WORKSPACE = original


class TestConsolidation(unittest.TestCase):
    def test_promotion_needs_independent_observers(self):
        """Three observations from one agent is one perspective repeated, not corroboration."""
        with tempfile.TemporaryDirectory() as tmp:
            original = memory.WORKSPACE
            try:
                memory.WORKSPACE = pathlib.Path(tmp)
                d = memory.mem_dir("v") / "episodic"
                d.mkdir(parents=True)
                for i in range(3):
                    (d / f"e{i}.json").write_text(json.dumps({
                        "id": f"e{i}", "type": "episodic", "status": "active",
                        "claim": "Hosts store spare linen in the property.", "scope": "v.x",
                        "provenance": {"author_agent": "same-agent", "evidence_grade": "sourced",
                                       "created_at": "2026-01-01T00:00:00+00:00"}}))
                memory.consolidate("v")
                semantic = [r for r in memory.load_all("v") if r["type"] == "semantic"]
                self.assertEqual(semantic, [], "one agent repeating itself must not become a fact")
            finally:
                memory.WORKSPACE = original

    def test_three_independent_observers_promote(self):
        with tempfile.TemporaryDirectory() as tmp:
            original = memory.WORKSPACE
            try:
                memory.WORKSPACE = pathlib.Path(tmp)
                d = memory.mem_dir("v") / "episodic"
                d.mkdir(parents=True)
                for i, agent in enumerate(["a", "b", "c"]):
                    (d / f"e{i}.json").write_text(json.dumps({
                        "id": f"e{i}", "type": "episodic", "status": "active",
                        "claim": "Hosts store spare linen in the property.", "scope": "v.x",
                        "provenance": {"author_agent": agent, "evidence_grade": "sourced",
                                       "created_at": "2026-01-01T00:00:00+00:00"}}))
                memory.consolidate("v")
                semantic = [r for r in memory.load_all("v") if r["type"] == "semantic"]
                self.assertEqual(len(semantic), 1)
                self.assertEqual(len(semantic[0]["promoted_from"]), 3)
            finally:
                memory.WORKSPACE = original


def artifact_lb(confidence: str, rows: list[tuple[str, str, str]]) -> str:
    """Like `artifact()`, but with an explicit Load-bearing column — rows are
    (claim, grade, 'yes'|'no')."""
    table = "\n".join(f"| {claim} | src | {grade} | {lb} |" for claim, grade, lb in rows)
    return f"""# Test artifact
- **Skill:** market-sizing
- **Confidence:** {confidence}

## Summary
A summary long enough to clear the minimum-length check that rejects stubs pretending to be work.

## Body
Body text.

## Evidence
| Claim | Source | Grade | Load-bearing |
|---|---|---|---|
{table}

## Open questions
Something unresolved.

## Next action
Someone does something.
"""


class TestLoadBearingColumn(unittest.TestCase):
    """rule 6 of OUTPUT_CONTRACT.md: a row is only excluded from the confidence check when marked,
    and the marker must come from the claim or grade cell, never from prose in the Source cell —
    an author should not be able to switch the check off by writing an explanation there."""

    def test_a_dedicated_column_marks_a_row_not_load_bearing(self):
        body = artifact_lb("sourced", [("headline number", "sourced", "yes"),
                                       ("logo colour", "guessed", "no")])
        rows = rw.parse_evidence_grades(body)
        load_bearing = [(c, g) for c, g, lb in rows if lb]
        self.assertEqual(len(load_bearing), 1)
        self.assertEqual(load_bearing[0][1], "sourced")

    def test_inline_marker_in_the_claim_cell_still_works(self):
        body = artifact("sourced", [("a", "sourced"),
                                    ("colour of the logo (not load-bearing)", "guessed")])
        rows = rw.parse_evidence_grades(body)
        load_bearing = [(c, g) for c, g, lb in rows if lb]
        self.assertEqual(len(load_bearing), 1)

    def test_prose_in_the_source_cell_does_not_switch_off_the_check(self):
        """An author writing 'this is why it is not load-bearing' in the Source column must not
        exempt the row -- only the claim cell, the grade cell, or a dedicated column may."""
        table = ('| a headline claim | this figure explains why it is not load-bearing here | '
                 'guessed |')
        body = f"""# Test artifact
- **Skill:** market-sizing
- **Confidence:** sourced

## Summary
A summary long enough to clear the minimum-length check that rejects stubs pretending to be work.

## Body
Body text.

## Evidence
| Claim | Source | Grade |
|---|---|---|
{table}

## Open questions
Something unresolved.

## Next action
Someone does something.
"""
        rows = rw.parse_evidence_grades(body)
        load_bearing = [(c, g) for c, g, lb in rows if lb]
        self.assertEqual(len(load_bearing), 1, "the guessed row must still count as load-bearing")
        self.assertEqual(load_bearing[0][1], "guessed")

    def test_confidence_check_uses_the_dedicated_column(self):
        body = artifact_lb("sourced", [("headline number", "sourced", "yes"),
                                       ("logo colour", "guessed", "no")])
        with tempfile.TemporaryDirectory() as tmp:
            venture_dir = pathlib.Path(tmp) / "v"
            original = rw.WORKSPACE
            try:
                rw.WORKSPACE = pathlib.Path(tmp)
                (venture_dir / "market").mkdir(parents=True)
                target = venture_dir / "market" / "out.md"
                target.write_text(body)
                run = {"venture": "v", "workflow": "wf", "steps": [
                    {"id": "s", "agent": "market-researcher", "skills": ["market-sizing"],
                     "does": "x", "produces": "out.md", "done_when": "x", "status": "pending"}]}
                (venture_dir / "run.json").write_text(json.dumps(run))
                org = Organisation()
                rc = rw.done("v", "s", org, tokens=None)
                self.assertEqual(rc, 0, "a not-load-bearing guess must not cap the confidence")
            finally:
                rw.WORKSPACE = original


class TestStepInvalidation(unittest.TestCase):
    """A finding can land on a step that already finished. The run must stop counting that step as
    done rather than showing 'done' and 'blocked' at once, and a block declared by a step that is
    itself invalidated must not be clearable on its own say-so."""

    def _run(self):
        return {
            "venture": "v", "workflow": "wf", "blocks": {},
            "steps": [
                {"id": "size", "agent": "a", "status": "done", "artifact": "market/size.md"},
                {"id": "competition", "agent": "b", "status": "done",
                 "artifact": "market/competition.md"},
                {"id": "pricing", "agent": "c", "status": "pending"},
            ],
        }

    def test_a_block_on_a_completed_step_reopens_it(self):
        run = self._run()
        reopened = rw.invalidate(run, ["size"], declared_by="competition")
        self.assertEqual(reopened, ["size"])
        step = next(s for s in run["steps"] if s["id"] == "size")
        self.assertEqual(step["status"], "invalidated")
        self.assertEqual(step["invalidated_by"], "competition")
        self.assertNotIn("artifact", step)
        self.assertEqual(step["superseded_artifact"], "market/size.md")

    def test_a_pending_step_is_not_invalidated_only_blocked(self):
        run = self._run()
        reopened = rw.invalidate(run, ["pricing"], declared_by="competition")
        self.assertEqual(reopened, [])
        self.assertEqual(next(s for s in run["steps"] if s["id"] == "pricing")["status"], "pending")

    def test_a_block_declared_by_a_now_invalidated_step_is_flagged_stale(self):
        run = self._run()
        run["blocks"]["pricing"] = {"declared_by": "size", "reason": "guessed inputs",
                                    "resolved_by": []}
        rw.invalidate(run, ["size"], declared_by="competition")
        self.assertTrue(run["blocks"]["pricing"].get("declared_by_invalidated"))

    def test_unblock_refuses_when_the_declaring_step_is_invalidated(self):
        with tempfile.TemporaryDirectory() as tmp:
            venture_dir = pathlib.Path(tmp) / "v"
            venture_dir.mkdir(parents=True)
            run = self._run()
            run["blocks"]["pricing"] = {"declared_by": "size", "reason": "guessed inputs",
                                        "resolved_by": [], "declared_by_invalidated": True}
            (venture_dir / "run.json").write_text(json.dumps(run))
            original = rw.WORKSPACE
            try:
                rw.WORKSPACE = pathlib.Path(tmp)
                rc = rw.unblock("v", "pricing", evidence="trying it anyway")
                self.assertEqual(rc, 1)
                after = json.loads((venture_dir / "run.json").read_text())
                self.assertIn("pricing", after["blocks"], "the block must remain in force")
            finally:
                rw.WORKSPACE = original

    def test_outstanding_blocks_reports_both_blocks_and_invalidated_steps(self):
        run = self._run()
        run["blocks"]["pricing"] = {"declared_by": "size", "reason": "x", "resolved_by": []}
        rw.invalidate(run, ["size"], declared_by="competition")
        health = rw.outstanding_blocks(run)
        self.assertIn("pricing", health["blocks"])
        self.assertIn("size", health["invalidated"])


class TestGovernedArtifactsAreSchemaChecked(unittest.TestCase):
    """A step whose done_when says 'schema-valid verdict' produced no schema check at all -- any
    markdown file of the right length and shape would pass. A step is only governed when a schema
    of the same name as its `produces` file exists; everything else is unaffected."""

    def test_schema_for_matches_by_produces_filename(self):
        self.assertEqual(rw.schema_for("council-verdict.md"), "council-verdict")
        self.assertIsNone(rw.schema_for("competitive-map.md"),
                          "most artifacts have no governing schema and must not require one")

    def test_a_governed_artifact_without_a_structured_block_is_refused(self):
        record, problem = rw.parse_structured("no fenced block here", "council-verdict")
        self.assertIsNone(record)
        self.assertIn("council-verdict", problem)

    def test_an_unparseable_structured_block_is_refused(self):
        body = "```council-verdict\nnot: [valid, yaml: broken\n```"
        record, problem = rw.parse_structured(body, "council-verdict")
        self.assertIsNone(record)
        self.assertIsNotNone(problem)

    def test_a_well_formed_block_parses(self):
        body = "```council-verdict\nverdict: reject\nfindings: []\n```"
        record, problem = rw.parse_structured(body, "council-verdict")
        self.assertIsNone(problem)
        self.assertEqual(record["verdict"], "reject")

    def test_council_step_completion_enforces_the_schema(self):
        """A council-verdict.md with no ```council-verdict block, or one that violates the schema,
        must be refused by `done` even though it otherwise satisfies the output contract."""
        prose = artifact("sourced", [("a", "sourced")])
        with tempfile.TemporaryDirectory() as tmp:
            venture_dir = pathlib.Path(tmp) / "v"
            original = rw.WORKSPACE
            try:
                rw.WORKSPACE = pathlib.Path(tmp)
                (venture_dir / "council").mkdir(parents=True)
                target = venture_dir / "council" / "council-verdict.md"
                target.write_text(prose)
                run = {"venture": "v", "workflow": "wf", "steps": [
                    {"id": "council", "agent": "council-director",
                     "skills": ["verdict-writing"], "does": "x",
                     "produces": "council-verdict.md", "done_when": "x", "status": "pending"}]}
                (venture_dir / "run.json").write_text(json.dumps(run))
                org = Organisation()
                rc = rw.done("v", "council", org, tokens=None)
                self.assertEqual(rc, 1, "prose with no structured verdict block must be refused")
            finally:
                rw.WORKSPACE = original


class TestCouncilVerdictSchemaIntegrity(unittest.TestCase):
    """The Council exists to say no. A schema that lets it write 'approve' over its own blocker
    findings would let a single verdict document contradict itself and still pass."""

    def setUp(self):
        root = pathlib.Path(__file__).resolve().parent.parent
        self.schema = schema_validate.load(root, "council-verdict")

    def _base(self, verdict: str, findings: list[dict]) -> dict:
        return {"id": "ver_x", "subject_artifact": "a.md", "requested_decision": "spend",
                "verdict": verdict, "findings": findings, "issued_by": "council-director",
                "issued_at": "2026-09-11T00:00:00Z"}

    def _blocker(self, **overrides) -> dict:
        finding = {"id": "F1", "severity": "blocker", "finding": "x",
                  "failure_scenario": "a concrete sequence of events leading to harm",
                  "raised_by": ["a"], "remedy": "r", "owner": "o", "acceptance_criterion": "c"}
        finding.update(overrides)
        return finding

    def test_approve_over_an_open_blocker_is_rejected(self):
        errors = schema_validate.validate(self._base("approve", [self._blocker()]), self.schema)
        self.assertTrue(errors)

    def test_reject_over_a_blocker_is_accepted(self):
        errors = schema_validate.validate(self._base("reject", [self._blocker()]), self.schema)
        self.assertEqual(errors, [])

    def test_a_blocker_without_an_acceptance_criterion_is_rejected(self):
        finding = self._blocker()
        del finding["acceptance_criterion"]
        errors = schema_validate.validate(self._base("reject", [finding]), self.schema)
        self.assertTrue(any("acceptance_criterion" in e for e in errors))

    def test_a_major_finding_without_a_remedy_is_rejected(self):
        finding = self._blocker(severity="major", id="F2")
        del finding["remedy"]
        errors = schema_validate.validate(self._base("reject", [finding]), self.schema)
        self.assertTrue(any("remedy" in e for e in errors))

    def test_approve_with_conditions_requires_at_least_one_finding(self):
        errors = schema_validate.validate(self._base("approve_with_conditions", []), self.schema)
        self.assertTrue(errors)

    def test_a_note_finding_does_not_block_approval(self):
        note = {"id": "F1", "severity": "note", "finding": "x",
               "failure_scenario": "a concrete sequence of events leading to harm",
               "raised_by": ["a"]}
        errors = schema_validate.validate(self._base("approve", [note]), self.schema)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
