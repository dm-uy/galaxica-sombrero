# region MODULE_CONTRACT [DOMAIN(9): ToolBinding, SessionOrientation; CONCEPT(9): InPlaceBinding, CompleteRefusal, NoFallback; TECH(8): pytest, subprocess, Python]
## @modulecontract
## @purpose Verify that the SessionStart hook states the in-place binding when the co-located checkout is intact, refuses with every reason when it is missing, stale, stubbed or detached, and always exits 0 with one valid JSON object.
## @scope hooks/session_start.py through direct imports for the pure functions and through the real process boundary (script path, the exact command of hooks.json run by a shell) against the real package and against owned copies of it with one deliberate defect each.
## @input The real package in this repository (read-only); owned temporary copies of the package with the six core owners and SPEC_VERSION; hook payload text; temporary target projects with or without record files.
## @output Pass or fail per behavior, with the important trace records (importance 7 to 10) printed before the assertions.
## @links [USES_API(8): subprocess.run; USES_API(7): pytest.tmp_path; USES_API(6): shutil.copytree; READS_DATA_FROM(9): implementations/claude/hooks/hooks.json, adapter.json, references/package-layout.json, SPEC_VERSION and the six core owners at the neutral root; no environment secrets]
## @invariants
## - The real package and the real neutral files are read-only here; every mutation happens in an owned temporary copy.
## - Every refusal case runs with the hook trace enabled and the set of critical (importance 10) events equals the expected set: no unrelated error is tolerated and no expected one is missing.
## - The happy path produces no importance 10 event and no stderr output unless tracing was requested.
## - Expected texts and counts are fixed in the tests, never derived from the hook output they judge.
## @rationale
## Q: Why run the hook as a real process as well as importing its functions?
## A: The pure functions are business logic and are tested by direct import; the stdout contract, the exit status and the opt-in stderr channel exist only at the process boundary, so that boundary is exercised for real, including the exact shell command of hooks.json.
## Q: Why one defect per owned copy?
## A: A single defect isolates which check refuses and proves the reason text names it; one extra test combines defects to prove that no check stops the others.
## Q: Why check the critical event set exactly?
## A: A refusal that fires for the wrong reason, or that fires an unrelated error as well, would pass a text-only assertion while hiding a broken check.
## @changes
## LAST_CHANGE: [2.1.0 - M37 Claude 2.1.0 identity literals; earlier 2.0.0 - M30 exact current release/census coupling; all prior cases/assertions/refusals retained.]
## Earlier: [2.0.0 - Initial suite for the first native Claude Code package: bound path, ten single-defect refusals, detached package, combined defects, bad payloads, closed input, record presence without content, bounds, internal error and the hooks.json command.]
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => test_session_start._module_contract
## FUNC 8[Copy the package and the neutral files it needs into an owned tree] => test_session_start.make_checkout
## FUNC 7[Apply one named defect to an owned checkout] => test_session_start.mutate
## FUNC 8[Run the hook script as the real process and return code, stdout and stderr] => test_session_start.run_hook
## FUNC 8[Validate the single JSON answer and return the context text] => test_session_start.answer
## FUNC 7[Parse hook trace lines into importance, function and block] => test_session_start.trace_events
## FUNC 8[Print the important trace lines before assertions] => test_session_start.show_trace
## FUNC 8[Print the important captured records before assertions] => test_session_start.show_records
## FUNC 9[The real package binds and states the duty] => test_session_start.test_real_package_binds_and_states_duty
## FUNC 9[Each single defect is refused with its reason and only its critical events] => test_session_start.test_single_defect_is_refused_with_its_reason
## FUNC 9[A package copied alone is refused as detached] => test_session_start.test_detached_package_is_refused
## FUNC 9[Defects are collected together, never one at a time] => test_session_start.test_all_defects_are_collected
## FUNC 9[Bad payloads and closed input still give one valid answer] => test_session_start.test_bad_payload_and_closed_input_still_answer
## FUNC 9[Project records are reported by presence only and nothing is written] => test_session_start.test_records_reported_by_presence_without_content
## FUNC 8[Orientation facts for each record combination] => test_session_start.test_orient_project_record_combinations
## FUNC 8[Project directory precedence] => test_session_start.test_project_directory_precedence
## FUNC 8[Card status parsing] => test_session_start.test_card_status_parsing
## FUNC 9[Package root resolution and the symlink case] => test_session_start.test_package_root_resolution_and_symlink
## FUNC 9[The context text stays inside its bound in both outcomes] => test_session_start.test_context_text_is_bounded
## FUNC 9[An internal error becomes a BLOCKED answer naming only the error type] => test_session_start.test_internal_error_becomes_blocked_answer
## FUNC 9[Trace is silent by default and ordered when requested] => test_session_start.test_trace_is_silent_by_default_and_ordered_when_requested
## FUNC 9[The exact hooks.json command runs through a shell] => test_session_start.test_hooks_json_command_runs_through_a_shell
## @usecases
## - [test_real_package_binds_and_states_duty]: Owner -> start a session in the co-located checkout -> the context states the bound neutral version and the reading duty.
## - [test_single_defect_is_refused_with_its_reason]: Owner -> start a session with a stale, stubbed or mismatched checkout -> BLOCKED with the exact reason.
## - [test_detached_package_is_refused]: Owner -> start a session from a copied package -> BLOCKED and no fallback to another copy.
## - [test_records_reported_by_presence_without_content]: Arriving root -> read the context -> learns which records exist and nothing else.
## - [test_hooks_json_command_runs_through_a_shell]: Claude Code -> runs the configured command -> one valid answer.
## @GREP_SUMMARY SessionStart hook tests, binding check, BLOCKED refusal, detached package, stub core card, wrong SPEC_VERSION, layout identity, adapter spec_root, collected reasons, bad payload, closed stdin, record presence, additionalContext bound, internal error, hooks.json command
## @STRUCTURE ▶ ┌real package or owned copy + one defect┐ → ⟦python3 session_start.py ← payload⟧ → ◇ one JSON object ∧ exit 0 → 〈bound ? sentence + duty : BLOCKED + exact reasons ∧ exact critical events〉 → assert
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import io
import json
import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import session_start

LOGGER = logging.getLogger("test_session_start")
HOOK_LOGGER = "session_start"
PACKAGE = Path(__file__).resolve().parents[1]
NEUTRAL = PACKAGE.parents[1]
HOOK = PACKAGE / "hooks" / "session_start.py"
CORE = ("concepts/principles.md", "roles/_base.md", "code/exoskeleton.md", "code/ldd.md", "code/doxygen.md", "code/tests.md")
TRACE_RE = re.compile(r"\[IMP:(\d+)\]\[([A-Za-z_.]+)\]\[([A-Z_]+)\]")
BLOCKED_HEAD = "methodology-claude binding BLOCKED: "
NO_FALLBACK = "never fall back to another installed copy"
COMMON_CRITICAL = {("check_binding", "BLOCKED"), ("render_context", "BLOCKED_TEXT")}
CASES = [
    ("missing_spec_version", ["SPEC_VERSION is missing at the neutral root"], {("_check_neutral_version", "READ_FAILURE")}),
    ("wrong_spec_version", ["SPEC_VERSION 9.0.0 differs from adapter spec_version 3.1.0"], {("_check_neutral_version", "VERSION_MISMATCH")}),
    ("missing_core_file", ["core owner missing: code/tests.md"], {("_check_core_owners", "OWNER_MISSING")}),
    ("stub_core_card", ["core owner card is not status draft: code/ldd.md (status stub)"], {("_check_core_owners", "OWNER_NOT_DRAFT")}),
    ("wrong_layout_package", ["package-layout package is methodology-codex, expected methodology-claude"], {("_check_layout", "IDENTITY_MISMATCH")}),
    ("wrong_layout_profile", ["package-layout profile is installed-copy, expected colocated-in-place"], {("_check_layout", "IDENTITY_MISMATCH")}),
    ("wrong_layout_version", ["package-layout version is 9.0.0, expected 2.2.0"], {("_check_layout", "IDENTITY_MISMATCH")}),
    ("missing_adapter", ["adapter.json is missing, unreadable or not a JSON object"], {("_read_json_object", "READ_FAILURE"), ("_check_adapter", "ADAPTER_UNUSABLE")}),
    ("wrong_spec_root", ["adapter spec_root is not ../../"], {("_check_adapter", "SPEC_ROOT_MISMATCH")}),
    ("missing_adapter_version", ["adapter spec_version is missing"], {("_check_adapter", "SPEC_VERSION_MISSING")}),
]


# region FUNC_make_checkout [DOMAIN(8): Testing; CONCEPT(8): OwnedFixture; TECH(6): shutil, pathlib]
## @purpose Give a test an owned co-located tree, the package under implementations/claude plus the six core owners and SPEC_VERSION at its neutral root, that it may damage freely.
## @uses shutil.copytree, shutil.copyfile, pathlib.Path.mkdir
## @io Input: tmp_path Path of an owned empty directory. Output: tuple of (root Path of the neutral root, package Path of root/implementations/claude).
##   Side effects: writes only below tmp_path; reads the real package and the real neutral files. Guarantees: generated directories (doxygen_output, __pycache__, .pytest_cache) are not copied and the six core owners keep their real bytes.
##   Raises: OSError when a real source file is missing. System importance: 8. Example: after the call, root/SPEC_VERSION and root/code/ldd.md exist and package/adapter.json equals the real adapter.
## @complexity 3
def make_checkout(tmp_path):
    # START_BLOCK_BusinessLogic
    root = tmp_path / "checkout"
    package = root / "implementations" / "claude"
    shutil.copytree(PACKAGE, package, ignore=shutil.ignore_patterns("doxygen_output", "__pycache__", ".pytest_cache"))
    for relative in CORE + ("SPEC_VERSION",):
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(NEUTRAL / relative, destination)
    # END_BLOCK_BusinessLogic
    LOGGER.info("[IMP:7][make_checkout][COPY] owned checkout built with %d core owners", len(CORE))
    return root, package
# endregion FUNC_make_checkout


# region FUNC_mutate [DOMAIN(8): Testing; CONCEPT(8): SingleDefect; TECH(6): pathlib, json]
## @purpose Introduce exactly one named defect into an owned checkout so that one check, and only that one, has to refuse.
## @uses pathlib.Path.write_text, pathlib.Path.unlink, json.loads, json.dumps
## @io Input: root Path and package Path of an owned checkout; name str, one of the ten case names in CASES. Output: None.
##   Side effects: edits or removes one file of the owned checkout. Guarantees: the stub case verifies that the card text really changed. Raises: ValueError for an unknown name; AssertionError when a replacement did not apply. System importance: 7.
##   Example: the name wrong_spec_version rewrites SPEC_VERSION to hold 9.0.0.
## @complexity 5
def mutate(root, package, name):
    # START_BLOCK_BusinessLogic
    layout_path = package / "references" / "package-layout.json"
    adapter_path = package / "adapter.json"
    if name == "missing_spec_version":
        (root / "SPEC_VERSION").unlink()
    elif name == "wrong_spec_version":
        (root / "SPEC_VERSION").write_text("9.0.0\n")
    elif name == "missing_core_file":
        (root / "code" / "tests.md").unlink()
    elif name == "stub_core_card":
        path = root / "code" / "ldd.md"
        original = path.read_text()
        path.write_text(original.replace("status: draft", "status: stub", 1))
        assert "status: stub" in path.read_text()
    elif name in ("wrong_layout_package", "wrong_layout_profile", "wrong_layout_version"):
        layout = json.loads(layout_path.read_text())
        key, value = {"wrong_layout_package": ("package", "methodology-codex"), "wrong_layout_profile": ("profile", "installed-copy"),
                      "wrong_layout_version": ("version", "9.0.0")}[name]
        layout[key] = value
        layout_path.write_text(json.dumps(layout))
    elif name == "missing_adapter":
        adapter_path.unlink()
    elif name in ("wrong_spec_root", "missing_adapter_version"):
        adapter = json.loads(adapter_path.read_text())
        if name == "wrong_spec_root":
            adapter["spec_root"] = "../"
        else:
            del adapter["spec_version"]
        adapter_path.write_text(json.dumps(adapter))
    else:
        raise ValueError("unknown defect name")
    # END_BLOCK_BusinessLogic
    LOGGER.info("[IMP:7][mutate][DEFECT] owned checkout damaged: %s", name)
# endregion FUNC_mutate


# region FUNC_run_hook [DOMAIN(8): Testing; CONCEPT(8): RealProcessBoundary; TECH(7): subprocess]
## @purpose Run the SessionStart script exactly as Claude Code does, as a separate process with a payload on stdin, and return what it printed.
## @uses subprocess.run, sys.executable
## @io Input: script Path of a session_start.py; workdir Path used as the process working directory; payload str written to stdin; package_root Path or None (sets CLAUDE_PLUGIN_ROOT when given); extra_env dict of str to str. Output: tuple of (exit code int, stdout str, stderr str).
##   Side effects: one child process; the environment is the test environment without CLAUDE_PLUGIN_ROOT, CLAUDE_PROJECT_DIR and METHODOLOGY_HOOK_LOG unless supplied. Guarantees: no shell, no timeout hang beyond 60 seconds. Raises: subprocess.TimeoutExpired.
##   System importance: 8. Example: run_hook with package_root set to the real package and an empty payload returns exit code 0 and one JSON line.
## @complexity 3
def run_hook(script, workdir, payload="", package_root=None, extra_env=None):
    env = {k: v for k, v in os.environ.items() if k not in ("CLAUDE_PLUGIN_ROOT", "CLAUDE_PROJECT_DIR", "METHODOLOGY_HOOK_LOG")}
    if package_root is not None:
        env["CLAUDE_PLUGIN_ROOT"] = str(package_root)
    env.update(extra_env or {})
    LOGGER.info("[IMP:7][run_hook][SPAWN] hook process starts")
    done = subprocess.run([sys.executable, str(script)], input=payload, capture_output=True, text=True, env=env, cwd=str(workdir), timeout=60)
    return done.returncode, done.stdout, done.stderr
# endregion FUNC_run_hook


# region FUNC_answer [DOMAIN(8): Testing; CONCEPT(8): OutputContract; TECH(6): json]
## @purpose Hold the hook's stdout to its documented contract and hand back the context text for further assertions.
## @uses json.loads
## @io Input: stdout str as printed by the hook. Output: str additionalContext. Side effects: none. Guarantees: stdout is exactly one JSON line; the object has only hookSpecificOutput with only hookEventName SessionStart and additionalContext; the text is a str of at most 1500 characters.
##   Raises: AssertionError when the contract is broken; ValueError for invalid JSON. System importance: 8. Example: the printed line for a bound session returns the sentence starting methodology-claude 1.0.0.
## @complexity 3
def answer(stdout):
    assert stdout.endswith("\n") and stdout.count("\n") == 1, "exactly one output line"
    value = json.loads(stdout)
    assert list(value) == ["hookSpecificOutput"]
    body = value["hookSpecificOutput"]
    assert sorted(body) == ["additionalContext", "hookEventName"] and body["hookEventName"] == "SessionStart"
    assert isinstance(body["additionalContext"], str) and 0 < len(body["additionalContext"]) <= 1500
    return body["additionalContext"]
# endregion FUNC_answer


# region FUNC_trace_events [DOMAIN(7): Testing; CONCEPT(7): TraceParsing; TECH(5): regex]
## @purpose Turn the hook's stderr trace text into comparable events.
## @uses re.compile
## @io Input: stderr str of bare trace lines. Output: list of (importance int, function str, block str) in output order; lines that do not start with the event identity are skipped.
##   Side effects: none. Guarantees: order is preserved. Raises: none. System importance: 7. Example: the line IMP 9 check_binding BOUND yields the tuple (9, check_binding, BOUND).
## @complexity 2
def trace_events(stderr):
    events = []
    for line in stderr.splitlines():
        match = TRACE_RE.match(line)
        if match:
            events.append((int(match.group(1)), match.group(2), match.group(3)))
    return events
# endregion FUNC_trace_events


# region FUNC_show_trace [DOMAIN(8): Testing; CONCEPT(9): AccessibleTrajectory; TECH(5): print]
## @purpose Expose the hook's actual important trace lines before the assertions, as the tests contract requires.
## @uses builtins.print, re.compile
## @io Input: stderr str of trace lines. Output: None. Side effects: prints the lines with importance 7 to 10 to the test's stdout. Guarantees: only real hook lines are printed, none is fabricated. Raises: none. System importance: 8. Example: a bound run prints the READ, VALID, MATCH and BOUND lines.
## @complexity 2
def show_trace(stderr):
    for line in stderr.splitlines():
        match = TRACE_RE.match(line)
        if match and 7 <= int(match.group(1)) <= 10:
            print(line)
# endregion FUNC_show_trace


# region FUNC_show_records [DOMAIN(8): Testing; CONCEPT(9): AccessibleTrajectory; TECH(5): logging]
## @purpose Expose captured in-process hook records of importance 7 to 10 before the assertions.
## @uses builtins.print
## @io Input: records list of logging.LogRecord from the session_start logger. Output: None. Side effects: prints the messages with importance 7 to 10. Guarantees: only this hook's own records are printed. Raises: none. System importance: 8.
##   Example: a direct check_binding call prints its READ and BOUND records.
## @complexity 2
def show_records(records):
    for record in records:
        message = record.getMessage()
        match = TRACE_RE.match(message)
        if record.name == HOOK_LOGGER and match and 7 <= int(match.group(1)) <= 10:
            print(message)
# endregion FUNC_show_records


# region FUNC_test_real_package_binds_and_states_duty [DOMAIN(9): ToolBinding; CONCEPT(9): BoundPath; TECH(7): subprocess, pytest]
## @purpose Verify that the real co-located package is bound, that the context states the neutral version, the absolute neutral root and the reading duty, and that the owned trajectory of a successful check is complete and error free.
## @uses test_session_start.run_hook, test_session_start.answer, test_session_start.trace_events, test_session_start.show_trace
## @io Input: tmp_path of an owned project directory. Output: None after the assertions. Side effects: one real hook process with tracing on; no writes to the package. Guarantees: the success events appear once each in order and no importance 10 event or unrelated stderr text appears.
##   Raises: AssertionError when the answer or the trace differs. System importance: 9. Example: the sentence methodology-claude 2.1.1 bound in place to neutral methodology 3.0.2 at the real neutral root is present.
## @complexity 5
def test_real_package_binds_and_states_duty(tmp_path):
    project = tmp_path / "project"
    project.mkdir()
    payload = json.dumps({"hook_event_name": "SessionStart", "source": "startup", "cwd": str(project)})
    code, stdout, stderr = run_hook(HOOK, tmp_path, payload, package_root=PACKAGE, extra_env={"METHODOLOGY_HOOK_LOG": "1"})
    show_trace(stderr)
    context = answer(stdout)
    events = trace_events(stderr)
    assert code == 0
    sentence = "methodology-claude 2.2.0 bound in place to neutral methodology 3.1.0 at %s" % os.path.realpath(NEUTRAL)
    assert context.startswith(sentence)
    assert "Before any methodology role or skill work, read %s/references/claude-runtime.md and the six core owners in full; Orient by checks/orient.md" % os.path.realpath(PACKAGE) in context
    for owner in CORE:
        assert owner in context
    assert "BLOCKED" not in context
    ordered = [(f, b) for imp, f, b in events if imp == 9]
    assert ordered == [("_check_adapter", "ADAPTER_VALID"), ("_check_neutral_version", "VERSION_MATCH"), ("_check_layout", "LAYOUT_VALID"),
                       ("_check_core_owners", "OWNERS_VALID"), ("check_binding", "BOUND"), ("render_context", "BOUND_TEXT"), ("main", "ANSWERED")]
    assert not [e for e in events if e[0] == 10]
    assert all(TRACE_RE.match(line) for line in stderr.splitlines())
# endregion FUNC_test_real_package_binds_and_states_duty


# region FUNC_test_single_defect_is_refused_with_its_reason [DOMAIN(9): ToolBinding; CONCEPT(10): CompleteRefusal; TECH(7): subprocess, pytest]
## @purpose Verify that each of ten single defects of the co-located checkout is refused with its own reason, with exit status 0, and with exactly the expected critical trace events.
## @uses test_session_start.make_checkout, test_session_start.mutate, test_session_start.run_hook, test_session_start.answer, test_session_start.trace_events, test_session_start.show_trace
## @io Input: case tuple (name str, expected reason substrings list, expected critical events set) and tmp_path. Output: None after the assertions. Side effects: an owned checkout copy per case, one hook process with tracing on.
##   Guarantees: the context starts with BLOCKED, holds the exact reason, the no-fallback instruction and the neutral root that was checked, never claims a binding; the set of importance 10 events equals the expected set plus the two common blocked events. Raises: AssertionError on any difference.
##   System importance: 9. Example: the stub case names code/ldd.md and the status stub.
## @complexity 6
@pytest.mark.parametrize("name,reasons,critical", CASES, ids=[case[0] for case in CASES])
def test_single_defect_is_refused_with_its_reason(name, reasons, critical, tmp_path):
    root, package = make_checkout(tmp_path)
    mutate(root, package, name)
    code, stdout, stderr = run_hook(package / "hooks" / "session_start.py", tmp_path, "{}", extra_env={"METHODOLOGY_HOOK_LOG": "1"})
    show_trace(stderr)
    context = answer(stdout)
    events = trace_events(stderr)
    assert code == 0
    assert context.startswith(BLOCKED_HEAD)
    for reason in reasons:
        assert reason in context
    assert NO_FALLBACK in context
    assert "neutral root checked: %s" % os.path.realpath(root) in context
    assert "bound in place" not in context
    assert {(f, b) for imp, f, b in events if imp == 10} == critical | COMMON_CRITICAL
    assert not [e for e in events if e[1:] == ("check_binding", "BOUND")]
# endregion FUNC_test_single_defect_is_refused_with_its_reason


# region FUNC_test_detached_package_is_refused [DOMAIN(9): ToolBinding; CONCEPT(10): NoFallback, Detached; TECH(7): subprocess, pytest]
## @purpose Verify that a package copied alone into a cache-like directory, with no neutral checkout two levels above it, is refused with the missing version and all six missing core owners.
## @uses test_session_start.run_hook, test_session_start.answer, test_session_start.trace_events, test_session_start.show_trace, shutil.copytree
## @io Input: tmp_path. Output: None after the assertions. Side effects: an owned copy of the package only; one hook process with tracing on, located by the script path alone. Guarantees: SPEC_VERSION and every core owner reason appear and the no-fallback instruction is stated.
##   Raises: AssertionError on any difference. System importance: 9. Example: the cache copy at cache/plugins/methodology-claude has no SPEC_VERSION at cache.
## @complexity 4
def test_detached_package_is_refused(tmp_path):
    package = tmp_path / "cache" / "plugins" / "methodology-claude"
    shutil.copytree(PACKAGE, package, ignore=shutil.ignore_patterns("doxygen_output", "__pycache__", ".pytest_cache"))
    code, stdout, stderr = run_hook(package / "hooks" / "session_start.py", tmp_path, "{}", extra_env={"METHODOLOGY_HOOK_LOG": "1"})
    show_trace(stderr)
    context = answer(stdout)
    events = trace_events(stderr)
    assert code == 0 and context.startswith(BLOCKED_HEAD) and NO_FALLBACK in context
    assert "SPEC_VERSION is missing at the neutral root" in context
    for owner in CORE:
        assert "core owner missing: %s" % owner in context
    assert sum(1 for e in events if e == (10, "_check_core_owners", "OWNER_MISSING")) == 6
    assert {(f, b) for imp, f, b in events if imp == 10} == {("_check_neutral_version", "READ_FAILURE"), ("_check_core_owners", "OWNER_MISSING")} | COMMON_CRITICAL
# endregion FUNC_test_detached_package_is_refused


# region FUNC_test_all_defects_are_collected [DOMAIN(9): ToolBinding; CONCEPT(9): CollectEveryReason; TECH(7): pytest]
## @purpose Verify that four independent defects are all reported together and in check order, so one repair pass can fix the checkout.
## @uses test_session_start.make_checkout, test_session_start.mutate, session_start.check_binding, test_session_start.show_records
## @io Input: tmp_path and caplog. Output: None after the assertions. Side effects: an owned checkout with four defects; direct calls only. Guarantees: ok is False and the reason list has exactly four entries in the order adapter, version, layout, owners (the two owner defects are in owner order); facts keep both roots.
##   Raises: AssertionError on any difference. System importance: 9. Example: a missing SPEC_VERSION, a wrong layout profile, a stub ldd card and a missing tests card give four reasons.
## @complexity 4
def test_all_defects_are_collected(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    root, package = make_checkout(tmp_path)
    for name in ("missing_spec_version", "wrong_layout_profile", "stub_core_card", "missing_core_file"):
        mutate(root, package, name)
    ok, reasons, facts = session_start.check_binding(package)
    show_records(caplog.records)
    assert ok is False
    assert reasons == ["SPEC_VERSION is missing at the neutral root",
                       "package-layout profile is installed-copy, expected colocated-in-place",
                       "core owner card is not status draft: code/ldd.md (status stub)",
                       "core owner missing: code/tests.md"]
    assert facts["package_root"] == os.path.realpath(package) and facts["neutral_root"] == os.path.realpath(root)
    assert any("[IMP:10][check_binding][BLOCKED] reasons=4" == record.getMessage() for record in caplog.records)
# endregion FUNC_test_all_defects_are_collected


# region FUNC_test_bad_payload_and_closed_input_still_answer [DOMAIN(9): ClaudeCodeHooks; CONCEPT(9): NeverFailSession; TECH(7): subprocess, pytest]
## @purpose Verify that payload text of any quality, a hostile working directory field and a closed standard input never stop the hook from printing one valid bound answer and exiting 0.
## @uses test_session_start.run_hook, test_session_start.answer, subprocess.run
## @io Input: tmp_path. Output: None after the assertions. Side effects: several real hook processes; one of them has its standard input closed before the interpreter starts (POSIX). Guarantees: for each of seven payloads the answer is valid and states the binding; the project line uses the environment directory when the payload gives no usable cwd.
##   Raises: AssertionError on any difference. System importance: 9. Example: the text not json and the text [1, 2] both give the bound sentence and AGENTS.md absent for the environment directory.
## @complexity 5
def test_bad_payload_and_closed_input_still_answer(tmp_path):
    project = tmp_path / "project"
    project.mkdir()
    (project / "AGENTS.md").write_text("project instructions\n")
    payloads = ["", "   \n", "not json", "[1, 2]", "42", json.dumps({"cwd": 5}), json.dumps({"cwd": "bad\u0000path"})]
    for payload in payloads:
        code, stdout, stderr = run_hook(HOOK, tmp_path, payload, package_root=PACKAGE, extra_env={"CLAUDE_PROJECT_DIR": str(project)})
        print("[IMP:9][test_bad_payload_and_closed_input_still_answer][PAYLOAD] exit=%d stdout_lines=%d stderr_chars=%d" % (code, stdout.count("\n"), len(stderr)))
        context = answer(stdout)
        assert code == 0 and stderr == ""
        assert context.startswith("methodology-claude 2.2.0 bound in place")
        if payload == json.dumps({"cwd": "bad\u0000path"}):
            assert "AGENTS.md absent" in context
        else:
            assert "Project %s: AGENTS.md present" % project in context
    env = {k: v for k, v in os.environ.items() if k not in ("CLAUDE_PLUGIN_ROOT", "CLAUDE_PROJECT_DIR", "METHODOLOGY_HOOK_LOG")}
    env["CLAUDE_PLUGIN_ROOT"] = str(PACKAGE)
    closed = subprocess.run([sys.executable, str(HOOK)], capture_output=True, text=True, env=env, cwd=str(tmp_path), timeout=60,
                            preexec_fn=lambda: os.close(0))
    print("[IMP:9][test_bad_payload_and_closed_input_still_answer][CLOSED_STDIN] exit=%d stderr_chars=%d" % (closed.returncode, len(closed.stderr)))
    assert closed.returncode == 0 and closed.stderr == ""
    assert answer(closed.stdout).startswith("methodology-claude 2.2.0 bound in place")
# endregion FUNC_test_bad_payload_and_closed_input_still_answer


# region FUNC_test_records_reported_by_presence_without_content [DOMAIN(9): SessionOrientation; CONCEPT(9): PresenceOnly, ReadOnly; TECH(7): subprocess, pytest]
## @purpose Verify that the context names which project records exist, never carries their content, and that the hook writes nothing into the checkout or the project.
## @uses test_session_start.make_checkout, test_session_start.run_hook, test_session_start.answer
## @io Input: tmp_path. Output: None after the assertions. Side effects: an owned checkout and a project with AGENTS.md, VISION.md, TASKS.md and HANDOFF.md holding a marker text; one hook process. Guarantees: the exact presence sentence appears, the marker does not, and the file listings with sizes and modification times are identical before and after.
##   Raises: AssertionError on any difference. System importance: 9. Example: the sentence ends with VISION.md present, ROADMAP.md absent, TASKS.md present, HANDOFF.md present.
## @complexity 5
def test_records_reported_by_presence_without_content(tmp_path):
    root, package = make_checkout(tmp_path)
    project = tmp_path / "project"
    project.mkdir()
    marker = "PRIVATE-RECORD-CONTENT-MARKER"
    for name in ("AGENTS.md", "VISION.md", "TASKS.md", "HANDOFF.md"):
        (project / name).write_text(marker + "\n")

    def snapshot():
        return sorted((str(p), p.stat().st_size, p.stat().st_mtime_ns) for base in (root, project) for p in base.rglob("*"))

    before = snapshot()
    code, stdout, stderr = run_hook(package / "hooks" / "session_start.py", tmp_path, json.dumps({"cwd": str(project)}))
    context = answer(stdout)
    print("[IMP:9][test_records_reported_by_presence_without_content][RECORDS] exit=%d context_chars=%d" % (code, len(context)))
    assert code == 0 and stderr == ""
    assert "Project %s: AGENTS.md present, CLAUDE.md absent; next to AGENTS.md: VISION.md present, ROADMAP.md absent, TASKS.md present, HANDOFF.md present." % project in context
    assert marker not in context
    assert snapshot() == before
# endregion FUNC_test_records_reported_by_presence_without_content


# region FUNC_test_orient_project_record_combinations [DOMAIN(8): SessionOrientation; CONCEPT(8): RecordPresence; TECH(6): pytest]
## @purpose Verify the orientation facts for four record combinations, including that the four records are only probed next to an existing AGENTS.md.
## @uses session_start.orient_project, test_session_start.show_records
## @io Input: tmp_path and caplog. Output: None after the assertions. Side effects: owned directories with empty files. Guarantees: expected dictionaries are fixed in the test. Raises: AssertionError on any difference. System importance: 8.
##   Example: a directory with only CLAUDE.md reports agents_md False, claude_md True and no records, even if VISION.md exists.
## @complexity 4
def test_orient_project_record_combinations(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    empty = tmp_path / "empty"
    only_agents = tmp_path / "only_agents"
    everything = tmp_path / "everything"
    claude_and_vision = tmp_path / "claude_and_vision"
    for directory in (empty, only_agents, everything, claude_and_vision):
        directory.mkdir()
    (only_agents / "AGENTS.md").write_text("")
    for name in ("AGENTS.md", "CLAUDE.md", "VISION.md", "ROADMAP.md", "TASKS.md", "HANDOFF.md"):
        (everything / name).write_text("")
    for name in ("CLAUDE.md", "VISION.md"):
        (claude_and_vision / name).write_text("")
    results = [session_start.orient_project(directory) for directory in (empty, only_agents, everything, claude_and_vision)]
    show_records(caplog.records)
    no_records = {"VISION.md": False, "ROADMAP.md": False, "TASKS.md": False, "HANDOFF.md": False}
    assert results[0] == {"project_dir": str(empty), "agents_md": False, "claude_md": False, "records": {}}
    assert results[1] == {"project_dir": str(only_agents), "agents_md": True, "claude_md": False, "records": no_records}
    assert results[2] == {"project_dir": str(everything), "agents_md": True, "claude_md": True,
                          "records": {"VISION.md": True, "ROADMAP.md": True, "TASKS.md": True, "HANDOFF.md": True}}
    assert results[3] == {"project_dir": str(claude_and_vision), "agents_md": False, "claude_md": True, "records": {}}
# endregion FUNC_test_orient_project_record_combinations


# region FUNC_test_project_directory_precedence [DOMAIN(8): SessionOrientation; CONCEPT(8): TargetProject; TECH(6): pytest]
## @purpose Verify that the target project is the payload cwd first, then CLAUDE_PROJECT_DIR, then the process working directory, and that unusable payload values fall through.
## @uses session_start._project_dir
## @io Input: monkeypatch and tmp_path. Output: None after the assertions. Side effects: changes the working directory of the test process for the last case only, restored afterwards. Guarantees: the order is checked with distinct values. Raises: AssertionError on any difference. System importance: 8.
##   Example: a payload cwd wins over the environment value.
## @complexity 3
def test_project_directory_precedence(monkeypatch, tmp_path):
    first = session_start._project_dir({"cwd": "/payload/dir"}, {"CLAUDE_PROJECT_DIR": "/env/dir"})
    second = session_start._project_dir({"cwd": ""}, {"CLAUDE_PROJECT_DIR": "/env/dir"})
    third = session_start._project_dir({"cwd": 7}, {"CLAUDE_PROJECT_DIR": "/env/dir"})
    monkeypatch.chdir(tmp_path)
    fourth = session_start._project_dir({}, {})
    print("[IMP:9][test_project_directory_precedence][ORDER] %s | %s | %s | %s" % (first, second, third, fourth))
    assert (first, second, third) == ("/payload/dir", "/env/dir", "/env/dir")
    assert fourth == os.getcwd()
    assert Path(fourth).resolve() == tmp_path.resolve()
# endregion FUNC_test_project_directory_precedence


# region FUNC_test_card_status_parsing [DOMAIN(8): NeutralCard; CONCEPT(8): CardStatus; TECH(6): pytest]
## @purpose Verify the card status reader on a draft card, a stub card, a status placed after other keys, a file without front matter, an unterminated block, undecodable bytes and a missing file.
## @uses session_start._card_status
## @io Input: tmp_path and caplog. Output: None after the assertions. Side effects: owned files. Guarantees: expected values are fixed in the test; a missing file records an importance 10 read failure and the others record none. Raises: AssertionError on any difference. System importance: 8.
##   Example: a file starting with a front matter block holding the line status: stub returns stub.
## @complexity 4
def test_card_status_parsing(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    files = {
        "draft.md": b"---\nid: a.b\ntitle: T\nstatus: draft\n---\n\n# Body\n",
        "stub.md": b"---\nid: a.b\nstatus: stub\n---\n",
        "late.md": b"---\nid: a.b\ntitle: T\nowner: x\nstatus: draft\n---\n",
        "plain.md": b"# No front matter\nstatus: draft\n",
        "open.md": b"---\nid: a.b\ntitle: T\n",
        "body_only.md": b"---\nid: a.b\n---\nstatus: draft\n",
        "binary.md": b"---\nstatus: draft\xff\xfe\n---\n",
    }
    for name, data in files.items():
        (tmp_path / name).write_bytes(data)
    values = {name: session_start._card_status(tmp_path / name) for name in files}
    missing = session_start._card_status(tmp_path / "absent.md")
    show_records(caplog.records)
    assert values["draft.md"] == "draft" and values["stub.md"] == "stub" and values["late.md"] == "draft"
    assert values["plain.md"] is None and values["open.md"] is None and values["body_only.md"] is None
    assert values["binary.md"] is not None and values["binary.md"].startswith("draft")
    assert missing is None
    failures = [r.getMessage() for r in caplog.records if r.levelno >= logging.ERROR]
    assert failures == ["[IMP:10][_card_status][READ_FAILURE] file=absent.md kind=FileNotFoundError"]
# endregion FUNC_test_card_status_parsing


# region FUNC_test_package_root_resolution_and_symlink [DOMAIN(9): ToolBinding; CONCEPT(9): PackageLocation; TECH(7): pytest, os.symlink]
## @purpose Verify that CLAUDE_PLUGIN_ROOT wins over the script location, that the script location is the fallback, and that a symlinked package root is resolved physically so the neutral root two levels above is the real one.
## @uses session_start.resolve_package_root, session_start.check_binding, test_session_start.make_checkout
## @io Input: tmp_path and caplog. Output: None after the assertions. Side effects: an owned checkout and one symbolic link to its package. Guarantees: the link case binds and reports the physical neutral root, not the parent of the link. Raises: AssertionError on any difference. System importance: 9.
##   Example: a link placed in a directory with no SPEC_VERSION still binds because the real checkout is two levels above the real package.
## @complexity 5
def test_package_root_resolution_and_symlink(tmp_path, caplog):
    caplog.set_level(logging.INFO)
    root, package = make_checkout(tmp_path)
    script = package / "hooks" / "session_start.py"
    by_environment = session_start.resolve_package_root({"CLAUDE_PLUGIN_ROOT": str(package)}, "/elsewhere/hooks/session_start.py")
    by_empty_environment = session_start.resolve_package_root({"CLAUDE_PLUGIN_ROOT": ""}, str(script))
    by_location = session_start.resolve_package_root({}, str(script))
    link_home = tmp_path / "links"
    link_home.mkdir()
    link = link_home / "methodology-claude"
    os.symlink(str(package), str(link))
    ok, reasons, facts = session_start.check_binding(link)
    show_records(caplog.records)
    assert by_environment == Path(os.path.realpath(package))
    assert by_empty_environment == by_location == Path(os.path.realpath(package))
    assert ok is True and reasons == []
    assert facts["neutral_root"] == os.path.realpath(root) and facts["package_root"] == os.path.realpath(package)
    assert facts["spec_version"] == "3.1.0" and facts["package_version"] == "2.2.0"
# endregion FUNC_test_package_root_resolution_and_symlink


# region FUNC_test_context_text_is_bounded [DOMAIN(9): SessionOrientation; CONCEPT(9): BoundedContext; TECH(7): pytest]
## @purpose Verify that the context never exceeds 1500 characters, that the BLOCKED instruction survives when the reasons are huge, and that the bound text keeps its sentence and duty when the paths are very long.
## @uses session_start.render_context, session_start._clip
## @io Input: none beyond caplog. Output: None after the assertions. Side effects: none. Guarantees: lengths are checked against the fixed limit 1500; the truncation mark appears only when text was cut. Raises: AssertionError on any difference. System importance: 9.
##   Example: eighty long reasons give a text of at most 1500 characters that still ends with the no-fallback instruction.
## @complexity 4
def test_context_text_is_bounded(caplog):
    caplog.set_level(logging.INFO)
    reasons = ["core owner missing: concepts/principles.md and a very long explanation number %d" % number + " x" * 40 for number in range(80)]
    orientation = {"project_dir": "/p", "agents_md": True, "claude_md": False,
                   "records": {"VISION.md": True, "ROADMAP.md": False, "TASKS.md": True, "HANDOFF.md": False}}
    blocked = session_start.render_context(False, reasons, {"neutral_root": "/n"}, orientation)
    long_root = "/" + "a" * 700
    long_facts = {"package_root": long_root + "/implementations/claude", "neutral_root": long_root, "spec_version": "1.0.0", "package_version": "1.0.0"}
    bound = session_start.render_context(True, [], long_facts, orientation)
    short = session_start.render_context(False, ["SPEC_VERSION is missing at the neutral root"], {}, None)
    show_records(caplog.records)
    assert len(blocked) <= 1500 and blocked.startswith(BLOCKED_HEAD) and blocked.endswith(NO_FALLBACK + ".")
    assert "[truncated]" in blocked
    assert len(bound) <= 1500 and bound.startswith("methodology-claude 1.0.0 bound in place to neutral methodology 1.0.0 at " + long_root)
    assert short == BLOCKED_HEAD + "SPEC_VERSION is missing at the neutral root; do not run methodology roles until the co-located checkout is restored; " + NO_FALLBACK + "."
    assert session_start._clip("abc", 3) == "abc" and session_start._clip("abcdef", 4) == "abcd" and session_start._clip("a" * 30, 20) == "a" * 8 + " [truncated]"
# endregion FUNC_test_context_text_is_bounded


# region FUNC_test_internal_error_becomes_blocked_answer [DOMAIN(9): ClaudeCodeHooks; CONCEPT(9): NeverFailSession; TECH(7): pytest, monkeypatch]
## @purpose Verify that an unexpected exception inside the check produces a BLOCKED answer that names only the error class, still exits 0 and does not leak the exception message.
## @uses session_start.main, session_start.check_binding, test_session_start.answer, test_session_start.show_records
## @io Input: monkeypatch, caplog. Output: None after the assertions. Side effects: replaces check_binding for the test only. Guarantees: the return value is 0, the output is one valid answer, an importance 10 FAIL record exists and no other error record exists. Raises: AssertionError on any difference.
##   System importance: 9. Example: a RuntimeError with the message secret detail yields the text internal error (RuntimeError) and not the message.
## @complexity 4
def test_internal_error_becomes_blocked_answer(monkeypatch, caplog):
    caplog.set_level(logging.INFO)

    def explode(package_root):
        raise RuntimeError("secret detail")

    monkeypatch.setattr(session_start, "check_binding", explode)
    out = io.StringIO()
    code = session_start.main(stdin=io.StringIO("{}"), stdout=out, environ={"CLAUDE_PLUGIN_ROOT": str(PACKAGE)})
    show_records(caplog.records)
    context = answer(out.getvalue())
    assert code == 0
    assert context.startswith(BLOCKED_HEAD + "internal error (RuntimeError)")
    assert "secret detail" not in context and NO_FALLBACK in context
    errors = [r.getMessage() for r in caplog.records if r.levelno >= logging.ERROR]
    assert errors == ["[IMP:10][main][FAIL] kind=RuntimeError", "[IMP:10][render_context][BLOCKED_TEXT] reasons=1 chars=%d" % len(context)]
# endregion FUNC_test_internal_error_becomes_blocked_answer


# region FUNC_test_trace_is_silent_by_default_and_ordered_when_requested [DOMAIN(8): Diagnostics; CONCEPT(8): OptInTrace; TECH(7): subprocess, pytest]
## @purpose Verify that stderr is empty by default, that the level names select the trace, and that the opt-in trace is ordered from the start event to the answered event.
## @uses test_session_start.run_hook, test_session_start.trace_events, test_session_start.show_trace
## @io Input: tmp_path. Output: None after the assertions. Side effects: four real hook processes. Guarantees: unset gives empty stderr; the value ERROR gives empty stderr on a bound run; the value DEBUG and the value 1 both trace from the INIT event to ANSWERED. Raises: AssertionError on any difference. System importance: 8.
##   Example: the value 1 produces the first event main INIT and the last event main ANSWERED.
## @complexity 4
def test_trace_is_silent_by_default_and_ordered_when_requested(tmp_path):
    silent = run_hook(HOOK, tmp_path, "", package_root=PACKAGE)
    errors_only = run_hook(HOOK, tmp_path, "", package_root=PACKAGE, extra_env={"METHODOLOGY_HOOK_LOG": "ERROR"})
    verbose = run_hook(HOOK, tmp_path, "", package_root=PACKAGE, extra_env={"METHODOLOGY_HOOK_LOG": "1"})
    debug = run_hook(HOOK, tmp_path, "", package_root=PACKAGE, extra_env={"METHODOLOGY_HOOK_LOG": "debug"})
    show_trace(verbose[2])
    assert silent[2] == "" and errors_only[2] == ""
    for result in (verbose, debug):
        events = trace_events(result[2])
        assert result[0] == 0 and events[0][1:] == ("_parse_payload", "EMPTY") and events[-1][1:] == ("main", "ANSWERED")
        assert [e[1:] for e in events if e[1] == "main"] == [("main", "INIT"), ("main", "ANSWERED")]
    assert answer(silent[1]) == answer(verbose[1]) == answer(debug[1])
# endregion FUNC_test_trace_is_silent_by_default_and_ordered_when_requested


# region FUNC_test_hooks_json_command_runs_through_a_shell [DOMAIN(9): ClaudeCodeHooks; CONCEPT(9): ConfiguredCommand; TECH(7): json, subprocess, pytest]
## @purpose Verify the SessionStart entry of hooks.json (matcher, timeout, command text) and run its exact command through a shell with CLAUDE_PLUGIN_ROOT set, as Claude Code does.
## @uses json.loads, subprocess.run, test_session_start.answer
## @io Input: tmp_path. Output: None after the assertions. Side effects: one shell process running python3 from the path. Guarantees: the configured command has no failure-swallowing suffix, names the script through CLAUDE_PLUGIN_ROOT, and its output is one valid bound answer with exit status 0. Raises: AssertionError on any difference.
##   System importance: 9. Example: the matcher is startup, resume, clear and compact joined by the pipe character and the timeout is 30.
## @complexity 4
def test_hooks_json_command_runs_through_a_shell(tmp_path):
    config = json.loads((PACKAGE / "hooks" / "hooks.json").read_text())
    entries = config["hooks"]["SessionStart"]
    assert len(entries) == 1 and entries[0]["matcher"] == "startup|resume|clear|compact"
    assert len(entries[0]["hooks"]) == 1
    hook = entries[0]["hooks"][0]
    assert hook["type"] == "command" and hook["timeout"] == 30
    assert hook["command"] == 'python3 "${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py"'
    assert "||" not in hook["command"] and ";" not in hook["command"]
    env = dict(os.environ, CLAUDE_PLUGIN_ROOT=str(PACKAGE))
    env.pop("METHODOLOGY_HOOK_LOG", None)
    done = subprocess.run(hook["command"], shell=True, input="{}", capture_output=True, text=True, env=env, cwd=str(tmp_path), timeout=60)
    print("[IMP:9][test_hooks_json_command_runs_through_a_shell][SHELL] exit=%d stdout_lines=%d stderr_chars=%d" % (done.returncode, done.stdout.count("\n"), len(done.stderr)))
    assert done.returncode == 0 and done.stderr == ""
    assert answer(done.stdout).startswith("methodology-claude 2.2.0 bound in place")
# endregion FUNC_test_hooks_json_command_runs_through_a_shell
