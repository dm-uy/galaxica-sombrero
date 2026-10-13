# region MODULE_CONTRACT [DOMAIN(9): TestHarness, AntiLoop; CONCEPT(8): Fixtures, Canary, Isolation; TECH(6): pytest, logging, shutil]
## @modulecontract
## @purpose To give every test of the repository one isolated place to run in and one honest way to fail: the Anti-Loop
## counter that escalates the advice on each red run, the copies of the repository the drills mutate, the synthetic deny
## list, the in-process command runner, the trace collector and the canary builders that plant private-looking values at
## run time instead of storing them.
## @scope Session hooks, fixtures, canary builders. No test lives here.
## @input The pytest session and its exit status; the repository on disk.
## @output Fixtures for the test modules; the attempt counter file and its printed advice.
## @links [USES_API(9): conform.main; READS_DATA_FROM(6): tests/.test_counter.json]
## @links_to_spec AC-6, AC-7, AC-11, AC-P3
## @invariants
## - A test never mutates the repository: drills run on a copy under the temporary directory.
## - No canary value is stored in a source line: each is built from fragments and random parts at run time.
## - The counter resets to 0 only on a fully green session.
## @rationale
## Q: Why build the canaries from fragments?
## A: The publication scan reads this file too; a stored canary would make the repository fail its own scan.
## Q: Why does the runner call the entry point in process?
## A: capsys then holds the real stdout and stderr the entry point wrote, and caplog holds its trace, without a
## subprocess per drill; a few tests still run real processes.
## @changes
## LAST_CHANGE: [v0.1.0 - Initial creation: Anti-Loop hooks, copies, deny list, runner, trace collector, canaries.]
## @modulemap
## FUNC 6[The advice for the nth red run] => anti_loop_message
## FUNC 4[Read the red-session counter, 0 when missing or damaged] => _read_counter
## FUNC 4[Write the red-session counter, ignoring a write failure] => _write_counter
## FUNC 7[Read the counter at session start] => pytest_sessionstart
## FUNC 8[Reset or raise the counter and print the advice] => pytest_sessionfinish
## FUNC 4[The repository root] => repo_root
## FUNC 6[An isolated copy of the repository] => repo_copy
## CLASS 5[The three paths of a harness copy] => HarnessCopy
## FUNC 7[A spec copy beside a harness copy with its adapter] => harness_copy
## FUNC 6[A synthetic deny list and its token] => deny_list
## FUNC 7[Run the entry point in process] => run_cli
## FUNC 7[Collect the important trace lines] => ldd_trajectory
## FUNC 6[Build the five canary values] => canary_values
## FUNC 5[Plant a value in a file of a copy] => plant_canary
## FUNC 4[Expose the advice function] => anti_loop
## FUNC 5[Find a row of a parsed report] => find_rows
## FUNC 5[Read the card and the body of a file] => read_card
## FUNC 6[Parse the table form of a report] => parse_table
## @usecases
## - [repo_copy]: Drill -> mutate a copy -> the real tree stays untouched
## - [harness_copy]: Adapter drill -> mutate the adapter, the harness files or the spec copy -> the real tree stays untouched
## - [pytest_sessionfinish]: Agent -> red run -> escalating advice, never an endless loop
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: pytest conftest, Anti-Loop counter, fixtures, repo copy, synthetic deny list, run_cli, caplog trajectory, canary builders, isolation
# STRUCTURE: ▶ session ┌start: read counter┐ → ⊕ fixtures ┌repo_copy, harness_copy, deny_list, run_cli, ldd_trajectory, canaries┐ → ⚡ tests → ◇ exit 0 ? reset : attempt+1 → ⎋ advice

import json
import logging
import pathlib
import re
import secrets
import shutil
import sys
from typing import Callable, Dict, List, NamedTuple, Tuple

import pytest

import conform

TESTS_DIR = pathlib.Path(__file__).resolve().parent
COUNTER_PATH = TESTS_DIR / ".test_counter.json"
_STATE = {"attempts": 0}
IMP_RE = re.compile(r"\[IMP:(\d{1,2})\]")

CHECKLIST = (
    "Anti-Loop checklist of the common errors of this project:\n"
    "  1. a pattern of the scanner that matches its own source line (build every pattern and canary from fragments);\n"
    "  2. a log line that carries content: a matched value, a token, a file's text (paths, counts and fingerprints only);\n"
    "  3. a fenced block not closed in a Markdown file (everything after it is read as an example);\n"
    "  4. CRLF not normalised before a hash, a comparison or a card read;\n"
    "  5. an argparse error escaping as SystemExit instead of the input.usage refusal;\n"
    "  6. sys.path changed from a test (pythonpath is set once in pytest.ini)."
)
DOC_HINT = (
    "Anti-Loop, attempt 3: stop editing by guesswork. Read tests/test_guide.md, checks/conform.md and FORMAT.md, build the\n"
    "code map with doxygen Doxyfile, and read the LDD trajectory of the failing test (run it with -s) before the next change."
)
LOOP_WARNING = (
    "Anti-Loop, attempt 4: you are probably looping. The same kind of edit has failed three times. Write down the\n"
    "hypotheses (at least two), the evidence for each, and change the approach, not the detail."
)
STOP_MESSAGE = (
    "Anti-Loop, attempt 5 or more: STOP. Do not run the suite again. Report the failing tests, the LDD lines and the\n"
    "hypotheses you tried, and ask for direction."
)


# region FUNC_anti_loop_message [DOMAIN(8): TestHarness; CONCEPT(9): AntiLoop, Ladder; TECH(3): str]
## @purpose The advice printed after the nth consecutive red session: the checklist twice, then the documentation hint,
## then the looping warning, then the stop.
## @io int -> str
## @complexity 2
def anti_loop_message(attempt: int) -> str:
    if attempt <= 2:
        return CHECKLIST
    if attempt == 3:
        return DOC_HINT
    if attempt == 4:
        return LOOP_WARNING
    return STOP_MESSAGE
# endregion FUNC_anti_loop_message


# region FUNC__read_counter [DOMAIN(7): TestHarness; CONCEPT(8): AntiLoop, Counter; TECH(5): json, pathlib]
## @purpose Read the number of consecutive red sessions from the counter file; a missing or damaged file reads as 0.
## @io None -> int
## @complexity 3
def _read_counter() -> int:
    try:
        data = json.loads(COUNTER_PATH.read_text(encoding="utf-8"))
        return int(data.get("attempts", 0))
    except (OSError, ValueError, AttributeError, TypeError):
        return 0
# endregion FUNC__read_counter


# region FUNC__write_counter [DOMAIN(7): TestHarness; CONCEPT(8): AntiLoop, Counter; TECH(5): json, pathlib]
## @purpose Write the counter file; a failure to write is ignored, because the counter is advice, not a verdict.
## @io int -> None
## @complexity 2
def _write_counter(value: int) -> None:
    try:
        COUNTER_PATH.write_text(json.dumps({"attempts": value}) + "\n", encoding="utf-8")
    except OSError:
        pass
# endregion FUNC__write_counter


# region FUNC_pytest_sessionstart [DOMAIN(8): TestHarness; CONCEPT(9): AntiLoop, SessionStart; TECH(5): pytest hook]
## @purpose Load the number of red sessions before this one, so the finish hook knows which attempt this is.
## @io pytest.Session -> None
## @complexity 2
def pytest_sessionstart(session) -> None:
    _STATE["attempts"] = _read_counter()
# endregion FUNC_pytest_sessionstart


# region FUNC_pytest_sessionfinish [DOMAIN(8): TestHarness; CONCEPT(9): AntiLoop, SessionFinish; TECH(5): pytest hook]
## @purpose On a fully green session reset the counter to 0; on a red one raise it and print the advice for that attempt.
## @io (pytest.Session, int) -> None
## @complexity 4
def pytest_sessionfinish(session, exitstatus) -> None:
    if int(exitstatus) == 0:
        _write_counter(0)
        return
    attempt = _STATE["attempts"] + 1
    _write_counter(attempt)
    reporter = session.config.pluginmanager.get_plugin("terminalreporter")
    text = "\n[ANTI-LOOP attempt %d]\n%s" % (attempt, anti_loop_message(attempt))
    if reporter is not None:
        reporter.write_line(text)
    else:
        sys.stderr.write(text + "\n")
# endregion FUNC_pytest_sessionfinish


# region FUNC_anti_loop [DOMAIN(6): TestHarness; CONCEPT(7): AntiLoop; TECH(4): fixture]
## @purpose Hand the advice function to a test, which cannot import this module by name.
## @io None -> Callable[[int], str]
## @complexity 1
@pytest.fixture
def anti_loop() -> Callable[[int], str]:
    return anti_loop_message
# endregion FUNC_anti_loop


# region FUNC_repo_root [DOMAIN(6): TestHarness; CONCEPT(7): Root; TECH(4): pathlib]
## @purpose The repository under test: the parent of the tests directory.
## @io None -> pathlib.Path
## @complexity 1
@pytest.fixture
def repo_root() -> pathlib.Path:
    return TESTS_DIR.parent
# endregion FUNC_repo_root


# region FUNC_repo_copy [DOMAIN(8): TestHarness; CONCEPT(9): Isolation, Copy; TECH(5): shutil.copytree]
## @purpose An isolated copy of the repository under the temporary directory, without git data, build output, caches and
## the counter file, for a drill to mutate.
## @uses shutil.copytree
## @io (pathlib.Path, pathlib.Path) -> pathlib.Path
## @complexity 2
@pytest.fixture
def repo_copy(tmp_path: pathlib.Path, repo_root: pathlib.Path) -> pathlib.Path:
    target = tmp_path / "copy"
    ignore = shutil.ignore_patterns(".git", "doxygen_output", "__pycache__", ".pytest_cache", ".test_counter.json")
    shutil.copytree(str(repo_root), str(target), ignore=ignore)
    return target
# endregion FUNC_repo_copy


# region CLASS_HarnessCopy [DOMAIN(7): TestHarness; CONCEPT(8): Adapter, Copy; TECH(4): NamedTuple]
## @purpose The three paths an adapter drill works on: the spec copy, the harness copy and the adapter file inside it.
class HarnessCopy(NamedTuple):
    spec: pathlib.Path
    harness: pathlib.Path
    adapter: pathlib.Path
# endregion CLASS_HarnessCopy


# region FUNC_harness_copy [DOMAIN(8): TestHarness, Adapter; CONCEPT(9): Isolation, Copy; TECH(5): shutil.copytree, json]
## @purpose A spec copy at tmp/spec and, beside it, the example harness at tmp/harness with the adapter pointing to the spec
## copy, so an adapter drill can damage the adapter, the harness files or the spec without touching the repository.
## @uses shutil.copytree, json
## @io (pathlib.Path, pathlib.Path) -> HarnessCopy
## @complexity 3
@pytest.fixture
def harness_copy(tmp_path: pathlib.Path, repo_root: pathlib.Path) -> HarnessCopy:
    spec = tmp_path / "spec"
    ignore = shutil.ignore_patterns(".git", "doxygen_output", "__pycache__", ".pytest_cache", ".test_counter.json")
    shutil.copytree(str(repo_root), str(spec), ignore=ignore)
    harness = tmp_path / "harness"
    shutil.copytree(str(spec / "examples"), str(harness))
    adapter = harness / "adapter.example.json"
    data = json.loads(adapter.read_text(encoding="utf-8"))
    data["spec_root"] = "../spec"
    adapter.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    return HarnessCopy(spec, harness, adapter)
# endregion FUNC_harness_copy


# region FUNC_deny_list [DOMAIN(8): Privacy, TestHarness; CONCEPT(8): DenyList, Synthetic; TECH(5): secrets]
## @purpose A synthetic deny list outside the copy: a comment line and one random token, returned with its path.
## @uses secrets.token_hex
## @io pathlib.Path -> Tuple[pathlib.Path, str]
## @complexity 2
@pytest.fixture
def deny_list(tmp_path: pathlib.Path) -> Tuple[pathlib.Path, str]:
    token = "zq" + secrets.token_hex(6)
    path = tmp_path / "deny-list.txt"
    path.write_text("# synthetic private words, one per line\n" + token + "\n", encoding="utf-8")
    return path, token
# endregion FUNC_deny_list


# region FUNC_run_cli [DOMAIN(8): TestHarness; CONCEPT(9): EntryPoint, Capture; TECH(5): capsys, conform.main]
## @purpose A runner that calls the frontend in process and returns the exit code with everything it wrote to stdout and
## stderr.
## @uses conform.main
## @io capsys -> Callable[[List[str]], Tuple[int, str, str]]
## @complexity 3
@pytest.fixture
def run_cli(capsys) -> Callable[[List[str]], Tuple[int, str, str]]:
    def _run(argv: List[str]) -> Tuple[int, str, str]:
        capsys.readouterr()
        code = conform.main(list(argv))
        captured = capsys.readouterr()
        return code, captured.out, captured.err
    return _run
# endregion FUNC_run_cli


# region FUNC_ldd_trajectory [DOMAIN(8): TestHarness; CONCEPT(9): Trajectory, LDD; TECH(5): caplog, logging]
## @purpose Turn the trace of the conform loggers on and return a collector that prints and returns the lines of importance
## seven and above, so a red test shows the trajectory of the run before its assert.
## @uses caplog
## @io caplog -> Callable[[], List[str]]
## @complexity 3
@pytest.fixture
def ldd_trajectory(caplog) -> Callable[[], List[str]]:
    caplog.set_level(logging.DEBUG, logger="conform")

    def _collect() -> List[str]:
        lines = []
        for record in caplog.records:
            if not record.name.startswith("conform"):
                continue
            message = record.getMessage()
            found = IMP_RE.search(message)
            if found and int(found.group(1)) >= 7:
                lines.append(message)
        for line in lines:
            print(line)
        return lines
    return _collect
# endregion FUNC_ldd_trajectory


# region FUNC_canary_values [DOMAIN(8): Privacy, TestHarness; CONCEPT(9): Canary, RunTime; TECH(5): secrets, str]
## @purpose Build the five canary values at run time from fragments and random parts: a POSIX home path, a Windows home
## path, a tilde path, an e-mail address and the deny token; no source line holds a value that matches a scan rule.
## @uses secrets.token_hex
## @io Tuple[pathlib.Path, str] -> Dict[str, str]
## @complexity 3
@pytest.fixture
def canary_values(deny_list: Tuple[pathlib.Path, str]) -> Dict[str, str]:
    stamp = secrets.token_hex(3)
    return {
        "posix-home": "/" + "Users" + "/" + "u" + stamp + "/" + "notes",
        "windows-home": "C" + ":" + "\\" + "Users" + "\\" + "u" + stamp + "\\" + "notes",
        "tilde": "~" + "/" + "d" + stamp,
        "email": "m" + stamp + "@" + "example" + "." + "org",
        "deny-token": deny_list[1].upper(),
    }
# endregion FUNC_canary_values


# region FUNC_plant_canary [DOMAIN(8): Privacy, TestHarness; CONCEPT(8): Canary, Plant; TECH(5): pathlib]
## @purpose A helper that writes a small text file into a copy with the value on its third line, and returns the path.
## @io () -> Callable[[pathlib.Path, str, str], pathlib.Path]
## @complexity 2
@pytest.fixture
def plant_canary() -> Callable[[pathlib.Path, str, str], pathlib.Path]:
    def _plant(copy: pathlib.Path, relative: str, value: str) -> pathlib.Path:
        target = copy / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("first line\nsecond line\nnote " + value + " end\nlast line\n", encoding="utf-8")
        return target
    return _plant
# endregion FUNC_plant_canary


# region FUNC_find_rows [DOMAIN(6): TestHarness; CONCEPT(7): Report, Lookup; TECH(4): list]
## @purpose A lookup over the rows of a parsed JSON report: the rows with the given rule and, when given, status and subject.
## @io () -> Callable[..., List[dict]]
## @complexity 2
@pytest.fixture
def find_rows() -> Callable[..., List[dict]]:
    def _find(report: dict, rule: str, status: str = "", subject: str = "") -> List[dict]:
        rows = []
        for row in report["rows"]:
            if row["rule"] != rule:
                continue
            if status and row["status"] != status:
                continue
            if subject and row["subject"] != subject:
                continue
            rows.append(row)
        return rows
    return _find
# endregion FUNC_find_rows


# region FUNC_read_card [DOMAIN(6): TestHarness; CONCEPT(7): Card, Reader; TECH(4): str.split]
## @purpose An independent reader of a neutral file for the tests: its card as a dictionary and its body lines, so that the
## count tests do not depend on the reader they check.
## @io () -> Callable[[pathlib.Path], Tuple[Dict[str, str], List[str]]]
## @complexity 3
@pytest.fixture
def read_card() -> Callable[[pathlib.Path], Tuple[Dict[str, str], List[str]]]:
    def _read(path: pathlib.Path) -> Tuple[Dict[str, str], List[str]]:
        lines = path.read_text(encoding="utf-8").split("\n")
        assert lines[0] == "---", "no card"
        end = lines.index("---", 1)
        card = {}
        for line in lines[1:end]:
            key, _, value = line.partition(": ")
            card[key] = value
        return card, lines[end + 1:]
    return _read
# endregion FUNC_read_card


# region FUNC_parse_table [DOMAIN(7): TestHarness; CONCEPT(8): Report, TableParser; TECH(4): str.split]
## @purpose A parser of the table form of a report back into rows and the summary line, so that the tests can compare the
## table with the JSON form without trusting the renderer they check.
## @io () -> Callable[[str], Tuple[List[dict], str]]
## @complexity 4
@pytest.fixture
def parse_table() -> Callable[[str], Tuple[List[dict], str]]:
    def _parse(text: str) -> Tuple[List[dict], str]:
        rows = []
        summary = ""
        for line in text.split("\n"):
            if not line:
                continue
            if line.startswith("SUMMARY  "):
                summary = line
                continue
            status = line[:7].strip()
            rule, subject, detail = (line[9:].split("  ", 2) + ["", ""])[:3]
            rows.append({"status": status, "rule": rule, "subject": subject, "detail": detail})
        return rows, summary
    return _parse
# endregion FUNC_parse_table
