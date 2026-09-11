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


if __name__ == "__main__":
    unittest.main(verbosity=2)
