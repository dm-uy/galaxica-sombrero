# region MODULE_CONTRACT [DOMAIN(10): Publication, Privacy; CONCEPT(9): Canary, Fingerprint, NoContentInOutput; TECH(6): pytest, subprocess, json]
## @modulecontract
## @purpose To prove that the publication scan bites, points at the right place, and never gives the value away: a planted
## address, home path, tilde path or deny word makes the run fail with the rule, the file and the line, while the value
## itself appears in no table, no JSON object, no trace line and no real process stream.
## @scope The four scan rules, the fingerprint shape, the file population (text, code, binary), the scanner's own source and
## the repository's own files. The format rules have their own module.
## @input A copy of the repository, a synthetic deny list, canary values built at run time.
## @output One pass or fail per property; the trajectory lines printed before the asserts.
## @links [USES_API(9): conform.main through run_cli; USES_API(7): subprocess for the real streams; USES_API(6): conformlib.scan]
## @links_to_spec AC-7, AC-P2, AC-P3
## @invariants
## - No source line of this module matches a scan rule: every canary is built from fragments at run time.
## - A drill plants its value in a copy under the temporary directory, never in the repository.
## - A value is looked for in every place the tool can write: the table, the JSON, the trace, both real streams.
## @rationale
## Q: Why also run a real process?
## A: In process, capsys shows what the entry point wrote; only a subprocess shows what reaches a terminal or a pipe, with
## the interpreter's own streams and no test plugin between.
## Q: Why look for the value in the JSON serialisation as well as the streams?
## A: A row could carry the value in a field the table does not print; the serialised object is the whole of the data.
## @changes
## LAST_CHANGE: [v1.0.0 - Add real typed-package privacy carrier controls; preserve all prior canary/refusal/exclusion/restoration populations.]
## PREVIOUS_CHANGE: [v0.1.0 - Initial creation: five canary drills, real streams, case, population, fingerprint, self-scan.]
## @modulemap
## FUNC 4[The self-run argument list over a copy, JSON form, full trace] => _self_argv
## FUNC 6[Every form a value could take in an output] => _forms
## FUNC 9[Each canary fails with its rule, file and line and stays out of every output] => test_canary_fails_with_rule_and_location
## FUNC 9[All canaries stay out of the real process streams] => test_canary_values_absent_from_real_process_streams
## FUNC 6[The deny word matches whatever the case] => test_deny_token_matches_case_insensitively
## FUNC 6[Python, JSON and extensionless files are scanned] => test_scan_covers_python_and_json_files
## FUNC 6[A binary or non-UTF-8 file is INFO and not scanned] => test_binary_file_is_info_not_scanned
## FUNC 6[A fingerprint is length and eight hex digits] => test_fingerprint_shape
## FUNC 7[The tool's own source passes its own scan] => test_scanner_source_does_not_match_itself
## FUNC 7[The whole repository passes the scan] => test_repository_tool_tests_and_fixtures_pass_the_scan
## FUNC 5[The drill-rule constant equals the table] => test_drill_rules_constant_matches_the_table
## FUNC 9[Git metadata exclusion with ordinary negative control] => test_worktree_git_metadata_excluded_but_ordinary_file_scanned
## FUNC 10[All existing canaries in actual native carrier families through real CLI] => test_scan.test_package_publication_channels
## @usecases
## - [test_canary_fails_with_rule_and_location]: QA agent -> plants a private-looking value on line 3 -> the tool names rule, file and line, not the value
## - [test_scanner_source_does_not_match_itself]: QA agent -> scans the tool's own folder -> no finding
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: publication scan drills, canary, home path, tilde path, e-mail, deny token, fingerprint, binary file, real process streams, no value in output, scanner self-scan
# STRUCTURE: ▶ canary ∈ {posix, windows, tilde, email, deny} → ⚡ plant line 3 → ⊕ run self --json --log-level DEBUG → ◇ exit 1 ∧ FAIL rule,file,line,fp → ∑ value ∉ {stdout, stderr, json, trace} → ⎋ assert

import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
from typing import List

import pytest

from conformlib import scan
from conformlib.report import Report

CANARY_RULES = [
    ("posix-home", "scan.home-path"),
    ("windows-home", "scan.home-path"),
    ("tilde", "scan.home-relative"),
    ("email", "scan.email"),
    ("deny-token", "scan.deny-token"),
]
SCAN_RULES = ["scan.home-path", "scan.home-relative", "scan.email", "scan.deny-token"]
DRILL_RULES = ("scan.binary", "scan.deny-token", "scan.email", "scan.home-path", "scan.home-relative")
FP_DETAIL_RE = re.compile(r"^line (\d+) fp=(\d+):([0-9a-f]{8})$")


# region FUNC__self_argv [DOMAIN(7): Drills; CONCEPT(8): Invocation; TECH(4): list]
## @purpose The argument list of a self run over a copy with a deny list, in the JSON form with the full trace.
## @io (pathlib.Path, pathlib.Path) -> List[str]
## @complexity 1
def _self_argv(copy: pathlib.Path, deny: pathlib.Path) -> List[str]:
    return ["self", "--root", str(copy), "--deny-list", str(deny), "--json", "--log-level", "DEBUG"]
# endregion FUNC__self_argv


# region FUNC__forms [DOMAIN(8): Privacy; CONCEPT(9): ValueForms, NoContent; TECH(4): json]
## @purpose Every form a value could take in an output: as it is, and as JSON writes it inside a string.
## @io str -> List[str]
## @complexity 2
def _forms(value: str) -> List[str]:
    return [value, json.dumps(value)[1:-1]]
# endregion FUNC__forms


# region FUNC_test_canary_fails_with_rule_and_location [DOMAIN(10): Publication; CONCEPT(10): Canary, Location, NoContent; TECH(6): pytest.parametrize, json]
## @purpose Prove, for one kind of private-looking value planted on line 3 of a new non-Markdown file, that the tool exits 1,
## gives one FAIL row with the rule, the file and the line and a fingerprint, keeps the other three scan rules PASS, and
## that the value appears in no output: stdout, stderr, the serialised report and every trace line.
## @uses run_cli, repo_copy, deny_list, canary_values, plant_canary, ldd_trajectory, caplog, find_rows
## @io (str, str, Callable, ...) -> None
## @complexity 6
@pytest.mark.parametrize("kind,rule", CANARY_RULES, ids=[c[0] for c in CANARY_RULES])
def test_canary_fails_with_rule_and_location(kind, rule, run_cli, repo_copy, deny_list, canary_values, plant_canary,
                                             ldd_trajectory, caplog, find_rows):
    value = canary_values[kind]
    plant_canary(repo_copy, "notes/drill.txt", value)
    code, out, err = run_cli(_self_argv(repo_copy, deny_list[0]))
    lines = ldd_trajectory()
    report = json.loads(out)
    fails = [row for row in report["rows"] if row["status"] == "FAIL"]
    every_trace = "\n".join(record.getMessage() for record in caplog.records)
    print("[IMP:9][test_canary_fails][RESULT] kind=%s rule=%s exit=%d fails=%d" % (kind, rule, code, len(fails)))
    assert code == 1
    assert len(fails) == 1
    assert fails[0]["rule"] == rule
    assert fails[0]["subject"] == "notes/drill.txt"
    assert fails[0]["detail"].startswith("line 3 fp=")
    assert FP_DETAIL_RE.match(fails[0]["detail"])
    for other in SCAN_RULES:
        if other != rule:
            assert find_rows(report, other, "PASS")
    assert any("[scan_tree][FINDING]" in line and "line=3" in line for line in lines)
    assert err, "the trace must reach standard error at DEBUG"
    for form in _forms(value):
        assert form not in out
        assert form not in err
        assert form not in json.dumps(report)
        assert form not in every_trace
# endregion FUNC_test_canary_fails_with_rule_and_location


# region FUNC_test_canary_values_absent_from_real_process_streams [DOMAIN(10): Publication; CONCEPT(10): RealStreams, NoContent; TECH(6): subprocess]
## @purpose Prove, with a real interpreter process and its own pipes, that all five canaries planted in one copy make the run
## fail with exit 1 and appear in neither standard output nor standard error, though the trace is on at DEBUG.
## @uses subprocess.run, repo_root, repo_copy, deny_list, canary_values, plant_canary
## @io (pathlib.Path, pathlib.Path, Tuple, Dict, Callable) -> None
## @complexity 5
def test_canary_values_absent_from_real_process_streams(repo_root, repo_copy, deny_list, canary_values, plant_canary):
    for kind, _rule in CANARY_RULES:
        plant_canary(repo_copy, "notes/real-" + kind + ".txt", canary_values[kind])
    command = [sys.executable, str(repo_root / "tools" / "conform.py")] + _self_argv(repo_copy, deny_list[0])
    done = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd=str(repo_copy))
    report = json.loads(done.stdout)
    fails = [row for row in report["rows"] if row["status"] == "FAIL"]
    print("[IMP:9][test_real_streams][RESULT] exit=%d fails=%d stdout_chars=%d stderr_chars=%d"
          % (done.returncode, len(fails), len(done.stdout), len(done.stderr)))
    assert done.returncode == 1
    assert sorted(row["subject"] for row in fails) == sorted("notes/real-" + kind + ".txt" for kind, _rule in CANARY_RULES)
    assert done.stderr, "the trace must reach standard error at DEBUG"
    for kind, _rule in CANARY_RULES:
        for form in _forms(canary_values[kind]):
            assert form not in done.stdout
            assert form not in done.stderr
# endregion FUNC_test_canary_values_absent_from_real_process_streams


# region FUNC_test_deny_token_matches_case_insensitively [DOMAIN(8): Privacy; CONCEPT(9): DenyList, CaseFolding; TECH(4): json]
## @purpose Prove that a deny word is found in upper, lower and mixed case, that one fingerprint (of the lowercase word) is
## reported for all of them, and that a fragment of the word is not a finding.
## @uses run_cli, repo_copy, deny_list
## @io (Callable, pathlib.Path, Tuple) -> None
## @complexity 4
def test_deny_token_matches_case_insensitively(run_cli, repo_copy, deny_list):
    token = deny_list[1]
    mixed = token[:2].upper() + token[2:]
    text = "\n".join(["a " + token.upper(), "b " + token.lower(), "c " + mixed, "d " + token[:-1], ""])
    (repo_copy / "notes").mkdir()
    (repo_copy / "notes" / "case.txt").write_text(text, encoding="utf-8")
    code, out, err = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    report = json.loads(out)
    fails = [row for row in report["rows"] if row["status"] == "FAIL" and row["rule"] == "scan.deny-token"]
    expected = "%d:%s" % (len(token), hashlib.sha256(token.lower().encode("utf-8")).hexdigest()[:8])
    print("[IMP:9][test_deny_token_case][RESULT] exit=%d fails=%d" % (code, len(fails)))
    assert code == 1
    assert [row["detail"] for row in fails] == ["line %d fp=%s" % (number, expected) for number in (1, 2, 3)]
# endregion FUNC_test_deny_token_matches_case_insensitively


# region FUNC_test_scan_covers_python_and_json_files [DOMAIN(8): Publication; CONCEPT(9): Population, AllTextFiles; TECH(4): json]
## @purpose Prove that the scan reads every text file, not only Markdown: a Python file, a JSON file, a Markdown file and a
## file with no extension each give a FAIL row for a planted address.
## @uses run_cli, repo_copy, deny_list, canary_values, plant_canary
## @io (Callable, pathlib.Path, Tuple, Dict, Callable) -> None
## @complexity 4
def test_scan_covers_python_and_json_files(run_cli, repo_copy, deny_list, canary_values, plant_canary):
    names = ["notes/planted.py", "notes/planted.json", "notes/planted.md", "notes/planted"]
    for name in names:
        plant_canary(repo_copy, name, canary_values["email"])
    code, out, err = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    report = json.loads(out)
    subjects = sorted(row["subject"] for row in report["rows"] if row["status"] == "FAIL" and row["rule"] == "scan.email")
    print("[IMP:9][test_scan_covers][RESULT] exit=%d subjects=%s" % (code, subjects))
    assert code == 1
    assert subjects == sorted(names)
# endregion FUNC_test_scan_covers_python_and_json_files


# region FUNC_test_binary_file_is_info_not_scanned [DOMAIN(8): Publication; CONCEPT(9): Binary, Info; TECH(4): bytes]
## @purpose Prove that a file with a NUL byte and a file that is not UTF-8 each give an INFO row scan.binary, are counted in
## the population, are not scanned (their planted address is no finding), and do not fail the run.
## @uses run_cli, repo_copy, deny_list, canary_values, find_rows
## @io (Callable, pathlib.Path, Tuple, Dict, Callable) -> None
## @complexity 5
def test_binary_file_is_info_not_scanned(run_cli, repo_copy, deny_list, canary_values, find_rows):
    address = canary_values["email"].encode("ascii")
    (repo_copy / "notes").mkdir()
    (repo_copy / "notes" / "blob.bin").write_bytes(b"\x00\x01 " + address + b" \x02")
    (repo_copy / "notes" / "latin.txt").write_bytes(b"\xff\xfe caf\xe9 " + address + b"\n")
    code, out, err = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    report = json.loads(out)
    infos = find_rows(report, "scan.binary", "INFO")
    print("[IMP:9][test_binary_info][RESULT] exit=%d info_rows=%d" % (code, len(infos)))
    assert code == 0
    assert sorted(row["subject"] for row in infos) == ["notes/blob.bin", "notes/latin.txt"]
    assert all(row["detail"] == "not scanned: binary or not UTF-8" for row in infos)
    assert not find_rows(report, "scan.email", "FAIL")
    assert report["summary"]["population"]["binary-files"] == 2
# endregion FUNC_test_binary_file_is_info_not_scanned


# region FUNC_test_fingerprint_shape [DOMAIN(8): Privacy; CONCEPT(9): Fingerprint, Shape; TECH(5): re, hashlib]
## @purpose Prove that every scan finding carries a fingerprint of the form length:eight-hex, and that for an address and a
## deny word (whose match is the whole value) it is exactly the length and the first eight hex digits of the SHA-256.
## @uses run_cli, repo_copy, deny_list, canary_values, plant_canary
## @io (Callable, pathlib.Path, Tuple, Dict, Callable) -> None
## @complexity 4
def test_fingerprint_shape(run_cli, repo_copy, deny_list, canary_values, plant_canary):
    for kind, _rule in CANARY_RULES:
        plant_canary(repo_copy, "notes/fp-" + kind + ".txt", canary_values[kind])
    code, out, err = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    report = json.loads(out)
    by_subject = {row["subject"]: row["detail"] for row in report["rows"] if row["status"] == "FAIL"}
    print("[IMP:9][test_fingerprint_shape][RESULT] exit=%d findings=%d" % (code, len(by_subject)))
    assert len(by_subject) == 5
    for detail in by_subject.values():
        assert re.match(r"^line 3 fp=\d+:[0-9a-f]{8}$", detail)
    address = canary_values["email"]
    assert by_subject["notes/fp-email.txt"] == "line 3 fp=%d:%s" % (len(address), hashlib.sha256(address.encode()).hexdigest()[:8])
    word = deny_list[1]
    assert by_subject["notes/fp-deny-token.txt"] == "line 3 fp=%d:%s" % (len(word), hashlib.sha256(word.lower().encode()).hexdigest()[:8])
# endregion FUNC_test_fingerprint_shape


# region FUNC_test_scanner_source_does_not_match_itself [DOMAIN(9): Privacy; CONCEPT(10): SelfScan, Fragments; TECH(6): shutil.copytree, conformlib.scan]
## @purpose Prove that a copy holding only the tool's own folder has no scan finding: the scanner's patterns and canaries are
## built from fragments, so its source does not match its own rules.
## @uses shutil.copytree, conformlib.scan.scan_tree, repo_root, deny_list
## @io (pathlib.Path, pathlib.Path, Tuple) -> None
## @complexity 4
def test_scanner_source_does_not_match_itself(repo_root, tmp_path, deny_list):
    only_tools = tmp_path / "only-tools"
    shutil.copytree(str(repo_root / "tools"), str(only_tools / "tools"), ignore=shutil.ignore_patterns("__pycache__"))
    report = Report("self")
    scan.scan_tree(str(only_tools), [deny_list[1]], scan.build_patterns(), report)
    fails = [row for row in report.rows if row.status == "FAIL"]
    print("[IMP:9][test_scanner_self_scan][RESULT] rows=%d fails=%d" % (len(report.rows), len(fails)))
    assert not fails
    assert [row.rule for row in report.rows if row.status == "PASS"] == SCAN_RULES
# endregion FUNC_test_scanner_source_does_not_match_itself


# region FUNC_test_repository_tool_tests_and_fixtures_pass_the_scan [DOMAIN(9): Publication; CONCEPT(10): WholeRepository, SelfScan; TECH(5): run_cli]
## @purpose Prove that the whole copy of the repository, its tool, its tests and its fixtures included, passes the four scan
## rules with a synthetic deny list: no finding, four PASS rows.
## @uses run_cli, repo_copy, deny_list, find_rows
## @io (Callable, pathlib.Path, Tuple, Callable) -> None
## @complexity 3
def test_repository_tool_tests_and_fixtures_pass_the_scan(run_cli, repo_copy, deny_list, find_rows):
    code, out, err = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    report = json.loads(out)
    scan_fails = [row for row in report["rows"] if row["status"] == "FAIL" and row["rule"].startswith("scan.")]
    print("[IMP:9][test_repository_scan][RESULT] exit=%d scan_fails=%d" % (code, len(scan_fails)))
    assert not scan_fails
    for rule in SCAN_RULES:
        assert len(find_rows(report, rule, "PASS")) == 1
# endregion FUNC_test_repository_tool_tests_and_fixtures_pass_the_scan


# region FUNC_test_drill_rules_constant_matches_the_table [DOMAIN(6): Drills; CONCEPT(7): FailureClass, Constant; TECH(4): set]
## @purpose Prove that the DRILL_RULES constant of this module, read by the failure-class map, is the set of rules the drills
## of this module produce: the four scan rules and the binary information rule.
## @io None -> None
## @complexity 1
def test_drill_rules_constant_matches_the_table():
    covered = {rule for _kind, rule in CANARY_RULES} | {"scan.binary"}
    print("[IMP:9][test_scan_drill_rules][COUNT] rules=%d" % len(covered))
    assert set(DRILL_RULES) == covered
    assert list(DRILL_RULES) == sorted(DRILL_RULES)
# endregion FUNC_test_drill_rules_constant_matches_the_table


# region FUNC__publication_process [DOMAIN(9): Publication; CONCEPT(9): RealStreams; TECH(6): subprocess]
## @purpose Deliver the real launcher report and DEBUG trajectory from an isolated copy.
## @uses subprocess.run
## @io (Path, Path, Path, bool) -> CompletedProcess
## @complexity 2
def _publication_process(repo_root, copy, deny, as_json=True):
    argv = [str(repo_root / "bin" / "conform"), "self", "--root", str(copy),
            "--deny-list", str(deny), "--log-level", "DEBUG"]
    return subprocess.run(argv + (["--json"] if as_json else []), cwd=str(copy.parent),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# endregion FUNC__publication_process


# region FUNC__permission_sequence [DOMAIN(10): Publication; CONCEPT(10): Coverage, Refusal; TECH(7): chmod, subprocess]
## @purpose Discriminate readable, denied and restored coverage, with a direct read or scandir failure.
## @uses _publication_process
## @io (Path, Path, Tuple, bool) -> None
## @complexity 6
def _permission_sequence(repo_root, copy, deny_list, directory):
    folder = copy / "probe-data"
    folder.mkdir()
    target = folder / "payload.txt"
    target.write_text(deny_list[1], encoding="utf-8")
    guarded = folder if directory else target
    mode = guarded.stat().st_mode
    before = _publication_process(repo_root, copy, deny_list[0])
    try:
        guarded.chmod(0)
        operation = "list(os.scandir(sys.argv[1]))" if directory else "open(sys.argv[1], 'rb').read()"
        probe = subprocess.run([sys.executable, "-c", "import os,sys; " + operation, str(guarded)],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        denied = _publication_process(repo_root, copy, deny_list[0])
    finally:
        guarded.chmod(mode)
    restored = _publication_process(repo_root, copy, deny_list[0])
    print("[IMP:9][permission_sequence][RESULT] directory=%s exits=%s direct=%d permission=%s" %
          (directory, [before.returncode, denied.returncode, restored.returncode], probe.returncode,
           "PermissionError" in probe.stderr))
    assert probe.returncode != 0 and "PermissionError" in probe.stderr, "host must actually deny the operation"
    assert [before.returncode, denied.returncode, restored.returncode] == [1, 2, 1]
    report = json.loads(denied.stdout)
    assert len(report["rows"]) == 1
    assert report["rows"][0]["status"] == "NOT RUN"
    assert report["rows"][0]["rule"] == "input.root"
    assert report["summary"]["population"] == {} and report["summary"]["probes"] == []
    assert "scan.binary" not in denied.stdout
    assert "[iter_text_files][REFUSAL]" in denied.stderr
    for result in (before, denied, restored):
        assert deny_list[1] not in result.stdout + result.stderr
# endregion FUNC__permission_sequence


# region FUNC_test_publication_file_read_failure_real_process [DOMAIN(10): Publication; CONCEPT(10): Coverage; TECH(7): subprocess]
## @purpose An unreadable non-Markdown UTF8 file refuses judgment rather than becoming binary.
## @uses _permission_sequence
## @io (Path, Path, Tuple) -> None
## @complexity 2
def test_publication_file_read_failure_real_process(repo_root, repo_copy, deny_list):
    _permission_sequence(repo_root, repo_copy, deny_list, False)
# endregion FUNC_test_publication_file_read_failure_real_process


# region FUNC_test_publication_directory_walk_failure_real_process [DOMAIN(10): Publication; CONCEPT(10): Coverage; TECH(7): subprocess]
## @purpose A denied directory traversal refuses judgment and restoration restores detection.
## @uses _permission_sequence
## @io (Path, Path, Tuple) -> None
## @complexity 2
def test_publication_directory_walk_failure_real_process(repo_root, repo_copy, deny_list):
    _permission_sequence(repo_root, repo_copy, deny_list, True)
# endregion FUNC_test_publication_directory_walk_failure_real_process


# region FUNC_test_private_format_diagnostic_real_process [DOMAIN(10): Privacy; CONCEPT(10): SharedBoundary, Diagnostics; TECH(7): subprocess]
## @purpose Format diagnostics, early refusals and parser path logs retain useful context without private values.
## @uses _publication_process
## @io (str, Path, Path, Tuple, Callable) -> None
## @complexity 7
@pytest.mark.parametrize("kind,rule", [("call", "call.resolves"), ("card", "card.keys"),
    ("registry", "registry.unique"), ("norm", "norm.unique"), ("path", "call.resolves"),
    ("refusal", "input.root")])
def test_private_format_diagnostic_real_process(kind, rule, repo_root, repo_copy, deny_list, parse_table):
    token = deny_list[1]
    if kind == "norm":
        token = "ZQ" + "".join(chr(65 + int(c, 16)) for c in token[2:]) + "-9001"
        deny_list[0].write_text(token + "\n", encoding="utf-8")
    target = repo_copy / "concepts" / "glossary.md"
    text = target.read_text(encoding="utf-8")
    if kind == "card":
        text = text.replace("---\n", "---\n" + token + ": extra\n", 1)
    elif kind == "registry":
        target = repo_copy / "runtime" / "capabilities.md"
        text = target.read_text(encoding="utf-8") + ("\n- **cap:" + token + "**: synthetic meaning\n") * 2
    elif kind == "norm":
        text += ("\n- **" + token + "** MUST: synthetic requirement.\n") * 2
    else:
        text += "\n{{cap:" + token + "}}\n"
    target.write_text(text, encoding="utf-8")
    if kind in ("path", "refusal"):
        moved = target.with_name(token + ".md")
        target.rename(moved)
        target = moved
    mode = target.stat().st_mode
    try:
        if kind == "refusal":
            target.chmod(0)
        table = _publication_process(repo_root, repo_copy, deny_list[0], False)
        result = _publication_process(repo_root, repo_copy, deny_list[0])
    finally:
        target.chmod(mode)
    report = json.loads(result.stdout)
    rows, summary = parse_table(table.stdout)
    hits = [r for r in report["rows"] if r["rule"] == rule and r["status"] in ("FAIL", "NOT RUN")]
    print("[IMP:9][private_format_diagnostic][RESULT] kind=%s exits=%d/%d hits=%d" %
          (kind, table.returncode, result.returncode, len(hits)))
    assert table.returncode == result.returncode == (2 if kind == "refusal" else 1)
    assert hits
    assert rows == report["rows"] and summary == report["summary"]["line"]
    if kind != "refusal":
        assert any(r["rule"] == "scan.deny-token" and "line " in r["detail"] and "fp=" in r["detail"] for r in rows)
        assert "fp=" in json.dumps(hits)
    for output in (table.stdout, table.stderr, result.stdout, result.stderr):
        assert token.lower() not in output.lower()
    assert "[parse_markdown][READ]" in result.stderr or kind == "refusal"
# endregion FUNC_test_private_format_diagnostic_real_process


# region FUNC_test_publication_scan_exclusions_remain_supported [DOMAIN(8): Publication; CONCEPT(9): Exclusion; TECH(5): pathlib]
## @purpose Deliberately excluded files, directories and symlinks never become read refusals or findings.
## @uses conformlib.scan.iter_text_files
## @io (Path, Tuple) -> None
## @complexity 4
def test_publication_scan_exclusions_remain_supported(tmp_path, deny_list):
    root = tmp_path / "scan-only"
    root.mkdir()
    locked = []
    try:
        for name in scan.SKIPPED_DIRS:
            folder = root / name
            folder.mkdir()
            (folder / "payload.txt").write_text(deny_list[1], encoding="utf-8")
            folder.chmod(0)
            locked.append(folder)
        (root / ".DS_Store").write_text(deny_list[1], encoding="utf-8")
        (root / "file-link").symlink_to(deny_list[0])
        (root / "dir-link").symlink_to(root / scan.SKIPPED_DIRS[0], target_is_directory=True)
        files = list(scan.iter_text_files(str(root)))
    finally:
        for folder in locked:
            folder.chmod(0o700)
    print("[IMP:9][scan_exclusions][RESULT] files=%d" % len(files))
    assert files == []
# endregion FUNC_test_publication_scan_exclusions_remain_supported


# region FUNC_test_worktree_git_metadata_excluded_but_ordinary_file_scanned [DOMAIN(9): Publication; CONCEPT(10): Metadata, NegativeControl; TECH(6): pytest, pathlib, json]
## @purpose Exclude Git directory/pointer metadata while proving the same forbidden payload in an ordinary file still fails.
## @uses run_cli, repo_copy, deny_list
## @io fixtures -> assertions
## @complexity 5
@pytest.mark.parametrize("metadata_kind", ["pointer", "directory"])
def test_worktree_git_metadata_excluded_but_ordinary_file_scanned(metadata_kind, run_cli, repo_copy, deny_list):
    payload = "gitdir: " + str(repo_copy.parent / deny_list[1])
    metadata = repo_copy / ".git"
    if metadata_kind == "pointer":
        metadata.write_text(payload, encoding="utf-8")
    else:
        metadata.mkdir()
        (metadata / "pointer").write_text(payload, encoding="utf-8")
    argv = ["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json", "--log-level", "INFO"]
    code, out, err = run_cli(argv)
    print("[IMP:9][worktree_metadata][CLEAN] kind=%s exit=%d" % (metadata_kind, code))
    assert code == 0
    assert deny_list[1] not in out + err
    if metadata_kind == "pointer":
        assert "[iter_text_files][SKIP_METADATA] git_pointer=1" in err
    visible = repo_copy / "ordinary.txt"
    visible.write_text(payload, encoding="utf-8")
    code, out, err = run_cli(argv)
    hits = [row for row in json.loads(out)["rows"] if row["status"] == "FAIL"]
    print("[IMP:9][worktree_metadata][NEGATIVE] kind=%s exit=%d hits=%d" % (metadata_kind, code, len(hits)))
    assert code == 1
    assert any(row["rule"] == "scan.deny-token" and row["subject"] == "ordinary.txt" for row in hits)
    assert all(not row["subject"].startswith(".git") for row in hits)
    assert deny_list[1] not in out + err
    visible.unlink()
    code, out, err = run_cli(argv)
    print("[IMP:9][worktree_metadata][RESTORED] kind=%s exit=%d" % (metadata_kind, code))
    assert code == 0
# endregion FUNC_test_worktree_git_metadata_excluded_but_ordinary_file_scanned


# region FUNC_test_package_publication_channels [DOMAIN(10): Publication; CONCEPT(10): NativeCoverage, RealDelivery, Restoration; TECH(7): pytest, subprocess]
## @purpose Prove all five existing privacy canaries bite in every real native package carrier family through the unchanged shipped scanner and real CLI.
## @uses test_scan._publication_process, test_scan._forms, pathlib.Path.read_bytes, pathlib.Path.write_bytes, pathlib.Path.chmod, json.loads
## @io Input: canonical repo_root, owned complete repo_copy, actual deny/canary fixtures and one existing native relative path.
##   Output: None after each exact scan-rule/location/fingerprint/stream refusal and full original bytes/numeric modes restored.
##   Side effects: real child stdout/stderr and only owned target file mutation/restoration. Guarantees: original source and protected sibling unchanged; no publication omission or scanner override.
##   Raises: AssertionError for wrong rule/exit/disclosure/restoration; OSError/ValueError for owned read/write/process/report failure. System importance:10 for complete public native coverage.
##   Example: a canary in actual native JSON fails privacy even though that JSON is outside neutral Markdown classification.
## @complexity 6
@pytest.mark.parametrize("relative", [
    "README.md", ".codex-plugin/plugin.json",
    "skills/feature-dev/scripts/run_state.py", "Doxyfile",
    "tests/test_guide.md", "pytest.ini",
])
def test_package_publication_channels(relative, repo_root, repo_copy, deny_list, canary_values):
    try:
        # START_BLOCK_Validation
        target = repo_copy / "implementations/codex" / relative
        sibling = repo_copy / "runtime/adapter.schema.json"
        original, mode = target.read_bytes(), target.stat().st_mode & 0o777
        sibling_bytes, sibling_mode = sibling.read_bytes(), sibling.stat().st_mode & 0o777
        baseline = _publication_process(repo_root, repo_copy, deny_list[0])
        print("[IMP:9][test_package_publication_channels][VALIDATION_SUCCESS] carrier=%s exit=%d" % (relative, baseline.returncode))
        assert baseline.returncode == 0
        # END_BLOCK_Validation
        # START_BLOCK_BusinessLogic
        for kind, rule in CANARY_RULES:
            value = canary_values[kind]
            try:
                target.write_bytes(original + b"\n" + value.encode("utf-8") + b"\n")
                result = _publication_process(repo_root, repo_copy, deny_list[0])
                report = json.loads(result.stdout)
                fails = [r for r in report["rows"] if r["status"] == "FAIL"]
                print("[IMP:9][test_package_publication_channels][REFUSAL] carrier=%s kind=%s exit=%d failures=%d" % (relative, kind, result.returncode, len(fails)))
                assert result.returncode == 1 and len(fails) == 1
                assert fails[0]["rule"] == rule and fails[0]["subject"] == "implementations/codex/" + relative
                assert FP_DETAIL_RE.match(fails[0]["detail"])
                for other in SCAN_RULES:
                    if other != rule:
                        assert any(r["rule"] == other and r["status"] == "PASS" for r in report["rows"])
                assert result.stderr and "[scan_tree][FINDING]" in result.stderr
                for form in _forms(value):
                    assert form not in result.stdout and form not in result.stderr and form not in json.dumps(report)
                assert sibling.read_bytes() == sibling_bytes and sibling.stat().st_mode & 0o777 == sibling_mode
            finally:
                target.write_bytes(original)
                target.chmod(mode)
            assert target.read_bytes() == original and target.stat().st_mode & 0o777 == mode
        restored = _publication_process(repo_root, repo_copy, deny_list[0])
        print("[IMP:9][test_package_publication_channels][RESULT] carrier=%s restored_exit=%d" % (relative, restored.returncode))
        assert restored.returncode == 0
        assert target.read_bytes() == original and target.stat().st_mode & 0o777 == mode
        # END_BLOCK_BusinessLogic
    # START_BLOCK_ErrorHandling
    except (OSError, UnicodeError, ValueError, subprocess.SubprocessError, AssertionError) as error:
        print("[IMP:10][test_package_publication_channels][FAILURE] kind=%s" % type(error).__name__)
        raise
    # END_BLOCK_ErrorHandling
# endregion FUNC_test_package_publication_channels
