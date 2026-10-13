# region MODULE_CONTRACT [DOMAIN(9): JsonSchema, AdapterContract; CONCEPT(9): Validator, KeywordSubset, PinnedCases; TECH(6): pytest, json]
## @modulecontract
## @purpose To prove that the standard-library validator honours the adapter schema the way a reference validator does: the
## schema stays inside the supported keyword subset, a schema outside the subset is refused and never half-checked, a valid
## adapter has no violation, each of the eight pinned faults gives exactly one violation with its pointer, keyword and rule,
## and a Python bool is never taken for a number.
## @scope The validator and the keyword check of tools/conformlib/schema.py against runtime/adapter.schema.json; the adapter
## checks that use them are proved in test_adapter.py.
## @input The real schema, the real example adapter, a small valid adapter built here, and small schemas built here.
## @output One pass or fail per pinned case and per property of the validator.
## @links [USES_API(9): conformlib.schema.validate, check_schema_keywords; READS_DATA_FROM(8): runtime/adapter.schema.json, examples/adapter.example.json]
## @links_to_spec AC-4, AC-5
## @invariants
## - The base adapter here is valid; each pinned case changes one thing of a deep copy of it.
## - A case asserts the pointer, the keyword and the rule of its one violation, and the number of violations.
## - No test writes a file.
## @rationale
## Q: Why pin eight cases and not compare with a reference validator at run time?
## A: The tool is standard-library only and so is its test suite; the eight cases were measured once against a reference
## validator and are recorded as data, so the suite runs everywhere without a third-party package.
## Q: Why a small base adapter and not the example?
## A: The pinned pointers name files a.md, c.md and d.md; a base built here keeps the pointers stable when the example changes.
## @changes
## LAST_CHANGE: [v0.1.0 - Initial creation: subset check, refusals, valid adapters, eight pinned cases, bool rule.]
## @modulemap
## FUNC 5[A small valid adapter] => _base_adapter
## FUNC 5[Load the real schema] => _real_schema
## FUNC 7[The schema stays in the supported subset] => test_schema_file_uses_only_supported_keywords
## FUNC 8[A keyword outside the subset is refused] => test_unsupported_keyword_raises
## FUNC 8[A foreign or dangling reference is refused] => test_foreign_ref_raises
## FUNC 8[A valid adapter has no violation] => test_valid_adapter_has_no_violation
## FUNC 10[Each pinned fault gives one violation] => test_pinned_case
## FUNC 7[A bool is not an integer] => test_bool_is_not_an_integer
## @usecases
## - [test_pinned_case]: QA agent -> damages one thing of a valid adapter -> the validator names the pointer, keyword and rule
## - [test_unsupported_keyword_raises]: QA agent -> adds a keyword outside the subset -> the run would be refused, not half-checked
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: json schema validator tests, keyword subset, pinned cases, pointer, keyword, rule, anyOf, minLength, enum, additionalProperties, bool not integer, valid adapter
# STRUCTURE: ▶ schema file → ◇ keywords ⊆ SUPPORTED → ⚡ base adapter → ⊕ mutate one thing ∀8 → ◇ 1 violation ∧ pointer ∧ keyword ∧ rule → ⚡ bool → ⎋ assert

import json
import pathlib

import pytest

from conformlib import schema

RULE_CAPABILITY = "adapter.capability"
RULE_PARAMETER = "adapter.parameter"
RULE_NOT_APPLIED = "adapter.not-applied"
RULE_OVERRIDE = "adapter.override"
RULE_FILE = "adapter.file-coverage"
RULE_REFERENCE = "adapter.reference"


# region FUNC__base_adapter [DOMAIN(7): AdapterContract; CONCEPT(8): ValidInstance; TECH(4): dict]
## @purpose A small valid adapter: two parameters, two capabilities, a reference file a.md and a vendored file c.md with two
## overrides, so every pinned case has the object it damages.
## @io None -> dict
## @complexity 2
def _base_adapter() -> dict:
    digest = "0" * 64
    return {
        "harness": "sample-harness",
        "owner": "the sample owner",
        "spec_version": "0.1.0",
        "spec_root": "..",
        "parameters": {"dialog-language": "English", "owner-label": "owner"},
        "capabilities": {
            "memory": {"mechanism": "a note file"},
            "schedule": {"fallback": "start by hand"},
        },
        "files": {
            "a.md": {"mode": "reference"},
            "b.md": {"mode": "reference", "via": "notes.md"},
            "c.md": {
                "mode": "vendored",
                "path": "c-copy.md",
                "sha256": digest,
                "overrides": [
                    {"anchor": "c.first", "reason": "a reason", "owner": "an owner", "until": "2999-12-31"},
                    {"anchor": "c.second", "reason": "a reason", "owner": "an owner", "trigger": "when it changes"},
                ],
            },
            "e.md": {"mode": "not-applied", "reason": "not needed here"},
        },
    }
# endregion FUNC__base_adapter


# region FUNC__real_schema [DOMAIN(7): AdapterContract; CONCEPT(8): Schema, Load; TECH(5): json, pathlib]
## @purpose Load the schema of the repository under test as a dictionary.
## @io pathlib.Path -> dict
## @complexity 1
def _real_schema(repo_root: pathlib.Path) -> dict:
    return json.loads((repo_root / "runtime" / "adapter.schema.json").read_text(encoding="utf-8"))
# endregion FUNC__real_schema


PINNED = [
    ("capability-empty", lambda d: d["capabilities"].update({"schedule": {}}),
     "/capabilities/schedule", "anyOf", RULE_CAPABILITY),
    ("capability-blank", lambda d: d["capabilities"].update({"schedule": {"mechanism": ""}}),
     "/capabilities/schedule", "anyOf", RULE_CAPABILITY),
    ("parameter-empty", lambda d: d["parameters"].update({"dialog-language": ""}),
     "/parameters/dialog-language", "minLength", RULE_PARAMETER),
    ("not-applied-without-reason", lambda d: d["files"].update({"d.md": {"mode": "not-applied"}}),
     "/files/d.md", "required", RULE_NOT_APPLIED),
    ("override-with-neither",
     lambda d: d["files"]["c.md"]["overrides"].append({"anchor": "c.third", "reason": "a reason", "owner": "an owner"}),
     "/files/c.md/overrides/2", "anyOf", RULE_OVERRIDE),
    ("unknown-mode", lambda d: d["files"].update({"a.md": {"mode": "copied"}}),
     "/files/a.md/mode", "enum", RULE_FILE),
    ("no-mode", lambda d: d["files"].update({"a.md": {}}),
     "/files/a.md", "required", RULE_FILE),
    ("extra-key-in-reference", lambda d: d["files"].update({"a.md": {"mode": "reference", "path": "x"}}),
     "/files/a.md", "additionalProperties", RULE_REFERENCE),
]


# region FUNC_test_schema_file_uses_only_supported_keywords [DOMAIN(8): JsonSchema; CONCEPT(9): KeywordSubset; TECH(5): check_schema_keywords]
## @purpose Prove that the real schema stays inside the keyword subset the validator honours, so the adapter mode never
## refuses its own contract.
## @uses repo_root, schema.check_schema_keywords
## @io pathlib.Path -> None
## @complexity 2
def test_schema_file_uses_only_supported_keywords(repo_root):
    data = _real_schema(repo_root)
    print("[IMP:9][test_schema_subset][KEYWORDS] top_level_keys=%d defs=%d" % (len(data), len(data["$defs"])))
    schema.check_schema_keywords(data)
    assert data["x-rule"] == "adapter.schema"
    assert sorted(data["$defs"]) == ["capability", "file", "notApplied", "override", "reference", "vendored"]
# endregion FUNC_test_schema_file_uses_only_supported_keywords


# region FUNC_test_unsupported_keyword_raises [DOMAIN(9): JsonSchema; CONCEPT(9): Refusal, KeywordSubset; TECH(5): pytest.raises]
## @purpose Prove that a schema with a keyword outside the subset, a subschema that is not an object, or a wrong shape of a
## known keyword is refused with SchemaUnsupported, so it is never half-checked.
## @uses schema.check_schema_keywords
## @io None -> None
## @complexity 3
def test_unsupported_keyword_raises():
    cases = [
        {"type": "object", "minItems": 1},
        {"type": "object", "properties": {"a": {"uniqueItems": True}}},
        {"type": "object", "properties": {"a": "not a schema"}},
        {"type": "thing"},
        {"enum": []},
        {"required": "name"},
        {"x-rule": ""},
    ]
    for case in cases:
        print("[IMP:9][test_unsupported_keyword][CASE] keys=%s" % sorted(case))
        with pytest.raises(schema.SchemaUnsupported):
            schema.check_schema_keywords(case)
# endregion FUNC_test_unsupported_keyword_raises


# region FUNC_test_foreign_ref_raises [DOMAIN(9): JsonSchema; CONCEPT(9): Refusal, Ref; TECH(5): pytest.raises]
## @purpose Prove that a reference outside the form #/$defs/NAME (a foreign document, a file) and a reference to a missing
## definition are both refused.
## @uses schema.check_schema_keywords
## @io None -> None
## @complexity 3
def test_foreign_ref_raises():
    cases = [
        {"$ref": "http://example.org/other.json"},
        {"$ref": "other.json#/$defs/x"},
        {"$ref": "#/properties/a"},
        {"$ref": "#/$defs/missing", "$defs": {"present": {"type": "string"}}},
    ]
    for case in cases:
        print("[IMP:9][test_foreign_ref][CASE] ref_length=%d" % len(case["$ref"]))
        with pytest.raises(schema.SchemaUnsupported):
            schema.check_schema_keywords(case)
# endregion FUNC_test_foreign_ref_raises


# region FUNC_test_valid_adapter_has_no_violation [DOMAIN(9): AdapterContract; CONCEPT(9): ValidInstance; TECH(5): schema.validate]
## @purpose Prove that the base adapter of this module and the real example adapter of the repository both validate with no
## violation against the real schema.
## @uses repo_root, schema.validate
## @io pathlib.Path -> None
## @complexity 3
def test_valid_adapter_has_no_violation(repo_root):
    real = _real_schema(repo_root)
    example = json.loads((repo_root / "examples" / "adapter.example.json").read_text(encoding="utf-8"))
    base_found = schema.validate(_base_adapter(), real)
    example_found = schema.validate(example, real)
    print("[IMP:9][test_valid_adapter][RESULT] base=%d example=%d" % (len(base_found), len(example_found)))
    assert base_found == []
    assert example_found == []
# endregion FUNC_test_valid_adapter_has_no_violation


# region FUNC_test_pinned_case [DOMAIN(10): AdapterContract; CONCEPT(10): PinnedCase, Pointer, Keyword, Rule; TECH(6): pytest.parametrize, schema.validate]
## @purpose Prove, for one of the eight pinned faults, that the validator gives exactly one violation, at the pinned pointer,
## of the pinned keyword and under the pinned rule, and that its message repeats no string value of the instance.
## @uses repo_root, schema.validate
## @io (str, Callable, str, str, str, pathlib.Path) -> None
## @complexity 6
@pytest.mark.parametrize("case_id,mutate,pointer,keyword,rule", PINNED, ids=[p[0] for p in PINNED])
def test_pinned_case(case_id, mutate, pointer, keyword, rule, repo_root):
    data = json.loads(json.dumps(_base_adapter()))
    mutate(data)
    found = schema.validate(data, _real_schema(repo_root))
    print("[IMP:9][test_pinned_case][RESULT] case=%s violations=%d" % (case_id, len(found)))
    for item in found:
        print("[IMP:9][test_pinned_case][VIOLATION] pointer=%s keyword=%s rule=%s" % (item.pointer, item.keyword, item.rule))
    assert len(found) == 1
    assert found[0].pointer == pointer
    assert found[0].keyword == keyword
    assert found[0].rule == rule
    assert "the sample owner" not in found[0].message
    assert "a reason" not in found[0].message
# endregion FUNC_test_pinned_case


# region FUNC_test_bool_is_not_an_integer [DOMAIN(8): JsonSchema; CONCEPT(9): TypeStrictness, Bool; TECH(5): schema.validate]
## @purpose Prove that a Python bool is not accepted as an integer or a number, and that a real integer and a real number are.
## @uses schema.validate
## @io None -> None
## @complexity 3
def test_bool_is_not_an_integer():
    integer = {"type": "integer"}
    number = {"type": "number"}
    results = {
        "true-as-integer": len(schema.validate(True, integer)),
        "false-as-number": len(schema.validate(False, number)),
        "one-as-integer": len(schema.validate(1, integer)),
        "half-as-number": len(schema.validate(0.5, number)),
        "one-as-boolean": len(schema.validate(1, {"type": "boolean"})),
    }
    print("[IMP:9][test_bool_is_not_an_integer][RESULT] %s" % sorted(results.items()))
    assert results["true-as-integer"] == 1
    assert results["false-as-number"] == 1
    assert results["one-as-integer"] == 0
    assert results["half-as-number"] == 0
    assert results["one-as-boolean"] == 1
# endregion FUNC_test_bool_is_not_an_integer
