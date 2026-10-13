# region MODULE_CONTRACT [DOMAIN(9): CommandLine, Launcher; CONCEPT(9): Streams, LDD, AnyDirectory; TECH(6): pytest, subprocess, os]
## @modulecontract
## @purpose To prove the command as a person or a script meets it: the launcher runs from any directory and through a symbolic
## link with the same result as the frontend, the report goes to standard output and the trace to standard error only when
## asked, every trace line has the Log Driven Development form at the level chosen, and the repository passes its own check.
## @scope The launcher bin/conform, the frontend tools/conform.py as real processes, in the self mode and the adapter mode, the
## trace format and levels, the help and the usage refusal.
## @input The repository, copies of it, a synthetic deny list, real interpreter processes.
## @output One pass or fail per property of the command line.
## @links [USES_API(9): subprocess; USES_API(7): conform.main through run_cli; READS_DATA_FROM(6): bin/conform]
## @links_to_spec AC-8, AC-9, AC-10, AC-11, AC-P3
## @invariants
## - The subprocess tests do not set PYTHONPATH: the launcher must find the tools by itself.
## - The real repository is only read; every mutation happens in a copy.
## @rationale
## Q: Why real processes for the launcher when the frontend can be called in process?
## A: The launcher's value is its behaviour outside pytest: the working directory, the link, the environment; in process none
## of these is real.
## @changes
## LAST_CHANGE: [v0.1.0 - Initial creation: launcher, link, streams, trace format, levels, help, usage, self-check.]
## @modulemap
## FUNC 3[The launcher path of the repository under test] => _launcher
## FUNC 6[Run a command as a real process with both streams piped] => _run
## FUNC 5[The launcher is an executable script] => test_bin_conform_is_executable
## FUNC 8[The launcher from another directory equals the frontend] => test_bin_conform_from_other_directory_matches_tools_conform
## FUNC 8[The launcher in the adapter mode equals the frontend] => test_bin_conform_adapter_matches_tools_conform
## FUNC 7[The launcher through a link equals the direct run] => test_bin_conform_through_symlink_matches
## FUNC 8[The trace reaches standard error only with the option] => test_logs_reach_stderr_only_with_log_level
## FUNC 8[Every trace line has the LDD form at its level] => test_stderr_lines_follow_ldd_format
## FUNC 6[The trajectory holds the verdict lines] => test_in_process_trajectory_has_verdict
## FUNC 6[The help exits 0] => test_help_prints_the_summary_and_exits_0
## FUNC 7[A wrong argument is a refusal on standard output] => test_real_process_usage_refusal_is_exit_2_on_stdout
## FUNC 9[The repository passes its own check] => test_repository_passes_itself_with_a_synthetic_deny_list
## @usecases
## - [test_bin_conform_through_symlink_matches]: Harness -> links bin/conform into its own bin -> the same verdict as the repository's
## - [test_logs_reach_stderr_only_with_log_level]: Script -> pipes stdout to a parser -> the JSON is clean whatever the trace level
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: conform command line tests, bin/conform launcher, executable, other directory, symlink, stderr trace, --log-level, LDD line format, help, usage refusal, self-check exit 0
# STRUCTURE: ▶ real process ┌launcher, frontend┐ → ⊕ cwd elsewhere ∨ symlink → ◇ same stdout ∧ same exit → ⚡ --log-level ∈ {none, ERROR, INFO, DEBUG} → ∑ stderr lines ~ LDD regex → ⎋ assert

import json
import os
import pathlib
import re
import stat
import subprocess
import sys
from typing import List

import pytest

LDD_LINE_RE = re.compile(r"^\[IMP:(\d{1,2})\]\[[A-Za-z_]+\]\[[A-Z_]+\] ")


# region FUNC__launcher [DOMAIN(7): CommandLine; CONCEPT(8): Launcher; TECH(4): pathlib]
## @purpose The path of the launcher of the repository under test.
## @io pathlib.Path -> pathlib.Path
## @complexity 1
def _launcher(repo_root: pathlib.Path) -> pathlib.Path:
    return repo_root / "bin" / "conform"
# endregion FUNC__launcher


# region FUNC__run [DOMAIN(8): CommandLine; CONCEPT(9): RealProcess; TECH(5): subprocess.run]
## @purpose Run a command as a real process with pipes for both streams, in a working directory, and return the result.
## @uses subprocess.run
## @io (List[str], pathlib.Path) -> subprocess.CompletedProcess
## @complexity 2
def _run(command: List[str], cwd: pathlib.Path) -> "subprocess.CompletedProcess":
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, cwd=str(cwd))
# endregion FUNC__run


# region FUNC_test_bin_conform_is_executable [DOMAIN(7): Launcher; CONCEPT(8): Executable, Shebang; TECH(4): os.stat]
## @purpose Prove that the launcher has an execute bit for its owner and begins with an interpreter line, since it has no
## extension for a tool to guess its language from.
## @io pathlib.Path -> None
## @complexity 2
def test_bin_conform_is_executable(repo_root):
    launcher = _launcher(repo_root)
    mode = os.stat(str(launcher)).st_mode
    first = launcher.read_text(encoding="utf-8").split("\n")[0]
    print("[IMP:9][test_bin_conform_executable][RESULT] mode=%s first=%s" % (oct(mode & 0o777), first))
    assert mode & stat.S_IXUSR
    assert os.access(str(launcher), os.X_OK)
    assert first.startswith("#!") and "python3" in first
# endregion FUNC_test_bin_conform_is_executable


# region FUNC_test_bin_conform_from_other_directory_matches_tools_conform [DOMAIN(9): Launcher; CONCEPT(10): AnyDirectory, SameResult; TECH(6): subprocess]
## @purpose Prove that the launcher, started from a directory that is not the repository and with no module path set, gives the
## same exit code and the same standard output as the frontend run directly, in the table form and in the JSON form.
## @uses subprocess, repo_root, repo_copy, deny_list, tmp_path
## @io (str, pathlib.Path, pathlib.Path, Tuple, pathlib.Path) -> None
## @complexity 4
@pytest.mark.parametrize("form", ["table", "json"])
def test_bin_conform_from_other_directory_matches_tools_conform(form, repo_root, repo_copy, deny_list, tmp_path):
    other = tmp_path / "elsewhere"
    other.mkdir()
    argv = ["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0])] + (["--json"] if form == "json" else [])
    launched = _run([str(_launcher(repo_root))] + argv, other)
    direct = _run([sys.executable, str(repo_root / "tools" / "conform.py")] + argv, other)
    print("[IMP:9][test_bin_conform_other_dir][RESULT] form=%s exit=%d/%d chars=%d" % (form, launched.returncode, direct.returncode, len(launched.stdout)))
    assert launched.returncode == direct.returncode == 0
    assert launched.stdout == direct.stdout
    assert launched.stderr == "" and direct.stderr == ""
    if form == "table":
        assert launched.stdout.count("SUMMARY  mode=self  exit=0") == 1
    else:
        assert json.loads(launched.stdout)["exit"] == 0
# endregion FUNC_test_bin_conform_from_other_directory_matches_tools_conform


# region FUNC_test_bin_conform_adapter_matches_tools_conform [DOMAIN(9): Launcher; CONCEPT(10): AdapterMode, AnyDirectory, SameResult; TECH(6): subprocess]
## @purpose Prove that the launcher in the adapter mode, started from a directory that is neither the repository nor the
## harness and with no module path set, gives the same exit code and the same standard output as the frontend run directly,
## in both forms, for a passing harness and for a failing one (a file with no entry); the spec root is found from the adapter
## file and not from the working directory.
## @uses subprocess, repo_root, harness_copy, tmp_path
## @io (str, str, pathlib.Path, HarnessCopy, pathlib.Path) -> None
## @complexity 5
@pytest.mark.parametrize("form", ["table", "json"])
@pytest.mark.parametrize("case,expected", [("control", 0), ("fail", 1)])
def test_bin_conform_adapter_matches_tools_conform(form, case, expected, repo_root, harness_copy, tmp_path):
    other = tmp_path / "elsewhere"
    other.mkdir()
    target = harness_copy.adapter
    if case == "fail":
        data = json.loads(target.read_text(encoding="utf-8"))
        data["files"].pop("roles/qa.md")
        target.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    argv = ["adapter", str(target)] + (["--json"] if form == "json" else [])
    launched = _run([str(_launcher(repo_root))] + argv, other)
    direct = _run([sys.executable, str(repo_root / "tools" / "conform.py")] + argv, other)
    print("[IMP:9][test_bin_conform_adapter][RESULT] case=%s form=%s exit=%d/%d chars=%d" % (case, form, launched.returncode, direct.returncode, len(launched.stdout)))
    assert launched.returncode == direct.returncode == expected
    assert launched.stdout == direct.stdout
    assert launched.stderr == "" and direct.stderr == ""
    if form == "table":
        assert launched.stdout.count("SUMMARY  mode=adapter  exit=%d" % expected) == 1
    else:
        assert json.loads(launched.stdout)["exit"] == expected
# endregion FUNC_test_bin_conform_adapter_matches_tools_conform


# region FUNC_test_bin_conform_through_symlink_matches [DOMAIN(8): Launcher; CONCEPT(9): Symlink, RealPath; TECH(5): os.symlink]
## @purpose Prove that the launcher reached through a symbolic link in another directory resolves the repository from the real
## file: with no root argument it checks the repository that holds it and gives the same output as the direct launch.
## @uses os.symlink, subprocess, repo_root, deny_list, tmp_path
## @io (pathlib.Path, Tuple, pathlib.Path) -> None
## @complexity 4
def test_bin_conform_through_symlink_matches(repo_root, deny_list, tmp_path):
    bin_dir = tmp_path / "harness-bin"
    bin_dir.mkdir()
    link = bin_dir / "conform"
    os.symlink(str(_launcher(repo_root)), str(link))
    argv = ["self", "--deny-list", str(deny_list[0]), "--json"]
    linked = _run([str(link)] + argv, tmp_path)
    direct = _run([str(_launcher(repo_root))] + argv, tmp_path)
    print("[IMP:9][test_bin_conform_symlink][RESULT] exit=%d/%d equal=%s" % (linked.returncode, direct.returncode, linked.stdout == direct.stdout))
    assert linked.returncode == direct.returncode == 0
    assert linked.stdout == direct.stdout
    assert json.loads(linked.stdout)["summary"]["population"]["neutral-files"] == 71
# endregion FUNC_test_bin_conform_through_symlink_matches


# region FUNC_test_logs_reach_stderr_only_with_log_level [DOMAIN(9): CommandLine; CONCEPT(10): Streams, LogLevel; TECH(6): subprocess, json]
## @purpose Prove with real processes that without the option nothing reaches standard error, that with it the trace does and
## the JSON on standard output stays byte for byte the same and parseable, that the level name is case-insensitive, and that
## the ERROR level stays silent on a clean run but speaks on a refusal.
## @uses subprocess, repo_root, repo_copy, deny_list, tmp_path
## @io (pathlib.Path, pathlib.Path, Tuple, pathlib.Path) -> None
## @complexity 6
def test_logs_reach_stderr_only_with_log_level(repo_root, repo_copy, deny_list, tmp_path):
    base = [str(_launcher(repo_root)), "self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"]
    quiet = _run(base, tmp_path)
    loud = _run(base + ["--log-level", "debug"], tmp_path)
    error_only = _run(base + ["--log-level", "ERROR"], tmp_path)
    refusal = _run([str(_launcher(repo_root)), "self", "--root", str(tmp_path / "nowhere"), "--deny-list", str(deny_list[0]),
                    "--json", "--log-level", "ERROR"], tmp_path)
    print("[IMP:9][test_logs_reach_stderr][RESULT] quiet=%d loud=%d error_only=%d refusal=%d"
          % (len(quiet.stderr), len(loud.stderr), len(error_only.stderr), len(refusal.stderr)))
    assert quiet.returncode == loud.returncode == error_only.returncode == 0
    assert quiet.stderr == ""
    assert loud.stderr != ""
    assert loud.stdout == quiet.stdout
    assert json.loads(loud.stdout)["exit"] == 0
    assert error_only.stderr == ""
    assert refusal.returncode == 2
    assert refusal.stderr != ""
    assert all(LDD_LINE_RE.match(line) and line.startswith("[IMP:10]") for line in refusal.stderr.strip().split("\n"))
# endregion FUNC_test_logs_reach_stderr_only_with_log_level


# region FUNC_test_stderr_lines_follow_ldd_format [DOMAIN(9): CommandLine; CONCEPT(10): LDD, Levels; TECH(5): re, run_cli]
## @purpose Prove that every line of the trace has the form [IMP:n][FUNCTION][BLOCK] with n from 1 to 10, that DEBUG shows
## importance 1 and up, INFO only 4 and up, ERROR only 10, and that DEBUG holds more lines than INFO.
## @uses run_cli, repo_copy, deny_list
## @io (Callable, pathlib.Path, Tuple) -> None
## @complexity 5
def test_stderr_lines_follow_ldd_format(run_cli, repo_copy, deny_list):
    seen = {}
    for level, floor in (("DEBUG", 1), ("INFO", 4), ("ERROR", 10)):
        code, out, err = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json", "--log-level", level])
        lines = [line for line in err.split("\n") if line]
        importances = []
        for line in lines:
            found = LDD_LINE_RE.match(line)
            assert found, "not an LDD line: " + line
            importances.append(int(found.group(1)))
        seen[level] = importances
        print("[IMP:9][test_stderr_lines_ldd][RESULT] level=%s exit=%d lines=%d min=%s" % (level, code, len(lines), min(importances) if importances else "-"))
        assert code == 0
        assert all(floor <= number <= 10 for number in importances)
    assert seen["ERROR"] == []
    assert len(seen["DEBUG"]) > len(seen["INFO"]) > 0
    assert any(number <= 3 for number in seen["DEBUG"])
    assert not any(number <= 3 for number in seen["INFO"])
# endregion FUNC_test_stderr_lines_follow_ldd_format


# region FUNC_test_in_process_trajectory_has_verdict [DOMAIN(8): CommandLine; CONCEPT(9): Trajectory, Verdict; TECH(5): caplog]
## @purpose Prove that a run's trajectory at importance 7 and above holds the boundary reads, the canary probe result, the
## verdict with its exit code and the exit line, so a failing run can be followed from its log alone.
## @uses run_cli, repo_copy, deny_list, ldd_trajectory
## @io (Callable, pathlib.Path, Tuple, Callable) -> None
## @complexity 4
def test_in_process_trajectory_has_verdict(run_cli, repo_copy, deny_list, ldd_trajectory):
    code, out, err = run_cli(["self", "--root", str(repo_copy), "--deny-list", str(deny_list[0]), "--json"])
    lines = ldd_trajectory()
    print("[IMP:9][test_in_process_trajectory][RESULT] exit=%d trajectory=%d" % (code, len(lines)))
    assert code == 0
    assert err == "", "the trace must not reach standard error without the option"
    assert any("[canary_probe][BITE]" in line and "ok=True" in line for line in lines)
    assert any("[run_self][VERDICT] exit=0" in line for line in lines)
    assert any("[main][EXIT] exit=0" in line for line in lines)
    assert any(line.startswith("[IMP:7]") for line in lines)
# endregion FUNC_test_in_process_trajectory_has_verdict


# region FUNC_test_help_prints_the_summary_and_exits_0 [DOMAIN(6): CommandLine; CONCEPT(7): Help; TECH(5): subprocess]
## @purpose Prove that the help option prints the argument summary on standard output and exits 0, as the tool's page says.
## @uses subprocess, repo_root, tmp_path
## @io (pathlib.Path, pathlib.Path) -> None
## @complexity 2
def test_help_prints_the_summary_and_exits_0(repo_root, tmp_path):
    done = _run([str(_launcher(repo_root)), "--help"], tmp_path)
    print("[IMP:9][test_help][RESULT] exit=%d chars=%d" % (done.returncode, len(done.stdout)))
    assert done.returncode == 0
    assert done.stdout.startswith("usage: conform")
    assert "--deny-list" in _run([str(_launcher(repo_root)), "self", "--help"], tmp_path).stdout
# endregion FUNC_test_help_prints_the_summary_and_exits_0


# region FUNC_test_real_process_usage_refusal_is_exit_2_on_stdout [DOMAIN(8): CommandLine; CONCEPT(9): Usage, Refusal; TECH(5): subprocess]
## @purpose Prove with a real process that a wrong argument and a missing subcommand are refusals, not crashes: exit 2, the one
## NOT RUN input.usage row on standard output, nothing on standard error, no traceback.
## @uses subprocess, repo_root, tmp_path
## @io (pathlib.Path, pathlib.Path) -> None
## @complexity 3
def test_real_process_usage_refusal_is_exit_2_on_stdout(repo_root, tmp_path):
    for argv in (["self", "--bogus"], []):
        done = _run([str(_launcher(repo_root))] + argv, tmp_path)
        print("[IMP:9][test_real_usage_refusal][RESULT] argv=%s exit=%d" % (argv, done.returncode))
        assert done.returncode == 2
        assert done.stdout.startswith("NOT RUN  input.usage  argv  ")
        assert done.stdout.count("\n") == 2
        assert done.stderr == ""
# endregion FUNC_test_real_process_usage_refusal_is_exit_2_on_stdout


# region FUNC_test_repository_passes_itself_with_a_synthetic_deny_list [DOMAIN(10): Publication; CONCEPT(10): SelfCheck, Repository; TECH(6): subprocess, json]
## @purpose Prove that the real repository, checked through the launcher with no root argument and a synthetic deny list, gives
## exit 0 and no FAIL, so a change that breaks the format or plants a private-looking value cannot go unnoticed.
## @uses subprocess, repo_root, deny_list, tmp_path
## @io (pathlib.Path, Tuple, pathlib.Path) -> None
## @complexity 3
def test_repository_passes_itself_with_a_synthetic_deny_list(repo_root, deny_list, tmp_path):
    done = _run([str(_launcher(repo_root)), "self", "--deny-list", str(deny_list[0]), "--json"], tmp_path)
    report = json.loads(done.stdout)
    fails = [row for row in report["rows"] if row["status"] == "FAIL"]
    print("[IMP:9][test_repository_passes_itself][RESULT] exit=%d fails=%d counts=%s" % (done.returncode, len(fails), report["summary"]["counts"]))
    assert done.returncode == 0
    assert not fails
    assert report["summary"]["counts"]["warn"] == 0
    assert done.stderr == ""
# endregion FUNC_test_repository_passes_itself_with_a_synthetic_deny_list


# region FUNC_test_self_privacy_guard_restores_logging [DOMAIN(10): Privacy; CONCEPT(10): Lifecycle, IndependentCalls; TECH(7): logging]
## @purpose Direct backend calls protect ancestor sinks before parsing and restore filters after success, refusal and crashes.
## @uses conformlib.run_self
## @io (Path, Tuple, Path, caplog, monkeypatch) -> None
## @complexity 7
def test_self_privacy_guard_restores_logging(repo_copy, deny_list, tmp_path, caplog, monkeypatch):
    import logging
    import conformlib
    token = deny_list[1]
    original_load = conformlib.load_deny_list
    reads = []
    def count_load(path):
        reads.append(path)
        return original_load(path)
    monkeypatch.setattr(conformlib, "load_deny_list", count_load)
    original_parse = conformlib.load_neutral_tree
    def parse_with_unrelated_log(root):
        logging.getLogger("other.application").warning("unrelated %s", token)
        return original_parse(root)
    monkeypatch.setattr(conformlib, "load_neutral_tree", parse_with_unrelated_log)
    def conform_trace():
        return "\n".join(r.getMessage() for r in caplog.records if r.name.startswith("conform"))
    target = repo_copy / "concepts" / "glossary.md"
    target.write_text(target.read_text(encoding="utf-8") + "\n{{cap:" + token + "}}\n", encoding="utf-8")
    moved = target.with_name(token + ".md")
    target.rename(moved)
    caplog.set_level(logging.DEBUG, logger="conform")
    handlers = list(logging.getLogger("conform").handlers) + list(logging.getLogger().handlers)
    filters = [list(h.filters) for h in handlers]
    first = conformlib.run_self(str(repo_copy), str(deny_list[0]))
    first_trace = conform_trace()
    print("[IMP:9][self_guard_cleanup][RESULT] first_exit=%d" % first.exit_code())
    assert first.exit_code() == 1
    assert token not in json.dumps(first.to_dict()) + first_trace
    assert "[parse_markdown][READ]" in first_trace
    assert any(r.name == "other.application" and token in r.getMessage() for r in caplog.records)
    assert [list(h.filters) for h in handlers] == filters
    caplog.clear()
    other = tmp_path / "other-deny.txt"
    other.write_text("other" + token + "suffix\n", encoding="utf-8")
    second = conformlib.run_self(str(repo_copy), str(other))
    assert token in json.dumps(second.to_dict())
    assert token in "\n".join(r.getMessage() for r in caplog.records)
    assert [list(h.filters) for h in handlers] == filters
    mode = moved.stat().st_mode
    try:
        moved.chmod(0)
        caplog.clear()
        refusal = conformlib.run_self(str(repo_copy), str(deny_list[0]))
    finally:
        moved.chmod(mode)
    assert refusal.exit_code() == 2
    assert token not in json.dumps(refusal.to_dict()) + conform_trace()
    assert [list(h.filters) for h in handlers] == filters
    def crash(root):
        raise RuntimeError(token)
    monkeypatch.setattr(conformlib, "load_neutral_tree", crash)
    crash_report = conformlib.run_self(str(repo_copy), str(deny_list[0]))
    assert crash_report.exit_code() == 2
    assert crash_report.rows[0].detail == "RuntimeError"
    assert reads == [str(deny_list[0]), str(other), str(deny_list[0]), str(deny_list[0])]
    assert [list(h.filters) for h in handlers] == filters
# endregion FUNC_test_self_privacy_guard_restores_logging
