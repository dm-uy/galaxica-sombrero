# region MODULE_CONTRACT [DOMAIN(10): SelfMode, Drills; CONCEPT(9): Mutation, Refusal, FailureClass; TECH(6): pytest, json, monkeypatch]
## @modulecontract
## @purpose To prove that the self mode catches every kind of damage it claims to catch and refuses every input it cannot
## judge: a clean copy passes, each of the 24 format mutations of a copy raises exactly its rule with exit 1, each of the ten
## bad inputs and faults ends in one NOT RUN row with exit 2, and every failure class of the rules table has a drill.
## @scope The format rules and the refusals of the self mode; the publication scan has its own module.
## @input A copy of the repository, a synthetic deny list, the in-process runner.
## @output One pass or fail per drill; the trajectory lines printed before each assert.
## @links [USES_API(9): conform.main through run_cli; USES_API(6): conformlib for the two fault injections]
## @links_to_spec AC-6, AC-P4
## @invariants
## - Every drill mutates a copy under the temporary directory; the repository is never written.
## - A drill asserts both the rule and the status of the row, and the exit code.
## - The calls a drill plants are built from fragments, so this file holds no live call.
## @rationale
## Q: Why assert a row and not only the exit code?
## A: A drill that fails for the wrong reason (a broken copy) would still exit 1; the rule and the subject prove the right
## check caught the right damage.
## Q: Why two fault injections through monkeypatch?
## A: A crash inside a check and a scanner whose pattern does not bite cannot be planted in a file; they are planted in the
## code, in the same process the runner calls.
## @changes
## LAST_CHANGE: [v0.20.0 - Reconcile promoted glossary card/status inputs and owner-approved norm-outside placement; preserve all24 drill identities, refusals, helpers and assertions; runtime checks NOT_RUN.]
## @modulemap
## FUNC 5[Replace one exact piece of a file of a copy, failing when it is absent] => _replace
## FUNC 4[Append lines to a file of a copy] => _append
## FUNC 3[Delete a file of a copy] => _delete_file
## FUNC 5[Build a call text from fragments] => _call_text
## FUNC 4[The self-run argument list over a copy, JSON form] => _self_argv
## FUNC 7[A clean copy passes with 24 PASS rows] => test_control_copy_passes
## FUNC 9[Each format mutation raises its rule] => test_self_drill
## FUNC 7[The argument list of one refusal case, with the files it plants] => _refusal_argv
## FUNC 9[Each bad input or fault is one NOT RUN row] => test_self_refusal
## FUNC 6[The drill-rule constant equals the tables] => test_drill_rules_constant_matches_the_tables
## FUNC 6[Read a module's drill-rule literal] => _declared_drill_rules
## FUNC 9[Every failure class of the table has a drill] => test_every_failure_class_has_a_drill
## @usecases
## - [test_self_drill]: QA agent -> damages one rule's subject in a copy -> the tool names the rule and exits 1
## - [test_self_refusal]: QA agent -> runs the tool without a deny list -> NOT RUN input.deny-list and exit 2
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: self drills, mutation of a repo copy, 24 mutations, refusals, input.usage, input.root, input.deny-list, scan.canary, internal.error, failure classes, control copy
# STRUCTURE: ▶ repo_copy → ◇ control: exit 0, 24 PASS → ⚡ mutate one line ∀24 → ⊕ FAIL row rule + exit 1 → ⚡ refuse ∀10 → ⊕ one NOT RUN + exit 2 → ∑ rules ⊆ DRILL_RULES → ⊕ ast.literal_eval(DRILL_RULES of 3 modules) ⊇ T.3 → ⎋ assert

import ast
import json
import pathlib
import re
from typing import Callable, List, Tuple

import pytest

import conformlib
from conformlib import selfcheck

GLOSSARY = "concepts/glossary.md"
DRILL_ANCHOR = "<!-- anchor: concepts.glossary.drill -->"
SELF_PASS_RULES = [
    "scan.canary", "card.present", "card.flat", "card.keys", "card.id", "card.status", "anchor.syntax", "anchor.unique",
    "norm.id", "norm.level", "norm.unique", "norm.anchored", "registry.present", "registry.syntax", "registry.meaning",
    "registry.unique", "call.syntax", "call.resolves", "version.semver", "version.changelog", "scan.home-path",
    "scan.home-relative", "scan.email", "scan.deny-token",
]
DRILL_RULES = (
    "anchor.syntax", "anchor.unique", "call.resolves", "call.syntax", "card.flat", "card.id", "card.keys", "card.present",
    "card.status", "input.deny-list", "input.root", "input.usage", "internal.error", "norm.anchored", "norm.id",
    "norm.level", "norm.unique", "registry.meaning", "registry.present", "registry.syntax", "registry.unique",
    "scan.canary", "version.changelog", "version.semver",
)
# The rule column of the rules table (T.3) whose status is FAIL, WARN or NOT RUN in at least one case: each needs a drill.
FAILURE_RULES = (
    "input.usage", "input.root", "input.deny-list", "input.adapter", "input.spec-root", "input.schema", "internal.error",
    "scan.canary", "card.present", "card.flat", "card.keys", "card.id", "card.status", "anchor.syntax", "anchor.unique",
    "norm.id", "norm.level", "norm.unique", "norm.anchored", "registry.present", "registry.syntax", "registry.meaning",
    "registry.unique", "call.syntax", "call.resolves", "version.semver", "version.changelog", "scan.home-path",
    "scan.home-relative", "scan.email", "scan.deny-token", "adapter.schema", "adapter.spec-version", "adapter.parameter",
    "adapter.capability", "adapter.file-coverage", "adapter.reference", "adapter.vendored", "adapter.override",
    "adapter.not-applied",
)
# The rules of the table that raise INFO only: a drill may cover them, none is owed.
INFO_ONLY_RULES = ("scan.binary",)
DRILL_MODULES = ("test_self_drills.py", "test_scan.py", "test_adapter.py")


# region FUNC__replace [DOMAIN(6): Drills; CONCEPT(7): Mutation, Replace; TECH(4): pathlib]
## @purpose Replace one exact piece of a file of a copy; a piece that is not there is a broken drill, not a pass.
## @io (pathlib.Path, str, str, str) -> None
## @complexity 2
def _replace(copy: pathlib.Path, relative: str, old: str, new: str) -> None:
    path = copy / relative
    text = path.read_text(encoding="utf-8")
    assert old in text, "drill target not found in " + relative
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
# endregion FUNC__replace


# region FUNC__append [DOMAIN(6): Drills; CONCEPT(7): Mutation, Append; TECH(4): pathlib]
## @purpose Append lines to a file of a copy, after making sure the file ends with a newline.
## @io (pathlib.Path, str, List[str]) -> None
## @complexity 2
def _append(copy: pathlib.Path, relative: str, lines: List[str]) -> None:
    path = copy / relative
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8")
# endregion FUNC__append


# region FUNC__delete_file [DOMAIN(6): Drills; CONCEPT(7): Mutation, Delete; TECH(4): pathlib]
## @purpose Delete a file of a copy.
## @io (pathlib.Path, str) -> None
## @complexity 1
def _delete_file(copy: pathlib.Path, relative: str) -> None:
    (copy / relative).unlink()
# endregion FUNC__delete_file


# region FUNC__call_text [DOMAIN(7): Drills; CONCEPT(8): Call, Fragments; TECH(3): str]
## @purpose Build a call text from fragments, so that no line of this file is a live call.
## @io str -> str
## @complexity 1
def _call_text(inner: str) -> str:
    return "{" + "{" + inner + "}" + "}"
# endregion FUNC__call_text


CARD_HEAD = "---\nid: concepts.glossary\ntitle: Glossary\nstatus: draft\n---\n"

DRILLS: List[Tuple[str, str, Callable[[pathlib.Path], None]]] = [
    ("card-missing", "card.present", lambda c: _replace(c, GLOSSARY, CARD_HEAD, "")),
    ("card-unclosed", "card.present", lambda c: _replace(c, GLOSSARY, "status: draft\n---\n", "status: draft\n")),
    ("card-flat", "card.flat", lambda c: _replace(c, GLOSSARY, "id: concepts.glossary\n", "id: concepts.glossary\n  nested: value\n")),
    ("card-key-missing", "card.keys", lambda c: _replace(c, GLOSSARY, "title: Glossary\n", "")),
    ("card-key-unknown", "card.keys", lambda c: _replace(c, GLOSSARY, "status: draft\n", "status: draft\nowner: someone\n")),
    ("card-skill-half", "card.keys", lambda c: _replace(c, GLOSSARY, "status: draft\n", "status: draft\nskill-name: glossary\n")),
    ("card-id-format", "card.id", lambda c: _replace(c, GLOSSARY, "id: concepts.glossary", "id: Concepts.Glossary")),
    ("card-id-duplicate", "card.id", lambda c: _replace(c, GLOSSARY, "id: concepts.glossary", "id: roles.qa")),
    ("card-status", "card.status", lambda c: _replace(c, GLOSSARY, "status: draft", "status: final")),
    ("anchor-syntax", "anchor.syntax", lambda c: _append(c, GLOSSARY, ["", "<!-- anchor: Bad Id -->", "text"])),
    ("anchor-duplicate", "anchor.unique", lambda c: _append(c, GLOSSARY, ["", "<!-- anchor: format.card -->", "text"])),
    ("norm-id", "norm.id", lambda c: _append(c, GLOSSARY, ["", DRILL_ANCHOR, "", "- **qa5** MUST: drill."])),
    ("norm-level", "norm.level", lambda c: _append(c, GLOSSARY, ["", DRILL_ANCHOR, "", "- **DRL-1** MUSTN'T: drill."])),
    ("norm-duplicate", "norm.unique", lambda c: _append(c, GLOSSARY, ["", DRILL_ANCHOR, "", "- **FMT-2** MUST: drill."])),
    ("norm-outside", "norm.anchored", lambda c: _replace(c, GLOSSARY, CARD_HEAD, CARD_HEAD + "\n- **DRL-2** MUST: drill.\n")),
    ("registry-missing", "registry.present", lambda c: _delete_file(c, "runtime/parameters.md")),
    ("registry-syntax", "registry.syntax", lambda c: _append(c, "runtime/capabilities.md", ["- **cap:Bad_Name** meaning."])),
    ("registry-meaning", "registry.meaning", lambda c: _append(c, "runtime/capabilities.md", ["- **cap:empty-meaning**"])),
    ("registry-duplicate", "registry.unique", lambda c: _append(c, "runtime/capabilities.md", ["- **cap:memory** again."])),
    ("call-syntax", "call.syntax", lambda c: _append(c, GLOSSARY, ["", "A bad call " + _call_text("cap:Bad Name") + " here."])),
    ("call-cap", "call.resolves", lambda c: _append(c, GLOSSARY, ["", "A call " + _call_text("cap:no-such-capability") + " here."])),
    ("call-param", "call.resolves", lambda c: _append(c, GLOSSARY, ["", "A call " + _call_text("param:no-such-parameter") + " here."])),
    ("version-semver", "version.semver", lambda c: (c / "SPEC_VERSION").write_text("0.1\n", encoding="utf-8")),
    ("version-changelog", "version.changelog", lambda c: (c / "SPEC_VERSION").write_text("0.1.1\n", encoding="utf-8")),
]

REFUSALS = [
    ("deny-flag-absent", "input.deny-list"),
    ("deny-file-missing", "input.deny-list"),
    ("deny-list-empty", "input.deny-list"),
    ("deny-list-blank", "input.deny-list"),
    ("root-missing", "input.root"),
    ("root-no-neutral-file", "input.root"),
    ("usage", "input.usage"),
    ("no-subcommand", "input.usage"),
    ("canary-broken", "scan.canary"),
    ("internal-error", "internal.error"),
]


# region FUNC__self_argv [DOMAIN(7): Drills; CONCEPT(8): Invocation; TECH(4): list]
## @purpose The argument list of a self run over a copy with a deny list, in the JSON form.
## @io (pathlib.Path, pathlib.Path) -> List[str]
## @complexity 1
def _self_argv(copy: pathlib.Path, deny: pathlib.Path) -> List[str]:
    return ["self", "--root", str(copy), "--deny-list", str(deny), "--json"]
# endregion FUNC__self_argv


# region FUNC_test_control_copy_passes [DOMAIN(9): SelfMode; CONCEPT(9): Control, Pass; TECH(6): run_cli, json]
## @purpose Prove that an unmutated copy of the repository passes: exit 0, no FAIL and no WARN, and one PASS row for each of
## the 24 rules of the self mode, so a drill that fails is failing because of its mutation.
## @uses run_cli, repo_copy, deny_list, ldd_trajectory
## @io (Callable, pathlib.Path, Tuple, Callable) -> None
## @complexity 4
def test_control_copy_passes(run_cli, repo_copy, deny_list, ldd_trajectory):
    code, out, err = run_cli(_self_argv(repo_copy, deny_list[0]))
    lines = ldd_trajectory()
    report = json.loads(out)
    passes = [row["rule"] for row in report["rows"] if row["status"] == "PASS"]
    print("[IMP:9][test_control_copy][RESULT] exit=%d counts=%s" % (code, report["summary"]["counts"]))
    assert code == 0
    assert err == ""
    assert report["summary"]["counts"]["fail"] == 0
    assert report["summary"]["counts"]["warn"] == 0
    assert passes == SELF_PASS_RULES
    assert any("[run_self][VERDICT] exit=0" in line for line in lines)
# endregion FUNC_test_control_copy_passes


# region FUNC_test_self_drill [DOMAIN(10): SelfMode; CONCEPT(10): Mutation, Rule, Exit; TECH(6): pytest.parametrize, json]
## @purpose Prove, for one mutation of a copy, that the tool exits 1, reports a FAIL row of the expected rule, and reaches its
## verdict line.
## @uses run_cli, repo_copy, deny_list, ldd_trajectory, find_rows
## @io (str, str, Callable, ...) -> None
## @complexity 5
@pytest.mark.parametrize("drill_id,rule,mutate", DRILLS, ids=[d[0] for d in DRILLS])
def test_self_drill(drill_id, rule, mutate, run_cli, repo_copy, deny_list, ldd_trajectory, find_rows):
    mutate(repo_copy)
    code, out, err = run_cli(_self_argv(repo_copy, deny_list[0]))
    lines = ldd_trajectory()
    report = json.loads(out)
    rows = find_rows(report, rule, "FAIL")
    print("[IMP:9][test_self_drill][RESULT] drill=%s rule=%s exit=%d fail_rows=%d" % (drill_id, rule, code, len(rows)))
    assert code == 1
    assert rows, "no FAIL row for " + rule
    assert not find_rows(report, rule, "PASS")
    assert err == ""
    assert any("[run_self][VERDICT] exit=1" in line for line in lines)
# endregion FUNC_test_self_drill


# region FUNC__refusal_argv [DOMAIN(8): Drills; CONCEPT(8): Refusal, Invocation; TECH(4): list]
## @purpose Build the argument list of one refusal case, planting the files the case needs under the temporary directory.
## @io (str, pathlib.Path, pathlib.Path, pathlib.Path) -> List[str]
## @complexity 4
def _refusal_argv(case: str, tmp: pathlib.Path, copy: pathlib.Path, deny: pathlib.Path) -> List[str]:
    if case == "deny-flag-absent":
        return ["self", "--root", str(copy), "--json"]
    if case == "deny-file-missing":
        return ["self", "--root", str(copy), "--deny-list", str(tmp / "no-such-deny-list.txt"), "--json"]
    if case == "deny-list-empty":
        only_comment = tmp / "comment-only.txt"
        only_comment.write_text("# nothing but a comment\n", encoding="utf-8")
        return ["self", "--root", str(copy), "--deny-list", str(only_comment), "--json"]
    if case == "deny-list-blank":
        blank = tmp / "blank.txt"
        blank.write_text("", encoding="utf-8")
        return ["self", "--root", str(copy), "--deny-list", str(blank), "--json"]
    if case == "root-missing":
        return ["self", "--root", str(tmp / "nowhere"), "--deny-list", str(deny), "--json"]
    if case == "root-no-neutral-file":
        empty = tmp / "empty-root"
        empty.mkdir()
        return ["self", "--root", str(empty), "--deny-list", str(deny), "--json"]
    if case == "usage":
        return ["self", "--bogus", "--json"]
    if case == "no-subcommand":
        return []
    return _self_argv(copy, deny)
# endregion FUNC__refusal_argv


# region FUNC_test_self_refusal [DOMAIN(10): SelfMode; CONCEPT(10): Refusal, NotRun, Exit2; TECH(6): pytest.parametrize, monkeypatch]
## @purpose Prove, for one bad input or injected fault, that the tool exits 2 with exactly one NOT RUN row of the expected
## rule, no population, no probes, and nothing on standard error.
## @uses run_cli, parse_table, monkeypatch
## @io (str, str, Callable, ...) -> None
## @complexity 6
@pytest.mark.parametrize("case,rule", REFUSALS, ids=[r[0] for r in REFUSALS])
def test_self_refusal(case, rule, run_cli, parse_table, repo_copy, deny_list, tmp_path, monkeypatch, ldd_trajectory):
    if case == "canary-broken":
        never = re.compile("(?!)")
        monkeypatch.setattr(conformlib, "build_patterns", lambda: [("scan.home-path", never), ("scan.email", never)])
    if case == "internal-error":
        def _boom(tree, report):
            raise RuntimeError("drill")
        monkeypatch.setattr(selfcheck, "check_cards", _boom)
    argv = _refusal_argv(case, tmp_path, repo_copy, deny_list[0])
    code, out, err = run_cli(argv)
    lines = ldd_trajectory()
    if "--json" in argv:
        report = json.loads(out)
        rows = report["rows"]
        summary = report["summary"]["line"]
    else:
        rows, summary = parse_table(out)
    print("[IMP:9][test_self_refusal][RESULT] case=%s rule=%s exit=%d rows=%d" % (case, rule, code, len(rows)))
    assert code == 2
    assert len(rows) == 1
    assert rows[0]["status"] == "NOT RUN" and rows[0]["rule"] == rule
    assert "population: none  probes: none" in summary
    assert "exit=2" in summary
    assert err == ""
    if case == "internal-error":
        assert rows[0]["detail"] == "RuntimeError"
    if case in ("deny-flag-absent", "deny-file-missing", "deny-list-empty", "deny-list-blank", "root-missing",
                "root-no-neutral-file", "canary-broken", "internal-error"):
        assert any("[main][EXIT] exit=2" in line for line in lines)
# endregion FUNC_test_self_refusal


# region FUNC_test_drill_rules_constant_matches_the_tables [DOMAIN(7): Drills; CONCEPT(8): FailureClass, Constant; TECH(4): set]
## @purpose Prove that the DRILL_RULES constant, which the failure-class map reads, is exactly the set of rules the drill tables
## of this module cover.
## @io None -> None
## @complexity 2
def test_drill_rules_constant_matches_the_tables():
    covered = {rule for _id, rule, _mutate in DRILLS} | {rule for _id, rule in REFUSALS}
    print("[IMP:9][test_drill_rules_constant][COUNT] drills=%d refusals=%d rules=%d" % (len(DRILLS), len(REFUSALS), len(covered)))
    assert len(DRILLS) == 24
    assert len(REFUSALS) == 10
    assert set(DRILL_RULES) == covered
    assert list(DRILL_RULES) == sorted(DRILL_RULES)
# endregion FUNC_test_drill_rules_constant_matches_the_tables


# region FUNC__declared_drill_rules [DOMAIN(7): Drills; CONCEPT(8): FailureClass, Literal; TECH(5): ast.literal_eval]
## @purpose Read the DRILL_RULES literal of a test module without importing it, so that a module that fails to import cannot
## hide its drills and no module has to import a sibling test module.
## @io pathlib.Path -> Tuple[str, ...]
## @complexity 3
def _declared_drill_rules(path: pathlib.Path) -> Tuple[str, ...]:
    assert path.exists(), "%s does not exist" % path.name
    for node in ast.parse(path.read_text(encoding="utf-8")).body:
        if isinstance(node, ast.Assign) and any(isinstance(item, ast.Name) and item.id == "DRILL_RULES" for item in node.targets):
            return tuple(ast.literal_eval(node.value))
    raise AssertionError("%s declares no DRILL_RULES literal" % path.name)
# endregion FUNC__declared_drill_rules


# region FUNC_test_every_failure_class_has_a_drill [DOMAIN(9): Drills; CONCEPT(9): FailureClass, Coverage; TECH(4): set]
## @purpose Prove AC-P4: every rule of the rules table that can end a run in FAIL, WARN or NOT RUN is the expected rule of at
## least one drill in the union of the drill modules, and no drill expects a rule the table does not have.
## @io repo_root -> None
## @complexity 4
def test_every_failure_class_has_a_drill(repo_root):
    declared = {}
    for module in DRILL_MODULES:
        declared[module] = set(_declared_drill_rules(repo_root / "tests" / module))
    union = set().union(*declared.values())
    owed = set(FAILURE_RULES)
    table = owed | set(INFO_ONLY_RULES)
    uncovered = sorted(owed - union)
    invented = sorted(union - table)
    print("[IMP:9][test_every_failure_class_has_a_drill][COVERAGE] owed=%d covered=%d uncovered=%s invented=%s" % (
        len(owed), len(owed & union), uncovered, invented))
    assert len(FAILURE_RULES) == 40 and len(set(FAILURE_RULES)) == 40
    assert uncovered == [], "rules with no drill: %s" % uncovered
    assert invented == [], "drills that expect a rule outside the table: %s" % invented
# endregion FUNC_test_every_failure_class_has_a_drill
