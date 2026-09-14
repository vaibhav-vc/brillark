"""Tests for the minimal JSON Schema validator (tools/validate.py).

Every knowledge schema in the repository is draft 2020-12; `jsonschema` is not a dependency, so this
file is the only thing standing between "the schema says X" and a document that violates X passing
anyway. It only needs to cover the keyword subset the schemas actually use -- see
test_system_integrity.py's schema sweep for the guarantee that stays true.

    python3 ai-system/tests/test_validate.py
"""
from __future__ import annotations

import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import validate  # noqa: E402


class TestPrimitives(unittest.TestCase):
    def test_type_mismatch_is_caught(self):
        self.assertTrue(validate.validate("x", {"type": "integer"}))

    def test_bool_is_not_an_integer(self):
        """Python's bool is an int subclass; a schema asking for an integer must not accept True."""
        self.assertTrue(validate.validate(True, {"type": "integer"}))

    def test_enum_rejects_an_unlisted_value(self):
        errors = validate.validate("z", {"enum": ["a", "b"]})
        self.assertTrue(errors)

    def test_pattern_is_enforced(self):
        self.assertTrue(validate.validate("abc", {"type": "string", "pattern": "^[0-9]+$"}))
        self.assertEqual(validate.validate("123", {"type": "string", "pattern": "^[0-9]+$"}), [])

    def test_min_and_max_length(self):
        self.assertTrue(validate.validate("hi", {"type": "string", "minLength": 5}))
        self.assertTrue(validate.validate("way too long", {"type": "string", "maxLength": 3}))

    def test_numeric_bounds(self):
        self.assertTrue(validate.validate(5, {"type": "integer", "minimum": 10}))
        self.assertTrue(validate.validate(5, {"type": "integer", "maximum": 1}))
        self.assertEqual(validate.validate(5, {"type": "integer", "minimum": 1, "maximum": 10}), [])


class TestObjectsAndArrays(unittest.TestCase):
    def test_missing_required_field(self):
        errors = validate.validate({"a": 1}, {"type": "object", "required": ["a", "b"]})
        self.assertTrue(any("'b'" in e for e in errors))

    def test_additional_properties_false_rejects_unknown_keys(self):
        schema = {"type": "object", "properties": {"a": {"type": "string"}},
                 "additionalProperties": False}
        self.assertTrue(validate.validate({"a": "x", "z": 1}, schema))
        self.assertEqual(validate.validate({"a": "x"}, schema), [])

    def test_nested_property_errors_carry_a_useful_path(self):
        schema = {"type": "object", "properties": {"findings": {"type": "array", "items": {
            "type": "object", "required": ["severity"]}}}}
        errors = validate.validate({"findings": [{}]}, schema)
        self.assertTrue(any("findings[0]" in e for e in errors))

    def test_min_and_max_items(self):
        schema = {"type": "array", "minItems": 2}
        self.assertTrue(validate.validate([1], schema))
        self.assertEqual(validate.validate([1, 2], schema), [])

    def test_unique_items(self):
        schema = {"type": "array", "uniqueItems": True}
        self.assertTrue(validate.validate([1, 1], schema))
        self.assertEqual(validate.validate([1, 2], schema), [])


class TestConditionals(unittest.TestCase):
    """These are the keywords council-verdict.schema.json actually relies on to make the schema
    itself enforce the Council's integrity rules, so they get direct coverage."""

    def test_if_then_applies_only_when_the_condition_matches(self):
        schema = {"if": {"properties": {"kind": {"const": "a"}}, "required": ["kind"]},
                  "then": {"required": ["extra"]}}
        self.assertTrue(validate.validate({"kind": "a"}, schema))
        self.assertEqual(validate.validate({"kind": "b"}, schema), [])
        self.assertEqual(validate.validate({"kind": "a", "extra": 1}, schema), [])

    def test_all_of_accumulates_every_branch(self):
        schema = {"allOf": [{"required": ["a"]}, {"required": ["b"]}]}
        errors = validate.validate({}, schema)
        self.assertEqual(len(errors), 2)

    def test_any_of_needs_only_one_match(self):
        schema = {"anyOf": [{"type": "string"}, {"type": "integer"}]}
        self.assertEqual(validate.validate(5, schema), [])
        self.assertTrue(validate.validate(5.5, schema))

    def test_one_of_rejects_when_more_than_one_branch_matches(self):
        schema = {"oneOf": [{"type": "number"}, {"minimum": 0}]}
        self.assertTrue(validate.validate(5, schema), "5 satisfies both branches, oneOf must fail")

    def test_contains_requires_at_least_one_matching_item(self):
        schema = {"type": "array", "contains": {"const": "blocker"}}
        self.assertTrue(validate.validate(["a", "b"], schema))
        self.assertEqual(validate.validate(["a", "blocker"], schema), [])

    def test_not_rejects_a_forbidden_shape(self):
        schema = {"not": {"const": "approve"}}
        self.assertTrue(validate.validate("approve", schema))
        self.assertEqual(validate.validate("reject", schema), [])


class TestUnsupportedKeywordFailsLoudly(unittest.TestCase):
    def test_an_unknown_keyword_is_refused_rather_than_silently_passed(self):
        errors = validate.validate({"a": 1}, {"type": "object", "propertyNames": {"minLength": 1}})
        self.assertTrue(errors)
        self.assertIn("does not support", errors[0])


class TestRealSchemas(unittest.TestCase):
    """The keyword sweep in test_system_integrity.py confirms every schema uses only supported
    keywords; this confirms the validator actually agrees with a real, well-formed instance."""

    def test_a_well_formed_council_verdict_validates_clean(self):
        schema = validate.load(ROOT, "council-verdict")
        doc = {
            "id": "ver_x", "subject_artifact": "a.md", "requested_decision": "spend",
            "verdict": "reject", "issued_by": "council-director",
            "issued_at": "2026-09-11T00:00:00Z",
            "findings": [{"id": "F1", "severity": "blocker", "finding": "x",
                         "failure_scenario": "a concrete sequence of events leading to harm",
                         "raised_by": ["a"], "remedy": "r", "owner": "o",
                         "acceptance_criterion": "c"}],
        }
        self.assertEqual(validate.validate(doc, schema), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
