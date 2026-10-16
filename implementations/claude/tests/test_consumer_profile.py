# region MODULE_CONTRACT [DOMAIN(9): ClaudePackage, ConsumerPM; CONCEPT(10): ProcessBoundaryEquality, BlockedNotDegraded; TECH(7): Python, pytest, subprocess]
## @modulecontract
## @purpose Prove that the three Claude launchers bin/orient, bin/codemap and bin/markup-migrate hand the process to the sibling Codex C2 scripts
##   with arguments, streams and exit status unchanged, refuse plainly (one BLOCKED line, exit 2) when the sibling cannot be used, and that the
##   thin carrier, the routed entries and the package Doxyfile say what the M37 specification fixes, that the launchers survive closed standard streams,
##   and that no text promises a bare launcher name without the PATH resolution check.
## @scope The real launcher files as child processes on synthetic owned fixtures; the launchers' own functions through an importlib load of owned
##   copies; the carrier, nine routed skills, searcher, two version-signature skills, reference resolution and Doxyfile coverage as finite text predicates.
## @input The real package and its sibling Codex package in this checkout (read-only), the doxygen tool, /bin/sh for the closed-descriptor cases, and owned tmp_path fixtures and copies.
## @output Assertions over exit status, stdout, stderr, file bytes and text predicates, and a visible IMP:7-10 trajectory printed before them; no file is written outside tmp_path.
## @links [USES_API(9): subprocess.run; USES_API(8): importlib.machinery.SourceFileLoader, ast.parse, ast.dump; USES_API(7): shutil.copy2, os.symlink, json.loads;
##   USES_API(6): logging; READS_DATA_FROM(9): bin/orient, bin/codemap, bin/markup-migrate, references/consumer-pm-profile.md, Doxyfile;
##   READS_DATA_FROM(9): ../codex/skills/pm/scripts/orient.py, codemap.py, markup_migrate.py, consumer_files.py, ../codex/skills/pm/templates/Doxyfile,
##   ../codex/references/consumer-pm-profile.md; READS_DATA_FROM(8): skills/*/SKILL.md, agents/*.md, references/claude-runtime.md]
## @links_to_spec examples/pm-project/specs/m37-claude-consumer-profile.md Behavior 1, Behavior 2, Behavior 3, BR-4, BR-6, AC1, AC2, AC4
## @invariants
## - Every fixture, copy, link and marker lives under tmp_path; the real package and the Codex package are read-only here and no bytecode is written beside them.
## - Expected exit codes, lines and texts are fixed in the tests and never derived from the output they judge; launcher output is compared with a direct python3 -B call of the Codex script.
## - The success branch of main is never called in process: it would replace the test process. Only refusal and failure branches run in process.
## - Every happy-path case rejects all ERROR records; each deliberate refusal case requires exactly its own expected ERROR records.
## - A missing doxygen fails the map test; nothing in this module skips.
## - A closed standard stream is produced by the shell redirection N>&- of a real child process, never by a null device, so the child interpreter really reports the stream as None.
## @rationale
## Q: Why compare the launcher with a direct python3 -B call of the Codex script?
## A: The launcher contract is pure pass-through, so equality of exit status, stdout and stderr is the oracle; the direct call is the Codex script's own behavior, not a copy of it.
## Q: Why run owned copies of the launchers for the refusal cases?
## A: A refusal needs a checkout whose sibling is missing, a directory, a link or an escaping link; mutating the real checkout would be unsafe, so the launcher is copied with the scripts into tmp_path.
## Q: Why test routing and the carrier here and not in test_package_contract.py?
## A: That module may change only version and membership facts; the unchanged module still resolves every plugin-root reference of every skill and agent, and this module repeats that check for the carrier.
## Q: Why fail instead of skip when doxygen is missing?
## A: A skipped map test covers zero acceptance criteria; the code map is a mandatory prerequisite of the profile.
## @changes
## LAST_CHANGE: [2.1.0 - Debug 1 of M37-C2: process-boundary and in-process tests for closed standard streams, text pins for the bare-name PATH caveat, the fixture-local grant sentence and the hook stderr merge. Earlier: initial M37 launcher process-boundary, carrier, routing and Doxyfile tests for the consumer PM profile.]
## @modulemap
## FUNC 5[Print owned important trace before assertions] => test_consumer_profile._show
## FUNC 6[List the owned ERROR messages of the module and the launcher loggers] => test_consumer_profile._errors
## FUNC 7[Build a child environment without interpreter or log steering] => test_consumer_profile._clean_env
## FUNC 8[Run one child process with captured text streams and print them] => test_consumer_profile._run
## FUNC 9[Run a launcher and the direct Codex script with the same arguments] => test_consumer_profile._pair
## FUNC 9[Require equal exit status, stdout and stderr for a launcher pair] => test_consumer_profile._assert_pair
## FUNC 6[Write one synthetic front-matter record] => test_consumer_profile._record
## FUNC 8[Create the adopted single-layer consumer fixture] => test_consumer_profile._adopted_fixture
## FUNC 8[Create the software fixture in current or legacy markup] => test_consumer_profile._source_fixture
## FUNC 9[Build the real fixture Doxygen map and its receipt] => test_consumer_profile._build_map
## FUNC 8[Copy the launchers and Codex scripts into an owned checkout] => test_consumer_profile._owned_checkout
## FUNC 7[Compute the sibling candidate path an owned checkout expects] => test_consumer_profile._candidate
## FUNC 7[Import an owned launcher copy without touching sys.path] => test_consumer_profile._load_launcher
## FUNC 8[Count and list unresolved plugin-root references and relative links] => test_consumer_profile._references
## FUNC 6[Read the package texts the routing predicates judge] => test_consumer_profile._package_texts
## FUNC 7[Wrap a command so chosen standard descriptors start really closed] => test_consumer_profile._closed_argv
## FUNC 9[Run a launcher and the direct Codex script with descriptors closed] => test_consumer_profile._closed_pair
## FUNC 9[List the bare-name promises that lack the PATH resolution check] => test_consumer_profile._bare_name_problems
## FUNC 9[List the carrier predicate violations of a text] => test_consumer_profile._carrier_problems
## FUNC 9[List the routing predicate violations of the package texts] => test_consumer_profile._routing_problems
## FUNC 6[Copy a text map with one replaced fragment for a contrary control] => test_consumer_profile._variant
## FUNC 6[Require that a captured stderr is one BLOCKED line and return it] => test_consumer_profile._one_line
## FUNC 7[Write one decoy script that records its execution in a marker file] => test_consumer_profile._decoy
## FUNC 9[Launchers are regular, executable, Python 3.9 grammar and AST-equivalent] => test_consumer_profile.test_launchers_are_regular_executable_and_equivalent
## FUNC 9[resolve_sibling classifies ok, missing, not-regular and outside exactly] => test_consumer_profile.test_resolve_sibling_refuses_unusable_siblings
## FUNC 9[main answers BLOCKED with exit 2 on every refusal and failure branch] => test_consumer_profile.test_main_reports_blocked_without_running
## FUNC 10[orient launcher equals the direct call: clean, check, defect, portfolio] => test_consumer_profile.test_orient_launcher_equals_direct_call
## FUNC 10[codemap launcher equals the direct call on a built map] => test_consumer_profile.test_codemap_launcher_equals_direct_call_on_built_map
## FUNC 10[markup-migrate check equals the direct call on current and legacy markup] => test_consumer_profile.test_markup_migrate_check_equals_direct_call
## FUNC 9[Arguments and exit status pass through for all three launchers] => test_consumer_profile.test_arguments_and_exit_status_pass_through
## FUNC 10[A missing, directory or escaping sibling blocks with no fallback] => test_consumer_profile.test_missing_sibling_blocks_without_fallback
## FUNC 9[A symbolic link to a launcher resolves the real package] => test_consumer_profile.test_symlinked_launcher_resolves_real_package
## FUNC 9[Executing the launcher by its shebang equals the direct call] => test_consumer_profile.test_shebang_invocation_equals_direct_call
## FUNC 9[The opt-in launcher trace is ordered and silent when unset] => test_consumer_profile.test_launcher_trace_is_owned_and_ordered
## FUNC 9[The launcher never writes bytecode beside the Codex scripts] => test_consumer_profile.test_launcher_never_writes_bytecode_beside_codex_scripts
## FUNC 10[Launchers equal the direct call with stdout, stderr or both closed] => test_consumer_profile.test_launchers_pass_through_with_closed_standard_streams
## FUNC 10[A BLOCKED refusal keeps exit 2 with stdout, stderr or both closed] => test_consumer_profile.test_blocked_refusal_exits_two_with_closed_standard_streams
## FUNC 9[main and the stream helper skip absent standard streams without raising] => test_consumer_profile.test_main_and_emit_skip_absent_standard_streams
## FUNC 9[Bare launcher names are promised only with the PATH resolution check] => test_consumer_profile.test_bare_names_require_path_resolution_check
## FUNC 9[The carrier states only the declared deltas] => test_consumer_profile.test_carrier_states_only_declared_deltas
## FUNC 9[Routed entries name the carrier and the launchers and every reference resolves] => test_consumer_profile.test_routed_entries_name_carrier_and_launchers
## FUNC 8[The package Doxyfile covers the extensionless launchers] => test_consumer_profile.test_doxyfile_covers_launchers
## @usecases
## - [test_launchers_are_regular_executable_and_equivalent]: Claude Code user -> put the plugin bin on PATH -> three executable launchers that differ only in two constants (AC2, BR-6).
## - [test_orient_launcher_equals_direct_call]: Claude Code root -> orient PROJECT and orient PROJECT --check -> the Codex report, exit 0 when clean and 1 with its row when defective (AC2).
## - [test_codemap_launcher_equals_direct_call_on_built_map]: Claude Code root -> codemap PROJECT TARGET on a built map -> the map-sourced answer unchanged (AC2).
## - [test_markup_migrate_check_equals_direct_call]: Claude Code root -> markup-migrate PROJECT --check -> up to date or migration due, sources unchanged (AC2).
## - [test_missing_sibling_blocks_without_fallback]: Root on a checkout without the Codex package -> run a launcher -> exit 2, one BLOCKED line, nothing else runs (AC2, BR-4).
## - [test_symlinked_launcher_resolves_real_package]: Owner -> reach a launcher through a symbolic link -> the real package and its sibling are used (AC2).
## - [test_launcher_never_writes_bytecode_beside_codex_scripts]: Maintainer -> run a launcher with bytecode writing enabled in the environment -> the Codex script directory stays byte-for-byte free of caches (BR-1).
## - [test_launchers_pass_through_with_closed_standard_streams]: Tool runner that closes stdout or stderr -> run a launcher -> the Codex script runs and the status and remaining stream equal the direct call (BR-4, AC2).
## - [test_blocked_refusal_exits_two_with_closed_standard_streams]: Tool runner with a closed stderr on a checkout without the Codex package -> run a launcher -> exit 2, never a crash (BR-4, AC2).
## - [test_bare_names_require_path_resolution_check]: Owner with a second enabled plugin that ships the same command names -> read the README, carrier and routes -> a bare name is used only after the PATH check (AC1, AC4).
## - [test_carrier_states_only_declared_deltas]: Reviewer -> read the carrier -> exactly the five Claude deltas, no duty of its own, every link resolves (AC1).
## - [test_routed_entries_name_carrier_and_launchers]: Reviewer -> read the routed entries -> the carrier and the launchers are named and every plugin-root reference resolves (AC4).
## @GREP_SUMMARY Claude consumer PM profile tests, launcher process boundary, direct call equality, BLOCKED exit 2, closed standard streams, bare name PATH shadowing, owned checkout, symlink, shebang, carrier deltas, routing, Doxyfile bin
## @STRUCTURE ▶ real launchers + owned copies → ⚡ child process vs direct python3 -B call → ◇ equal (exit, stdout, stderr) → ○ refusal in owned checkout → ◇ one BLOCKED line, exit 2 → ○ carrier + routing text predicates → ⎋ assertions
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import ast
import datetime
import importlib.machinery
import importlib.util
import io
import json
import logging
import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys

import pytest

LOGGER = logging.getLogger(__name__)
LAUNCHER_LOGGER = "methodology_claude.launcher"
PACKAGE = pathlib.Path(__file__).resolve().parents[1]
CODEX = PACKAGE.parent / "codex"
SCRIPTS = CODEX / "skills/pm/scripts"
TEMPLATES = CODEX / "skills/pm/templates"
LAUNCHERS = {"orient": "orient.py", "codemap": "codemap.py", "markup-migrate": "markup_migrate.py"}
ROUTED = ("pm", "pm-bootstrap", "pm-plan-batch", "pm-run-batch", "pm-handoff", "durable-layer", "roadmap",
          "document-protocol", "greenfield-bootstrap")
# The plan's exact routing texts for these two documentation entries name the carrier and the orient launcher but not the profile identity.
IDENTITY_EXEMPT = ("document-protocol", "greenfield-bootstrap")
CARRIER = "${CLAUDE_PLUGIN_ROOT}/references/consumer-pm-profile.md"
BARE_ORIENT = "(bare `orient` only when `command -v orient` resolves to that launcher)"
BIN = "${CLAUDE_PLUGIN_ROOT}/bin/"
BLOCKED_PREFIX = "methodology-claude BLOCKED: "
PROFILE = "methodology-consumer-pm/1.0.0"
HEADINGS = ["# Consumer PM profile for Claude Code — methodology-claude 2.1.0", "## Claude Code deltas", "### 1. Invocation",
            "### 2. Consent", "### 3. Delegation model", "### 4. No package hook", "### 5. Optional per-project SessionStart hook"]
PLUGIN_REFERENCE = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./-]+)")
MARKDOWN_LINK = re.compile(r"\]\(([^)\s]+)\)")
SCOPED_ENV = ("PYTHONPATH", "PYTHONHOME", "METHODOLOGY_LAUNCHER_LOG", "ORIENT_LOG", "CODEMAP_LOG", "MARKUP_MIGRATE_LOG")


# region FUNC__show [DOMAIN(5): Tests; CONCEPT(6): VisibleTrace; TECH(4): print]
## @purpose Expose this module's own important records, and the launcher records of the code under test, before the assertions that depend on them (TST-301).
## @uses builtins.print, logging.LogRecord.getMessage
## @io Input: records list of logging.LogRecord, for example caplog.records. Output: None; prints every record of this module's logger or of the launcher logger whose message carries an importance from 7 to 10.
##   Side effects: stdout lines only. Guarantees: foreign loggers and importance below 7 are never printed. Raises: none for LogRecord input. System importance: 5.
##   Example: a VALIDATION_FAILURE record of resolve_sibling is printed as its bracketed message line.
## @complexity 2
def _show(records):
    # START_BLOCK_BusinessLogic
    for record in records:
        if record.name in (LOGGER.name, LAUNCHER_LOGGER) and any("[IMP:%d]" % n in record.getMessage() for n in range(7, 11)):
            print(record.getMessage())
    # END_BLOCK_BusinessLogic
# endregion FUNC__show


# region FUNC__errors [DOMAIN(6): Tests; CONCEPT(7): ExpectedOnlyErrors; TECH(4): logging]
## @purpose List the ERROR-level messages of this module and of the launcher logger, so a test can demand an exact error population (TST-303).
## @uses logging.LogRecord.getMessage
## @io Input: caplog pytest fixture. Output: list of str messages of records of this module's logger or of the launcher logger with level ERROR or above, in emission order.
##   Side effects: none. Guarantees: foreign loggers never count. Raises: none. System importance: 6. Example: a missing sibling yields one VALIDATION_FAILURE message.
## @complexity 1
def _errors(caplog):
    # START_BLOCK_BusinessLogic
    return [r.getMessage() for r in caplog.records if r.name in (LOGGER.name, LAUNCHER_LOGGER) and r.levelno >= logging.ERROR]
    # END_BLOCK_BusinessLogic
# endregion FUNC__errors


# region FUNC__clean_env [DOMAIN(6): Tests; CONCEPT(8): ControlledEnvironment; TECH(5): os.environ]
## @purpose Give every child process an environment without interpreter-path or log-level steering, so equality of launcher and direct call cannot depend on the caller's shell.
## @uses os.environ
## @io Input: extra optional dict of str to str applied last. Output: dict of str to str, a copy of os.environ without PYTHONPATH, PYTHONHOME, METHODOLOGY_LAUNCHER_LOG, ORIENT_LOG, CODEMAP_LOG and MARKUP_MIGRATE_LOG, then updated by extra.
##   Side effects: none; os.environ itself is never changed. Guarantees: extra wins over removal. Raises: none for a mapping input. System importance: 7.
##   Example: _clean_env({"METHODOLOGY_LAUNCHER_LOG": "INFO"}) keeps only that one log variable.
## @complexity 2
def _clean_env(extra=None):
    # START_BLOCK_BusinessLogic
    env = {k: v for k, v in os.environ.items() if k not in SCOPED_ENV}
    env.update(extra or {})
    return env
    # END_BLOCK_BusinessLogic
# endregion FUNC__clean_env


# region FUNC__run [DOMAIN(8): ProcessBoundary; CONCEPT(9): CapturedStreams; TECH(7): subprocess]
## @purpose Run one real child process and keep its exact exit status and text streams, printed before any assertion.
## @uses subprocess.run, test_consumer_profile._show
## @io Input: argv list of str; cwd pathlib.Path of an existing directory; env dict of str to str. Output: subprocess.CompletedProcess with text stdout and stderr.
##   Side effects: one child process with captured pipes; an IMP:8 PROCESS record; argv, exit, stdout and stderr printed. Guarantees: no shell; stdin is inherited and never read by the code under test.
##   Raises: OSError when argv[0] cannot be started. System importance: 8. Example: _run([sys.executable, "-c", "print(1)"], cwd, env) returns exit 0 and stdout 1 newline.
## @complexity 2
def _run(argv, cwd, env):
    # START_BLOCK_BusinessLogic
    result = subprocess.run(argv, cwd=str(cwd), env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    LOGGER.info("[IMP:8][_run][PROCESS] exit=%d stdout_lines=%d stderr_lines=%d", result.returncode,
                len(result.stdout.splitlines()), len(result.stderr.splitlines()))
    print("argv", argv, "cwd", cwd)
    print("exit", result.returncode)
    print("stdout", repr(result.stdout))
    print("stderr", repr(result.stderr))
    return result
    # END_BLOCK_BusinessLogic
# endregion FUNC__run


# region FUNC__pair [DOMAIN(9): ProcessBoundary; CONCEPT(10): DirectCallOracle; TECH(7): subprocess]
## @purpose Produce the two results that must be equal: the real launcher run, and the Codex script run directly with python3 -B and the same arguments.
## @uses test_consumer_profile._run, test_consumer_profile._clean_env
## @io Input: interpreter str path; name str, one of orient, codemap, markup-migrate; args list of str; cwd pathlib.Path. Output: tuple of (launcher result, direct result), both subprocess.CompletedProcess, run from the same cwd with the same clean environment.
##   Side effects: two child processes. Guarantees: the launcher is the real file under PACKAGE/bin and the direct call is the real Codex script, so no behavior is copied into the test. Raises: KeyError for an unknown name; OSError when the interpreter cannot start.
##   System importance: 9. Example: _pair(sys.executable, "orient", [str(root), "--check"], cwd) returns the launcher result and the python3 -B orient.py result.
## @complexity 3
def _pair(interpreter, name, args, cwd):
    # START_BLOCK_BusinessLogic
    env = _clean_env()
    launched = _run([interpreter, str(PACKAGE / "bin" / name)] + list(args), cwd, env)
    direct = _run([interpreter, "-B", str(SCRIPTS / LAUNCHERS[name])] + list(args), cwd, env)
    return launched, direct
    # END_BLOCK_BusinessLogic
# endregion FUNC__pair


# region FUNC__assert_pair [DOMAIN(9): ProcessBoundary; CONCEPT(10): ExactEquality; TECH(5): assert]
## @purpose Require that the launcher and the direct call agree on exit status, stdout and stderr, and leave a trace record of the agreement.
## @uses logging.Logger.info
## @io Input: pair tuple of two CompletedProcess; label str naming the case. Output: the common exit status int after (returncode, stdout, stderr) of both are equal.
##   Side effects: one IMP:9 PAIR_EQUAL record. Guarantees: a differing stream or status fails with both triples in the message. Raises: AssertionError on any difference.
##   System importance: 9. Example: two results with exit 0 and the same report text return 0.
## @complexity 2
def _assert_pair(pair, label):
    # START_BLOCK_Validation
    launched, direct = pair
    left = (launched.returncode, launched.stdout, launched.stderr)
    right = (direct.returncode, direct.stdout, direct.stderr)
    assert left == right, "launcher and direct call differ for %s: %r vs %r" % (label, left, right)
    # END_BLOCK_Validation
    # START_BLOCK_Result
    LOGGER.info("[IMP:9][_assert_pair][PAIR_EQUAL] case=%s exit=%d", label, launched.returncode)
    return launched.returncode
    # END_BLOCK_Result
# endregion FUNC__assert_pair


# region FUNC__record [DOMAIN(6): Fixtures; CONCEPT(7): SyntheticRecord; TECH(5): json]
## @purpose Write one filled synthetic front-matter record into a fixture project, with fictional generation provenance and no consent.
## @uses json.dumps, pathlib.Path.write_text
## @io Input: root pathlib.Path of an owned fixture; generated dict of str to str (by, at); name str relative file name; kind str; body str; extra optional dict overriding front-matter fields. Output: None; one UTF-8 file with type, title, generated, status current and extra fields, each value JSON-encoded.
##   Side effects: one file under root. Guarantees: deterministic bytes. Raises: OSError when root is not writable. System importance: 6. Example: a TASKS record with extra batch B-001 and status proposed.
## @complexity 2
def _record(root, generated, name, kind, body, extra=None):
    # START_BLOCK_BusinessLogic
    fields = {"type": kind, "title": "Owned synthetic " + kind, "generated": generated, "status": "current"}
    fields.update(extra or {})
    text = "---\n" + "\n".join(k + ": " + json.dumps(v) for k, v in fields.items()) + "\n---\n\n" + body
    (root / name).write_text(text, encoding="utf-8")
    # END_BLOCK_BusinessLogic
# endregion FUNC__record


# region FUNC__adopted_fixture [DOMAIN(8): Fixtures; CONCEPT(9): AdoptedProject; TECH(6): pathlib]
## @purpose Create the smallest explicitly synthetic project that adopts methodology-consumer-pm/1.0.0 in single-layer mode, so the real orient script can judge it.
## @uses test_consumer_profile._record, pathlib.Path.mkdir, pathlib.Path.write_text
## @io Input: root pathlib.Path that does not exist yet and whose parent exists. Output: root, holding AGENTS.md, CONVENTIONS.md with the profile front matter, VISION.md, ROADMAP.md with one WE ARE HERE marker, a Mermaid block and a Deferred heading, HANDOFF.md with the four headings, TASKS.md with batch B-001 and task T-001, a Doxyfile reading src, and an empty src directory.
##   Side effects: owned files under root only. Guarantees: generation provenance is fictional (claude:test, 2020-01-01T00:00:00Z) and grants nothing. Raises: FileExistsError when root exists.
##   System importance: 8. Example: _adopted_fixture(tmp_path / "project") returns the project path.
## @complexity 3
def _adopted_fixture(root):
    # START_BLOCK_BusinessLogic
    root.mkdir()
    (root / "src").mkdir()
    generated = {"by": "claude:test", "at": "2020-01-01T00:00:00Z"}
    (root / "AGENTS.md").write_text(
        "profile methodology-consumer-pm/1.0.0 conventions_version 1.0.0 mode single-layer layer .\n"
        "Read actual five declared homes; fixtures authenticate no product consent.\n", encoding="utf-8")
    (root / "CONVENTIONS.md").write_text(
        "---\nprofile: methodology-consumer-pm/1.0.0\nconventions_version: 1.0.0\nmode: single-layer\nlayer: .\ntype: Conventions\n"
        "title: Owned synthetic conventions\nstatus: adopted\ngenerated: {by: claude:test, at: \"2020-01-01T00:00:00Z\"}\n---\n",
        encoding="utf-8")
    _record(root, generated, "VISION.md", "Vision", "# Owned record pilot\nGoal: read the bounded queue; arrival is recoverable current state.\n")
    _record(root, generated, "ROADMAP.md", "Roadmap",
            "# Route\n- [ ] **P0.** 🔜 Useful records `<<< WE ARE HERE`\n## Deferred on purpose\n- Product Code held until exact spec.\n"
            "```mermaid\nflowchart LR\nP0[\"P0 🔜 Useful records\"]\n```\n")
    _record(root, generated, "HANDOFF.md", "Handoff",
            "# Handoff\n## Blocked on the owner\n- Product Code and integration remain reserved.\n## State\n"
            "Owned fixture current records; no Git revision or product consent.\n## Queue\nTASKS.md next T-001.\n"
            "## Traps\nDo not promote fixture metadata to authentic consent.\n")
    _record(root, generated, "TASKS.md", "Tasks",
            "# Packet\n## T-001 bounded note\n- **Class:** S\n- **Status:** todo\n- **Done when:** Exact note exists.\n"
            "- **Stop and ask when:** Scope would change.\n- **Links:** P0; VISION.md\n", {"batch": "B-001", "status": "proposed"})
    (root / "Doxyfile").write_text("INPUT = src\nFILE_PATTERNS = *.py\nRECURSIVE = YES\nOUTPUT_DIRECTORY = map\nGENERATE_XML = YES\nXML_OUTPUT = xml\n",
                                   encoding="utf-8")
    return root
    # END_BLOCK_BusinessLogic
# endregion FUNC__adopted_fixture


# region FUNC__source_fixture [DOMAIN(8): Fixtures; CONCEPT(9): SoftwareProject, LegacyMarkup; TECH(6): pathlib]
## @purpose Create an adopted project that also holds a small Python source with a rich contract, in current form or in the legacy summary and structure form, bound to the real Codex Doxyfile seed.
## @uses test_consumer_profile._adopted_fixture, pathlib.Path.read_text
## @io Input: root pathlib.Path that does not exist yet; old bool, default False. Output: root, holding the adopted fixture plus src/records.py (function summarize, contract with GREP_SUMMARY and STRUCTURE in the module contract, or, when old is True, as legacy comment lines after the code) and src/support.py (VALUE = 11), and a Doxyfile made from the Codex seed with INPUT src and OUTPUT_DIRECTORY map (plus a trailing paragraph-closing mark on the invariants alias when old is True).
##   Side effects: owned files under root only; the seed is read, never written. Guarantees: the legacy form leaves exactly two files due for migration, the Doxyfile alias and the source. Raises: OSError when the seed cannot be read.
##   System importance: 8. Example: _source_fixture(tmp_path / "p", old=True) is reported by markup-migrate --check as migration due for 2 files.
## @complexity 3
def _source_fixture(root, old=False):
    # START_BLOCK_BusinessLogic
    _adopted_fixture(root)
    seed = (TEMPLATES / "Doxyfile").read_text(encoding="utf-8")
    config = (seed.replace("INPUT                  = src tests", "INPUT                  = src")
              .replace("OUTPUT_DIRECTORY       = doxygen_output", "OUTPUT_DIRECTORY       = map"))
    (root / "Doxyfile").write_text(config.replace("invariants=@par Invariants:", "invariants=@par Invariants:^^") if old else config,
                                   encoding="utf-8")
    text = ("# region MODULE_CONTRACT\n## @modulecontract\n## @purpose Keep exact count sum.\n## @scope Pure fixture counts.\n"
            "## @input Finite plain counts.\n## @output Exact total.\n## @links [USES_API(7): sum]\n## @invariants\n"
            "## All values counted.\n## Wrapped own paragraph survives.\n## @rationale\n## Q: Why unequal values?\n"
            "## A: Sum differs from first, last and max.\n## @changes\n## LAST_CHANGE: [1.0.0 - owned fixture.]\n## @modulemap\n"
            "## FUNC 9[Sum every value] => records.summarize\n## @usecases\n## Caller -> exact counts ->18.\n"
            "## @GREP_SUMMARY own count sum\n## @STRUCTURE counts to total\ndef _module_contract():\n    pass\n"
            "# endregion MODULE_CONTRACT\n\n# region FUNC_summarize\n## @purpose Return exact unequal-count sum.\n## @uses sum\n"
            "## @io values sequence to total integer; no external effect.\n## @complexity 2\ndef summarize(values):\n"
            "    return sum(values)\n# endregion FUNC_summarize\n")
    if old:
        text = (text.replace("## @GREP_SUMMARY own count sum\n", "").replace("## @STRUCTURE counts to total\n", "")
                + "\n# GREP_SUMMARY: own count sum\n# STRUCTURE: counts to total\n")
    (root / "src/records.py").write_text(text, encoding="utf-8")
    (root / "src/support.py").write_text("VALUE = 11\n", encoding="utf-8")
    return root
    # END_BLOCK_BusinessLogic
# endregion FUNC__source_fixture


# region FUNC__build_map [DOMAIN(8): Fixtures; CONCEPT(9): RealCodeMap, Receipt; TECH(7): doxygen, subprocess]
## @purpose Build the fixture's real Doxygen map silently and write the current map receipt that the Codex codemap script requires, using the read-only Codex helpers.
## @uses subprocess.run, importlib.util.spec_from_file_location, codemap.source_population, consumer_files.identity
## @io Input: root pathlib.Path of a software fixture; monkeypatch pytest fixture. Output: pathlib.Path of map/xml/index.xml after doxygen Doxyfile exited 0 with empty stdout and stderr and the receipt files .methodology/maps/build-001.stdout, .stderr, build-001.json and current.json were written (config and index SHA-256, source identities, argv, cwd, exit, times, environment names, stream paths).
##   Side effects: child process doxygen; files under root only; consumer_files and codemap are loaded read-only from the Codex scripts with bytecode writing disabled and registered in sys.modules through monkeypatch, which undoes both. Guarantees: nothing is written under the Codex directory.
##   Raises: AssertionError when doxygen is absent, exits nonzero or is not silent (no skip); OSError for unreadable resources. System importance: 8. Example: after _build_map(root, monkeypatch) the codemap script answers from the map.
## @complexity 4
def _build_map(root, monkeypatch):
    # START_BLOCK_Validation
    assert shutil.which("doxygen") is not None, "doxygen is required for the map test"
    monkeypatch.setattr(sys, "dont_write_bytecode", True)
    modules = {}
    for name in ("consumer_files", "codemap"):
        spec = importlib.util.spec_from_file_location(name, str(SCRIPTS / (name + ".py")))
        module = importlib.util.module_from_spec(spec)
        monkeypatch.setitem(sys.modules, name, module)
        spec.loader.exec_module(module)
        modules[name] = module
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run(["doxygen", "Doxyfile"], cwd=str(root), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    LOGGER.info("[IMP:8][_build_map][DOXYGEN] exit=%d stdout_bytes=%d stderr_bytes=%d", result.returncode, len(result.stdout), len(result.stderr))
    print("actual Doxygen", result.args, start, result.returncode, repr(result.stdout), repr(result.stderr))
    assert result.returncode == 0 and not result.stdout and not result.stderr
    directory = root / ".methodology/maps"
    directory.mkdir(parents=True, exist_ok=True)
    prefix = "build-%03d" % (len(list(directory.glob("build-*.json"))) + 1)
    (directory / (prefix + ".stdout")).write_text(result.stdout, encoding="utf-8")
    (directory / (prefix + ".stderr")).write_text(result.stderr, encoding="utf-8")
    identity = modules["consumer_files"].identity
    info, population = modules["codemap"].source_population(root)
    index = root / "map/xml/index.xml"
    receipt = {"config": {"path": "Doxyfile", "sha256": identity(root / "Doxyfile")["sha256"]},
               "sources": population.source_identities,
               "index": {"path": "map/xml/index.xml", "sha256": identity(index)["sha256"]},
               "build": {"argv": result.args, "cwd": str(root), "exitCode": result.returncode,
                         "at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "start": start,
                         "environmentNames": sorted(os.environ), "stdout": ".methodology/maps/" + prefix + ".stdout",
                         "stderr": ".methodology/maps/" + prefix + ".stderr"}}
    (directory / (prefix + ".json")).write_text(json.dumps(receipt), encoding="utf-8")
    (directory / "current.json").write_text(json.dumps(receipt), encoding="utf-8")
    LOGGER.info("[IMP:9][_build_map][RECEIPT] build=%s sources=%d", prefix, len(population.source_identities))
    return index
    # END_BLOCK_BusinessLogic
# endregion FUNC__build_map


# region FUNC__owned_checkout [DOMAIN(8): Isolation; CONCEPT(9): OwnedCheckout; TECH(6): shutil.copy2]
## @purpose Give a refusal case its own writable checkout holding byte copies of the three launchers and the four Codex scripts at the paths the launcher resolves.
## @uses shutil.copy2, pathlib.Path.mkdir
## @io Input: base pathlib.Path that does not exist yet. Output: base / checkout, holding implementations/claude/bin/{orient,codemap,markup-migrate} (mode 0o755 asserted) and implementations/codex/skills/pm/scripts/{orient,codemap,markup_migrate,consumer_files}.py.
##   Side effects: owned files under base only. Guarantees: the real package and the Codex package are only read. Raises: AssertionError when a copied launcher is not owner-executable; OSError for unreadable sources.
##   System importance: 8. Example: _owned_checkout(tmp_path / "c1") returns tmp_path/c1/checkout.
## @complexity 3
def _owned_checkout(base):
    # START_BLOCK_BusinessLogic
    checkout = base / "checkout"
    bin_dir = checkout / "implementations/claude/bin"
    script_dir = checkout / "implementations/codex/skills/pm/scripts"
    bin_dir.mkdir(parents=True)
    script_dir.mkdir(parents=True)
    for name in LAUNCHERS:
        shutil.copy2(str(PACKAGE / "bin" / name), str(bin_dir / name))
        assert (bin_dir / name).stat().st_mode & 0o100
    for script in list(LAUNCHERS.values()) + ["consumer_files.py"]:
        shutil.copy2(str(SCRIPTS / script), str(script_dir / script))
    return checkout
    # END_BLOCK_BusinessLogic
# endregion FUNC__owned_checkout


# region FUNC__candidate [DOMAIN(7): Isolation; CONCEPT(8): ExpectedPath; TECH(5): os.path]
## @purpose State independently of the launcher where an owned checkout expects its sibling script, so the refusal tests compare a fixed expectation.
## @uses os.path.realpath, os.path.normpath
## @io Input: checkout pathlib.Path of an owned checkout; script str file name of the Codex script. Output: str normalized absolute path realpath(checkout)/implementations/codex/skills/pm/scripts/script.
##   Side effects: none. Guarantees: no symbolic link below implementations/codex is resolved, because the launcher reports the path where the sibling is expected. Raises: none. System importance: 7.
##   Example: for checkout /t/c1/checkout and orient.py the result is /t/c1/checkout/implementations/codex/skills/pm/scripts/orient.py.
## @complexity 1
def _candidate(checkout, script):
    # START_BLOCK_BusinessLogic
    return os.path.normpath(os.path.join(os.path.realpath(str(checkout)), "implementations/codex/skills/pm/scripts", script))
    # END_BLOCK_BusinessLogic
# endregion FUNC__candidate


# region FUNC__load_launcher [DOMAIN(8): Isolation; CONCEPT(9): ImportWithoutSideEffects; TECH(7): importlib.machinery]
## @purpose Import an owned launcher copy as a module so its pure functions can be called directly, without a sys.path change or a sys.modules entry.
## @uses importlib.machinery.SourceFileLoader, importlib.util.spec_from_loader, importlib.util.module_from_spec
## @io Input: path pathlib.Path of an owned launcher copy (never the real bin file); name str module name. Output: the executed module object; its __name__ is not __main__, so its entry guard does not run.
##   Side effects: executes the launcher's top-level statements (constants and one NullHandler on the launcher logger). Guarantees: sys.path and sys.modules are unchanged. Raises: ImportError or SyntaxError when the file cannot be loaded.
##   System importance: 7. Example: _load_launcher(owned / "orient", "launcher_orient").resolve_sibling(str(owned / "orient")) classifies the sibling.
## @complexity 2
def _load_launcher(path, name):
    # START_BLOCK_BusinessLogic
    loader = importlib.machinery.SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module
    # END_BLOCK_BusinessLogic
# endregion FUNC__load_launcher


# region FUNC__references [DOMAIN(8): InPlaceBinding; CONCEPT(9): ReferenceResolution; TECH(6): re]
## @purpose Count and list every plugin-root reference and every relative Markdown link of a text that does not resolve to an existing path.
## @uses re.Pattern.findall, pathlib.Path.exists
## @io Input: text str; base pathlib.Path, the directory that relative Markdown links are resolved against. Output: tuple of (references int, unresolved list of str); a ${CLAUDE_PLUGIN_ROOT}/path reference resolves against the package root with trailing dots stripped, a link without a scheme or a pure fragment resolves against base with any fragment removed; existence is required.
##   Side effects: file system existence checks. Guarantees: a link with a scheme (for example https) or a pure fragment is not counted. Raises: none for str input. System importance: 8.
##   Example: a text naming ${CLAUDE_PLUGIN_ROOT}/bin/missing returns (1, ["bin/missing"]).
## @complexity 4
def _references(text, base):
    # START_BLOCK_BusinessLogic
    unresolved = []
    plugin = PLUGIN_REFERENCE.findall(text)
    for raw in plugin:
        target = raw.rstrip(".")
        if not (PACKAGE / target).exists():
            unresolved.append(target)
    links = [t for t in MARKDOWN_LINK.findall(text) if "://" not in t and not t.startswith(("#", "mailto:"))]
    for raw in links:
        target = raw.split("#", 1)[0]
        if target and not (base / target).exists():
            unresolved.append(raw)
    return len(plugin) + len(links), unresolved
    # END_BLOCK_BusinessLogic
# endregion FUNC__references


# region FUNC__package_texts [DOMAIN(7): Routing; CONCEPT(8): TextPopulation; TECH(5): pathlib]
## @purpose Read, in one place, the package texts that the carrier and routing predicates judge, keyed by their package-relative path.
## @uses pathlib.Path.read_text, pathlib.Path.glob
## @io Input: none. Output: dict of str package-relative path to str text for every skills/*/SKILL.md, every agents/*.md, references/consumer-pm-profile.md and references/claude-runtime.md.
##   Side effects: file reads only. Guarantees: keys use forward slashes and are sorted by construction. Raises: OSError when a file is unreadable. System importance: 6.
##   Example: the key skills/pm/SKILL.md maps to the text of the pm entry.
## @complexity 2
def _package_texts():
    # START_BLOCK_BusinessLogic
    paths = sorted(PACKAGE.glob("skills/*/SKILL.md")) + sorted(PACKAGE.glob("agents/*.md"))
    paths += [PACKAGE / "references/consumer-pm-profile.md", PACKAGE / "references/claude-runtime.md"]
    return {p.relative_to(PACKAGE).as_posix(): p.read_text(encoding="utf-8") for p in paths}
    # END_BLOCK_BusinessLogic
# endregion FUNC__package_texts


# region FUNC__carrier_problems [DOMAIN(9): Carrier; CONCEPT(10): DeclaredDeltasOnly; TECH(6): re, json]
## @purpose List every way a text fails to be the thin carrier: wrong headings, a missing identity or link, a duty row of its own, an unresolved reference or a malformed hook recipe.
## @uses re.Pattern.findall, json.loads, test_consumer_profile._references
## @io Input: text str of the candidate carrier; base pathlib.Path, the carrier's directory. Output: list of str problems, empty exactly when the text has outside code fences exactly the seven HEADINGS in order, names the profile identity, the relative Codex carrier link, the three plugin-root bin paths, AskUserQuestion, model and .claude/settings.local.json, has no table row starting with CV- or CHECK-, resolves every reference, states the PATH resolution check for bare names (command -v, the absolute launcher path, the markup-migrate --apply rule) without the former same-file promise, states the fixture-local grant without the former blanket fixture-grant sentence, and holds one json fence with exactly one SessionStart entry of one command hook whose command names implementations/claude/bin/orient and $CLAUDE_PROJECT_DIR, merges stderr with 2>&1 and ends with || true.
##   Side effects: none. Guarantees: the same predicate judges the real carrier and the contrary in-memory controls. Raises: none for str input. System importance: 9.
##   Example: a text with an added sixth delta heading returns a heading problem.
## @complexity 8
def _carrier_problems(text, base):
    # START_BLOCK_Validation
    problems = []
    outside, fences, inside, current = [], [], False, []
    for line in text.split("\n"):
        if line.startswith("```"):
            if inside:
                fences.append("\n".join(current))
                current = []
            inside = not inside
            continue
        (current if inside else outside).append(line)
    headings = [line for line in outside if line.startswith("#")]
    if headings != HEADINGS:
        problems.append("headings")
    for needle in (PROFILE, "../../codex/references/consumer-pm-profile.md", BIN + "orient", BIN + "codemap", BIN + "markup-migrate",
                   "AskUserQuestion", "model", ".claude/settings.local.json", "command -v", "absolute launcher path",
                   "`markup-migrate --apply` always", "fixture-local grant", "never stands in for a consumer's batch or result gate"):
        if needle not in text:
            problems.append("missing " + needle)
    if "| CV-" in text or "| CHECK-" in text:
        problems.append("own duty or checker row")
    # BUG_FIX_CONTEXT: Review of M37-C2 candidate 4878641e found that the carrier promised the bare names as the same file and said a fixture grant never authenticates consent.
    # Previous: the predicate pinned only headings, links and the recipe shape, so both statements passed. Problem: another enabled plugin can shadow a bare name, and the Codex route records a fixture-local grant.
    # Fix: pin the PATH resolution check, the absolute-path rule and the fixture-local grant sentence, and reject the former table header and the former blanket sentence.
    for former in ("Same file", "A template, a fixture grant"):
        if former in text:
            problems.append("former statement " + former)
    count, unresolved = _references(text, base)
    problems.extend("unresolved " + item for item in unresolved)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    blocks = re.findall(r"```json\n(.*?)```", text, re.S)
    if len(blocks) != 1:
        problems.append("hook recipe fence count")
        return problems
    # END_BLOCK_BusinessLogic
    # START_BLOCK_ErrorHandling
    try:
        recipe = json.loads(blocks[0])
        entries = recipe["hooks"]["SessionStart"]
        commands = [h for entry in entries for h in entry["hooks"]]
    except (ValueError, KeyError, TypeError):
        problems.append("hook recipe shape")
        return problems
    # END_BLOCK_ErrorHandling
    # START_BLOCK_Result
    if len(entries) != 1 or len(commands) != 1 or commands[0].get("type") != "command":
        problems.append("hook recipe entries")
    else:
        command = commands[0].get("command", "")
        if ("implementations/claude/bin/orient" not in command or "$CLAUDE_PROJECT_DIR" not in command
                or not command.endswith(" 2>&1 || true")):
            problems.append("hook recipe command")
    return problems
    # END_BLOCK_Result
# endregion FUNC__carrier_problems


# region FUNC__routing_problems [DOMAIN(9): Routing; CONCEPT(10): NamedCarrierAndLaunchers; TECH(6): re]
## @purpose List every way the package texts fail the M37 routing: a routed skill without the carrier, the orient launcher or the profile identity, a pm-bootstrap without the other launchers and the templates, a searcher with the wrong tools or no carrier, a stale version signature, or any unresolved reference.
## @uses test_consumer_profile._references
## @io Input: texts dict of str package-relative path to str text, as returned by _package_texts (a mutated copy for a contrary control). Output: list of str problems, empty exactly when the nine ROUTED skills name the carrier and ${CLAUDE_PLUGIN_ROOT}/bin/orient and, except the two IDENTITY_EXEMPT documentation entries, the profile identity; pm-bootstrap also names bin/codemap, bin/markup-migrate, ../codex/skills/pm/templates/ and still the neutral templates index; the searcher names the carrier and bin/codemap and its tools line is exactly Read, Glob, Grep; semantic-exoskeleton and devplan-protocol contain methodology-claude 2.1.0 and no 2.0.2; and no listed text has an unresolved reference.
##   Side effects: none. Guarantees: the same predicate judges the real texts and the contrary in-memory controls. Raises: KeyError when a required text is absent from texts. System importance: 9.
##   Example: pm-bootstrap text without the templates directory name yields a problem naming it.
## @complexity 7
def _routing_problems(texts):
    # START_BLOCK_Validation
    problems = []
    for topic in ROUTED:
        body = texts["skills/%s/SKILL.md" % topic]
        for needle in (CARRIER, BIN + "orient") + (() if topic in IDENTITY_EXEMPT else (PROFILE,)):
            if needle not in body:
                problems.append("%s lacks %s" % (topic, needle))
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    bootstrap = texts["skills/pm-bootstrap/SKILL.md"]
    for needle in (BIN + "codemap", BIN + "markup-migrate", "${CLAUDE_PLUGIN_ROOT}/../codex/skills/pm/templates/",
                   "${CLAUDE_PLUGIN_ROOT}/../../documents/templates/INDEX.md"):
        if needle not in bootstrap:
            problems.append("pm-bootstrap lacks " + needle)
    searcher = texts["agents/searcher.md"]
    tools = re.findall(r"^tools: (.*)$", searcher.split("\n---\n", 1)[0], re.M)
    if tools != ["Read, Glob, Grep"]:
        problems.append("searcher tools")
    for needle in (CARRIER, BIN + "codemap"):
        if needle not in searcher:
            problems.append("searcher lacks " + needle)
    for topic in ("semantic-exoskeleton", "devplan-protocol"):
        body = texts["skills/%s/SKILL.md" % topic]
        if "methodology-claude 2.1.0" not in body or "2.0.2" in body:
            problems.append(topic + " version signature")
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    for relative, body in sorted(texts.items()):
        count, unresolved = _references(body, (PACKAGE / relative).parent)
        problems.extend("%s unresolved %s" % (relative, item) for item in unresolved)
    return problems
    # END_BLOCK_Result
# endregion FUNC__routing_problems


# region FUNC__bare_name_problems [DOMAIN(9): Routing; CONCEPT(10): BareNameShadowing, PathResolutionCheck; TECH(6): str]
## @purpose List every text that promises a bare launcher name (orient, codemap, markup-migrate) without the PATH resolution check, because another enabled plugin may ship a command of the same name and PATH order between plugins is unspecified.
## @uses test_consumer_profile.BARE_ORIENT
## @io Input: readme str, the package README; texts dict of str package-relative path to str text, as returned by _package_texts (a mutated copy for a contrary control). Output: list of str problems, empty exactly when every text of texts and the README that says by bare name or has a backticked bare name also names command -v, the README names the absolute path, and the pm, pm-bootstrap and pm-handoff entries hold the exact BARE_ORIENT parenthetical.
##   Side effects: none. Guarantees: the same predicate judges the real texts and the contrary in-memory controls; it is a finite text predicate, whether the sentence is true is the reviewer's judgment (AC1). Raises: KeyError when a required skill text is absent from texts. System importance: 9.
##   Example: the pm entry with the old parenthetical (bare orient while the package is loaded in place) yields a problem naming pm.
## @complexity 4
def _bare_name_problems(readme, texts):
    # START_BLOCK_Validation
    problems = []
    bodies = dict(texts)
    bodies["README.md"] = readme
    for key, body in sorted(bodies.items()):
        if ("by bare name" in body or "bare `" in body) and "command -v" not in body:
            problems.append("%s promises a bare name without command -v" % key)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for topic in ("pm", "pm-bootstrap", "pm-handoff"):
        if BARE_ORIENT not in texts["skills/%s/SKILL.md" % topic]:
            problems.append("%s lacks the conditional bare orient" % topic)
    if "absolute" not in readme or "markup-migrate --apply" not in readme:
        problems.append("README lacks the absolute path rule")
    return problems
    # END_BLOCK_BusinessLogic
# endregion FUNC__bare_name_problems


# region FUNC__variant [DOMAIN(6): Tests; CONCEPT(8): ContraryControl; TECH(4): dict]
## @purpose Make an in-memory copy of a text map with exactly one fragment replaced, so a contrary control reaches the same predicate as the real texts.
## @uses str.replace
## @io Input: texts dict of str to str; key str present in texts; old str that must occur in texts[key]; new str. Output: a new dict equal to texts except that the first occurrence of old in texts[key] is replaced by new.
##   Side effects: none; texts is not changed. Guarantees: a control that does not change anything fails fast. Raises: AssertionError when old does not occur. System importance: 6.
##   Example: _variant(texts, "agents/searcher.md", "tools: Read, Glob, Grep", "tools: Read, Glob, Grep, Bash").
## @complexity 1
def _variant(texts, key, old, new):
    # START_BLOCK_Validation
    assert old in texts[key], "control fragment not found"
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    changed = dict(texts)
    changed[key] = texts[key].replace(old, new, 1)
    return changed
    # END_BLOCK_BusinessLogic
# endregion FUNC__variant


# region FUNC__one_line [DOMAIN(6): Tests; CONCEPT(9): SingleBlockedLine; TECH(4): str]
## @purpose Require that a captured stderr text is exactly one newline-terminated line that starts with the BLOCKED prefix, and return that line.
## @uses str.splitlines
## @io Input: text str, the captured stderr. Output: str, the single line without its newline.
##   Side effects: none. Guarantees: zero lines, two lines, a missing final newline or a foreign prefix fails. Raises: AssertionError on any violation. System importance: 6.
##   Example: the text methodology-claude BLOCKED: orient sibling script missing: /x plus a newline returns the line without the newline.
## @complexity 1
def _one_line(text):
    # START_BLOCK_Validation
    lines = text.splitlines()
    assert len(lines) == 1 and text.endswith("\n") and lines[0].startswith(BLOCKED_PREFIX), repr(text)
    # END_BLOCK_Validation
    # START_BLOCK_Result
    return lines[0]
    # END_BLOCK_Result
# endregion FUNC__one_line


# region FUNC__decoy [DOMAIN(7): Isolation; CONCEPT(9): NoFallbackProbe; TECH(5): pathlib]
## @purpose Plant a harmless decoy script that proves, by a marker file, whether anything ever executed it.
## @uses pathlib.Path.write_text, pathlib.Path.chmod
## @io Input: path pathlib.Path of the decoy to create; marker pathlib.Path that the decoy writes when run; python bool, True for a Python body and False for a /bin/sh body. Output: None; an executable file at path whose only effect when executed is writing the marker.
##   Side effects: one file under the owned tree. Guarantees: the decoy touches nothing else. Raises: OSError when path is not writable. System importance: 7.
##   Example: a decoy orient.py in a PYTHONPATH directory writes marker-pp-orient only if the launcher ever imports or runs it.
## @complexity 2
def _decoy(path, marker, python):
    # START_BLOCK_BusinessLogic
    body = "import pathlib\npathlib.Path(%r).write_text('ran')\n" % str(marker) if python else "#!/bin/sh\necho ran > '%s'\n" % marker
    path.write_text(body, encoding="utf-8")
    path.chmod(0o755)
    # END_BLOCK_BusinessLogic
# endregion FUNC__decoy


# region FUNC__closed_argv [DOMAIN(8): ProcessBoundary; CONCEPT(9): ClosedDescriptors; TECH(6): sh, exec]
## @purpose Wrap a command so that its process starts with chosen standard descriptors really closed, not redirected to a null device, which is the exact condition under which a Python interpreter reports sys.stdout or sys.stderr as None.
## @uses str.join
## @io Input: argv list of str; closed str made of the digits 1 and 2, empty allowed. Output: list of str, the argv of /bin/sh -c that replaces itself (exec) by argv with each listed descriptor closed through the redirection N>&-.
##   Side effects: none. Guarantees: argv reaches the command as positional parameters, never through shell parsing; descriptor 0 stays as inherited. Raises: none for list and str input. System importance: 7.
##   Example: _closed_argv(["python3", "x.py"], "12") starts python3 x.py with descriptors 1 and 2 closed.
## @complexity 1
def _closed_argv(argv, closed):
    # START_BLOCK_BusinessLogic
    redirections = "".join(" %s>&-" % descriptor for descriptor in closed)
    return ["/bin/sh", "-c", 'exec "$@"' + redirections, "sh"] + list(argv)
    # END_BLOCK_BusinessLogic
# endregion FUNC__closed_argv


# region FUNC__closed_pair [DOMAIN(9): ProcessBoundary; CONCEPT(10): DirectCallOracle, ClosedDescriptors; TECH(7): subprocess]
## @purpose Produce the two results that must be equal when the caller closed a standard stream: the real launcher and the Codex script run directly with python3 -B, both under the same closed descriptors.
## @uses test_consumer_profile._run, test_consumer_profile._closed_argv, test_consumer_profile._clean_env
## @io Input: interpreter str path; name str, one of orient, codemap, markup-migrate; args list of str; cwd pathlib.Path; closed str of the digits 1 and 2; env optional dict of str to str, default the clean environment. Output: tuple of (launcher result, direct result), both subprocess.CompletedProcess, run from the same cwd with the same environment.
##   Side effects: two child processes and one IMP:8 CLOSED_PAIR record. Guarantees: the launcher is the real file under PACKAGE/bin and the direct call is the real Codex script, so no behavior is copied into the test. Raises: KeyError for an unknown name; OSError when /bin/sh or the interpreter cannot start.
##   System importance: 9. Example: _closed_pair(sys.executable, "orient", ["--help"], cwd, "1") returns the launcher result and the python3 -B orient.py --help result, both with descriptor 1 closed.
## @complexity 2
def _closed_pair(interpreter, name, args, cwd, closed, env=None):
    # START_BLOCK_BusinessLogic
    env = _clean_env() if env is None else env
    launched = _run(_closed_argv([interpreter, str(PACKAGE / "bin" / name)] + list(args), closed), cwd, env)
    direct = _run(_closed_argv([interpreter, "-B", str(SCRIPTS / LAUNCHERS[name])] + list(args), closed), cwd, env)
    LOGGER.info("[IMP:8][_closed_pair][CLOSED_PAIR] command=%s closed=%s launcher_exit=%d direct_exit=%d", name, closed or "-",
                launched.returncode, direct.returncode)
    return launched, direct
    # END_BLOCK_BusinessLogic
# endregion FUNC__closed_pair


# region FUNC_test_launchers_are_regular_executable_and_equivalent [DOMAIN(9): Launchers; CONCEPT(9): Structure, Python39; TECH(7): ast, os]
## @purpose Prove that the three launchers are regular owner-executable files with the agreed shebang and Python 3.9 grammar, name the agreed Codex scripts, and differ in no executable statement other than the two constants COMMAND and SCRIPT.
## @uses ast.parse, ast.dump, os.lstat, test_consumer_profile._show
## @io Input: caplog. Output: None after the interpreter version is printed first (AC2 interpreter evidence), each launcher is a regular non-link file with the owner execute bit and the first line #!/usr/bin/env python3, parses with feature_version (3, 9), the three ASTs are identical once the values of COMMAND and SCRIPT are replaced by one placeholder, and the SCRIPT values are exactly orient.py, codemap.py and markup_migrate.py.
##   Side effects: reads the three launcher files. Guarantees: a fourth variation in any executable statement of one launcher fails. Raises: AssertionError on any difference. System importance: 9.
##   Example: a launcher with an extra statement in main changes its normalized AST and fails the equality.
## @complexity 6
def test_launchers_are_regular_executable_and_equivalent(caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    print("interpreter", sys.version)
    dumps, scripts = {}, {}
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for name in LAUNCHERS:
        path = PACKAGE / "bin" / name
        mode = os.lstat(str(path)).st_mode
        text = path.read_text(encoding="utf-8")
        assert stat.S_ISREG(mode) and not path.is_symlink() and mode & 0o100
        assert text.split("\n", 1)[0] == "#!/usr/bin/env python3"
        tree = ast.parse(text, filename=str(path), feature_version=(3, 9))
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) \
                    and node.targets[0].id in ("COMMAND", "SCRIPT"):
                if node.targets[0].id == "SCRIPT":
                    scripts[name] = node.value.value
                node.value = ast.Constant(value="PLACEHOLDER")
        dumps[name] = ast.dump(tree)
        LOGGER.info("[IMP:8][test_launchers_are_regular_executable_and_equivalent][LAUNCHER] name=%s mode=%o bytes=%d", name,
                    stat.S_IMODE(mode), len(text.encode("utf-8")))
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert len(set(dumps.values())) == 1 and len(dumps) == 3
    assert scripts == {"orient": "orient.py", "codemap": "codemap.py", "markup-migrate": "markup_migrate.py"}
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_launchers_are_regular_executable_and_equivalent


# region FUNC_test_resolve_sibling_refuses_unusable_siblings [DOMAIN(9): Launchers; CONCEPT(10): SiblingClassification; TECH(7): importlib, os.symlink]
## @purpose Prove that resolve_sibling of each owned launcher copy classifies a usable sibling as ok and a missing file, a directory, a symbolic link and a parent link that escapes the checkout as missing, not-regular, not-regular and outside, each with exactly one ERROR record of its own.
## @uses test_consumer_profile._owned_checkout, test_consumer_profile._load_launcher, test_consumer_profile._candidate, test_consumer_profile._errors, test_consumer_profile._show, orient.resolve_sibling, codemap.resolve_sibling, markup-migrate.resolve_sibling
## @io Input: tmp_path and caplog. Output: None after, for each of the three launchers, one ok case with no ERROR record and four refusal cases in fresh owned checkouts, each returning (None, the expected candidate, the expected cause) and exactly one ERROR record from the launcher logger beginning with the bracketed VALIDATION_FAILURE event, command and cause.
##   Side effects: owned checkouts and links under tmp_path only. Guarantees: the real bin files are never loaded; the escaping case moves the Codex directory outside the checkout and links it back. Raises: AssertionError on any difference. System importance: 9.
##   Example: replacing the sibling by a symbolic link to another regular script inside the checkout gives not-regular, never ok.
## @complexity 7
def test_resolve_sibling_refuses_unusable_siblings(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO)
    counter = 0
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for command, script in LAUNCHERS.items():
        counter += 1
        checkout = _owned_checkout(tmp_path / ("case%d" % counter))
        module = _load_launcher(checkout / "implementations/claude/bin" / command, "launcher_" + command.replace("-", "_"))
        launcher = str(checkout / "implementations/claude/bin" / command)
        expected = _candidate(checkout, script)
        assert module.COMMAND == command and module.SCRIPT == script
        assert module.resolve_sibling(launcher) == (expected, expected, "ok")
        _show(caplog.records)
        assert _errors(caplog) == []
        caplog.clear()
        for cause in ("missing", "directory", "link", "outside"):
            counter += 1
            checkout = _owned_checkout(tmp_path / ("case%d" % counter))
            sibling = checkout / "implementations/codex/skills/pm/scripts" / script
            launcher = str(checkout / "implementations/claude/bin" / command)
            if cause == "missing":
                sibling.unlink()
            elif cause == "directory":
                sibling.unlink()
                sibling.mkdir()
            elif cause == "link":
                other = sibling.parent / "consumer_files.py"
                sibling.unlink()
                os.symlink(str(other), str(sibling))
            else:
                outside = tmp_path / ("outside%d" % counter)
                outside.mkdir()
                shutil.move(str(checkout / "implementations/codex"), str(outside / "codex"))
                os.symlink(str(outside / "codex"), str(checkout / "implementations/codex"))
            want = {"missing": "missing", "directory": "not-regular", "link": "not-regular", "outside": "outside"}[cause]
            answer = module.resolve_sibling(launcher)
            _show(caplog.records)
            LOGGER.info("[IMP:9][test_resolve_sibling_refuses_unusable_siblings][CLASSIFIED] command=%s case=%s cause=%s", command, cause, want)
            assert answer == (None, _candidate(checkout, script), want)
            errors = _errors(caplog)
            assert len(errors) == 1
            assert errors[0].startswith("[IMP:10][resolve_sibling][VALIDATION_FAILURE] command=%s cause=%s" % (command, want))
            assert [r.name for r in caplog.records if r.levelno >= logging.ERROR] == [LAUNCHER_LOGGER]
            caplog.clear()
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_resolve_sibling_refuses_unusable_siblings


# region FUNC_test_main_reports_blocked_without_running [DOMAIN(9): Launchers; CONCEPT(10): BlockedNotDegraded; TECH(7): capsys, monkeypatch]
## @purpose Prove that main of an owned launcher copy answers every refusal and failure branch with return value 2, empty stdout and exactly one methodology-claude BLOCKED line on stderr, and never runs anything: a missing sibling, an empty interpreter path and an interpreter that cannot start.
## @uses test_consumer_profile._owned_checkout, test_consumer_profile._load_launcher, test_consumer_profile._candidate, test_consumer_profile._one_line, test_consumer_profile._errors, test_consumer_profile._show, orient.main
## @io Input: tmp_path, capsys, caplog and monkeypatch. Output: None after (a) a missing sibling gives the BLOCKED line naming the candidate and one VALIDATION_FAILURE record, (b) a present sibling with sys.executable set to an empty string gives the no-interpreter line and one INTERPRETER_FAILURE record, (c) a present sibling with sys.executable set to a path that does not exist (asserted first) gives the could-not-start line and one EXEC_FAILURE record; every case returns 2 with empty stdout.
##   Side effects: owned checkouts under tmp_path; sys.executable and the log variable are patched and restored by monkeypatch. Guarantees: the success branch of main is never called, because it would replace the test process. Raises: AssertionError on any difference. System importance: 9.
##   Example: main([]) on a checkout without orient.py returns 2 and prints one line starting methodology-claude BLOCKED: orient sibling script missing.
## @complexity 6
def test_main_reports_blocked_without_running(tmp_path, capsys, caplog, monkeypatch):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO)
    monkeypatch.delenv("METHODOLOGY_LAUNCHER_LOG", raising=False)
    checkout = _owned_checkout(tmp_path / "blocked")
    module = _load_launcher(checkout / "implementations/claude/bin/orient", "launcher_orient_main")
    candidate = _candidate(checkout, "orient.py")
    absent = str(tmp_path / "absent-interpreter")
    assert not os.path.exists(absent)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    sibling = checkout / "implementations/codex/skills/pm/scripts/orient.py"
    saved = sibling.read_bytes()
    sibling.unlink()
    assert module.main([]) == 2
    out, err = capsys.readouterr()
    with capsys.disabled():
        _show(caplog.records)
        print("stdout", repr(out), "stderr", repr(err))
    assert out == "" and _one_line(err) == BLOCKED_PREFIX + "orient sibling script missing: " + candidate
    assert len(_errors(caplog)) == 1 and "[IMP:10][resolve_sibling][VALIDATION_FAILURE] command=orient cause=missing" in _errors(caplog)[0]
    caplog.clear()
    sibling.write_bytes(saved)
    monkeypatch.setattr(sys, "executable", "")
    assert module.main([]) == 2
    out, err = capsys.readouterr()
    with capsys.disabled():
        _show(caplog.records)
        print("stdout", repr(out), "stderr", repr(err))
    assert out == "" and _one_line(err) == BLOCKED_PREFIX + "orient has no current interpreter path"
    assert _errors(caplog) == ["[IMP:10][main][INTERPRETER_FAILURE] command=orient cause=no-interpreter"]
    caplog.clear()
    monkeypatch.setattr(sys, "executable", absent)
    assert module.main([]) == 2
    out, err = capsys.readouterr()
    with capsys.disabled():
        _show(caplog.records)
        print("stdout", repr(out), "stderr", repr(err))
    line = _one_line(err)
    assert out == "" and line.startswith(BLOCKED_PREFIX + "orient could not start the current interpreter (") and line.endswith(")")
    assert len(_errors(caplog)) == 1 and _errors(caplog)[0].startswith("[IMP:10][main][EXEC_FAILURE] command=orient kind=")
    # END_BLOCK_BusinessLogic
# endregion FUNC_test_main_reports_blocked_without_running


# region FUNC_test_orient_launcher_equals_direct_call [DOMAIN(9): Launchers, Orient; CONCEPT(10): DirectCallOracle; TECH(7): subprocess]
## @purpose Prove that the real bin/orient equals a direct python3 -B call of the Codex orient script on an adopted fixture: a clean read, a clean check, a defective check that reports its row, and a two-root portfolio, without changing a fixture byte.
## @uses test_consumer_profile._adopted_fixture, test_consumer_profile._pair, test_consumer_profile._assert_pair, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after: orient PROJECT exits 0; orient PROJECT --check exits 0 with a line containing CHECK-22 PASS and no line containing a FAIL status; orient --portfolio ROOT ROOT --check exits 0 with exactly two lines equal to the profile identity line; after the WE ARE HERE marker is removed from ROADMAP the check exits 1 with a line starting CHECK-02 FAIL; every pair is equal and every fixture byte is unchanged after the restore.
##   Side effects: two owned fixtures and child processes under tmp_path. Guarantees: expected exit codes and rows are fixed here, not derived from the output. Raises: AssertionError on any difference. System importance: 10.
##   Example: the defect case shows that the launcher passes exit status 1 through unchanged.
## @complexity 6
def test_orient_launcher_equals_direct_call(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    root = _adopted_fixture(tmp_path / "project")
    second = _adopted_fixture(tmp_path / "second")
    before = {str(p): p.read_bytes() for base in (root, second) for p in base.rglob("*") if p.is_file()}
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    plain = _pair(sys.executable, "orient", [str(root)], tmp_path)
    assert _assert_pair(plain, "orient PROJECT") == 0
    check = _pair(sys.executable, "orient", [str(root), "--check"], tmp_path)
    assert _assert_pair(check, "orient PROJECT --check") == 0
    assert "CHECK-22 PASS" in check[0].stdout and not [line for line in check[0].stdout.splitlines() if " FAIL " in line]
    portfolio = _pair(sys.executable, "orient", ["--portfolio", str(root), str(second), "--check"], tmp_path)
    assert _assert_pair(portfolio, "orient --portfolio") == 0
    assert sum(line == "profile: methodology-consumer-pm/1.0.0" for line in portfolio[0].stdout.splitlines()) == 2
    roadmap = root / "ROADMAP.md"
    original = roadmap.read_bytes()
    roadmap.write_bytes(original.replace(" `<<< WE ARE HERE`".encode("utf-8"), b""))
    assert roadmap.read_bytes() != original
    defect = _pair(sys.executable, "orient", [str(root), "--check"], tmp_path)
    assert _assert_pair(defect, "orient defect") == 1
    assert [line for line in defect[0].stdout.splitlines() if line.startswith("CHECK-02 FAIL")]
    roadmap.write_bytes(original)
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert {str(p): p.read_bytes() for base in (root, second) for p in base.rglob("*") if p.is_file()} == before
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_orient_launcher_equals_direct_call


# region FUNC_test_codemap_launcher_equals_direct_call_on_built_map [DOMAIN(9): Launchers, CodeMap; CONCEPT(10): DirectCallOracle, RealMap; TECH(7): subprocess, doxygen]
## @purpose Prove that the real bin/codemap equals a direct python3 -B call of the Codex codemap script on a fixture whose Doxygen map is really built and receipted: a symbol answer from the map, a file answer and a not-found answer with exit 1.
## @uses test_consumer_profile._source_fixture, test_consumer_profile._build_map, test_consumer_profile._pair, test_consumer_profile._assert_pair, test_consumer_profile._show
## @io Input: tmp_path, caplog and monkeypatch. Output: None after doxygen is found on PATH (asserted, never skipped); codemap PROJECT summarize exits 0 with a line symbol: records.summarize and a line starting source: Doxygen:; codemap PROJECT src/records.py exits 0 with a line file: src/records.py; codemap PROJECT nosuchsymbol exits 1 with stdout exactly codemap: not found and a newline; every pair is equal.
##   Side effects: one owned fixture, one doxygen run and child processes under tmp_path. Guarantees: the answers come from the built map, because the receipt names its index and sources. Raises: AssertionError on any difference or a missing doxygen. System importance: 10.
##   Example: the symbol answer carries the map source label, which a fallback to raw source would not.
## @complexity 5
def test_codemap_launcher_equals_direct_call_on_built_map(tmp_path, caplog, monkeypatch):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    assert shutil.which("doxygen") is not None
    root = _source_fixture(tmp_path / "project")
    index = _build_map(root, monkeypatch)
    assert index.is_file()
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    symbol = _pair(sys.executable, "codemap", [str(root), "summarize"], tmp_path)
    assert _assert_pair(symbol, "codemap symbol") == 0
    lines = symbol[0].stdout.splitlines()
    assert "symbol: records.summarize" in lines and [line for line in lines if line.startswith("source: Doxygen:")]
    target = _pair(sys.executable, "codemap", [str(root), "src/records.py"], tmp_path)
    assert _assert_pair(target, "codemap file") == 0
    assert "file: src/records.py" in target[0].stdout.splitlines()
    missing = _pair(sys.executable, "codemap", [str(root), "nosuchsymbol"], tmp_path)
    assert _assert_pair(missing, "codemap not found") == 1
    assert missing[0].stdout == "codemap: not found\n"
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_codemap_launcher_equals_direct_call_on_built_map


# region FUNC_test_markup_migrate_check_equals_direct_call [DOMAIN(9): Launchers, MarkupMigrate; CONCEPT(10): DirectCallOracle, ReadOnlyCheck; TECH(7): subprocess]
## @purpose Prove that the real bin/markup-migrate --check equals a direct python3 -B call of the Codex script for current markup (up to date) and legacy markup (migration due), and that the check changes no source byte.
## @uses test_consumer_profile._source_fixture, test_consumer_profile._pair, test_consumer_profile._assert_pair, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after the current fixture exits 0 with stdout ending markup-migrate: up to date and a newline, the legacy fixture exits 1 with a line markup-migrate: migration due: 2 files (its Doxyfile alias with the paragraph-closing mark and its legacy source markup are the two due files, named by their diff headers), both pairs are equal, and the bytes under src of both fixtures are unchanged.
##   Side effects: two owned fixtures and child processes under tmp_path. Guarantees: the check mode writes nothing. Raises: AssertionError on any difference. System importance: 10.
##   Example: the legacy form leaves summary and structure as trailing comment lines and a paragraph-closing mark on the invariants alias, so exactly two files are due.
## @complexity 5
def test_markup_migrate_check_equals_direct_call(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    current = _source_fixture(tmp_path / "current")
    legacy = _source_fixture(tmp_path / "legacy", old=True)
    before = {str(p): p.read_bytes() for base in (current, legacy) for p in (base / "src").rglob("*") if p.is_file()}
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    up_to_date = _pair(sys.executable, "markup-migrate", [str(current), "--check"], tmp_path)
    assert _assert_pair(up_to_date, "markup-migrate current") == 0
    assert up_to_date[0].stdout.endswith("markup-migrate: up to date\n")
    due = _pair(sys.executable, "markup-migrate", [str(legacy), "--check"], tmp_path)
    assert _assert_pair(due, "markup-migrate legacy") == 1
    assert "markup-migrate: migration due: 2 files" in due[0].stdout.splitlines()
    assert "--- a/Doxyfile" in due[0].stdout.splitlines() and "--- a/src/records.py" in due[0].stdout.splitlines()
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert {str(p): p.read_bytes() for base in (current, legacy) for p in (base / "src").rglob("*") if p.is_file()} == before
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_markup_migrate_check_equals_direct_call


# region FUNC_test_arguments_and_exit_status_pass_through [DOMAIN(9): Launchers; CONCEPT(9): ArgumentPassThrough, NoCwdDefault; TECH(7): subprocess]
## @purpose Prove for all three launchers that no argument gives exit 2 from inside an adopted project (no working-directory default), --help gives exit 0, and an argument with a space and a non-ASCII letter reaches the script unchanged and gives the same nonzero exit and streams as the direct call.
## @uses test_consumer_profile._adopted_fixture, test_consumer_profile._pair, test_consumer_profile._assert_pair, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after, for each launcher, three equal pairs: no argument from cwd inside the fixture (exit 2), --help (exit 0), and the single argument tmp_path/dir with space ü naming a missing directory (equal nonzero exit and equal streams).
##   Side effects: one owned fixture and 18 child processes. Guarantees: the launcher adds no default project and no option. Raises: AssertionError on any difference. System importance: 9.
##   Example: bin/orient with no argument inside an adopted project still exits 2 like the script does.
## @complexity 5
def test_arguments_and_exit_status_pass_through(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    root = _adopted_fixture(tmp_path / "project")
    odd = str(tmp_path / "dir with space ü")
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for name in LAUNCHERS:
        assert _assert_pair(_pair(sys.executable, name, [], root), name + " no argument") == 2
        helped = _pair(sys.executable, name, ["--help"], root)
        assert _assert_pair(helped, name + " --help") == 0 and "usage:" in helped[0].stdout
        strange = _pair(sys.executable, name, [odd], root)
        assert _assert_pair(strange, name + " odd argument") != 0
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_arguments_and_exit_status_pass_through


# region FUNC_test_missing_sibling_blocks_without_fallback [DOMAIN(9): Launchers; CONCEPT(10): BlockedNotDegraded, NoFallback; TECH(7): subprocess, decoys]
## @purpose Prove for all three launchers that a missing sibling, a directory sibling and an escaping sibling link each give exit 2, empty stdout and exactly one BLOCKED line naming the real expected path, and that decoy scripts in the working directory, on PYTHONPATH and on PATH are never executed.
## @uses test_consumer_profile._owned_checkout, test_consumer_profile._candidate, test_consumer_profile._clean_env, test_consumer_profile._decoy, test_consumer_profile._run, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after nine child processes (three launchers times three defects) each give returncode 2, stdout empty, stderr exactly BLOCKED_PREFIX plus command, sibling script, the state (missing, not a regular file, outside the checkout), a colon and the owned candidate, and none of the marker files written by the decoys exists.
##   Side effects: owned checkouts, decoys and markers under tmp_path. Guarantees: no other location is consulted. Raises: AssertionError on any difference. System importance: 10.
##   Example: a decoy orient.py on PYTHONPATH that writes a marker file leaves no marker after the refused run.
## @complexity 7
def test_missing_sibling_blocks_without_fallback(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    cwd = tmp_path / "cwd"
    pythonpath = tmp_path / "pp"
    pathbin = tmp_path / "pathbin"
    for directory in (cwd, pythonpath, pathbin):
        directory.mkdir()
    markers = []
    for command, script in LAUNCHERS.items():
        for place, directory, name, python in (("cwd", cwd, script, True), ("pp", pythonpath, script, True),
                                               ("path-script", pathbin, script, False), ("path-command", pathbin, command, False)):
            marker = tmp_path / ("marker-%s-%s" % (place, command))
            markers.append(marker)
            _decoy(directory / name, marker, python)
    env = _clean_env({"PYTHONPATH": str(pythonpath), "PATH": str(pathbin) + os.pathsep + os.environ.get("PATH", "")})
    states = {"missing": "missing", "directory": "not a regular file", "outside": "outside the checkout"}
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for command, script in LAUNCHERS.items():
        for defect, state in states.items():
            checkout = _owned_checkout(tmp_path / ("%s-%s" % (command, defect)))
            sibling = checkout / "implementations/codex/skills/pm/scripts" / script
            if defect == "missing":
                sibling.unlink()
            elif defect == "directory":
                sibling.unlink()
                sibling.mkdir()
            else:
                outside = tmp_path / ("outside-%s" % command)
                outside.mkdir()
                shutil.move(str(checkout / "implementations/codex"), str(outside / "codex"))
                os.symlink(str(outside / "codex"), str(checkout / "implementations/codex"))
            result = _run([sys.executable, str(checkout / "implementations/claude/bin" / command), "x"], cwd, env)
            expected = BLOCKED_PREFIX + "%s sibling script %s: %s\n" % (command, state, _candidate(checkout, script))
            LOGGER.info("[IMP:9][test_missing_sibling_blocks_without_fallback][REFUSED] command=%s defect=%s exit=%d", command, defect, result.returncode)
            assert (result.returncode, result.stdout, result.stderr) == (2, "", expected)
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert [m for m in markers if m.exists()] == []
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_missing_sibling_blocks_without_fallback


# region FUNC_test_symlinked_launcher_resolves_real_package [DOMAIN(9): Launchers; CONCEPT(9): RealPathResolution; TECH(7): os.symlink, subprocess]
## @purpose Prove that a symbolic link to the real launcher still resolves the real package and its sibling script (equal to the direct call), and that a link to an owned launcher whose sibling is missing is refused naming the owned checkout's candidate and not a path beside the link.
## @uses test_consumer_profile._adopted_fixture, test_consumer_profile._owned_checkout, test_consumer_profile._candidate, test_consumer_profile._run, test_consumer_profile._clean_env, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after orient reached through tmp_path/links/orient equals the direct call for orient PROJECT --check (exit 0), and the link to an owned launcher gives exit 2, empty stdout and exactly one BLOCKED line equal to the expected one for the owned candidate, which contains no links directory component.
##   Side effects: owned links, fixture and checkout under tmp_path. Guarantees: launchers are resolved through realpath. Raises: AssertionError on any difference. System importance: 9.
##   Example: a link /t/links/orient to /pkg/bin/orient resolves /pkg as the package root, not /t.
## @complexity 5
def test_symlinked_launcher_resolves_real_package(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    root = _adopted_fixture(tmp_path / "project")
    links = tmp_path / "links"
    links.mkdir()
    os.symlink(str(PACKAGE / "bin/orient"), str(links / "orient"))
    checkout = _owned_checkout(tmp_path / "owned")
    (checkout / "implementations/codex/skills/pm/scripts/orient.py").unlink()
    os.symlink(str(checkout / "implementations/claude/bin/orient"), str(links / "owned-orient"))
    env = _clean_env()
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    through = _run([sys.executable, str(links / "orient"), str(root), "--check"], tmp_path, env)
    direct = _run([sys.executable, "-B", str(SCRIPTS / "orient.py"), str(root), "--check"], tmp_path, env)
    assert _assert_pair((through, direct), "orient through a link") == 0
    refused = _run([sys.executable, str(links / "owned-orient"), str(root), "--check"], tmp_path, env)
    expected = BLOCKED_PREFIX + "orient sibling script missing: " + _candidate(checkout, "orient.py") + "\n"
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert (refused.returncode, refused.stdout, refused.stderr) == (2, "", expected)
    assert str(links) not in refused.stderr
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_symlinked_launcher_resolves_real_package


# region FUNC_test_shebang_invocation_equals_direct_call [DOMAIN(9): Launchers; CONCEPT(9): ShebangExecution; TECH(7): subprocess, shutil.which]
## @purpose Prove that executing the launcher file itself, as the plugin bin on PATH does, equals a direct python3 -B call of the Codex orient script on the interpreter that python3 resolves to.
## @uses test_consumer_profile._adopted_fixture, test_consumer_profile._clean_env, test_consumer_profile._run, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after python3 is found on the child PATH (asserted), the launcher file executed directly with PROJECT and --check gives the same exit status, stdout and stderr as that python3 -B orient.py PROJECT --check, and the exit status is 0.
##   Side effects: one owned fixture and two child processes. Guarantees: the shebang line is exercised, not the explicit interpreter form. Raises: AssertionError on any difference or a missing python3. System importance: 9.
##   Example: bin/orient PROJECT --check runs with the first python3 of PATH, exactly as in a Claude Code Bash tool.
## @complexity 4
def test_shebang_invocation_equals_direct_call(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    root = _adopted_fixture(tmp_path / "project")
    env = _clean_env()
    python = shutil.which("python3", path=env["PATH"])
    assert python is not None
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    launched = _run([str(PACKAGE / "bin/orient"), str(root), "--check"], tmp_path, env)
    direct = _run([python, "-B", str(SCRIPTS / "orient.py"), str(root), "--check"], tmp_path, env)
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert _assert_pair((launched, direct), "orient by shebang") == 0
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_shebang_invocation_equals_direct_call


# region FUNC_test_launcher_trace_is_owned_and_ordered [DOMAIN(9): Launchers, Observability; CONCEPT(9): OwnedTrajectory, OptIn; TECH(7): subprocess, stderr]
## @purpose Prove that METHODOLOGY_LAUNCHER_LOG=INFO shows the launcher's own trajectory in order on the real stderr (trace on, init, resolve, validation success, exec; and on refusal resolve, one validation failure, blocked answer, then the BLOCKED line), and that with the variable unset a successful run carries no launcher line.
## @uses test_consumer_profile._owned_checkout, test_consumer_profile._candidate, test_consumer_profile._clean_env, test_consumer_profile._run, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after the real bin/orient --help with INFO gives exit 0 and a stderr that starts with the five expected records in that order and holds no IMP:10 record; an owned launcher with a missing sibling gives exit 2 and the stderr lines TRACE_ON, INIT, RESOLVE, one VALIDATION_FAILURE with cause missing and kind FileNotFoundError, BLOCKED_ANSWER, then the BLOCKED line; the unset run has no line containing [IMP:.
##   Side effects: child processes and one owned checkout. Guarantees: the whole stderr of every run is read (LDD-801), not a filtered excerpt. Raises: AssertionError on any difference. System importance: 9.
##   Example: argc is 1 for the single argument --help.
## @complexity 6
def test_launcher_trace_is_owned_and_ordered(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    traced = _clean_env({"METHODOLOGY_LAUNCHER_LOG": "INFO"})
    checkout = _owned_checkout(tmp_path / "owned")
    (checkout / "implementations/codex/skills/pm/scripts/orient.py").unlink()
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    head = ["[IMP:5][_configure_logging][TRACE_ON] level=INFO", "[IMP:4][main][INIT] command=orient argc=1",
            "[IMP:7][resolve_sibling][RESOLVE] command=orient", "[IMP:9][resolve_sibling][VALIDATION_SUCCESS] command=orient cause=ok",
            "[IMP:8][main][EXEC] command=orient argc=1"]
    success = _run([sys.executable, str(PACKAGE / "bin/orient"), "--help"], tmp_path, traced)
    assert success.returncode == 0
    assert success.stderr.splitlines() == head
    assert "[IMP:10]" not in success.stderr
    refused = _run([sys.executable, str(checkout / "implementations/claude/bin/orient"), "--help"], tmp_path, traced)
    blocked = BLOCKED_PREFIX + "orient sibling script missing: " + _candidate(checkout, "orient.py")
    assert refused.returncode == 2 and refused.stdout == ""
    assert refused.stderr.splitlines() == [head[0], head[1], head[2],
                                           "[IMP:10][resolve_sibling][VALIDATION_FAILURE] command=orient cause=missing kind=FileNotFoundError",
                                           "[IMP:9][main][BLOCKED_ANSWER] command=orient exit=2", blocked]
    quiet = _run([sys.executable, str(PACKAGE / "bin/orient"), "--help"], tmp_path, _clean_env())
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert quiet.returncode == 0 and quiet.stderr == "" and "[IMP:" not in quiet.stdout
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_launcher_trace_is_owned_and_ordered


# region FUNC_test_launcher_never_writes_bytecode_beside_codex_scripts [DOMAIN(9): Launchers; CONCEPT(9): CodexBytesUntouched, DashB; TECH(7): subprocess, pycache prefix]
## @purpose Prove that the -B option of the launcher keeps every bytecode cache of the Codex scripts from being written even when the environment would allow caches, with a control that shows the probe can see a cache when -B is absent.
## @uses test_consumer_profile._adopted_fixture, test_consumer_profile._owned_checkout, test_consumer_profile._clean_env, test_consumer_profile._run, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after a launcher run from an owned checkout, with PYTHONDONTWRITEBYTECODE removed and PYTHONPYCACHEPREFIX pointing at an absent owned directory, exits 0 and writes no .pyc file for any owned Codex script under that prefix (the interpreter may cache its own standard library there) and leaves no __pycache__ beside the owned Codex scripts, while a control run of the same owned script without -B and with its own cache prefix exits 0 and writes at least one .pyc file for an owned Codex script there.
##   Side effects: two owned checkouts, one fixture and two child processes under tmp_path. Guarantees: the real Codex directory is not used, and the cache prefix makes the probe independent of an interpreter whose default cache location is not beside the source. Raises: AssertionError on any difference. System importance: 9.
##   Example: dropping -B from the launcher exec list makes the first assertion fail because consumer_files is imported and cached.
## @complexity 4
def test_launcher_never_writes_bytecode_beside_codex_scripts(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    root = _adopted_fixture(tmp_path / "project")
    through = _owned_checkout(tmp_path / "through")
    control = _owned_checkout(tmp_path / "control")
    prefix_through = tmp_path / "cache-through"
    prefix_control = tmp_path / "cache-control"
    env = _clean_env()
    env.pop("PYTHONDONTWRITEBYTECODE", None)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    env.update({"PYTHONPYCACHEPREFIX": str(prefix_through)})
    launched = _run([sys.executable, str(through / "implementations/claude/bin/orient"), str(root), "--check"], tmp_path, env)
    env.update({"PYTHONPYCACHEPREFIX": str(prefix_control)})
    plain = _run([sys.executable, str(control / "implementations/codex/skills/pm/scripts/orient.py"), str(root), "--check"], tmp_path, env)
    marker = "implementations/codex/skills/pm/scripts"
    cached_through = sorted(p for p in prefix_through.rglob("*.pyc") if marker in p.as_posix()) if prefix_through.exists() else []
    cached_control = sorted(p for p in prefix_control.rglob("*.pyc") if marker in p.as_posix()) if prefix_control.exists() else []
    beside = [p for base in (through, control) for p in (base / "implementations/codex").rglob("__pycache__")]
    LOGGER.info("[IMP:9][test_launcher_never_writes_bytecode_beside_codex_scripts][CACHES] launcher=%d control=%d beside=%d",
                len(cached_through), len(cached_control), len(beside))
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert launched.returncode == 0 and plain.returncode == 0
    assert cached_through == [] and beside == []
    assert len(cached_control) >= 1
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_launcher_never_writes_bytecode_beside_codex_scripts


# region FUNC_test_launchers_pass_through_with_closed_standard_streams [DOMAIN(9): Launchers; CONCEPT(10): ClosedStreamPassThrough, DirectCallOracle; TECH(7): subprocess, sh]
## @purpose Prove for all three launchers that a caller who closes stdout, stderr or both still gets the Codex script run, with its own exit status and remaining stream unchanged: --help equals the direct python3 -B call (exit 0 with either one stream closed), a missing project gives the same nonzero status, orient --check on an adopted fixture gives the script's own 0 (clean) and 1 (defect) whatever is closed, and the opt-in launcher trace is harmless while stderr is closed.
## @uses test_consumer_profile._closed_pair, test_consumer_profile._assert_pair, test_consumer_profile._adopted_fixture, test_consumer_profile._clean_env, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after, for each launcher and each of the closed sets 1, 2 and 12, the --help pair is equal with no Traceback text (and exit 0 for 1 and 2, usage on the launcher stdout exactly when descriptor 1 is open) and the missing-project pair is equal with a nonzero status; for each closed set orient PROJECT --check is equal to the direct call with exit 0 on the clean fixture and exit 1 once the WE ARE HERE marker is removed; the traced orient --help pair with descriptor 2 closed is equal with exit 0.
##   Side effects: one owned fixture and child processes only; the project argument of the refusal names a directory that does not exist. Guarantees: the closed descriptor is really closed by the shell redirection, so the child interpreter sees sys.stdout or sys.stderr as None; the oracle is the Codex script itself, and the fixed 0 and 1 are independent of the interpreter version (with both streams closed Python 3.9 argparse exits 1 on --help by itself, so that one pair is compared, not pinned). Raises: AssertionError on any difference. System importance: 10.
##   Example: bin/codemap --help with descriptor 1 closed exits 0 like python3 -B codemap.py --help; on the former bytes it ended with an AttributeError on sys.stdout.flush and exit 1.
## @complexity 7
def test_launchers_pass_through_with_closed_standard_streams(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    absent = str(tmp_path / "absent project")
    assert not os.path.exists(absent)
    root = _adopted_fixture(tmp_path / "project")
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    # BUG_FIX_CONTEXT: the Review of M37-C2 candidate 4878641e showed the launchers ending with an AttributeError (exit 1) when descriptor 1 or 2 was closed.
    # Previous: every pass-through test ran with both streams open, so the unconditional sys.stdout.flush() and sys.stderr.flush() before the exec were never exercised on None.
    # Problem: a closed descriptor makes the interpreter set the stream to None, the flush raised, and the Codex script never ran. Fix: close the descriptors for real and require the direct-call result.
    for name in LAUNCHERS:
        for closed in ("1", "2", "12"):
            helped = _closed_pair(sys.executable, name, ["--help"], tmp_path, closed)
            status = _assert_pair(helped, "%s --help closed=%s" % (name, closed))
            assert status == 0 or closed == "12"
            assert ("usage:" in helped[0].stdout) == ("1" not in closed)
            assert "Traceback" not in helped[0].stderr
            missing = _closed_pair(sys.executable, name, [absent], tmp_path, closed)
            assert _assert_pair(missing, "%s missing project closed=%s" % (name, closed)) != 0
            assert "Traceback" not in missing[0].stderr
    for closed in ("1", "2", "12"):
        clean = _closed_pair(sys.executable, "orient", [str(root), "--check"], tmp_path, closed)
        assert _assert_pair(clean, "orient --check clean closed=%s" % closed) == 0
    roadmap = root / "ROADMAP.md"
    original = roadmap.read_bytes()
    roadmap.write_bytes(original.replace(" `<<< WE ARE HERE`".encode("utf-8"), b""))
    assert roadmap.read_bytes() != original
    for closed in ("1", "2", "12"):
        defect = _closed_pair(sys.executable, "orient", [str(root), "--check"], tmp_path, closed)
        assert _assert_pair(defect, "orient --check defect closed=%s" % closed) == 1
    roadmap.write_bytes(original)
    traced = _closed_pair(sys.executable, "orient", ["--help"], tmp_path, "2", _clean_env({"METHODOLOGY_LAUNCHER_LOG": "INFO"}))
    assert _assert_pair(traced, "orient --help traced, stderr closed") == 0
    assert "usage:" in traced[0].stdout
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_launchers_pass_through_with_closed_standard_streams


# region FUNC_test_blocked_refusal_exits_two_with_closed_standard_streams [DOMAIN(9): Launchers; CONCEPT(10): BlockedNotDegraded, ClosedStreamPassThrough; TECH(7): subprocess, sh]
## @purpose Prove for all three launchers that the BLOCKED refusal of a checkout without the Codex sibling keeps exit status 2 whatever standard streams the caller closed: the one BLOCKED line while stderr is open, nothing while it is closed.
## @uses test_consumer_profile._owned_checkout, test_consumer_profile._candidate, test_consumer_profile._closed_argv, test_consumer_profile._clean_env, test_consumer_profile._run, test_consumer_profile._show
## @io Input: tmp_path and caplog. Output: None after, for each launcher in its own owned checkout without the sibling script and for the closed sets none, 1, 2 and 12, the child gives stdout empty, exit status 2 and a stderr equal to the single expected BLOCKED line when descriptor 2 is open and to the empty text when it is closed.
##   Side effects: three owned checkouts and twelve child processes under tmp_path. Guarantees: the expected line is built here from the owned candidate path, not read from the output. Raises: AssertionError on any difference. System importance: 10.
##   Example: bin/orient x on a checkout without orient.py and with descriptor 2 closed exits 2 with empty streams; before the fix it ended with an AttributeError and exit 1.
## @complexity 5
def test_blocked_refusal_exits_two_with_closed_standard_streams(tmp_path, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    env = _clean_env()
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    # BUG_FIX_CONTEXT: with descriptor 2 closed the BLOCKED answer of every launcher raised an AttributeError and left exit status 1 instead of 2.
    # Previous: the refusal tests read the BLOCKED line from an open stderr pipe only. Problem: a caller that closes stderr turned the plain refusal into a crash, against BR-4.
    # Fix: run the same refusal with each closed set and require exit 2 and the exact remaining stream.
    for command, script in LAUNCHERS.items():
        checkout = _owned_checkout(tmp_path / command)
        (checkout / "implementations/codex/skills/pm/scripts" / script).unlink()
        launcher = str(checkout / "implementations/claude/bin" / command)
        line = BLOCKED_PREFIX + "%s sibling script missing: %s\n" % (command, _candidate(checkout, script))
        for closed in ("", "1", "2", "12"):
            result = _run(_closed_argv([sys.executable, launcher, "x"], closed), tmp_path, env)
            LOGGER.info("[IMP:9][test_blocked_refusal_exits_two_with_closed_standard_streams][REFUSED] command=%s closed=%s exit=%d",
                        command, closed or "-", result.returncode)
            assert (result.returncode, result.stdout, result.stderr) == (2, "", "" if "2" in closed else line)
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_blocked_refusal_exits_two_with_closed_standard_streams


# region FUNC_test_main_and_emit_skip_absent_standard_streams [DOMAIN(9): Launchers; CONCEPT(10): AbsentStreamSkipped, BlockedNotDegraded; TECH(7): importlib, monkeypatch]
## @purpose Prove in process that the stream helper of an owned launcher copy skips an absent (None) stream and writes and flushes a real one, and that main answers every refusal and failure branch with return value 2 while both sys.stdout and sys.stderr are None: a missing sibling, an empty interpreter path and an interpreter that cannot start, the last of which flushes both streams before the exec.
## @uses test_consumer_profile._owned_checkout, test_consumer_profile._load_launcher, test_consumer_profile._errors, test_consumer_profile._show, orient._emit, orient.main
## @io Input: tmp_path, capsys, caplog and monkeypatch. Output: None after _emit(StringIO, text) returns True and leaves exactly the text (an empty text only flushes), _emit(None, text) returns False, and the three main calls return 2 without raising while stdout and stderr are None, leave the captured real streams empty, emit exactly their three expected ERROR records and exactly five IMP:9 STREAM_CLOSED records (one, one and three), after the direct _emit(None, text) call left exactly one such record.
##   Side effects: one owned checkout under tmp_path; sys.stdout, sys.stderr and sys.executable are patched inside one monkeypatch context and restored. Guarantees: the success branch of main is never called. Raises: AssertionError on any difference. System importance: 9.
##   Example: with sys.stderr None and a missing sibling main([]) returns 2 and writes nothing; before the fix it raised AttributeError.
## @complexity 6
def test_main_and_emit_skip_absent_standard_streams(tmp_path, capsys, caplog, monkeypatch):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO)
    monkeypatch.delenv("METHODOLOGY_LAUNCHER_LOG", raising=False)
    checkout = _owned_checkout(tmp_path / "absent-streams")
    module = _load_launcher(checkout / "implementations/claude/bin/orient", "launcher_orient_absent")
    sibling = checkout / "implementations/codex/skills/pm/scripts/orient.py"
    saved = sibling.read_bytes()
    absent = str(tmp_path / "absent-interpreter")
    assert not os.path.exists(absent)
    sink = io.StringIO()
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    # BUG_FIX_CONTEXT: main wrote and flushed sys.stdout and sys.stderr unconditionally, and both are None when the caller closed the descriptors.
    # Previous: the in-process tests of main always ran under pytest capture objects, which are never None. Problem: the None case was unreachable from the suite.
    # Fix: patch both streams to None inside one context and require return value 2 from every refusal and failure branch.
    assert module._emit(sink, "line\n") is True and sink.getvalue() == "line\n"
    assert module._emit(sink, "") is True and sink.getvalue() == "line\n"
    assert module._emit(None, "line\n") is False
    assert len([r for r in caplog.records if "[IMP:9][_emit][STREAM_CLOSED]" in r.getMessage()]) == 1
    caplog.clear()
    sibling.unlink()
    with monkeypatch.context() as patch:
        patch.setattr(sys, "stdout", None)
        patch.setattr(sys, "stderr", None)
        missing = module.main([])
        sibling.write_bytes(saved)
        patch.setattr(sys, "executable", "")
        no_interpreter = module.main([])
        patch.setattr(sys, "executable", absent)
        cannot_start = module.main([])
    out, err = capsys.readouterr()
    with capsys.disabled():
        _show(caplog.records)
        print("returns", (missing, no_interpreter, cannot_start), "stdout", repr(out), "stderr", repr(err))
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert (missing, no_interpreter, cannot_start) == (2, 2, 2)
    assert (out, err) == ("", "")
    errors = _errors(caplog)
    assert len(errors) == 3
    assert errors[0].startswith("[IMP:10][resolve_sibling][VALIDATION_FAILURE] command=orient cause=missing")
    assert errors[1] == "[IMP:10][main][INTERPRETER_FAILURE] command=orient cause=no-interpreter"
    assert errors[2].startswith("[IMP:10][main][EXEC_FAILURE] command=orient kind=")
    assert len([r for r in caplog.records if "[IMP:9][_emit][STREAM_CLOSED]" in r.getMessage()]) == 5
    # END_BLOCK_Result
# endregion FUNC_test_main_and_emit_skip_absent_standard_streams


# region FUNC_test_carrier_states_only_declared_deltas [DOMAIN(9): Carrier; CONCEPT(10): ByReference, FiveDeltas; TECH(7): re, json]
## @purpose Prove that the Claude carrier has exactly the identity, the five declared Claude deltas and a well-formed hook recipe, adds no duty or checker row, resolves every reference, while the Codex carrier keeps its 75 duty rows and 22 checker rows, and that contrary in-memory controls fail the same predicate.
## @uses test_consumer_profile._carrier_problems, test_consumer_profile._references, test_consumer_profile._show
## @io Input: caplog. Output: None after the real carrier text has no problem, a text with an added sixth delta heading, a text with a pasted duty table row, a text without the recipe fence, a text whose recipe command lacks || true, a text whose recipe command lacks the 2>&1 stderr merge, a text without the command -v check, a text without the absolute launcher path rule, a text without the markup-migrate --apply rule, a text with the former Same file table header and a text with the former blanket fixture-grant sentence each have a problem, and the Codex carrier holds exactly 75 rows of the form | CV-n | and 22 of the form | CHECK-nn |.
##   Side effects: file reads only. Guarantees: structural, not semantic: whether the carrier adds or removes a duty by meaning is the independent reviewer's judgment (AC1). Raises: AssertionError on any difference. System importance: 9.
##   Example: appending a heading ### 6. Extra to the carrier text makes the heading list differ from the seven declared headings.
## @complexity 7
def test_carrier_states_only_declared_deltas(caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    path = PACKAGE / "references/consumer-pm-profile.md"
    text = path.read_text(encoding="utf-8")
    codex = (CODEX / "references/consumer-pm-profile.md").read_text(encoding="utf-8")
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    real = _carrier_problems(text, path.parent)
    LOGGER.info("[IMP:9][test_carrier_states_only_declared_deltas][CARRIER] problems=%d", len(real))
    controls = {
        "sixth delta": text + "\n### 6. Extra delta\n\nA sixth delta.\n",
        "pasted duty row": text + "\n| CV-1 | a duty the carrier must not own |\n",
        "no recipe": text.replace("```json", "```text", 1),
        "recipe without true": text.replace(" || true", "", 1),
        # BUG_FIX_CONTEXT: Review of M37-C2 candidate 4878641e: the carrier promised bare names as the same file, said a fixture grant never authenticates consent and gave a hook recipe that hid a BLOCKED line.
        # Previous: the controls covered headings, a duty row and two recipe defects only. Problem: removing the PATH caveat, restoring the blanket sentence or dropping 2>&1 passed unnoticed.
        # Fix: one contrary control per pinned statement, each reaching the same predicate as the real text.
        "recipe without stderr merge": text.replace(" 2>&1 || true", " || true", 1),
        "no path resolution check": text.replace("command -v", "ls"),
        "no absolute path rule": text.replace("absolute launcher path", "launcher"),
        "no apply rule": text.replace("`markup-migrate --apply` always", "`markup-migrate --apply` may"),
        "former same-file table": text.replace("| Command | Launcher file | Runs |", "| Bare command | Same file | Runs |", 1),
        "former blanket fixture sentence": text.replace("A template, a worker's message", "A template, a fixture grant, a worker's message", 1),
    }
    refused = {name: _carrier_problems(body, path.parent) for name, body in controls.items()}
    assert all(body != text for body in controls.values())
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert real == []
    assert all(refused[name] for name in controls), refused
    assert sum("| CV-%d |" % i in codex for i in range(1, 76)) == 75
    assert sum("| CHECK-%02d |" % i in codex for i in range(1, 23)) == 22
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_carrier_states_only_declared_deltas


# region FUNC_test_routed_entries_name_carrier_and_launchers [DOMAIN(9): Routing; CONCEPT(10): NamedCarrierAndLaunchers, ReferenceResolution; TECH(7): re, pathlib]
## @purpose Prove that the nine routed skills name the carrier and the orient launcher (seven of them also the profile identity), pm-bootstrap also names the other launchers and the Codex templates and keeps its neutral templates index, the searcher names the carrier and bin/codemap with tools exactly Read, Glob, Grep, the two version-signature skills read 2.1.0, and that every plugin-root reference and relative link of all 28 skills, six agents, the carrier and the runtime reference resolves, with contrary in-memory controls refused by the same predicate.
## @uses test_consumer_profile._package_texts, test_consumer_profile._routing_problems, test_consumer_profile._references, test_consumer_profile._show
## @io Input: caplog. Output: None after the real package texts have no routing problem (28 skills, 6 agents, carrier, runtime read), and a copy without the carrier name in one routed body, a copy whose pm-bootstrap names a missing Codex directory, a copy with a searcher tools line that adds Bash, and a copy with a stale version signature each yield a problem.
##   Side effects: file reads only. Guarantees: finite text predicates; whether the routed text means the right thing is the independent review's judgment (AC4). Raises: AssertionError on any difference. System importance: 9.
##   Example: removing the carrier path from the roadmap entry leaves a roadmap lacks problem.
## @complexity 6
def test_routed_entries_name_carrier_and_launchers(caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    texts = _package_texts()
    skills = [k for k in texts if k.startswith("skills/")]
    agents = [k for k in texts if k.startswith("agents/")]
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    real = _routing_problems(texts)
    LOGGER.info("[IMP:9][test_routed_entries_name_carrier_and_launchers][ROUTING] skills=%d agents=%d problems=%d", len(skills), len(agents), len(real))
    controls = {
        "carrier name removed": _variant(texts, "skills/roadmap/SKILL.md", CARRIER, "${CLAUDE_PLUGIN_ROOT}/references/claude-runtime.md"),
        "missing codex directory": _variant(texts, "skills/pm-bootstrap/SKILL.md", "pm/templates/", "pm/templates-missing/"),
        "searcher with Bash": _variant(texts, "agents/searcher.md", "tools: Read, Glob, Grep", "tools: Read, Glob, Grep, Bash"),
        "stale signature": _variant(texts, "skills/devplan-protocol/SKILL.md", "methodology-claude 2.1.0", "methodology-claude 2.0.2"),
    }
    refused = {name: _routing_problems(body) for name, body in controls.items()}
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert (len(skills), len(agents)) == (28, 6)
    assert real == []
    assert all(refused[name] for name in controls), refused
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_routed_entries_name_carrier_and_launchers


# region FUNC_test_bare_names_require_path_resolution_check [DOMAIN(9): Routing; CONCEPT(10): BareNameShadowing, PathResolutionCheck; TECH(7): re, pathlib]
## @purpose Prove that no package text promises a bare launcher name without the PATH resolution check: the README, the carrier-independent routes of pm, pm-bootstrap and pm-handoff and every skill, agent and reference text that says by bare name or shows a backticked bare name also name command -v, with contrary in-memory controls refused by the same predicate.
## @uses test_consumer_profile._package_texts, test_consumer_profile._bare_name_problems, test_consumer_profile._variant, test_consumer_profile._show
## @io Input: caplog. Output: None after the real README and package texts have no problem, and a README without command -v, a README without the absolute path rule, and a pm, pm-bootstrap and pm-handoff entry each with the former parenthetical bare orient while the package is loaded in place each yield a problem.
##   Side effects: file reads only. Guarantees: finite text predicates; whether the caveat is true and sufficient is the independent review's judgment (AC1, AC4). Raises: AssertionError on any difference. System importance: 8.
##   Example: a README that keeps the words by bare name but loses command -v leaves a promises a bare name without command -v problem.
## @complexity 4
def test_bare_names_require_path_resolution_check(caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    texts = _package_texts()
    readme = (PACKAGE / "README.md").read_text(encoding="utf-8")
    former_route = "(bare `orient` while the package is loaded in place)"
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    # BUG_FIX_CONTEXT: Review of M37-C2 candidate 4878641e: README, carrier and three routes called the bare names the package's own files, while an enabled second plugin can export the same names earlier on PATH.
    # Previous: no test judged how a bare name is promised. Problem: the unconditional wording passed every suite although a bare markup-migrate --apply could run another implementation.
    # Fix: require command -v wherever a bare name is promised, the exact conditional parenthetical in the three routes and the absolute path rule in the README.
    real = _bare_name_problems(readme, texts)
    LOGGER.info("[IMP:9][test_bare_names_require_path_resolution_check][BARE_NAMES] texts=%d problems=%d", len(texts) + 1, len(real))
    controls = {
        "README without the check": (readme.replace("command -v", "ls"), texts),
        "README without absolute rule": (readme.replace("absolute", "full"), texts),
    }
    for topic in ("pm", "pm-bootstrap", "pm-handoff"):
        controls["%s former parenthetical" % topic] = (readme, _variant(texts, "skills/%s/SKILL.md" % topic, BARE_ORIENT, former_route))
    refused = {name: _bare_name_problems(*pair) for name, pair in controls.items()}
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert real == []
    assert all(refused[name] for name in controls), refused
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_bare_names_require_path_resolution_check


# region FUNC_test_doxyfile_covers_launchers [DOMAIN(8): Doxygen; CONCEPT(9): ExtensionlessCoverage; TECH(6): re]
## @purpose Prove that the package Doxyfile maps the extensionless launchers: bin is an input, their three names are file patterns beside *.py, and the extension mapping for files without an extension is Python.
## @uses re.Pattern.findall, test_consumer_profile._show
## @io Input: caplog. Output: None after INPUT equals the tokens bin hooks skills/feature-dev/scripts skills/devplan-protocol/scripts tests, FILE_PATTERNS equals *.py orient codemap markup-migrate and EXTENSION_MAPPING equals no_extension=Python, each assigned exactly once.
##   Side effects: one file read. Guarantees: continuation lines are not used by these three assignments. Raises: AssertionError on any difference. System importance: 8.
##   Example: dropping markup-migrate from the patterns leaves that launcher out of the code map.
## @complexity 3
def test_doxyfile_covers_launchers(caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    text = (PACKAGE / "Doxyfile").read_text(encoding="utf-8")
    found = {key: re.findall(r"^%s\s*=\s*(.*)$" % key, text, re.M) for key in ("INPUT", "FILE_PATTERNS", "EXTENSION_MAPPING")}
    # END_BLOCK_Validation
    # START_BLOCK_Result
    LOGGER.info("[IMP:9][test_doxyfile_covers_launchers][ASSIGNMENTS] input=%d patterns=%d mapping=%d", len(found["INPUT"]),
                len(found["FILE_PATTERNS"]), len(found["EXTENSION_MAPPING"]))
    _show(caplog.records)
    assert [len(v) for v in found.values()] == [1, 1, 1]
    assert found["INPUT"][0].split() == ["bin", "hooks", "skills/feature-dev/scripts", "skills/devplan-protocol/scripts", "tests"]
    assert found["FILE_PATTERNS"][0].split() == ["*.py", "orient", "codemap", "markup-migrate"]
    assert found["EXTENSION_MAPPING"][0].split() == ["no_extension=Python"]
    assert _errors(caplog) == []
    # END_BLOCK_Result
# endregion FUNC_test_doxyfile_covers_launchers
