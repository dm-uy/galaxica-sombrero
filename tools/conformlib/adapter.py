# region MODULE_CONTRACT [DOMAIN(10): Adapter, Conformance; CONCEPT(10): Contract, FileCoverage, Vendored, Override, Reference; TECH(7): json, sha256, dataclass]
## @modulecontract
## @purpose To let a harness maintainer, or an agent, learn in one run whether a harness's adapter keeps the contract of
## the methodology: the adapter is valid against the schema of the spec it names, targets a known version, sets every
## parameter, meets every capability, accounts for every neutral file, and states its references, vendored copies,
## overrides and exclusions honestly. The methodology stays neutral only if drift is reported, not discovered.
## @scope The adapter mode: reading the adapter and the spec, the structural check by the schema, and the semantic rules
## of the version, parameters, capabilities, files, references, vendored copies and overrides.
## @input An adapter path; the spec root the adapter names (the neutral tree, the registries, the schema, SPEC_VERSION).
## @output Rows in a Report (FAIL, WARN, INFO, PASS) and the populations of the run; a Refusal when the run cannot judge.
## @links [USES_API(9): conformlib.markdown, conformlib.schema, conformlib.selfcheck, conformlib.report; READS_DATA_FROM(10): the adapter JSON, the spec root, harness files named by via and path]
## @links_to_spec BR-4, BR-5, AC-4, AC-5, FMT-26..FMT-38
## @invariants
## - Every refusal is a Refusal; nothing here prints, exits or parses arguments.
## - A schema fault is reported once, under its own rule; a semantic check never repeats it and skips the part it named.
## - A fresh vendored hash makes a section difference a FAIL; a stale hash makes it a WARN (the neutral file moved on).
## - The hash of a neutral file is taken over its bytes after CR and CRLF became LF.
## - Paths of the adapter (spec_root, via, path) are resolved against the adapter file's directory unless absolute.
## - A log line carries paths of the spec, counts, rules and booleans, never a string value read from the adapter.
## @rationale
## Q: Why skip an entry that already has a schema fault?
## A: A vendored entry with a malformed hash or override has no defined meaning to compare; the schema row already tells
## the reader what to fix, and the next run reports what remains.
## Q: Why compare sections by anchor and not the whole file?
## A: A harness may word one section its own way for a stated reason and a limited time; the anchor is the unit that an
## override names, so a difference outside an override is drift.
## Q: Why is a trigger checked for presence only?
## A: The tool cannot know whether a harness event has happened; it can only require that the override says when it ends.
## @changes
## LAST_CHANGE: [v0.1.0 - Initial creation of the adapter mode: loaders, structure, version, parameters, capabilities, files, references, vendored copies, overrides.]
## @modulemap
## CLASS 6[The spec an adapter names: version, registries, tree, schema] => Spec
## FUNC 5[Resolve an adapter path against the adapter's directory] => _resolve
## FUNC 3[Keep a row's subject non-empty] => _subject
## FUNC 5[Whether the schema check named a fault at or below a pointer] => _invalid_under
## FUNC 6[One PASS row for a rule that has no FAIL row] => _settle
## FUNC 8[Read the adapter JSON or refuse] => load_adapter
## FUNC 7[Resolve spec_root against the adapter's directory] => resolve_spec_root
## FUNC 5[Read a file as bytes, or None when it cannot be read] => _read_bytes
## FUNC 9[Read the spec root or refuse] => load_spec
## FUNC 9[Validate the adapter by the schema and report each fault] => check_structure
## FUNC 6[The population of the run] => record_population
## FUNC 7[spec_version against SPEC_VERSION] => check_spec_version
## FUNC 8[Parameters against the registry] => check_parameters
## FUNC 8[Capabilities against the registry] => check_capabilities
## FUNC 10[File coverage and one check per entry] => check_files
## FUNC 7[A reference entry names the neutral file] => check_reference
## FUNC 10[A vendored entry: copy, hash, overrides, sections] => check_vendored
## FUNC 8[Overrides: anchor, uniqueness, date or trigger] => check_overrides
## FUNC 8[Section differences between a neutral file and its copy] => compare_sections
## @usecases
## - [check_files]: Harness maintainer -> conform adapter -> every neutral file accounted for
## - [check_vendored]: Harness maintainer -> refresh a copy -> know which sections drifted and whether the hash is stale
## - [check_overrides]: Harness maintainer -> word a section its own way -> the override is dated or has a trigger
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: adapter mode, spec_root, load_adapter, load_spec, schema validation, spec_version, parameters, capabilities, file coverage, reference via, vendored sha256, stale hash, override until trigger, not-applied, sections by anchor
# STRUCTURE: ▶ ┌adapter path┐ → ⊕ load_adapter → ⊕ resolve spec_root → ⊕ load_spec ⚡ refusals → ⚡ schema → ◇ version → ◇ parameters → ◇ capabilities → ○ files: 〈reference | vendored ⟅sha256 fresh?, overrides, sections⟆ | not-applied〉 → ∑ rows → ⎋ Report

import datetime
import json
import logging
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

from conformlib.markdown import Parsed, load_neutral_tree, normalized_sha256, parse_markdown
from conformlib.report import Refusal, Report
from conformlib.schema import SchemaUnsupported, check_schema_keywords, escape_pointer, validate
from conformlib.selfcheck import CAPABILITIES_PATH, PARAMETERS_PATH, SEMVER, load_registries

logger = logging.getLogger("conform.adapter")

SCHEMA_PATH = "runtime/adapter.schema.json"


# region CLASS_Spec [DOMAIN(9): Adapter; CONCEPT(9): Spec, Registry, Tree; TECH(5): dataclass]
## @purpose Everything of the spec an adapter is checked against, read once: the root, the version, the declared
## capabilities and parameters with their meanings, the parsed neutral tree and the parsed schema.
@dataclass
class Spec:
    root: str
    version: str
    capabilities: Dict[str, str]
    parameters: Dict[str, str]
    tree: Dict[str, Parsed]
    schema: dict
# endregion CLASS_Spec


# region FUNC__resolve [DOMAIN(5): Adapter; CONCEPT(7): Path; TECH(4): os.path]
## @purpose Resolve a path of the adapter against the directory of the adapter file unless it is absolute (FMT-27).
## @io (str, str) -> str
## @complexity 1
def _resolve(adapter_dir: str, value: str) -> str:
    return value if os.path.isabs(value) else os.path.join(adapter_dir, value)
# endregion FUNC__resolve


# region FUNC__subject [DOMAIN(4): Adapter; CONCEPT(6): Row; TECH(4): str]
## @purpose Keep a row's subject non-empty, so a table line stays parseable when an adapter key is blank.
## @io str -> str
## @complexity 1
def _subject(text: str) -> str:
    return text if text.strip() else "(blank)"
# endregion FUNC__subject


# region FUNC__invalid_under [DOMAIN(5): Adapter; CONCEPT(7): Pointer, Skip; TECH(4): str.startswith]
## @purpose Tell whether the schema check named a fault at a pointer or below it, so a semantic check skips a part that
## already has its row.
## @io (Set[str], str) -> bool
## @complexity 2
def _invalid_under(invalid: Set[str], prefix: str) -> bool:
    return any(pointer == prefix or pointer.startswith(prefix + "/") for pointer in invalid)
# endregion FUNC__invalid_under


# region FUNC__settle [DOMAIN(6): Adapter; CONCEPT(7): PassRow; TECH(3): Report.add]
## @purpose Add one PASS row for a rule that has no FAIL row in the report, with the phrase that states its population.
## @io (Report, str, str) -> None
## @complexity 2
def _settle(report: Report, rule: str, phrase: str) -> None:
    if not report.has("FAIL", rule):
        report.add("PASS", rule, "*", phrase)
# endregion FUNC__settle


# region FUNC_load_adapter [DOMAIN(9): Adapter; CONCEPT(9): Refusal, Json; TECH(6): open, json.loads]
## @purpose Read the adapter file as a JSON object or refuse the run: a missing file, a directory, an unreadable file,
## text that is not UTF-8, text that is not JSON and JSON that is not an object each end the run as input.adapter.
## @uses open, json.loads
## @io str -> dict
## @complexity 6
def load_adapter(path: str) -> dict:
    # === LOG DRIVEN DEVELOPMENT 2.0 (LDD) ===
    # One IMP:8 line at the boundary (the count of top-level keys); a refusal logs IMP:10 with the reason class only.
    if not os.path.exists(path):
        logger.error("[IMP:10][load_adapter][READ] reason=missing")
        raise Refusal("input.adapter", path, "adapter file does not exist")
    if os.path.isdir(path):
        logger.error("[IMP:10][load_adapter][READ] reason=directory")
        raise Refusal("input.adapter", path, "adapter is a directory, not a file")
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError as error:
        logger.error("[IMP:10][load_adapter][READ] reason=%s", type(error).__name__)
        raise Refusal("input.adapter", path, "adapter file cannot be read")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        logger.error("[IMP:10][load_adapter][READ] reason=not-utf8")
        raise Refusal("input.adapter", path, "adapter is not UTF-8 text")
    try:
        data = json.loads(text)
    except (ValueError, RecursionError):
        logger.error("[IMP:10][load_adapter][READ] reason=not-json")
        raise Refusal("input.adapter", path, "adapter is not valid JSON")
    if not isinstance(data, dict):
        logger.error("[IMP:10][load_adapter][READ] reason=not-object")
        raise Refusal("input.adapter", path, "adapter is not a JSON object")
    logger.info("[IMP:8][load_adapter][READ] keys=%d", len(data))
    return data
# endregion FUNC_load_adapter


# region FUNC_resolve_spec_root [DOMAIN(8): Adapter; CONCEPT(8): Refusal, SpecRoot; TECH(4): os.path]
## @purpose Find the directory of the spec the adapter names: spec_root must be a non-empty string, resolved against the
## directory of the adapter file unless absolute, and must be a directory; otherwise the run is refused (input.spec-root).
## @uses os.path
## @io (dict, str) -> str
## @complexity 4
def resolve_spec_root(adapter: dict, adapter_dir: str) -> str:
    value = adapter.get("spec_root")
    if not isinstance(value, str) or not value.strip():
        logger.error("[IMP:10][resolve_spec_root][SPEC_ROOT] reason=absent-or-not-a-string")
        raise Refusal("input.spec-root", "spec_root", "spec_root is absent, empty or not a string")
    resolved = os.path.normpath(_resolve(adapter_dir, value))
    if not os.path.isdir(resolved):
        logger.error("[IMP:10][resolve_spec_root][SPEC_ROOT] reason=not-a-directory")
        raise Refusal("input.spec-root", "spec_root", "spec_root does not name a directory")
    logger.debug("[IMP:3][resolve_spec_root][SPEC_ROOT] resolved_is_absolute=%s", os.path.isabs(resolved))
    return resolved
# endregion FUNC_resolve_spec_root


# region FUNC__read_bytes [DOMAIN(5): Adapter; CONCEPT(6): File; TECH(4): open]
## @purpose Read a file as bytes, or None when it is missing, a directory or unreadable.
## @io str -> Optional[bytes]
## @complexity 2
def _read_bytes(path: str) -> Optional[bytes]:
    try:
        with open(path, "rb") as handle:
            return handle.read()
    except OSError:
        return None
# endregion FUNC__read_bytes


# region FUNC_load_spec [DOMAIN(9): Adapter; CONCEPT(9): Spec, Refusal, Registry, Schema; TECH(6): json, load_neutral_tree]
## @purpose Read the spec root the adapter names or refuse the run: SPEC_VERSION (one semantic version), the neutral tree
## (at least one file), both registries, and the adapter schema, which must parse and stay inside the supported keyword
## subset. A fault of the root is input.spec-root; a fault of the schema is input.schema.
## @uses load_neutral_tree, load_registries, check_schema_keywords
## @io str -> Spec
## @complexity 8
def load_spec(spec_root: str) -> Spec:
    raw = _read_bytes(os.path.join(spec_root, "SPEC_VERSION"))
    version = ""
    if raw is not None:
        try:
            text = raw.decode("utf-8").replace("\r\n", "\n")
            version = text[:-1] if text.endswith("\n") else text
        except UnicodeDecodeError:
            version = ""
    if not SEMVER.match(version):
        logger.error("[IMP:10][load_spec][READ] reason=version")
        raise Refusal("input.spec-root", "SPEC_VERSION", "missing or not one semantic version line")
    try:
        tree = load_neutral_tree(spec_root)
    except Refusal as refusal:
        raise Refusal("input.spec-root", refusal.subject, refusal.reason)
    if not tree:
        logger.error("[IMP:10][load_spec][READ] reason=no-neutral-file")
        raise Refusal("input.spec-root", "spec_root", "no neutral file under the spec root")
    for registry in (CAPABILITIES_PATH, PARAMETERS_PATH):
        if registry not in tree:
            logger.error("[IMP:10][load_spec][READ] reason=registry-missing file=%s", registry)
            raise Refusal("input.spec-root", registry, "registry file missing")
    capabilities, parameters = load_registries(tree)
    schema_bytes = _read_bytes(os.path.join(spec_root, *SCHEMA_PATH.split("/")))
    if schema_bytes is None:
        logger.error("[IMP:10][load_spec][READ] reason=schema-missing")
        raise Refusal("input.schema", SCHEMA_PATH, "schema missing or unreadable")
    try:
        schema = json.loads(schema_bytes.decode("utf-8"))
    except (UnicodeDecodeError, ValueError, RecursionError):
        logger.error("[IMP:10][load_spec][READ] reason=schema-not-json")
        raise Refusal("input.schema", SCHEMA_PATH, "schema is not valid JSON")
    try:
        check_schema_keywords(schema)
    except SchemaUnsupported as error:
        raise Refusal("input.schema", SCHEMA_PATH, str(error))
    logger.info("[IMP:8][load_spec][READ] neutral_files=%d capabilities=%d parameters=%d",
                len(tree), len(capabilities), len(parameters))
    return Spec(spec_root, version, capabilities, parameters, tree, schema)
# endregion FUNC_load_spec


# region FUNC_check_structure [DOMAIN(9): Adapter; CONCEPT(9): Schema, Violation, Rule; TECH(6): validate]
## @purpose Validate the adapter by the schema and add one FAIL row per violation under the rule the schema names for its
## subtree (the subject is the JSON pointer, or * for the whole adapter). Give the set of invalid pointers, so the semantic
## checks skip what already has a row. A schema that cannot be followed to the end refuses the run (input.schema).
## @uses validate
## @io (dict, dict, Report) -> Set[str]
## @complexity 5
def check_structure(adapter: dict, schema: dict, report: Report) -> Set[str]:
    try:
        violations = validate(adapter, schema)
    except SchemaUnsupported as error:
        raise Refusal("input.schema", SCHEMA_PATH, str(error))
    for violation in violations:
        report.add("FAIL", violation.rule, _subject(violation.pointer or "*"),
                   "%s: %s" % (violation.keyword, violation.message))
    logger.info("[IMP:7][check_structure][VALIDATE] violations=%d", len(violations))
    _settle(report, "adapter.schema", "top-level keys and identity fields are valid against the schema")
    return {violation.pointer for violation in violations}
# endregion FUNC_check_structure


# region FUNC_record_population [DOMAIN(6): Adapter; CONCEPT(7): Population; TECH(4): Report.populate]
## @purpose Record what the run looked at, in the fixed order of the summary line: the spec's files, anchors, norms,
## capabilities, parameters and version, then the adapter's files, parameters and capabilities.
## @io (dict, Spec, Report) -> None
## @complexity 3
def record_population(adapter: dict, spec: Spec, report: Report) -> None:
    def size(key: str) -> int:
        value = adapter.get(key)
        return len(value) if isinstance(value, dict) else 0
    report.populate("neutral-files", len(spec.tree))
    report.populate("anchors", sum(len(parsed.anchors) for parsed in spec.tree.values()))
    report.populate("norms", sum(len(parsed.norms) for parsed in spec.tree.values()))
    report.populate("capabilities", len(spec.capabilities))
    report.populate("parameters", len(spec.parameters))
    report.populate("spec-version", spec.version)
    report.populate("adapter-files", size("files"))
    report.populate("adapter-parameters", size("parameters"))
    report.populate("adapter-capabilities", size("capabilities"))
# endregion FUNC_record_population


# region FUNC_check_spec_version [DOMAIN(8): Adapter; CONCEPT(8): Version, Drift; TECH(5): tuple compare]
## @purpose Compare the version the adapter targets with SPEC_VERSION: equal is a PASS, older a WARN, newer a FAIL. A
## missing or malformed version already has its schema row and is skipped.
## @uses SEMVER
## @io (dict, Spec, Set[str], Report) -> int
## @complexity 4
def check_spec_version(adapter: dict, spec: Spec, invalid: Set[str], report: Report) -> int:
    value = adapter.get("spec_version")
    if not isinstance(value, str) or "/spec_version" in invalid or not SEMVER.match(value):
        logger.info("[IMP:5][check_spec_version][RESULT] compared=False fails=0")
        return 0
    report.probe("spec-version")
    have = tuple(int(part) for part in value.split("."))
    want = tuple(int(part) for part in spec.version.split("."))
    fails = 0
    if have == want:
        report.add("PASS", "adapter.spec-version", "*", "adapter targets %s, equal to the spec" % value)
    elif have < want:
        report.add("WARN", "adapter.spec-version", "spec_version", "adapter targets %s, the spec is %s" % (value, spec.version))
    else:
        report.add("FAIL", "adapter.spec-version", "spec_version", "adapter targets %s, newer than the spec %s" % (value, spec.version))
        fails = 1
    logger.info("[IMP:5][check_spec_version][RESULT] compared=True fails=%d", fails)
    return fails
# endregion FUNC_check_spec_version


# region FUNC_check_parameters [DOMAIN(8): Adapter; CONCEPT(9): Parameter, Registry; TECH(4): set compare]
## @purpose Prove that the adapter names exactly the declared parameters: one FAIL for each declared name it lacks and for
## each name it adds that no registry declares. An empty value already has its schema row.
## @uses Spec.parameters
## @io (dict, Spec, Set[str], Report) -> int
## @complexity 4
def check_parameters(adapter: dict, spec: Spec, invalid: Set[str], report: Report) -> int:
    values = adapter.get("parameters")
    if not isinstance(values, dict):
        return 0
    report.probe("parameter")
    fails_before = report.counts()["fail"]
    for name in sorted(spec.parameters):
        if name not in values:
            report.add("FAIL", "adapter.parameter", _subject(name), "declared, no value")
    for name in sorted(values):
        if name not in spec.parameters:
            report.add("FAIL", "adapter.parameter", _subject(name), "not declared in runtime/parameters.md")
    _settle(report, "adapter.parameter", "%d declared parameters have a value" % len(spec.parameters))
    fails = report.counts()["fail"] - fails_before
    logger.info("[IMP:5][check_parameters][RESULT] declared=%d given=%d fails=%d", len(spec.parameters), len(values), fails)
    return fails
# endregion FUNC_check_parameters


# region FUNC_check_capabilities [DOMAIN(8): Adapter; CONCEPT(9): Capability, Registry; TECH(4): set compare]
## @purpose Prove that the adapter meets exactly the declared capabilities: one FAIL for each declared name it lacks and
## for each name it adds that no registry declares. An entry with neither mechanism nor fallback already has its schema
## row; the PASS row counts the entries with a mechanism and those with a fallback only.
## @uses Spec.capabilities
## @io (dict, Spec, Set[str], Report) -> int
## @complexity 5
def check_capabilities(adapter: dict, spec: Spec, invalid: Set[str], report: Report) -> int:
    values = adapter.get("capabilities")
    if not isinstance(values, dict):
        return 0
    report.probe("capability")
    fails_before = report.counts()["fail"]
    for name in sorted(spec.capabilities):
        if name not in values:
            report.add("FAIL", "adapter.capability", _subject(name), "declared, not met")
    for name in sorted(values):
        if name not in spec.capabilities:
            report.add("FAIL", "adapter.capability", _subject(name), "not declared in runtime/capabilities.md")
    with_mechanism = 0
    fallback_only = 0
    for name, entry in values.items():
        if not isinstance(entry, dict):
            continue
        mechanism = entry.get("mechanism")
        if isinstance(mechanism, str) and mechanism:
            with_mechanism += 1
        elif isinstance(entry.get("fallback"), str) and entry.get("fallback"):
            fallback_only += 1
    _settle(report, "adapter.capability",
            "%d declared capabilities met (%d with a mechanism, %d with a fallback only)"
            % (len(spec.capabilities), with_mechanism, fallback_only))
    fails = report.counts()["fail"] - fails_before
    logger.info("[IMP:5][check_capabilities][RESULT] declared=%d given=%d fails=%d", len(spec.capabilities), len(values), fails)
    return fails
# endregion FUNC_check_capabilities


# region FUNC_check_reference [DOMAIN(8): Adapter; CONCEPT(9): Reference, Via; TECH(5): open, substring]
## @purpose Prove that the harness file a reference entry names in via exists and names the neutral file: its card id or
## its path must occur in the file's text. Without via the entry is a plain reference and passes.
## @uses _resolve, _read_bytes
## @io (dict, str, Parsed, str, Report) -> int
## @complexity 5
def check_reference(entry: dict, rel: str, parsed: Parsed, adapter_dir: str, report: Report) -> int:
    via = entry.get("via")
    if via is None:
        report.add("PASS", "adapter.reference", rel, "mode=reference")
        return 0
    raw = _read_bytes(_resolve(adapter_dir, via))
    text = None
    if raw is not None:
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = None
    if text is None:
        report.add("FAIL", "adapter.reference", rel, "via file missing, unreadable or not UTF-8: %s" % via)
        logger.info("[IMP:6][check_reference][RESULT] via_readable=False")
        return 1
    identifier = parsed.card.get("id") if parsed.card is not None else None
    if (identifier and identifier in text) or rel in text:
        report.add("PASS", "adapter.reference", rel, "mode=reference via=%s" % via)
        logger.info("[IMP:6][check_reference][RESULT] via_readable=True names=True")
        return 0
    report.add("FAIL", "adapter.reference", rel, "via file names neither %s nor %s" % (identifier or "an id", rel))
    logger.info("[IMP:6][check_reference][RESULT] via_readable=True names=False")
    return 1
# endregion FUNC_check_reference


# region FUNC_check_overrides [DOMAIN(8): Adapter; CONCEPT(9): Override, Until, Trigger; TECH(5): datetime.date]
## @purpose Vet the overrides of one vendored entry in order: the anchor exists in the neutral file and is overridden once,
## an until is a calendar date that has not passed, and an override with only a trigger gets an INFO row (the trigger is
## checked for presence only). Give the anchors the entry may differ in.
## @uses datetime.date, Parsed.anchors
## @io (list, str, Parsed, Report, Optional[date]) -> Set[str]
## @complexity 7
def check_overrides(overrides: list, rel: str, parsed: Parsed, report: Report,
                    today: Optional[datetime.date] = None) -> Set[str]:
    # === LOG DRIVEN DEVELOPMENT 2.0 (LDD) ===
    # One IMP:6 line at the end: how many overrides were vetted and how many faults (counts only).
    today = today or datetime.date.today()
    known = {anchor for anchor, _line in parsed.anchors}
    overridden = set()  # type: Set[str]
    fails = 0
    for override in overrides:
        anchor = override.get("anchor", "")
        subject = _subject("%s#%s" % (rel, anchor))
        if anchor not in known:
            report.add("FAIL", "adapter.override", subject, "anchor not in the neutral file")
            fails += 1
        else:
            if anchor in overridden:
                report.add("FAIL", "adapter.override", subject, "anchor overridden twice")
                fails += 1
            overridden.add(anchor)
        until = override.get("until")
        if until is not None:
            try:
                due = datetime.date.fromisoformat(until)
            except (ValueError, TypeError):
                report.add("FAIL", "adapter.override", subject, "until is not a calendar date")
                fails += 1
            else:
                if due < today:
                    report.add("FAIL", "adapter.override", subject, "until %s has passed" % due.isoformat())
                    fails += 1
        elif override.get("trigger"):
            report.add("INFO", "adapter.override", subject, "trigger checked for presence only")
    logger.info("[IMP:6][check_overrides][RESULT] vetted=%d fails=%d", len(overrides), fails)
    return overridden
# endregion FUNC_check_overrides


# region FUNC_compare_sections [DOMAIN(8): Adapter; CONCEPT(9): Section, Drift, Anchor; TECH(5): dict compare]
## @purpose Compare a neutral file and its copy by anchor: for each neutral anchor not overridden, absent from the copy or
## unequal in text is a difference; each anchor of the copy that the neutral file lacks, and each anchor the copy repeats,
## is a difference too. The text before the first anchor is not compared. Give the differences as (anchor, phrase).
## @uses Parsed.anchors, Parsed.sections
## @io (Parsed, Parsed, Set[str]) -> List[Tuple[str, str]]
## @complexity 6
def compare_sections(neutral: Parsed, copy: Parsed, overridden: Set[str]) -> List[Tuple[str, str]]:
    differences = []  # type: List[Tuple[str, str]]
    neutral_ids = []  # type: List[str]
    for anchor, _line in neutral.anchors:
        if anchor not in neutral_ids:
            neutral_ids.append(anchor)
    for anchor in neutral_ids:
        if anchor in overridden:
            continue
        if anchor not in copy.sections:
            differences.append((anchor, "missing in the copy"))
        elif copy.sections[anchor] != neutral.sections.get(anchor):
            differences.append((anchor, "differs from the neutral section"))
    seen = set()  # type: Set[str]
    for anchor, _line in copy.anchors:
        if anchor in seen:
            if (anchor, "repeated in the copy") not in differences:
                differences.append((anchor, "repeated in the copy"))
            continue
        seen.add(anchor)
        if anchor not in neutral_ids:
            differences.append((anchor, "not in the neutral file"))
    return differences
# endregion FUNC_compare_sections


# region FUNC_check_vendored [DOMAIN(10): Adapter; CONCEPT(10): Vendored, Hash, Stale, Drift; TECH(7): sha256, parse_markdown]
## @purpose Judge one vendored entry: the copy must exist; the overrides are vetted; each section of the copy that no
## override names must equal the neutral section (a difference is a FAIL when the recorded hash is fresh and a WARN when the
## neutral file has moved on); a stale hash is a WARN. A clean fresh entry earns one PASS row.
## @uses normalized_sha256, check_overrides, compare_sections, parse_markdown
## @io (dict, str, Parsed, str, Report, Optional[date]) -> int
## @complexity 9
def check_vendored(entry: dict, rel: str, parsed: Parsed, adapter_dir: str, report: Report,
                   today: Optional[datetime.date] = None) -> int:
    # === LOG DRIVEN DEVELOPMENT 2.0 (LDD) ===
    # IMP:9 DRIFT names the neutral path, whether the hash is fresh and how many differences; never a copy's text.
    fails_before = report.counts()["fail"]
    current = normalized_sha256(parsed.text.encode("utf-8"))
    fresh = entry["sha256"] == current
    raw = _read_bytes(_resolve(adapter_dir, entry["path"]))
    copy_text = None
    if raw is not None:
        try:
            copy_text = raw.decode("utf-8")
        except UnicodeDecodeError:
            copy_text = None
    if copy_text is None:
        report.add("FAIL", "adapter.vendored", rel, "copy missing, unreadable or not UTF-8: %s" % entry["path"])
        logger.info("[IMP:9][check_vendored][DRIFT] path=%s fresh=%s differences=0", rel, fresh)
        return 1
    overrides = entry.get("overrides", [])
    overridden = check_overrides(overrides, rel, parsed, report, today)
    copy = parse_markdown(rel, copy_text)
    differences = compare_sections(parsed, copy, overridden)
    status = "FAIL" if fresh else "WARN"
    for anchor, phrase in differences:
        report.add(status, "adapter.vendored", _subject("%s#%s" % (rel, anchor)), phrase)
    if not fresh:
        report.add("WARN", "adapter.vendored", rel, "mode=vendored stale: recorded %s current %s"
                   % (entry["sha256"][:12], current[:12]))
    logger.info("[IMP:9][check_vendored][DRIFT] path=%s fresh=%s differences=%d", rel, fresh, len(differences))
    fails = report.counts()["fail"] - fails_before
    if fresh and not differences and fails == 0:
        report.add("PASS", "adapter.vendored", rel, "mode=vendored sections=%d overrides=%d"
                   % (len(set(anchor for anchor, _line in parsed.anchors)), len(overrides)))
    return fails
# endregion FUNC_check_vendored


# region FUNC_check_files [DOMAIN(10): Adapter; CONCEPT(10): FileCoverage, Entry, Mode; TECH(6): sorted paths, dispatch]
## @purpose Prove that the adapter accounts for every neutral file and only for them, then judge each valid entry in path
## order by its mode: reference, vendored (with its overrides) or not-applied. An entry that already has a schema row is
## skipped. Record which entry probes ran, in the canonical order of the summary line.
## @uses check_reference, check_vendored
## @io (dict, str, Spec, Set[str], Report) -> int
## @complexity 9
def check_files(adapter: dict, adapter_dir: str, spec: Spec, invalid: Set[str], report: Report,
                today: Optional[datetime.date] = None) -> int:
    # === LOG DRIVEN DEVELOPMENT 2.0 (LDD) ===
    # IMP:5 at the end: entries judged per mode, faults. Per-entry detail is in the rows and in the DRIFT line.
    files = adapter.get("files")
    if not isinstance(files, dict):
        return 0
    report.probe("file-coverage")
    fails_before = report.counts()["fail"]
    for rel in sorted(spec.tree):
        if rel not in files:
            report.add("FAIL", "adapter.file-coverage", _subject(rel), "not accounted for")
    for key in sorted(files):
        if key not in spec.tree:
            report.add("FAIL", "adapter.file-coverage", _subject(key), "not a neutral file of the spec")
    _settle(report, "adapter.file-coverage", "%d neutral files accounted for" % len(spec.tree))
    ran = set()  # type: Set[str]
    judged = {"reference": 0, "vendored": 0, "not-applied": 0}
    for rel in sorted(files):
        entry = files[rel]
        if rel not in spec.tree or _invalid_under(invalid, "/files/" + escape_pointer(rel)):
            continue
        mode = entry.get("mode")
        parsed = spec.tree[rel]
        if mode == "reference":
            ran.add("reference")
            check_reference(entry, rel, parsed, adapter_dir, report)
        elif mode == "vendored":
            ran.add("vendored")
            if entry.get("overrides"):
                ran.add("override")
            check_vendored(entry, rel, parsed, adapter_dir, report, today)
        elif mode == "not-applied":
            ran.add("not-applied")
            report.add("PASS", "adapter.not-applied", rel, "mode=not-applied")
        else:
            continue
        judged[mode] += 1
    for name in ("reference", "vendored", "override", "not-applied"):
        if name in ran:
            report.probe(name)
    fails = report.counts()["fail"] - fails_before
    logger.info("[IMP:5][check_files][RESULT] reference=%d vendored=%d not_applied=%d fails=%d",
                judged["reference"], judged["vendored"], judged["not-applied"], fails)
    return fails
# endregion FUNC_check_files
