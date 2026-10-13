# region MODULE_CONTRACT [DOMAIN(10): AdapterMode, Drills; CONCEPT(10): Adapter, Vendored, Override, Refusal, FailureClass; TECH(6): pytest, json, monkeypatch]
## @modulecontract
## @purpose To prove that the adapter mode judges a harness against the spec it names: the example adapter of the repository
## passes with a row of every mode, a control harness copy passes with the same rows, each of the 36 damages of an adapter, a
## harness file or the spec copy raises exactly its rule with the right status and exit code, and the semantic choices of the
## format (paths, line endings, the preamble, the day an override runs out, no adapter value in the trace) hold.
## @scope The adapter mode end to end and the adapter helpers that carry a format decision; the schema validator has its own
## module and the report shape has its own.
## @input The real repository, a harness copy beside a spec copy, the in-process runner.
## @output One pass or fail per drill and per property; the trajectory lines printed before each assert.
## @links [USES_API(9): conform.main through run_cli; USES_API(7): conformlib.adapter, markdown, report; READS_DATA_FROM(9): examples/adapter.example.json]
## @links_to_spec AC-4, AC-5, AC-8, AC-P4
## @invariants
## - Every drill mutates the harness copy or the spec copy under the temporary directory; the repository is never written.
## - A drill asserts the rule, the status, the subject where the drill fixes one, the exit code and the verdict or refusal line.
## - The example adapter is judged in place; nothing is copied for it.
## - No adapter string value appears in the trace of a run.
## @rationale
## Q: Why a harness copy and a spec copy side by side?
## A: The adapter names its spec by a relative path; keeping both under one temporary directory lets a drill damage either the
## adapter, the harness files or the spec (a stale hash, a broken schema) without touching the repository.
## Q: Why drills return the adapter path?
## A: Two refusals (a missing file, a directory) need a path other than the adapter of the copy; every other drill returns
## nothing and the standard path is used.
## @changes
## LAST_CHANGE: [v1.0.0 - Reconcile only the independent neutral namespace/current facts; preserve original controls and full publication coverage; runtime checks pending.]
## @modulemap
## FUNC 6[The neutral files by the definition of the format] => _neutral_paths
## FUNC 6[Read and write the adapter JSON of a copy] => _edit_adapter
## FUNC 5[Read, change and write any JSON file] => _edit_json
## FUNC 5[Write a text file] => _write
## FUNC 4[Delete a file] => _delete
## FUNC 4[Append a line to a file] => _append_line
## FUNC 6[Change the first line of a section of a copy] => _touch_section
## FUNC 4[The vendored copy of the harness] => _vendored_copy
## FUNC 4[The argument list of an adapter run] => _adapter_argv
## FUNC 7[The example passes with a row of each mode] => test_example_exits_0_with_a_row_of_each_mode
## FUNC 8[The example accounts for every neutral file] => test_example_accounts_for_every_neutral_file
## FUNC 8[The vendored entry of the example is fresh] => test_example_vendored_entry_is_fresh
## FUNC 7[A trigger override is INFO, presence only] => test_trigger_override_is_info_presence_only
## FUNC 7[The control harness passes with the example's rows] => test_control_harness_passes
## FUNC 10[Each damage raises its rule] => test_adapter_drill
## FUNC 6[The drill-rule constant equals the table] => test_drill_rules_constant_matches_the_table
## FUNC 7[A CRLF copy is not a difference] => test_crlf_copies_are_not_a_difference
## FUNC 7[The preamble before the first anchor is not compared] => test_preamble_before_the_first_anchor_is_not_compared
## FUNC 7[The day an override runs out] => test_until_on_the_day_itself_has_not_passed
## FUNC 7[Sections are compared by anchor] => test_compare_sections_by_anchor
## FUNC 8[No adapter value in the trace] => test_adapter_string_values_absent_from_the_trace
## FUNC 7[A crash is one NOT RUN row] => test_adapter_internal_error_is_one_not_run_row
## @usecases
## - [test_adapter_drill]: QA agent -> damages one thing of a harness copy -> the tool names the rule and exits 1, 0 or 2
## - [test_example_exits_0_with_a_row_of_each_mode]: New harness author -> runs the example -> sees what a passing adapter looks like
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: adapter drills, harness copy, spec copy, vendored, stale hash, override until trigger, via reference, not-applied, file coverage, spec version, input.adapter, input.spec-root, input.schema, CRLF, preamble, trace privacy
# STRUCTURE: ▶ example → ◇ exit 0 ∧ 9 probes → ⚡ harness_copy → ◇ control rows = example rows → ⚡ mutate one thing ∀36 → ⊕ rule + status + subject + exit → ∑ rules ⊆ DRILL_RULES → ⚡ CRLF, preamble, until, anchors → ∑ trace ∌ adapter values → ⎋ assert

import datetime
import hashlib
import json
import pathlib
import re
from typing import Callable, List, Optional, Set

import pytest

import conformlib
from conformlib import adapter as adapter_module
from conformlib.markdown import parse_markdown
from conformlib.report import Report

VENDORED = "checks/conform.md"
DRILL_RULES = (
    "adapter.capability", "adapter.file-coverage", "adapter.not-applied", "adapter.override", "adapter.parameter",
    "adapter.reference", "adapter.schema", "adapter.spec-version", "adapter.vendored", "input.adapter", "input.schema",
    "input.spec-root",
)
NOT_RUN = "NOT RUN"
SCHEMA_REL = "runtime/adapter.schema.json"
ANCHOR_LINE = re.compile(r"^<!-- anchor: ([a-z][a-z0-9.-]*) -->$")
MODE_WORDS = {"reference", "vendored", "not-applied"}


# region FUNC__neutral_paths [DOMAIN(7): Skeleton; CONCEPT(8): NeutralFiles; TECH(5): pathlib.rglob]
## @purpose The neutral files by the definition of the format, found here independently of the tool: every Markdown file
## except the root README and CHANGELOG and everything under tests, examples, typed implementations and the build directories.
## @io pathlib.Path -> List[str]
## @complexity 3
def _neutral_paths(root: pathlib.Path) -> List[str]:
    skipped = {".git", "doxygen_output", "__pycache__", ".pytest_cache", "tests", "examples", "implementations"}
    found = []
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root)
        if relative.parts[0] in skipped:
            continue
        if len(relative.parts) == 1 and relative.name in {"README.md", "CHANGELOG.md"}:
            continue
        found.append(relative.as_posix())
    return found
# endregion FUNC__neutral_paths


# region FUNC__edit_json [DOMAIN(6): Drills; CONCEPT(7): Mutation, Json; TECH(4): json]
## @purpose Read a JSON file, let a function change the parsed value, and write it back in the tool's own JSON style.
## @io (pathlib.Path, Callable) -> None
## @complexity 2
def _edit_json(path: pathlib.Path, change: Callable) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    change(data)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
# endregion FUNC__edit_json


# region FUNC__edit_adapter [DOMAIN(7): Drills; CONCEPT(8): Mutation, Adapter; TECH(4): json]
## @purpose Change the adapter file of a harness copy through a function of the parsed adapter.
## @io (HarnessCopy, Callable) -> None
## @complexity 1
def _edit_adapter(copy, change: Callable) -> None:
    _edit_json(copy.adapter, change)
# endregion FUNC__edit_adapter


# region FUNC__write [DOMAIN(5): Drills; CONCEPT(6): Mutation, Write; TECH(4): pathlib]
## @purpose Replace a file of a copy with the given text.
## @io (pathlib.Path, str) -> None
## @complexity 1
def _write(path: pathlib.Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
# endregion FUNC__write


# region FUNC__delete [DOMAIN(5): Drills; CONCEPT(6): Mutation, Delete; TECH(4): pathlib]
## @purpose Delete a file of a copy; a file that is not there is a broken drill.
## @io pathlib.Path -> None
## @complexity 1
def _delete(path: pathlib.Path) -> None:
    path.unlink()
# endregion FUNC__delete


# region FUNC__touch_section [DOMAIN(7): Drills; CONCEPT(8): Mutation, Section; TECH(4): str]
## @purpose Change one line of a section: the first non-blank line after the section's anchor gets a suffix. An anchor that
## is not there is a broken drill, not a pass.
## @io (pathlib.Path, str) -> None
## @complexity 4
def _touch_section(path: pathlib.Path, anchor: str) -> None:
    lines = path.read_text(encoding="utf-8").split("\n")
    marker = "<!-- anchor: %s -->" % anchor
    assert marker in lines, "drill target not found: " + anchor
    index = lines.index(marker) + 1
    while not lines[index].strip():
        index += 1
    lines[index] = lines[index] + " (changed)"
    path.write_text("\n".join(lines), encoding="utf-8")
# endregion FUNC__touch_section


# region FUNC__vendored_copy [DOMAIN(6): Drills; CONCEPT(7): Vendored, Path; TECH(4): pathlib]
## @purpose The vendored copy of checks/conform.md inside a harness copy.
## @io HarnessCopy -> pathlib.Path
## @complexity 1
def _vendored_copy(copy) -> pathlib.Path:
    return copy.harness / "harness" / "conform.md"
# endregion FUNC__vendored_copy


# region FUNC__adapter_argv [DOMAIN(6): Drills; CONCEPT(7): Invocation; TECH(4): list]
## @purpose The argument list of an adapter run in the JSON form.
## @io pathlib.Path -> List[str]
## @complexity 1
def _adapter_argv(path: pathlib.Path) -> List[str]:
    return ["adapter", str(path), "--json"]
# endregion FUNC__adapter_argv


# region FUNC__append_line [DOMAIN(5): Drills; CONCEPT(6): Mutation, Append; TECH(4): pathlib]
## @purpose Append one line (which may hold a newline of its own) to a text file of a copy.
## @io (pathlib.Path, str) -> None
## @complexity 1
def _append_line(path: pathlib.Path, line: str) -> None:
    text = path.read_text(encoding="utf-8")
    path.write_text(text + ("" if text.endswith("\n") else "\n") + line + "\n", encoding="utf-8")
# endregion FUNC__append_line


CRED = "policies/credentials.md"
QA = "roles/qa.md"

# id, rule, status, exit, subject ("" = any), mutation of the harness copy (returns an adapter path or None)
DRILLS = [
    ("file-unaccounted", "adapter.file-coverage", "FAIL", 1, QA,
     lambda h: _edit_adapter(h, lambda d: d["files"].pop(QA))),
    ("file-unknown", "adapter.file-coverage", "FAIL", 1, "roles/nobody.md",
     lambda h: _edit_adapter(h, lambda d: d["files"].update({"roles/nobody.md": {"mode": "reference"}}))),
    ("mode-unknown", "adapter.file-coverage", "FAIL", 1, "/files/roles~1qa.md/mode",
     lambda h: _edit_adapter(h, lambda d: d["files"].update({QA: {"mode": "copied"}}))),
    ("vendored-edited", "adapter.vendored", "FAIL", 1, VENDORED + "#checks.conform.exit",
     lambda h: _touch_section(_vendored_copy(h), "checks.conform.exit")),
    ("vendored-copy-missing", "adapter.vendored", "FAIL", 1, VENDORED,
     lambda h: _delete(_vendored_copy(h))),
    ("vendored-extra-anchor", "adapter.vendored", "FAIL", 1, VENDORED + "#checks.conform.extra",
     lambda h: _append_line(_vendored_copy(h), "<!-- anchor: checks.conform.extra -->\nan extra section")),
    ("vendored-bad-sha", "adapter.vendored", "FAIL", 1, "/files/checks~1conform.md/sha256",
     lambda h: _edit_adapter(h, lambda d: d["files"][VENDORED].update({"sha256": "xyz"}))),
    ("override-missing-anchor", "adapter.override", "FAIL", 1, VENDORED + "#checks.conform.nowhere",
     lambda h: _edit_adapter(h, lambda d: d["files"][VENDORED]["overrides"][0].update({"anchor": "checks.conform.nowhere"}))),
    ("override-until-passed", "adapter.override", "FAIL", 1, VENDORED + "#checks.conform.run",
     lambda h: _edit_adapter(h, lambda d: d["files"][VENDORED]["overrides"][0].update({"until": "2000-01-01"}))),
    ("override-until-not-date", "adapter.override", "FAIL", 1, VENDORED + "#checks.conform.run",
     lambda h: _edit_adapter(h, lambda d: d["files"][VENDORED]["overrides"][0].update({"until": "2026-02-30"}))),
    ("override-neither", "adapter.override", "FAIL", 1, "/files/checks~1conform.md/overrides/0",
     lambda h: _edit_adapter(h, lambda d: d["files"][VENDORED]["overrides"][0].pop("until"))),
    ("override-twice", "adapter.override", "FAIL", 1, VENDORED + "#checks.conform.run",
     lambda h: _edit_adapter(h, lambda d: d["files"][VENDORED]["overrides"][1].update({"anchor": "checks.conform.run"}))),
    ("capability-neither", "adapter.capability", "FAIL", 1, "/capabilities/schedule",
     lambda h: _edit_adapter(h, lambda d: d["capabilities"].update({"schedule": {}}))),
    ("capability-empty", "adapter.capability", "FAIL", 1, "/capabilities/memory",
     lambda h: _edit_adapter(h, lambda d: d["capabilities"].update({"memory": {"mechanism": ""}}))),
    ("capability-absent", "adapter.capability", "FAIL", 1, "memory",
     lambda h: _edit_adapter(h, lambda d: d["capabilities"].pop("memory"))),
    ("capability-undeclared", "adapter.capability", "FAIL", 1, "teleport",
     lambda h: _edit_adapter(h, lambda d: d["capabilities"].update({"teleport": {"mechanism": "x"}}))),
    ("parameter-absent", "adapter.parameter", "FAIL", 1, "owner-label",
     lambda h: _edit_adapter(h, lambda d: d["parameters"].pop("owner-label"))),
    ("parameter-empty", "adapter.parameter", "FAIL", 1, "/parameters/owner-label",
     lambda h: _edit_adapter(h, lambda d: d["parameters"].update({"owner-label": ""}))),
    ("parameter-undeclared", "adapter.parameter", "FAIL", 1, "colour",
     lambda h: _edit_adapter(h, lambda d: d["parameters"].update({"colour": "blue"}))),
    ("via-missing", "adapter.reference", "FAIL", 1, QA,
     lambda h: _edit_adapter(h, lambda d: d["files"][QA].update({"via": "harness/NOPE.md"}))),
    ("via-not-naming", "adapter.reference", "FAIL", 1, QA,
     lambda h: _write(h.harness / "harness" / "AGENTS.md", "# Entry\n\nThis file names nothing of the spec.\n")),
    ("not-applied-no-reason", "adapter.not-applied", "FAIL", 1, "/files/policies~1credentials.md",
     lambda h: _edit_adapter(h, lambda d: d["files"][CRED].pop("reason"))),
    ("top-level-extra", "adapter.schema", "FAIL", 1, "*",
     lambda h: _edit_adapter(h, lambda d: d.update({"extra": True}))),
    ("spec-version-newer", "adapter.spec-version", "FAIL", 1, "spec_version",
     lambda h: _edit_adapter(h, lambda d: d.update({"spec_version": "9.0.0"}))),
    ("spec-version-malformed", "adapter.spec-version", "FAIL", 1, "/spec_version",
     lambda h: _edit_adapter(h, lambda d: d.update({"spec_version": "1.0"}))),
    ("spec-version-older", "adapter.spec-version", "WARN", 0, "spec_version",
     lambda h: _edit_adapter(h, lambda d: d.update({"spec_version": "0.0.1"}))),
    ("stale-hash", "adapter.vendored", "WARN", 0, VENDORED + "#checks.conform.purpose",
     lambda h: _touch_section(h.spec / "checks" / "conform.md", "checks.conform.purpose")),
    ("adapter-missing", "input.adapter", NOT_RUN, 2, "",
     lambda h: h.harness / "no-such-adapter.json"),
    ("adapter-directory", "input.adapter", NOT_RUN, 2, "",
     lambda h: h.harness),
    ("adapter-invalid-json", "input.adapter", NOT_RUN, 2, "",
     lambda h: _write(h.adapter, "{")),
    ("adapter-not-object", "input.adapter", NOT_RUN, 2, "",
     lambda h: _write(h.adapter, "[]")),
    ("spec-root-absent", "input.spec-root", NOT_RUN, 2, "spec_root",
     lambda h: _edit_adapter(h, lambda d: d.pop("spec_root"))),
    ("spec-root-missing", "input.spec-root", NOT_RUN, 2, "spec_root",
     lambda h: _edit_adapter(h, lambda d: d.update({"spec_root": "../nowhere"}))),
    ("spec-root-no-version", "input.spec-root", NOT_RUN, 2, "SPEC_VERSION",
     lambda h: _delete(h.spec / "SPEC_VERSION")),
    ("schema-unsupported", "input.schema", NOT_RUN, 2, SCHEMA_REL,
     lambda h: _edit_json(h.spec / "runtime" / "adapter.schema.json",
                          lambda s: s["properties"]["files"].update({"minItems": 1}))),
    ("schema-invalid-json", "input.schema", NOT_RUN, 2, SCHEMA_REL,
     lambda h: _write(h.spec / "runtime" / "adapter.schema.json", "{")),
]


# region FUNC_test_example_exits_0_with_a_row_of_each_mode [DOMAIN(9): AdapterMode; CONCEPT(9): Example, Pass, Modes; TECH(6): run_cli, json]
## @purpose Prove that the example adapter of the repository, run in place, passes: exit 0, no FAIL and no WARN, a PASS row
## for each of the five rule-level checks and at least one PASS row of each mode (reference, vendored, not-applied), and the
## verdict line of the run.
## @uses run_cli, repo_root, ldd_trajectory, find_rows
## @io (Callable, pathlib.Path, Callable, Callable) -> None
## @complexity 5
def test_example_exits_0_with_a_row_of_each_mode(run_cli, repo_root, ldd_trajectory, find_rows):
    code, out, err = run_cli(_adapter_argv(repo_root / "examples" / "adapter.example.json"))
    lines = ldd_trajectory()
    report = json.loads(out)
    counts = report["summary"]["counts"]
    print("[IMP:9][test_example_exits_0][RESULT] exit=%d counts=%s" % (code, counts))
    assert code == 0
    assert err == ""
    assert counts["fail"] == 0 and counts["warn"] == 0 and counts["not-run"] == 0
    for rule in ("adapter.schema", "adapter.spec-version", "adapter.parameter", "adapter.capability",
                 "adapter.file-coverage"):
        assert len(find_rows(report, rule, "PASS", "*")) == 1, rule
    for rule in ("adapter.reference", "adapter.vendored", "adapter.not-applied"):
        assert find_rows(report, rule, "PASS"), rule
    assert any("[run_adapter][VERDICT] exit=0" in line for line in lines)
    assert report["mode"] == "adapter"
# endregion FUNC_test_example_exits_0_with_a_row_of_each_mode


# region FUNC_test_example_accounts_for_every_neutral_file [DOMAIN(9): AdapterMode; CONCEPT(9): FileCoverage, Population; TECH(5): set, json]
## @purpose Prove that the example gives a file entry to each of the 65 neutral files (found here independently of the tool)
## and to nothing else, and that the run judged each one: the subject of every PASS row of the three mode rules is a neutral
## file, and together they are the whole set.
## @uses run_cli, repo_root, find_rows
## @io (Callable, pathlib.Path, Callable) -> None
## @complexity 4
def test_example_accounts_for_every_neutral_file(run_cli, repo_root, find_rows):
    neutral = set(_neutral_paths(repo_root))
    example = json.loads((repo_root / "examples" / "adapter.example.json").read_text(encoding="utf-8"))
    code, out, err = run_cli(_adapter_argv(repo_root / "examples" / "adapter.example.json"))
    report = json.loads(out)
    judged = set()  # type: Set[str]
    for rule in ("adapter.reference", "adapter.vendored", "adapter.not-applied"):
        judged |= {row["subject"] for row in find_rows(report, rule, "PASS")}
    print("[IMP:9][test_example_accounts][COUNT] neutral=%d entries=%d judged=%d" % (len(neutral), len(example["files"]), len(judged)))
    assert len(neutral) == 71
    assert set(example["files"]) == neutral
    assert judged == neutral
    assert report["summary"]["population"]["adapter-files"] == 71
    assert len(example["capabilities"]) == 28
    assert len(example["parameters"]) == 7
# endregion FUNC_test_example_accounts_for_every_neutral_file


# region FUNC_test_example_vendored_entry_is_fresh [DOMAIN(9): AdapterMode; CONCEPT(9): Vendored, Hash, Sections; TECH(6): hashlib, re]
## @purpose Prove, with a hash and a section split computed here and not by the tool, that the example's recorded sha256 is
## the LF-normalised hash of checks/conform.md, that its copy equals the neutral file in every section except the two it
## overrides, and that the two sections it overrides differ.
## @uses repo_root
## @io pathlib.Path -> None
## @complexity 5
def test_example_vendored_entry_is_fresh(repo_root):
    example = json.loads((repo_root / "examples" / "adapter.example.json").read_text(encoding="utf-8"))
    entry = example["files"][VENDORED]
    neutral = (repo_root / VENDORED).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    digest = hashlib.sha256(neutral).hexdigest()
    copy_text = (repo_root / "examples" / entry["path"]).read_text(encoding="utf-8")

    def sections(text: str) -> dict:
        found = {}
        current = None
        for line in text.split("\n"):
            matched = ANCHOR_LINE.match(line)
            if matched:
                current = matched.group(1)
                found[current] = []
            if current is not None:
                found[current].append(line)
        return {key: "\n".join(value) for key, value in found.items()}

    theirs = sections(neutral.decode("utf-8"))
    ours = sections(copy_text)
    overridden = {item["anchor"] for item in entry["overrides"]}
    differing = {key for key in theirs if ours.get(key) != theirs[key]}
    print("[IMP:9][test_example_vendored_fresh][RESULT] fresh=%s sections=%d differing=%s" % (digest == entry["sha256"], len(theirs), sorted(differing)))
    assert entry["sha256"] == digest
    assert set(theirs) == set(ours)
    assert differing == overridden == {"checks.conform.run", "checks.conform.logs"}
    assert len(entry["overrides"]) == 2
# endregion FUNC_test_example_vendored_entry_is_fresh


# region FUNC_test_trigger_override_is_info_presence_only [DOMAIN(8): AdapterMode; CONCEPT(9): Override, Trigger, Info; TECH(5): find_rows]
## @purpose Prove that an override that names only a trigger gets one INFO row saying the trigger is checked for presence
## only, that the override with a date gets none, and that neither ends the run in a failure.
## @uses run_cli, repo_root, find_rows
## @io (Callable, pathlib.Path, Callable) -> None
## @complexity 3
def test_trigger_override_is_info_presence_only(run_cli, repo_root, find_rows):
    code, out, err = run_cli(_adapter_argv(repo_root / "examples" / "adapter.example.json"))
    report = json.loads(out)
    rows = find_rows(report, "adapter.override", "INFO")
    print("[IMP:9][test_trigger_override][RESULT] exit=%d info_rows=%d" % (code, len(rows)))
    assert code == 0
    assert len(rows) == 1
    assert rows[0]["subject"] == VENDORED + "#checks.conform.logs"
    assert rows[0]["detail"] == "trigger checked for presence only"
    assert report["summary"]["counts"]["info"] == 1
# endregion FUNC_test_trigger_override_is_info_presence_only


# region FUNC_test_control_harness_passes [DOMAIN(9): AdapterMode; CONCEPT(9): Control, Copy; TECH(6): run_cli, json]
## @purpose Prove that the unmutated harness copy beside its spec copy passes with exactly the rows of the example run in
## place, so a drill that fails is failing because of its mutation and not because of the copy.
## @uses run_cli, harness_copy, repo_root
## @io (Callable, HarnessCopy, pathlib.Path) -> None
## @complexity 4
def test_control_harness_passes(run_cli, harness_copy, repo_root):
    in_place = run_cli(_adapter_argv(repo_root / "examples" / "adapter.example.json"))
    copied = run_cli(_adapter_argv(harness_copy.adapter))
    first = json.loads(in_place[1])
    second = json.loads(copied[1])
    print("[IMP:9][test_control_harness][RESULT] exit=%d rows=%d in_place_rows=%d" % (copied[0], len(second["rows"]), len(first["rows"])))
    assert copied[0] == 0
    assert copied[2] == ""
    assert second["rows"] == first["rows"]
    assert second["summary"]["line"] == first["summary"]["line"]
# endregion FUNC_test_control_harness_passes


# region FUNC_test_adapter_drill [DOMAIN(10): AdapterMode; CONCEPT(10): Mutation, Rule, Status, Exit; TECH(7): pytest.parametrize, json, ldd]
## @purpose Prove, for one damage of a harness copy, that the tool exits with the code of the case, reports a row of the
## expected rule and status (and subject, where the drill fixes one), and reaches its verdict line, or, for a refusal, gives
## exactly one NOT RUN row and the refusal line. The stale-hash drill also asserts the WARN section row and the WARN stale
## row and that no FAIL row exists.
## @uses run_cli, harness_copy, ldd_trajectory, find_rows
## @io (str, str, str, int, str, Callable, ...) -> None
## @complexity 8
@pytest.mark.parametrize("drill_id,rule,status,expected,subject,mutate", DRILLS, ids=[d[0] for d in DRILLS])
def test_adapter_drill(drill_id, rule, status, expected, subject, mutate, run_cli, harness_copy, ldd_trajectory, find_rows):
    other = mutate(harness_copy)
    target = other if other is not None else harness_copy.adapter
    code, out, err = run_cli(_adapter_argv(target))
    lines = ldd_trajectory()
    report = json.loads(out)
    rows = find_rows(report, rule, status, subject)
    counts = report["summary"]["counts"]
    print("[IMP:9][test_adapter_drill][RESULT] drill=%s rule=%s status=%s exit=%d rows=%d counts=%s" % (
        drill_id, rule, status, code, len(rows), counts))
    assert code == expected
    assert rows, "no %s row for %s" % (status, rule)
    assert err == ""
    if status == NOT_RUN:
        assert len(report["rows"]) == 1
        assert "population: none  probes: none" in report["summary"]["line"]
        assert any("[run_adapter][REFUSAL] rule=%s" % rule in line for line in lines)
        assert any("[main][EXIT] exit=2" in line for line in lines)
        return
    assert any("[run_adapter][VERDICT] exit=%d" % expected in line for line in lines)
    if status == "FAIL":
        assert counts["fail"] >= 1
    if status == "WARN":
        assert counts["fail"] == 0
    if drill_id == "stale-hash":
        stale = find_rows(report, "adapter.vendored", "WARN", VENDORED)
        assert len(stale) == 1 and "stale: recorded" in stale[0]["detail"]
        assert not find_rows(report, "adapter.vendored", "PASS")
        assert any("[check_vendored][DRIFT]" in line and "fresh=False" in line for line in lines)
    if drill_id == "vendored-edited":
        assert any("[check_vendored][DRIFT]" in line and "fresh=True" in line and "differences=1" in line for line in lines)
# endregion FUNC_test_adapter_drill


# region FUNC_test_drill_rules_constant_matches_the_table [DOMAIN(7): Drills; CONCEPT(8): FailureClass, Constant; TECH(4): set]
## @purpose Prove that the DRILL_RULES constant, which the failure-class map reads, is exactly the set of rules the drill table
## of this module covers, and that the table has its 36 drills, each id once.
## @io None -> None
## @complexity 3
def test_drill_rules_constant_matches_the_table():
    covered = {drill[1] for drill in DRILLS}
    ids = [drill[0] for drill in DRILLS]
    print("[IMP:9][test_drill_rules_constant][COUNT] drills=%d rules=%d" % (len(DRILLS), len(covered)))
    assert len(DRILLS) == 36
    assert len(set(ids)) == 36
    assert set(DRILL_RULES) == covered
    assert list(DRILL_RULES) == sorted(DRILL_RULES)
# endregion FUNC_test_drill_rules_constant_matches_the_table


# region FUNC_test_crlf_copies_are_not_a_difference [DOMAIN(8): AdapterMode; CONCEPT(9): LineEndings, Hash; TECH(5): bytes.replace]
## @purpose Prove that line endings decide nothing: with the vendored copy and the spec's own file both converted to CRLF, the
## recorded hash is still fresh and the copy still equals the neutral file in every section, so the entry passes.
## @uses run_cli, harness_copy, find_rows
## @io (Callable, HarnessCopy, Callable) -> None
## @complexity 4
def test_crlf_copies_are_not_a_difference(run_cli, harness_copy, find_rows):
    for path in (_vendored_copy(harness_copy), harness_copy.spec / "checks" / "conform.md"):
        raw = path.read_bytes().replace(b"\r\n", b"\n")
        path.write_bytes(raw.replace(b"\n", b"\r\n"))
    code, out, err = run_cli(_adapter_argv(harness_copy.adapter))
    report = json.loads(out)
    print("[IMP:9][test_crlf_copies][RESULT] exit=%d fail=%d warn=%d" % (code, report["summary"]["counts"]["fail"], report["summary"]["counts"]["warn"]))
    assert code == 0
    assert report["summary"]["counts"]["fail"] == 0 and report["summary"]["counts"]["warn"] == 0
    assert len(find_rows(report, "adapter.vendored", "PASS", VENDORED)) == 1
# endregion FUNC_test_crlf_copies_are_not_a_difference


# region FUNC_test_preamble_before_the_first_anchor_is_not_compared [DOMAIN(8): AdapterMode; CONCEPT(9): Preamble, Sections; TECH(5): str.replace]
## @purpose Prove that text a harness adds before the first anchor of its vendored copy is not a difference: only sections are
## compared, so the entry still passes.
## @uses run_cli, harness_copy, find_rows
## @io (Callable, HarnessCopy, Callable) -> None
## @complexity 3
def test_preamble_before_the_first_anchor_is_not_compared(run_cli, harness_copy, find_rows):
    path = _vendored_copy(harness_copy)
    text = path.read_text(encoding="utf-8")
    first = "<!-- anchor: checks.conform.purpose -->"
    assert first in text
    path.write_text(text.replace(first, "A note the harness adds before the first section.\n\n" + first, 1), encoding="utf-8")
    code, out, err = run_cli(_adapter_argv(harness_copy.adapter))
    report = json.loads(out)
    print("[IMP:9][test_preamble][RESULT] exit=%d fail=%d" % (code, report["summary"]["counts"]["fail"]))
    assert code == 0
    assert report["summary"]["counts"]["fail"] == 0
    assert len(find_rows(report, "adapter.vendored", "PASS", VENDORED)) == 1
# endregion FUNC_test_preamble_before_the_first_anchor_is_not_compared


# region FUNC_test_until_on_the_day_itself_has_not_passed [DOMAIN(8): AdapterMode; CONCEPT(9): Override, Until, Boundary; TECH(6): datetime.date, Report]
## @purpose Prove the boundary of an override's until with an injected today: on the day itself it has not passed, the day
## after it has, and an impossible calendar date is refused however the day falls.
## @uses adapter_module.check_overrides, parse_markdown, Report
## @io None -> None
## @complexity 4
def test_until_on_the_day_itself_has_not_passed():
    text = "---\nid: a.b\ntitle: T\nstatus: stub\n---\n<!-- anchor: a.b.c -->\ntext\n"
    parsed = parse_markdown("a.md", text)
    due = datetime.date(2030, 6, 15)
    results = {}
    for label, today, until in (
        ("on-the-day", due, "2030-06-15"),
        ("day-after", due + datetime.timedelta(days=1), "2030-06-15"),
        ("impossible", due, "2030-02-30"),
    ):
        report = Report("adapter")
        adapter_module.check_overrides([{"anchor": "a.b.c", "until": until}], "a.md", parsed, report, today)
        results[label] = report.counts()["fail"]
    print("[IMP:9][test_until_boundary][RESULT] %s" % sorted(results.items()))
    assert results == {"on-the-day": 0, "day-after": 1, "impossible": 1}
# endregion FUNC_test_until_on_the_day_itself_has_not_passed


# region FUNC_test_compare_sections_by_anchor [DOMAIN(8): AdapterMode; CONCEPT(9): Section, Anchor, Difference; TECH(5): parse_markdown]
## @purpose Prove the comparison rules on small texts: equal sections and a different preamble give no difference; a changed
## section, a section missing from the copy, an anchor only the copy has and an anchor the copy repeats each give one; an
## overridden section may differ.
## @uses adapter_module.compare_sections, parse_markdown
## @io None -> None
## @complexity 5
def test_compare_sections_by_anchor():
    card = "---\nid: a.b\ntitle: T\nstatus: stub\n---\n"
    neutral = parse_markdown("a.md", card + "<!-- anchor: a.one -->\none\n<!-- anchor: a.two -->\ntwo\n")

    def differences(body: str, overridden: Optional[Set[str]] = None) -> List[str]:
        copy = parse_markdown("a.md", card + body)
        return sorted("%s:%s" % pair for pair in adapter_module.compare_sections(neutral, copy, overridden or set()))

    same = differences("<!-- anchor: a.one -->\none\n<!-- anchor: a.two -->\ntwo\n")
    preamble = differences("a harness preface\n<!-- anchor: a.one -->\none\n<!-- anchor: a.two -->\ntwo\n")
    changed = differences("<!-- anchor: a.one -->\none\n<!-- anchor: a.two -->\nTWO\n")
    missing = differences("<!-- anchor: a.one -->\none\n")
    extra = differences("<!-- anchor: a.one -->\none\n<!-- anchor: a.two -->\ntwo\n<!-- anchor: a.three -->\nthree\n")
    repeated = differences("<!-- anchor: a.one -->\none\n<!-- anchor: a.one -->\none\n<!-- anchor: a.two -->\ntwo\n")
    excused = differences("<!-- anchor: a.one -->\none\n<!-- anchor: a.two -->\nTWO\n", {"a.two"})
    print("[IMP:9][test_compare_sections][RESULT] same=%s changed=%s missing=%s extra=%s repeated=%s" % (same, changed, missing, extra, repeated))
    assert same == [] and preamble == [] and excused == []
    assert changed == ["a.two:differs from the neutral section"]
    assert missing == ["a.two:missing in the copy"]
    assert extra == ["a.three:not in the neutral file"]
    assert repeated == ["a.one:repeated in the copy"]
# endregion FUNC_test_compare_sections_by_anchor


# region FUNC_test_adapter_string_values_absent_from_the_trace [DOMAIN(9): Privacy, AdapterMode; CONCEPT(9): NoContent, Trace; TECH(6): caplog, json]
## @purpose Prove that no string value of the adapter (the owner, the reasons, the mechanisms, the fallbacks, the triggers, the
## parameter values, the paths and the hash) appears in any trace line of a run at the most verbose level, on the example
## and on a drill that fails, so a harness's own text never travels through the log.
## @uses run_cli, harness_copy, caplog
## @io (Callable, HarnessCopy, pytest.LogCaptureFixture) -> None
## @complexity 5
def test_adapter_string_values_absent_from_the_trace(run_cli, harness_copy, caplog):
    import logging
    caplog.set_level(logging.DEBUG, logger="conform")
    _edit_adapter(harness_copy, lambda d: d["files"][VENDORED]["overrides"][0].update({"until": "2000-01-01"}))
    data = json.loads(harness_copy.adapter.read_text(encoding="utf-8"))
    values = set()  # type: Set[str]

    def collect(node) -> None:
        if isinstance(node, str):
            values.add(node)
        elif isinstance(node, dict):
            for item in node.values():
                collect(item)
        elif isinstance(node, list):
            for item in node:
                collect(item)

    collect(data)
    values = {value for value in values if len(value) >= 6 and value not in MODE_WORDS and value != data["spec_version"]}
    code, out, err = run_cli(_adapter_argv(harness_copy.adapter))
    trace = "\n".join(record.getMessage() for record in caplog.records if record.name.startswith("conform"))
    leaked = sorted(value for value in values if value in trace)
    print("[IMP:9][test_adapter_values_absent][RESULT] exit=%d values=%d trace_lines=%d leaked=%d" % (
        code, len(values), trace.count("\n") + 1, len(leaked)))
    assert code == 1
    assert len(values) > 30
    assert "[IMP:9][run_adapter][VERDICT]" in trace
    assert leaked == []
# endregion FUNC_test_adapter_string_values_absent_from_the_trace


# region FUNC_test_adapter_internal_error_is_one_not_run_row [DOMAIN(8): AdapterMode; CONCEPT(9): Crash, Refusal; TECH(5): monkeypatch]
## @purpose Prove that a crash inside a check of the adapter mode ends the run as one NOT RUN internal.error row carrying the
## exception class only, exit 2, and the internal line of the trace.
## @uses run_cli, harness_copy, monkeypatch, ldd_trajectory
## @io (Callable, HarnessCopy, pytest.MonkeyPatch, Callable) -> None
## @complexity 4
def test_adapter_internal_error_is_one_not_run_row(run_cli, harness_copy, monkeypatch, ldd_trajectory):
    def _boom(*args, **kwargs):
        raise RuntimeError("drill")
    monkeypatch.setattr(conformlib, "check_files", _boom)
    code, out, err = run_cli(_adapter_argv(harness_copy.adapter))
    lines = ldd_trajectory()
    report = json.loads(out)
    print("[IMP:9][test_adapter_internal_error][RESULT] exit=%d rows=%d" % (code, len(report["rows"])))
    assert code == 2
    assert len(report["rows"]) == 1
    assert report["rows"][0]["status"] == NOT_RUN and report["rows"][0]["rule"] == "internal.error"
    assert report["rows"][0]["detail"] == "RuntimeError"
    assert any("[run_adapter][INTERNAL]" in line and "class=RuntimeError" in line for line in lines)
# endregion FUNC_test_adapter_internal_error_is_one_not_run_row
