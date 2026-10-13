# region MODULE_CONTRACT [DOMAIN(9): Verdict, Report; CONCEPT(9): ExitContract, TwoForms, Summary; TECH(6): pytest, json]
## @modulecontract
## @purpose To prove that the verdict is one thing in two shapes: the exit code follows one precedence, the table and the JSON
## object carry the same rows and the same summary line, the summary states what each probe looked at, a refusal is a single
## NOT RUN row with no population, and NOT RUN never appears next to any other exit code.
## @scope The Report model and both renderings, for the self mode and the adapter mode; the adapter's own damages are drilled in test_adapter.
## @input Copies of the repository with and without a mutation, the in-process runner.
## @output One pass or fail per property of the report.
## @links [USES_API(9): conform.main through run_cli; USES_API(7): conformlib.report.Report]
## @links_to_spec AC-8, AC-P4
## @invariants
## - The table is parsed back by the parse_table fixture, not by the renderer under test.
## - Every comparison is made between two runs of the same input, one per form.
## @rationale
## Q: Why run each input twice, once per form?
## A: The claim is that the two forms cannot drift; only two real runs of the same input can show that they do not.
## @changes
## LAST_CHANGE: [v1.0.0 - Reconcile current M19 boundary/release facts and paired source operands; preserve original assertions/pins/refusals/restoration; runtime checks pending.]
## @modulemap
## FUNC 6[Run the same arguments as a table and as JSON] => _both_forms
## FUNC 6[The clean, one-FAIL and refusal inputs of the two-form tests] => _self_inputs
## FUNC 5[Plant exactly one format FAIL in a copy] => _damage
## FUNC 8[The exit code follows one precedence] => test_exit_code_precedence
## FUNC 4[The inputs of the two-form tests for the adapter mode] => _adapter_inputs
## FUNC 3[A variant of the adapter file beside the adapter] => _variant
## FUNC 9[The JSON rows are the table rows] => test_json_rows_equal_table_rows_self
## FUNC 9[The JSON rows are the table rows, adapter mode] => test_json_rows_equal_table_rows_adapter
## FUNC 6[The JSON object has its documented shape] => test_json_object_has_the_documented_shape
## FUNC 7[The summary line is the same in both forms] => test_summary_line_equal_in_both_forms
## FUNC 8[The summary states population and probes] => test_summary_states_population_and_probes_self
## FUNC 8[The adapter summary states population and probes] => test_summary_states_population_and_probes_adapter
## FUNC 8[A refusal has no population and exit 2] => test_refusal_summary_has_no_population_and_exit_2
## FUNC 9[NOT RUN appears only with exit 2] => test_not_run_only_on_exit_2
## @usecases
## - [test_json_rows_equal_table_rows_self]: Script -> reads the JSON of a run -> gets the rows a person reads in the table
## - [test_not_run_only_on_exit_2]: Caller -> sees exit 2 -> knows nothing was judged
## - [test_summary_states_population_and_probes_adapter]: Harness author -> reads the summary -> knows what the adapter run looked at
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: report tests, exit code precedence, table and JSON same rows, summary line, population, probes, refusal, NOT RUN only on exit 2, parse_table
# STRUCTURE: ▶ Report unit ⚡ precedence ∀8 → ⊕ run input ∀ mode ┌self, adapter┐ ∀ form ┌table, json┐ → ◇ rows table = rows json ∧ summary = summary → ∑ NOT RUN ⇒ exit 2 → ⎋ assert

import hashlib
import json
import pathlib
import re
import shutil
from typing import Callable, List, Tuple

import pytest

from conformlib.report import Report

PROBES_ADAPTER = [
    "structure", "spec-version", "parameter", "capability", "file-coverage", "reference", "vendored", "override",
    "not-applied",
]
POPULATION_KEYS_ADAPTER = [
    "neutral-files", "anchors", "norms", "capabilities", "parameters", "spec-version", "adapter-files",
    "adapter-parameters", "adapter-capabilities",
]
ANCHOR_LINE = re.compile(r"^<!-- anchor: [a-z][a-z0-9.-]* -->$")
PROBES_SELF = ["scan.canary", "card", "anchor", "norm", "registry", "call", "version", "scan"]
POPULATION_KEYS_SELF = [
    "neutral-files", "anchors", "norms", "calls", "capabilities", "parameters", "text-files", "binary-files",
    "deny-list", "deny-list-fp", "skipped",
]
PRECEDENCE = [
    ("empty", [], 0),
    ("pass-warn-info", ["PASS", "WARN", "INFO"], 0),
    ("fail", ["PASS", "FAIL"], 1),
    ("fail-and-warn", ["WARN", "FAIL", "INFO"], 1),
    ("not-run", ["NOT RUN"], 2),
    ("not-run-over-fail", ["FAIL", "NOT RUN"], 2),
    ("not-run-first", ["NOT RUN", "FAIL", "PASS"], 2),
    ("many-fail", ["FAIL", "FAIL", "PASS"], 1),
]


# region FUNC__both_forms [DOMAIN(8): Report; CONCEPT(9): TwoForms; TECH(5): run_cli]
## @purpose Run the same arguments twice, without and with the JSON option, and return both results.
## @io (Callable, List[str]) -> Tuple[Tuple[int, str, str], Tuple[int, str, str]]
## @complexity 2
def _both_forms(run_cli: Callable, argv: List[str]):
    table = run_cli(list(argv))
    as_json = run_cli(list(argv) + ["--json"])
    return table, as_json
# endregion FUNC__both_forms


# region FUNC__self_inputs [DOMAIN(8): Report; CONCEPT(8): Inputs; TECH(4): list]
## @purpose The inputs of the two-form tests: a clean copy, a second copy with one FAIL, and three refusals (no deny list, a missing
## root, no arguments), each as an argument list.
## @io (pathlib.Path, pathlib.Path, pathlib.Path) -> List[Tuple[str, List[str], int]]
## @complexity 3
def _self_inputs(copy: pathlib.Path, deny: pathlib.Path, tmp: pathlib.Path) -> List[Tuple[str, List[str], int]]:
    damaged = tmp / "damaged-copy"
    shutil.copytree(str(copy), str(damaged))
    _damage(damaged)
    return [
        ("control", ["self", "--root", str(copy), "--deny-list", str(deny)], 0),
        ("fail", ["self", "--root", str(damaged), "--deny-list", str(deny)], 1),
        ("no-deny-list", ["self", "--root", str(copy)], 2),
        ("missing-root", ["self", "--root", str(tmp / "nowhere"), "--deny-list", str(deny)], 2),
        ("bad-option", ["self", "--bogus"], 2),
    ]
# endregion FUNC__self_inputs


# region FUNC__damage [DOMAIN(6): Report; CONCEPT(7): Mutation; TECH(4): pathlib]
## @purpose Damage a copy the cheapest way that gives exactly one format FAIL: a card status outside the three allowed.
## @io pathlib.Path -> pathlib.Path
## @complexity 2
def _damage(copy: pathlib.Path) -> pathlib.Path:
    target = copy / "concepts" / "glossary.md"
    target.write_text(target.read_text(encoding="utf-8").replace("status: draft", "status: final", 1), encoding="utf-8")
    return copy
# endregion FUNC__damage


# region FUNC__variant [DOMAIN(6): Report; CONCEPT(7): Mutation, Adapter; TECH(4): json]
## @purpose Write a changed copy of the harness copy's adapter next to it under another name, so several inputs share one
## harness and one spec copy, and return its path.
## @io (HarnessCopy, str, Callable) -> pathlib.Path
## @complexity 2
def _variant(copy, name: str, change: Callable) -> pathlib.Path:
    data = json.loads(copy.adapter.read_text(encoding="utf-8"))
    change(data)
    path = copy.harness / ("variant-%s.json" % name)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    return path
# endregion FUNC__variant


# region FUNC__adapter_inputs [DOMAIN(8): Report; CONCEPT(8): Inputs, Adapter; TECH(4): list]
## @purpose The inputs of the two-form tests for the adapter mode: the control (exit 0), one FAIL (a file with no entry), one
## WARN (an older spec version, exit 0), and four refusals (a missing adapter, an adapter that is not JSON, a spec root that is
## not there, an unknown option), each as an argument list.
## @io HarnessCopy -> List[Tuple[str, List[str], int]]
## @complexity 3
def _adapter_inputs(copy) -> List[Tuple[str, List[str], int]]:
    broken = copy.harness / "variant-not-json.json"
    broken.write_text("{", encoding="utf-8")
    return [
        ("adapter-control", ["adapter", str(copy.adapter)], 0),
        ("adapter-fail", ["adapter", str(_variant(copy, "fail", lambda d: d["files"].pop("roles/qa.md")))], 1),
        ("adapter-warn", ["adapter", str(_variant(copy, "warn", lambda d: d.update({"spec_version": "0.0.1"})))], 0),
        ("adapter-missing", ["adapter", str(copy.harness / "no-such-adapter.json")], 2),
        ("adapter-not-json", ["adapter", str(broken)], 2),
        ("adapter-no-spec", ["adapter", str(_variant(copy, "no-spec", lambda d: d.update({"spec_root": "../nowhere"})))], 2),
        ("adapter-bad-option", ["adapter", "--bogus"], 2),
    ]
# endregion FUNC__adapter_inputs


# region FUNC_test_exit_code_precedence [DOMAIN(9): Verdict; CONCEPT(10): ExitContract, Precedence; TECH(6): pytest.parametrize, Report]
## @purpose Prove the exit contract on the model itself: NOT RUN over FAIL over everything else, and 0 for a report of only
## PASS, WARN and INFO rows or of no row.
## @io (str, List[str], int) -> None
## @complexity 3
@pytest.mark.parametrize("case,statuses,expected", PRECEDENCE, ids=[p[0] for p in PRECEDENCE])
def test_exit_code_precedence(case, statuses, expected):
    report = Report("self")
    for number, status in enumerate(statuses):
        report.add(status, "unit.rule", "subject-%d" % number, "detail")
    print("[IMP:9][test_exit_code_precedence][RESULT] case=%s statuses=%s exit=%d" % (case, statuses, report.exit_code()))
    assert report.exit_code() == expected
    assert ("exit=%d" % expected) in report.summary_line()
# endregion FUNC_test_exit_code_precedence


# region FUNC_test_json_rows_equal_table_rows_self [DOMAIN(10): Report; CONCEPT(10): TwoForms, SameRows; TECH(6): parse_table, json]
## @purpose Prove, for a clean run, a failing run and three refusals, that the table (parsed back) and the JSON object hold the
## same rows in the same order, that each table line is exactly the documented row format, and that the exit codes agree.
## @uses run_cli, parse_table, repo_copy, deny_list, tmp_path
## @io (Callable, Callable, pathlib.Path, Tuple, pathlib.Path) -> None
## @complexity 6
def test_json_rows_equal_table_rows_self(run_cli, parse_table, repo_copy, deny_list, tmp_path):
    for name, argv, expected in _self_inputs(repo_copy, deny_list[0], tmp_path):
        (t_code, t_out, t_err), (j_code, j_out, j_err) = _both_forms(run_cli, argv)
        table_rows, _summary = parse_table(t_out)
        report = json.loads(j_out)
        print("[IMP:9][test_json_rows_equal_table][RESULT] input=%s exit=%d/%d rows=%d" % (name, t_code, j_code, len(table_rows)))
        assert t_code == j_code == expected
        assert t_err == "" and j_err == ""
        assert table_rows == report["rows"]
        lines = t_out.split("\n")
        for index, row in enumerate(report["rows"]):
            assert lines[index] == "%-7s  %s  %s  %s" % (row["status"], row["rule"], row["subject"], row["detail"])
# endregion FUNC_test_json_rows_equal_table_rows_self


# region FUNC_test_json_rows_equal_table_rows_adapter [DOMAIN(10): Report; CONCEPT(10): TwoForms, SameRows, Adapter; TECH(6): parse_table, json]
## @purpose Prove, for the adapter mode (a clean run, a FAIL, a WARN and four refusals), that the table (parsed back) and the
## JSON object hold the same rows in the same order, that each table line is the documented row format, and that the exit
## codes agree with the case.
## @uses run_cli, parse_table, harness_copy
## @io (Callable, Callable, HarnessCopy) -> None
## @complexity 6
def test_json_rows_equal_table_rows_adapter(run_cli, parse_table, harness_copy):
    for name, argv, expected in _adapter_inputs(harness_copy):
        (t_code, t_out, t_err), (j_code, j_out, j_err) = _both_forms(run_cli, argv)
        table_rows, table_summary = parse_table(t_out)
        report = json.loads(j_out)
        print("[IMP:9][test_json_rows_equal_table_adapter][RESULT] input=%s exit=%d/%d rows=%d" % (name, t_code, j_code, len(table_rows)))
        assert t_code == j_code == expected
        assert t_err == "" and j_err == ""
        assert report["mode"] == "adapter"
        assert table_rows == report["rows"]
        assert table_summary == report["summary"]["line"]
        lines = t_out.split("\n")
        for index, row in enumerate(report["rows"]):
            assert lines[index] == "%-7s  %s  %s  %s" % (row["status"], row["rule"], row["subject"], row["detail"])
# endregion FUNC_test_json_rows_equal_table_rows_adapter


# region FUNC_test_json_object_has_the_documented_shape [DOMAIN(8): Report; CONCEPT(9): Json, Shape; TECH(4): json]
## @purpose Prove that the JSON object has the keys the documentation names, that the row keys are the four fields, that the
## counts sum to the number of rows, and that a population number stays a number.
## @uses run_cli, repo_copy, deny_list
## @io (Callable, pathlib.Path, Tuple) -> None
## @complexity 4
def test_json_object_has_the_documented_shape(run_cli, repo_copy, deny_list):
    code, out, err = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    report = json.loads(out)
    print("[IMP:9][test_json_shape][RESULT] exit=%d keys=%s" % (code, sorted(report)))
    assert sorted(report) == ["exit", "mode", "rows", "summary"]
    assert report["mode"] == "self" and report["exit"] == code
    assert all(sorted(row) == ["detail", "rule", "status", "subject"] for row in report["rows"])
    assert sorted(report["summary"]) == ["counts", "line", "population", "probes"]
    assert sum(report["summary"]["counts"].values()) == len(report["rows"])
    assert isinstance(report["summary"]["population"]["neutral-files"], int)
    assert isinstance(report["summary"]["population"]["deny-list-fp"], str)
# endregion FUNC_test_json_object_has_the_documented_shape


# region FUNC_test_summary_line_equal_in_both_forms [DOMAIN(8): Report; CONCEPT(9): Summary, TwoForms; TECH(5): parse_table]
## @purpose Prove that the summary line printed under the table is byte for byte the line the JSON object carries, for the
## clean run, the failing run and the refusals.
## @uses run_cli, parse_table, repo_copy, deny_list, tmp_path
## @io (Callable, Callable, pathlib.Path, Tuple, pathlib.Path) -> None
## @complexity 4
def test_summary_line_equal_in_both_forms(run_cli, parse_table, repo_copy, deny_list, tmp_path):
    for name, argv, expected in _self_inputs(repo_copy, deny_list[0], tmp_path):
        (t_code, t_out, _t_err), (j_code, j_out, _j_err) = _both_forms(run_cli, argv)
        _rows, table_summary = parse_table(t_out)
        json_summary = json.loads(j_out)["summary"]["line"]
        print("[IMP:9][test_summary_line_equal][RESULT] input=%s equal=%s" % (name, table_summary == json_summary))
        assert table_summary == json_summary
        assert table_summary.startswith("SUMMARY  mode=")
        assert ("  exit=%d  " % expected) in table_summary
# endregion FUNC_test_summary_line_equal_in_both_forms


# region FUNC_test_summary_states_population_and_probes_self [DOMAIN(9): Report; CONCEPT(10): Population, Probes; TECH(5): json, hashlib]
## @purpose Prove that a self run states what it looked at: the population keys in their fixed order with the counts of the
## layout (neutral files, norms, capabilities, parameters), the deny list's count and fingerprint computed independently, the
## skipped set, and the probes that ran, in the order they ran.
## @uses run_cli, repo_copy, deny_list
## @io (Callable, pathlib.Path, Tuple) -> None
## @complexity 5
def test_summary_states_population_and_probes_self(run_cli, repo_copy, deny_list):
    code, out, err = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    summary = json.loads(out)["summary"]
    population = summary["population"]
    expected_fp = hashlib.sha256(deny_list[1].lower().encode("utf-8")).hexdigest()[:12]
    print("[IMP:9][test_summary_population][RESULT] exit=%d keys=%d probes=%s" % (code, len(population), summary["probes"]))
    assert code == 0
    assert list(population) == POPULATION_KEYS_SELF
    assert population["neutral-files"] == 71
    assert population["norms"] == 1220
    assert population["capabilities"] == 28
    assert population["parameters"] == 7
    assert population["anchors"] >= 25
    assert population["deny-list"] == 1
    assert population["deny-list-fp"] == expected_fp
    assert population["skipped"] == ".git,doxygen_output,__pycache__,.pytest_cache,.DS_Store"
    assert summary["probes"] == PROBES_SELF
    assert ("  probes: " + ",".join(PROBES_SELF)) in summary["line"]
    assert ("population: neutral-files=71 ") in summary["line"]
# endregion FUNC_test_summary_states_population_and_probes_self


# region FUNC_test_summary_states_population_and_probes_adapter [DOMAIN(9): Report; CONCEPT(10): Population, Probes, Adapter; TECH(5): json, re]
## @purpose Prove that an adapter run states what it looked at: the nine population keys in their fixed order, the spec's
## counts (the anchors counted here outside fenced blocks), the spec version read from SPEC_VERSION, the adapter's own counts,
## and the nine probes in the order they ran; and that a refusal before the checks states neither population nor probes.
## @uses run_cli, repo_root
## @io (Callable, pathlib.Path) -> None
## @complexity 5
def test_summary_states_population_and_probes_adapter(run_cli, repo_root):
    code, out, err = run_cli(["adapter", str(repo_root / "examples" / "adapter.example.json"), "--json"])
    summary = json.loads(out)["summary"]
    population = summary["population"]
    version = (repo_root / "SPEC_VERSION").read_text(encoding="utf-8").strip()
    anchors = 0
    for path in repo_root.rglob("*.md"):
        relative = path.relative_to(repo_root)
        if relative.parts[0] in {".git", "doxygen_output", "tests", "examples", "__pycache__", ".pytest_cache", "implementations"}:
            continue
        if len(relative.parts) == 1 and relative.name in {"README.md", "CHANGELOG.md"}:
            continue
        fenced = False
        for line in path.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n"):
            if line.startswith("```"):
                fenced = not fenced
            elif not fenced and ANCHOR_LINE.match(line):
                anchors += 1
    print("[IMP:9][test_summary_population_adapter][RESULT] exit=%d keys=%d probes=%s anchors=%d" % (code, len(population), summary["probes"], anchors))
    assert code == 0
    assert list(population) == POPULATION_KEYS_ADAPTER
    assert population["neutral-files"] == 71
    assert population["anchors"] == anchors
    assert population["norms"] == 1220
    assert population["capabilities"] == 28
    assert population["parameters"] == 7
    assert population["spec-version"] == version
    assert population["adapter-files"] == 71
    assert population["adapter-parameters"] == 7
    assert population["adapter-capabilities"] == 28
    assert summary["probes"] == PROBES_ADAPTER
    assert ("  probes: " + ",".join(PROBES_ADAPTER)) in summary["line"]
    assert "population: neutral-files=71 " in summary["line"]
# endregion FUNC_test_summary_states_population_and_probes_adapter


# region FUNC_test_refusal_summary_has_no_population_and_exit_2 [DOMAIN(9): Report; CONCEPT(10): Refusal, NoPopulation; TECH(5): json]
## @purpose Prove that a refusal states no population and no probes, counts exactly one NOT RUN row and nothing else, and exits
## 2, so that no count can read as a clean bill of health.
## @uses run_cli, repo_copy
## @io (Callable, pathlib.Path) -> None
## @complexity 3
def test_refusal_summary_has_no_population_and_exit_2(run_cli, repo_copy):
    code, out, err = run_cli(["self", "--root", str(repo_copy), "--json"])
    report = json.loads(out)
    summary = report["summary"]
    print("[IMP:9][test_refusal_summary][RESULT] exit=%d line=%s" % (code, summary["line"]))
    assert code == 2
    assert summary["population"] == {} and summary["probes"] == []
    assert summary["counts"] == {"pass": 0, "warn": 0, "fail": 0, "info": 0, "not-run": 1}
    assert summary["line"].endswith("  population: none  probes: none")
    assert "not-run=1" in summary["line"]
# endregion FUNC_test_refusal_summary_has_no_population_and_exit_2


# region FUNC_test_not_run_only_on_exit_2 [DOMAIN(10): Report; CONCEPT(10): NotRun, Exit2, OneRow; TECH(5): parse_table, json]
## @purpose Prove, in both forms and both modes, for the clean run, the failing run, the warning run and the refusals, that a
## NOT RUN row appears if and only if the exit code is 2, and that an exit-2 report is that one row and no other.
## @uses run_cli, parse_table, repo_copy, deny_list, tmp_path, harness_copy
## @io (Callable, Callable, pathlib.Path, Tuple, pathlib.Path, HarnessCopy) -> None
## @complexity 5
def test_not_run_only_on_exit_2(run_cli, parse_table, repo_copy, deny_list, tmp_path, harness_copy):
    for name, argv, expected in _self_inputs(repo_copy, deny_list[0], tmp_path) + _adapter_inputs(harness_copy):
        (t_code, t_out, _t_err), (j_code, j_out, _j_err) = _both_forms(run_cli, argv)
        table_rows, _summary = parse_table(t_out)
        json_rows = json.loads(j_out)["rows"]
        for code, rows in ((t_code, table_rows), (j_code, json_rows)):
            not_run = [row for row in rows if row["status"] == "NOT RUN"]
            print("[IMP:9][test_not_run_only_on_exit_2][RESULT] input=%s exit=%d rows=%d not_run=%d" % (name, code, len(rows), len(not_run)))
            assert code == expected
            assert bool(not_run) == (code == 2)
            if code == 2:
                assert len(rows) == 1 and len(not_run) == 1
# endregion FUNC_test_not_run_only_on_exit_2


# region FUNC_test_report_protection_preserves_safe_context [DOMAIN(10): Privacy; CONCEPT(10): SharedBoundary; TECH(6): Report]
## @purpose One policy protects diagnostic data and refusals while retaining safe values, statuses, counts and keys.
## @uses conformlib.scan.redact_diagnostic, conformlib.report.refused
## @io Tuple -> None
## @complexity 4
def test_report_protection_preserves_safe_context(deny_list):
    from conformlib.scan import build_patterns, redact_diagnostic
    from conformlib.report import Refusal, refused
    token = deny_list[1]
    protect = lambda value: redact_diagnostic(value, [token, token[2:]], build_patterns())
    report = Report("self", protect=protect)
    report.add("FAIL", "call.resolves", "concepts/" + token + ".md", "line 7 undeclared cap:" + token.upper())
    report.add("FAIL", "call.resolves", "concepts/safe.md", "line 8 undeclared cap:ordinary-missing")
    report.populate("count", 3)
    report.populate("context", token)
    one = refused("self", Refusal("input.root", token, "unreadable " + token), protect=protect)
    print("[IMP:9][report_protection][RESULT] exits=%d/%d rows=%d" % (report.exit_code(), one.exit_code(), len(report.rows)))
    assert token.lower() not in json.dumps(report.to_dict()).lower()
    assert token.lower() not in json.dumps(one.to_dict()).lower()
    assert report.rows[0].subject.startswith("concepts/") and report.rows[0].subject.endswith(".md")
    assert report.rows[0].detail.startswith("line 7 undeclared cap:") and "fp=" in report.rows[0].detail
    assert report.rows[1].detail == "line 8 undeclared cap:ordinary-missing"
    assert report.population["count"] == 3 and list(report.population) == ["count", "context"]
    assert report.exit_code() == 1 and one.exit_code() == 2
    assert one.population == {} and one.probes == []
# endregion FUNC_test_report_protection_preserves_safe_context


# region FUNC_test_diagnostic_patterns_and_overlap [DOMAIN(10): Privacy; CONCEPT(10): MatchSemantics; TECH(6): regex]
## @purpose Every scanner pattern and overlapping case-insensitive token spans remain protected with safe suffixes intact.
## @uses conformlib.scan.redact_diagnostic
## @io Dict, Tuple -> None
## @complexity 4
def test_diagnostic_patterns_and_overlap(canary_values, deny_list):
    from conformlib.scan import build_patterns, redact_diagnostic
    patterns = build_patterns()
    token = deny_list[1]
    values = list(canary_values.values()) + [token.upper() + token[2:].upper()]
    for value in values:
        protected = redact_diagnostic("line 9 " + value + " safe-context", [token, token[2:]], patterns)
        print("[IMP:9][diagnostic_patterns][RESULT] fp_present=%s" % ("fp=" in protected))
        assert value not in protected
        assert token.lower() not in protected.lower()
        assert protected.startswith("line 9 ") and protected.endswith(" safe-context")
        assert "fp=" in protected
    assert redact_diagnostic("ordinary context", [token], patterns) == "ordinary context"
# endregion FUNC_test_diagnostic_patterns_and_overlap
