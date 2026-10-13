# region MODULE_CONTRACT [DOMAIN(9): JsonSchema, Adapter; CONCEPT(9): Validator, KeywordSubset, RuleAnnotation; TECH(6): re, dataclass]
## @modulecontract
## @purpose To validate an adapter against runtime/adapter.schema.json with the standard library alone, so the adapter
## contract is enforced by the tool itself and a violation names the JSON pointer, the keyword and the report rule of the
## fault, without a third-party validator and without ever repeating a string value of the adapter.
## @scope The supported keyword subset, the keyword check of a schema, the validator, the pointer escaping.
## @input A parsed JSON instance and a parsed JSON schema.
## @output A list of Violation (pointer, rule, keyword, message); SchemaUnsupported when the schema leaves the subset.
## @links [USES_API(6): re; READS_DATA_FROM(9): runtime/adapter.schema.json (parsed by the caller)]
## @links_to_spec BR-4, BR-5, AC-4, AC-5
## @invariants
## - validate never raises for an instance; only a schema outside the subset raises SchemaUnsupported.
## - A Python bool is never an integer or a number.
## - A violation message names keys and keywords and never a string value of the instance.
## - x-rule replaces the rule for its subtree; a $ref follows the definition, whose own x-rule then applies.
## @rationale
## Q: Why a validator of our own and not the jsonschema package?
## A: The tool is standard-library only (AC-P1), and the schema uses a small subset; an unsupported keyword is refused
## (input.schema) so a schema that outgrows the subset is noticed, not silently half-checked.
## Q: Why does each violation carry a rule?
## A: One row per fault under a named rule lets a drill and a reader tell a capability fault from a file fault.
## @changes
## LAST_CHANGE: [v0.1.0 - Initial creation: keyword subset check and validator with x-rule.]
## @modulemap
## CLASS 6[One schema fault: pointer, rule, keyword, message] => Violation
## CLASS 5[A schema outside the supported subset] => SchemaUnsupported
## FUNC 7[Escape a key as an RFC 6901 pointer token] => escape_pointer
## FUNC 3[Whether a value can stand as a subschema] => _is_schema_object
## FUNC 9[Refuse a schema that leaves the subset] => check_schema_keywords
## FUNC 7[Whether a value has a JSON type; a bool is never a number] => _json_type_ok
## FUNC 6[JSON equality in which True is not 1 and False is not 0] => _json_equal
## FUNC 10[Validate an instance against a schema] => validate
## @usecases
## - [check_schema_keywords]: Adapter mode -> vet the schema of the spec -> an unsupported keyword refuses the run
## - [validate]: Adapter mode -> validate the adapter -> one violation per fault with its pointer and rule
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: json schema validator, keyword subset, x-rule, $ref, $defs, anyOf, allOf, if then else, pointer RFC 6901, SchemaUnsupported, Violation, stdlib
# STRUCTURE: ▶ ┌instance,schema┐ → ◇ x-rule ? rule← → ⚡ $ref → ◇ type ✗ → ⎋ one violation → ○ enum const required properties additionalProperties items minLength pattern → ⊕ anyOf allOf if/then/else → ⟦List⟅Violation⟆⟧

import logging
import re
from dataclasses import dataclass
from typing import List, Optional

logger = logging.getLogger("conform.schema")

SUPPORTED = {
    "type", "enum", "const", "required", "properties", "additionalProperties", "items", "minLength", "pattern",
    "anyOf", "allOf", "if", "then", "else", "$ref", "$defs",
}
ANNOTATIONS = {"$schema", "$id", "$comment", "title", "description", "x-rule"}

_TYPES = ("object", "array", "string", "integer", "number", "boolean", "null")
_REF_FORM = re.compile(r"^#/\$defs/([A-Za-z0-9_-]+)$")
_MAX_DEPTH = 200


# region CLASS_Violation [DOMAIN(8): JsonSchema; CONCEPT(9): Violation, Pointer, Rule; TECH(5): dataclass]
## @purpose One fault of an instance: where it is (an RFC 6901 pointer), which report rule owns it, which keyword found it
## and a message that names keys and keywords only.
@dataclass(frozen=True)
class Violation:
    pointer: str
    rule: str
    keyword: str
    message: str
# endregion CLASS_Violation


# region CLASS_SchemaUnsupported [DOMAIN(8): JsonSchema; CONCEPT(9): Refusal, KeywordSubset; TECH(5): Exception]
## @purpose The signal that a schema uses a keyword, a reference or a shape outside the supported subset; the adapter mode
## turns it into NOT RUN input.schema.
class SchemaUnsupported(Exception):
    pass
# endregion CLASS_SchemaUnsupported


# region FUNC_escape_pointer [DOMAIN(5): JsonSchema; CONCEPT(6): Pointer; TECH(4): str.replace]
## @purpose Escape one key or index as an RFC 6901 token: the tilde first, then the slash, so a pointer is unambiguous.
## @io str -> str
## @complexity 1
def escape_pointer(token: str) -> str:
    return token.replace("~", "~0").replace("/", "~1")
# endregion FUNC_escape_pointer


# region FUNC__is_schema_object [DOMAIN(4): JsonSchema; CONCEPT(5): Shape; TECH(4): isinstance]
## @purpose Say whether a value can stand as a subschema in this subset: only an object can.
## @io object -> bool
## @complexity 1
def _is_schema_object(value: object) -> bool:
    return isinstance(value, dict)
# endregion FUNC__is_schema_object


# region FUNC_check_schema_keywords [DOMAIN(9): JsonSchema; CONCEPT(9): KeywordSubset, Ref; TECH(6): recursion, re]
## @purpose Walk every subschema and refuse anything the validator would not honour: a keyword outside SUPPORTED and
## ANNOTATIONS, a value of the wrong shape, a $ref not of the form #/$defs/NAME, or a $ref to a missing definition. A
## schema that passes is one validate can follow to the end.
## @uses SUPPORTED, ANNOTATIONS, _REF_FORM
## @io (dict, Optional[dict], str) -> None
## @complexity 8
def check_schema_keywords(schema: object, root: Optional[dict] = None, where: str = "#") -> None:
    # === LOG DRIVEN DEVELOPMENT 2.0 (LDD) ===
    # The walk logs one line at IMP:2 per subschema (the place only); a refusal logs IMP:10 with the place.
    if not _is_schema_object(schema):
        logger.error("[IMP:10][check_schema_keywords][SUBSET] where=%s reason=not-an-object", where)
        raise SchemaUnsupported("subschema at %s is not an object" % where)
    if root is None:
        root = schema  # type: ignore[assignment]
    logger.debug("[IMP:2][check_schema_keywords][WALK] where=%s keys=%d", where, len(schema))  # type: ignore[arg-type]
    for key, value in schema.items():  # type: ignore[union-attr]
        if key == "x-rule":
            if not isinstance(value, str) or not value:
                raise SchemaUnsupported("x-rule at %s is not a non-empty string" % where)
            continue
        if key in ANNOTATIONS:
            continue
        if key not in SUPPORTED:
            logger.error("[IMP:10][check_schema_keywords][SUBSET] where=%s keyword=%s", where, key)
            raise SchemaUnsupported("keyword %s at %s is outside the supported subset" % (key, where))
        here = where + "/" + key
        if key == "type":
            if value not in _TYPES:
                raise SchemaUnsupported("type at %s is not one of the seven types" % where)
        elif key == "enum":
            if not isinstance(value, list) or not value:
                raise SchemaUnsupported("enum at %s is not a non-empty list" % where)
        elif key == "required":
            if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                raise SchemaUnsupported("required at %s is not a list of strings" % where)
        elif key == "properties":
            if not isinstance(value, dict):
                raise SchemaUnsupported("properties at %s is not an object" % where)
            for name, sub in value.items():
                check_schema_keywords(sub, root, here + "/" + name)
        elif key == "additionalProperties":
            if isinstance(value, dict):
                check_schema_keywords(value, root, here)
            elif not isinstance(value, bool):
                raise SchemaUnsupported("additionalProperties at %s is neither a boolean nor an object" % where)
        elif key in ("items", "if", "then", "else"):
            check_schema_keywords(value, root, here)
        elif key == "minLength":
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise SchemaUnsupported("minLength at %s is not a non-negative integer" % where)
        elif key == "pattern":
            try:
                re.compile(value)  # type: ignore[arg-type]
            except (re.error, TypeError):
                raise SchemaUnsupported("pattern at %s is not a regular expression" % where)
        elif key in ("anyOf", "allOf"):
            if not isinstance(value, list) or not value:
                raise SchemaUnsupported("%s at %s is not a non-empty list" % (key, where))
            for index, member in enumerate(value):
                check_schema_keywords(member, root, here + "/" + str(index))
        elif key == "$defs":
            if not isinstance(value, dict):
                raise SchemaUnsupported("$defs at %s is not an object" % where)
            for name, sub in value.items():
                check_schema_keywords(sub, root, here + "/" + name)
        elif key == "$ref":
            found = _REF_FORM.match(value) if isinstance(value, str) else None
            if found is None:
                logger.error("[IMP:10][check_schema_keywords][SUBSET] where=%s reason=ref-form", where)
                raise SchemaUnsupported("$ref at %s is not of the form #/$defs/NAME" % where)
            definitions = root.get("$defs")
            if not isinstance(definitions, dict) or found.group(1) not in definitions:
                logger.error("[IMP:10][check_schema_keywords][SUBSET] where=%s reason=ref-missing", where)
                raise SchemaUnsupported("$ref at %s names a definition that does not exist" % where)
# endregion FUNC_check_schema_keywords


# region FUNC__json_type_ok [DOMAIN(6): JsonSchema; CONCEPT(8): Type, BoolIsNotNumber; TECH(4): isinstance]
## @purpose Tell whether a Python value has a JSON type; a bool is a boolean and never an integer or a number.
## @io (object, str) -> bool
## @complexity 3
def _json_type_ok(value: object, name: str) -> bool:
    if name == "object":
        return isinstance(value, dict)
    if name == "array":
        return isinstance(value, list)
    if name == "string":
        return isinstance(value, str)
    if name == "boolean":
        return isinstance(value, bool)
    if name == "null":
        return value is None
    if isinstance(value, bool):
        return False
    if name == "integer":
        return isinstance(value, int)
    return isinstance(value, (int, float))
# endregion FUNC__json_type_ok


# region FUNC__json_equal [DOMAIN(5): JsonSchema; CONCEPT(7): Equality, BoolIsNotNumber; TECH(4): type]
## @purpose Compare two JSON values so that True is not 1 and False is not 0, as enum and const require.
## @io (object, object) -> bool
## @complexity 3
def _json_equal(left: object, right: object) -> bool:
    if isinstance(left, bool) or isinstance(right, bool):
        return isinstance(left, bool) and isinstance(right, bool) and left == right
    return left == right
# endregion FUNC__json_equal


# region FUNC_validate [DOMAIN(10): JsonSchema; CONCEPT(10): Validator, Pointer, Rule; TECH(7): recursion, x-rule, $ref]
## @purpose Judge an instance against a schema of the supported subset and return every violation in a fixed order, each
## with its pointer, its rule (x-rule of the nearest subschema that has one) and its keyword. A type mismatch is the only
## violation of its subschema; anyOf gives one violation at its own pointer when no member is clean.
## @uses check_schema_keywords (the caller vets the schema), escape_pointer, _json_type_ok, _json_equal
## @io (object, dict, Optional[dict], str, str) -> List[Violation]
## @complexity 10
def validate(instance: object, schema: dict, root: Optional[dict] = None, pointer: str = "",
             rule: str = "adapter.schema", _depth: int = 0) -> List[Violation]:
    # === LOG DRIVEN DEVELOPMENT 2.0 (LDD) ===
    # A trace line at IMP:1 per subschema visit would flood; the only lines here are IMP:10 for a refused schema depth.
    if _depth > _MAX_DEPTH:
        logger.error("[IMP:10][validate][DEPTH] pointer_depth=%d", _depth)
        raise SchemaUnsupported("schema nests deeper than %d levels (a reference cycle)" % _MAX_DEPTH)
    if root is None:
        root = schema
    found = []  # type: List[Violation]
    rule = schema.get("x-rule", rule)
    kind = schema.get("type")
    if kind is not None and not _json_type_ok(instance, kind):
        found.append(Violation(pointer, rule, "type", "expected a value of type %s" % kind))
        return found
    if "$ref" in schema:
        name = _REF_FORM.match(schema["$ref"]).group(1)  # type: ignore[union-attr]
        found.extend(validate(instance, root["$defs"][name], root, pointer, rule, _depth + 1))
    if "enum" in schema and not any(_json_equal(instance, member) for member in schema["enum"]):
        found.append(Violation(pointer, rule, "enum", "value is not one of the allowed values"))
    if "const" in schema and not _json_equal(instance, schema["const"]):
        found.append(Violation(pointer, rule, "const", "value differs from the required constant"))
    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance:
                found.append(Violation(pointer, rule, "required", "missing key %s" % key))
        properties = schema.get("properties", {})
        for key, sub in properties.items():
            if key in instance:
                found.extend(validate(instance[key], sub, root, pointer + "/" + escape_pointer(key), rule, _depth + 1))
        if "additionalProperties" in schema:
            extra = schema["additionalProperties"]
            for key in instance:
                if key in properties:
                    continue
                if extra is False:
                    found.append(Violation(pointer, rule, "additionalProperties", "unexpected key %s" % key))
                elif isinstance(extra, dict):
                    found.extend(validate(instance[key], extra, root, pointer + "/" + escape_pointer(key), rule,
                                          _depth + 1))
    if isinstance(instance, list) and "items" in schema:
        for index, item in enumerate(instance):
            found.extend(validate(item, schema["items"], root, pointer + "/" + str(index), rule, _depth + 1))
    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            found.append(Violation(pointer, rule, "minLength", "shorter than %d characters" % schema["minLength"]))
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            found.append(Violation(pointer, rule, "pattern", "does not match the required pattern"))
    if "anyOf" in schema:
        if not any(not validate(instance, member, root, pointer, rule, _depth + 1) for member in schema["anyOf"]):
            found.append(Violation(pointer, rule, "anyOf", "matches none of the alternatives"))
    if "allOf" in schema:
        for member in schema["allOf"]:
            found.extend(validate(instance, member, root, pointer, rule, _depth + 1))
    if "if" in schema:
        holds = not validate(instance, schema["if"], root, pointer, rule, _depth + 1)
        branch = schema.get("then") if holds else schema.get("else")
        if branch is not None:
            found.extend(validate(instance, branch, root, pointer, rule, _depth + 1))
    return found
# endregion FUNC_validate
