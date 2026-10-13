# region MODULE_CONTRACT [DOMAIN(9): Format, SelfCheck; CONCEPT(9): Card, Anchor, Norm, Registry, Call, Version; TECH(7): re, os]
## @modulecontract
## @purpose To let a maintainer or an agent know, in one run, that the repository still obeys its own format: every
## neutral file has a valid card, anchors and norms are well formed and unique, the two registries are well formed, every
## call resolves to a declaration, and the version has its changelog entry. A repository that breaks its own format cannot
## be the reference a harness adopts.
## @scope The format probes of the self mode: card, anchor, norm, registry, call, version. The publication scan lives in scan.
## @input The repository root, the parsed neutral tree, a Report to write rows into.
## @output FAIL rows per finding and one PASS row per rule that found nothing, with the population it covered; the
## populations of the run.
## @links [USES_API(8): conformlib.markdown, conformlib.report; READS_DATA_FROM(8): SPEC_VERSION, CHANGELOG.md]
## @links_to_spec BR-1, BR-2, BR-3, BR-5, BR-6, BR-11, AC-1, AC-2, AC-3, AC-6, AC-12
## @invariants
## - Every rule of a probe ends the probe with a FAIL row or a PASS row; none is silently absent (except version.changelog
##   when the version itself is unreadable, which is an INFO row).
## - A row names a path, a line, a key or an id; it never quotes a file's text.
## - The functions add rows; they neither print nor exit.
## @rationale
## Q: Why does the tree carry the issues instead of the checks re-reading the files?
## A: The reader is the one place that knows what a fence, a code span and an anchor line are; the checks turn its
## issues into rows and add the cross-file rules (uniqueness, resolution) that a single-file reader cannot know.
## Q: Why a PASS row per rule?
## A: A run that shows only failures cannot prove a rule ran; a PASS row with its population does.
## @changes
## LAST_CHANGE: [v0.1.0 - Initial creation of the format probes.]
## @modulemap
## FUNC 5[Add one FAIL row and remember its rule] => _fail
## FUNC 6[One PASS row per rule of a probe that raised no FAIL] => _settle
## FUNC 7[Turn the reader's issues for the named rules into FAIL rows] => _emit_issues
## FUNC 9[Card rules over the tree] => check_cards
## FUNC 8[Anchor syntax and uniqueness] => check_anchors
## FUNC 8[Norm id, level, anchoring, uniqueness] => check_norms
## FUNC 8[Name to meaning maps of the two registries] => load_registries
## FUNC 8[Registry presence, syntax, meaning, uniqueness] => check_registries
## FUNC 8[Call syntax and resolution] => check_calls
## FUNC 7[SPEC_VERSION and its changelog entry] => check_version
## FUNC 10[All probes in order, populations] => run_format_checks
## @usecases
## - [run_format_checks]: Maintainer -> conform self -> know the repository obeys its format
## - [load_registries]: Adapter mode -> read the declared names -> check an adapter against them
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: self check, format probes, card keys, id, status, anchor unique, norm unique, registry, call resolves, SPEC_VERSION, CHANGELOG, PASS rows, populations
# STRUCTURE: ▶ ┌root,tree,report┐ → ○ probe: card → anchor → norm → registry → call → version → ◇ finding ? FAIL row : ⊕ PASS row with population → ∑ populations → ⎋ fails per probe

import logging
import os
import re
from typing import Dict, Iterable, List, Set, Tuple

from conformlib.markdown import ID_RE, Parsed
from conformlib.report import Report

logger = logging.getLogger("conform.selfcheck")

CARD_RULES = ("card.present", "card.flat", "card.keys", "card.id", "card.status")
ANCHOR_RULES = ("anchor.syntax", "anchor.unique")
NORM_RULES = ("norm.id", "norm.level", "norm.unique", "norm.anchored")
REGISTRY_RULES = ("registry.present", "registry.syntax", "registry.meaning", "registry.unique")
CALL_RULES = ("call.syntax", "call.resolves")
VERSION_RULES = ("version.semver", "version.changelog")
MANDATORY_KEYS = ("id", "title", "status")
OPTIONAL_KEYS = ("skill-name", "skill-when")
STATUS_VALUES = ("stub", "draft", "stable")
CAPABILITIES_PATH = "runtime/capabilities.md"
PARAMETERS_PATH = "runtime/parameters.md"
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


# region FUNC__fail [DOMAIN(5): SelfCheck; CONCEPT(6): Finding; TECH(3): Report.add]
## @purpose Add one FAIL row and remember its rule, so the probe knows which rules earn a PASS row.
## @uses Report.add
## @io (Report, Set, str, str, str) -> None
## @complexity 1
def _fail(report: Report, failed: Set[str], rule: str, subject: str, detail: str) -> None:
    report.add("FAIL", rule, subject, detail)
    failed.add(rule)
# endregion FUNC__fail


# region FUNC__settle [DOMAIN(6): SelfCheck; CONCEPT(7): PassRow; TECH(3): Report.add]
## @purpose Give every rule of a probe that raised no FAIL one PASS row that states the population it covered.
## @uses Report.add
## @io (Report, Iterable[str], Set[str], str) -> None
## @complexity 2
def _settle(report: Report, rules: Iterable[str], failed: Set[str], phrase: str) -> None:
    for rule in rules:
        if rule not in failed:
            report.add("PASS", rule, "*", phrase)
# endregion FUNC__settle


# region FUNC__emit_issues [DOMAIN(6): SelfCheck; CONCEPT(7): ReaderIssues; TECH(3): Parsed.issues]
## @purpose Turn the issues the reader raised for the named rules into FAIL rows, in path order, each with its line.
## @uses Parsed.issues
## @io (Dict[str, Parsed], Iterable[str], Report, Set[str]) -> None
## @complexity 3
def _emit_issues(tree: Dict[str, Parsed], rules: Iterable[str], report: Report, failed: Set[str]) -> None:
    wanted = tuple(rules)
    for path in sorted(tree):
        for rule, line, message in tree[path].issues:
            if rule in wanted:
                _fail(report, failed, rule, path, "line %d %s" % (line, message))
# endregion FUNC__emit_issues


# region FUNC_check_cards [DOMAIN(9): SelfCheck; CONCEPT(9): Card; TECH(4): dict]
## @purpose Prove that every neutral file opens with a valid flat card: present, mandatory keys, no unknown or repeated
## key, skill keys together, a dotted lowercase id used once in the repository, and a status of stub, draft or stable.
## @uses conformlib.markdown.ID_RE
## @io (Dict[str, Parsed], Report) -> int
## @complexity 6
def check_cards(tree: Dict[str, Parsed], report: Report) -> int:
    failed = set()  # type: Set[str]
    fails_before = report.counts()["fail"]
    _emit_issues(tree, ("card.present", "card.flat"), report, failed)
    seen_ids = {}  # type: Dict[str, str]
    for path in sorted(tree):
        card = tree[path].card
        if card is None:
            continue
        keys = card.keys()
        distinct = []  # type: List[str]
        for key in keys:
            if key not in distinct:
                distinct.append(key)
        for key in distinct:
            if keys.count(key) > 1:
                _fail(report, failed, "card.keys", path, "key %s given more than once" % key)
            if key not in MANDATORY_KEYS and key not in OPTIONAL_KEYS:
                _fail(report, failed, "card.keys", path, "unknown key %s" % key)
        for key in MANDATORY_KEYS:
            if not card.get(key):
                _fail(report, failed, "card.keys", path, "mandatory key %s missing or empty" % key)
        has_name = "skill-name" in distinct
        has_when = "skill-when" in distinct
        if has_name != has_when:
            _fail(report, failed, "card.keys", path, "skill-name and skill-when go together")
        elif has_name and (not card.get("skill-name") or not card.get("skill-when")):
            _fail(report, failed, "card.keys", path, "skill-name and skill-when must both be non-empty")
        card_id = card.get("id")
        if card_id:
            if not ID_RE.match(card_id):
                _fail(report, failed, "card.id", path, "id is not dotted lowercase")
            elif card_id in seen_ids:
                _fail(report, failed, "card.id", path, "id already used by %s" % seen_ids[card_id])
            else:
                seen_ids[card_id] = path
        status = card.get("status")
        if status and status not in STATUS_VALUES:
            _fail(report, failed, "card.status", path, "status is not one of stub, draft, stable")
    _settle(report, CARD_RULES, failed, "%d neutral files" % len(tree))
    fails = report.counts()["fail"] - fails_before
    logger.info("[IMP:5][check_cards][RESULT] files=%d fails=%d", len(tree), fails)
    return fails
# endregion FUNC_check_cards


# region FUNC_check_anchors [DOMAIN(8): SelfCheck; CONCEPT(9): Anchor; TECH(4): dict]
## @purpose Prove that every anchor line is exactly an anchor with a valid id and that no anchor id is used twice in the
## repository, so a section can be addressed by its id alone.
## @uses Parsed.anchors
## @io (Dict[str, Parsed], Report) -> int
## @complexity 5
def check_anchors(tree: Dict[str, Parsed], report: Report) -> int:
    failed = set()  # type: Set[str]
    fails_before = report.counts()["fail"]
    _emit_issues(tree, ("anchor.syntax",), report, failed)
    first_seen = {}  # type: Dict[str, Tuple[str, int]]
    total = 0
    for path in sorted(tree):
        for anchor_id, line in tree[path].anchors:
            total += 1
            if anchor_id in first_seen:
                origin = first_seen[anchor_id]
                _fail(report, failed, "anchor.unique", path,
                      "line %d anchor id also at %s line %d" % (line, origin[0], origin[1]))
            else:
                first_seen[anchor_id] = (path, line)
    _settle(report, ANCHOR_RULES, failed, "%d anchors" % total)
    fails = report.counts()["fail"] - fails_before
    logger.info("[IMP:5][check_anchors][RESULT] anchors=%d fails=%d", total, fails)
    return fails
# endregion FUNC_check_anchors


# region FUNC_check_norms [DOMAIN(8): SelfCheck; CONCEPT(9): Norm; TECH(4): dict]
## @purpose Prove that norms are well formed: a level-shaped item carries a norm id, a norm carries one of the five
## levels and a colon, sits after the first anchor of its file, and its id is used once in the repository.
## @uses Parsed.norms
## @io (Dict[str, Parsed], Report) -> int
## @complexity 5
def check_norms(tree: Dict[str, Parsed], report: Report) -> int:
    failed = set()  # type: Set[str]
    fails_before = report.counts()["fail"]
    _emit_issues(tree, ("norm.id", "norm.level", "norm.anchored"), report, failed)
    first_seen = {}  # type: Dict[str, Tuple[str, int]]
    total = 0
    for path in sorted(tree):
        for norm_id, _level, line in tree[path].norms:
            total += 1
            if norm_id in first_seen:
                origin = first_seen[norm_id]
                _fail(report, failed, "norm.unique", path,
                      "line %d norm %s also at %s line %d" % (line, norm_id, origin[0], origin[1]))
            else:
                first_seen[norm_id] = (path, line)
    _settle(report, NORM_RULES, failed, "%d norms" % total)
    fails = report.counts()["fail"] - fails_before
    logger.info("[IMP:5][check_norms][RESULT] norms=%d fails=%d", total, fails)
    return fails
# endregion FUNC_check_norms


# region FUNC_load_registries [DOMAIN(8): Registry; CONCEPT(9): Capability, Parameter; TECH(4): dict]
## @purpose Give the declared capability names and parameter names, each with its meaning, from the parsed registry
## files, so a call or an adapter is checked against one source. A missing registry file gives an empty map.
## @uses Parsed.declarations
## @io Dict[str, Parsed] -> (Dict[str, str], Dict[str, str])
## @complexity 3
def load_registries(tree: Dict[str, Parsed]) -> Tuple[Dict[str, str], Dict[str, str]]:
    capabilities = {}  # type: Dict[str, str]
    parameters = {}  # type: Dict[str, str]
    for path, target in ((CAPABILITIES_PATH, capabilities), (PARAMETERS_PATH, parameters)):
        parsed = tree.get(path)
        if parsed is None:
            continue
        for _kind, name, meaning, _line in parsed.declarations:
            target.setdefault(name, meaning)
    logger.debug("[IMP:3][load_registries][READ] capabilities=%d parameters=%d", len(capabilities), len(parameters))
    return capabilities, parameters
# endregion FUNC_load_registries


# region FUNC_check_registries [DOMAIN(8): SelfCheck; CONCEPT(9): Registry; TECH(4): dict]
## @purpose Prove that both registry files exist, that every declaration has a valid name with its own registry's prefix
## and a meaning, and that no name is declared twice in a file.
## @uses Parsed.declarations, Parsed.issues
## @io (Dict[str, Parsed], Report) -> int
## @complexity 6
def check_registries(tree: Dict[str, Parsed], report: Report) -> int:
    failed = set()  # type: Set[str]
    fails_before = report.counts()["fail"]
    for path in (CAPABILITIES_PATH, PARAMETERS_PATH):
        if path not in tree:
            _fail(report, failed, "registry.present", path, "registry file missing")
    _emit_issues(tree, ("registry.syntax", "registry.meaning"), report, failed)
    for path in (CAPABILITIES_PATH, PARAMETERS_PATH):
        parsed = tree.get(path)
        if parsed is None:
            continue
        first_line = {}  # type: Dict[str, int]
        for _kind, name, _meaning, line in parsed.declarations:
            if name in first_line:
                _fail(report, failed, "registry.unique", path,
                      "line %d name %s already declared at line %d" % (line, name, first_line[name]))
            else:
                first_line[name] = line
    capabilities, parameters = load_registries(tree)
    _settle(report, REGISTRY_RULES, failed,
            "%d capabilities and %d parameters declared" % (len(capabilities), len(parameters)))
    fails = report.counts()["fail"] - fails_before
    logger.info("[IMP:5][check_registries][RESULT] capabilities=%d parameters=%d fails=%d",
                len(capabilities), len(parameters), fails)
    return fails
# endregion FUNC_check_registries


# region FUNC_check_calls [DOMAIN(8): SelfCheck; CONCEPT(9): AdaptationPoint, Call; TECH(4): dict]
## @purpose Prove that every live call in the neutral text is well formed and names a declared capability or parameter,
## so no neutral text depends on an adaptation point that no adapter can meet.
## @uses Parsed.calls, Parsed.issues
## @io (Dict[str, Parsed], Dict[str, str], Dict[str, str], Report) -> int
## @complexity 5
def check_calls(tree: Dict[str, Parsed], capabilities: Dict[str, str], parameters: Dict[str, str],
                report: Report) -> int:
    failed = set()  # type: Set[str]
    fails_before = report.counts()["fail"]
    _emit_issues(tree, ("call.syntax",), report, failed)
    total = 0
    for path in sorted(tree):
        for kind, name, line in tree[path].calls:
            total += 1
            declared = capabilities if kind == "cap" else parameters
            if name not in declared:
                _fail(report, failed, "call.resolves", path,
                      "line %d call to undeclared %s:%s" % (line, kind, name))
    _settle(report, CALL_RULES, failed, "%d calls" % total)
    fails = report.counts()["fail"] - fails_before
    logger.info("[IMP:5][check_calls][RESULT] calls=%d fails=%d", total, fails)
    return fails
# endregion FUNC_check_calls


# region FUNC_check_version [DOMAIN(7): SelfCheck; CONCEPT(8): Version, Changelog; TECH(4): re, open]
## @purpose Prove that SPEC_VERSION holds exactly one semantic version and that CHANGELOG.md has an entry for it, so a
## harness's adapter can name the version it targets and find what changed.
## @uses re, open
## @io (str, Report) -> int
## @complexity 5
def check_version(root: str, report: Report) -> int:
    failed = set()  # type: Set[str]
    fails_before = report.counts()["fail"]
    version = ""
    try:
        with open(os.path.join(root, "SPEC_VERSION"), "rb") as handle:
            raw = handle.read().decode("utf-8")
        raw = raw.replace("\r\n", "\n")
        if raw.endswith("\n"):
            raw = raw[:-1]
        if SEMVER.match(raw):
            version = raw
        else:
            _fail(report, failed, "version.semver", "SPEC_VERSION", "not one semantic version line")
    except (OSError, UnicodeDecodeError) as error:
        logger.error("[IMP:10][check_version][READ] file=SPEC_VERSION error=%s", type(error).__name__)
        _fail(report, failed, "version.semver", "SPEC_VERSION", "missing or unreadable")
    if version:
        _settle(report, ("version.semver",), failed, "SPEC_VERSION is %s" % version)
        entry = re.compile(r"^## \[?%s\]?(\s|$)" % re.escape(version), re.MULTILINE)
        try:
            with open(os.path.join(root, "CHANGELOG.md"), "rb") as handle:
                changelog = handle.read().decode("utf-8").replace("\r\n", "\n")
            if not entry.search(changelog):
                _fail(report, failed, "version.changelog", "CHANGELOG.md", "no entry for version %s" % version)
        except (OSError, UnicodeDecodeError) as error:
            logger.error("[IMP:10][check_version][READ] file=CHANGELOG.md error=%s", type(error).__name__)
            _fail(report, failed, "version.changelog", "CHANGELOG.md", "missing or unreadable")
        _settle(report, ("version.changelog",), failed, "CHANGELOG.md has an entry for %s" % version)
    else:
        report.add("INFO", "version.changelog", "*", "not checked: SPEC_VERSION holds no valid version")
    fails = report.counts()["fail"] - fails_before
    logger.info("[IMP:5][check_version][RESULT] version_found=%s fails=%d", bool(version), fails)
    return fails
# endregion FUNC_check_version


# region FUNC_run_format_checks [DOMAIN(10): SelfCheck; CONCEPT(10): Probes, Population; TECH(5): Report]
## @purpose Run the six format probes in their fixed order, record each as a probe of the run, and record the populations
## the PASS rows speak about, so the summary line states what the run covered.
## @uses check_cards, check_anchors, check_norms, check_registries, check_calls, check_version, load_registries
## @io (str, Dict[str, Parsed], Report) -> None
## @complexity 6
def run_format_checks(root: str, tree: Dict[str, Parsed], report: Report) -> None:
    capabilities, parameters = load_registries(tree)
    steps = (
        ("card", check_cards(tree, report)),
        ("anchor", check_anchors(tree, report)),
        ("norm", check_norms(tree, report)),
        ("registry", check_registries(tree, report)),
        ("call", check_calls(tree, capabilities, parameters, report)),
        ("version", check_version(root, report)),
    )
    for name, fails in steps:
        report.probe(name)
        logger.info("[IMP:6][run_format_checks][PROBE] probe=%s fails=%d", name, fails)
    report.populate("neutral-files", len(tree))
    report.populate("anchors", sum(len(parsed.anchors) for parsed in tree.values()))
    report.populate("norms", sum(len(parsed.norms) for parsed in tree.values()))
    report.populate("calls", sum(len(parsed.calls) for parsed in tree.values()))
    report.populate("capabilities", len(capabilities))
    report.populate("parameters", len(parameters))
# endregion FUNC_run_format_checks
