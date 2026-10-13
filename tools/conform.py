# region MODULE_CONTRACT [DOMAIN(10): Conformance, CommandLine; CONCEPT(9): Frontend, ExitContract, Refusal; TECH(7): argparse, logging, json]
## @modulecontract
## @purpose To give the owner, a hook and an agent one command that says whether the repository is fit to publish and
## whether a harness's adapter keeps the contract: it parses the arguments, calls the backend once, prints the report as
## a table or as JSON, sends logs to stderr on request, and returns the exit code 0, 1 or 2.
## @scope The command line, the two output forms, the logging switch, the exit code. No check lives here.
## @input argv: the subcommand self or adapter, its options, --json, --log-level.
## @output The report on stdout, LDD lines on stderr only with --log-level, the exit code.
## @links [USES_API(9): conformlib.run_self, conformlib.run_adapter, conformlib.report; READS_DATA_FROM(6): argv]
## @links_to_spec BR-8, BR-9, BR-10, AC-8, AC-9, AC-11
## @invariants
## - Exit 0 is a pass (warnings allowed), exit 1 is a finding, exit 2 is a run that could not judge.
## - Every usage error, including no subcommand, becomes a NOT RUN input.usage report in the requested form.
## - Nothing but the report reaches stdout and nothing reaches stderr without --log-level.
## - The table and the JSON carry the same rows and the same summary line.
## @rationale
## Q: Why does the parser raise instead of exiting?
## A: argparse exits with its own text and status 2 on an error; the report, and --json, would then not carry the
## refusal. Raising Refusal from error() keeps one output shape for every failure.
## Q: Why does main detach its log handler at the end?
## A: main runs in-process many times in tests; a handler left bound to a closed stream would duplicate or crash.
## @changes
## LAST_CHANGE: [v0.1.0 - Initial creation of the frontend: self and adapter subcommands.]
## @modulemap
## CLASS 8[Argument parser that raises Refusal] => RefusingParser
## FUNC 5[The repository that holds this tool] => default_root
## FUNC 7[The parser of the two subcommands] => build_parser
## FUNC 8[Attach or detach the stderr log handler] => configure_logging
## FUNC 6[The report as one line per row plus the summary] => render_table
## FUNC 6[The report as JSON] => render_json
## FUNC 7[Write the report in the requested form and return its exit code] => _emit
## FUNC 10[Parse, run, render, return the exit code] => main
## @usecases
## - [main]: Owner -> conform self --deny-list FILE -> exit 0 means fit to publish
## - [main]: Harness maintainer -> conform adapter ADAPTER -> exit 0 means the adapter keeps the contract
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: conform command line, argparse, RefusingParser, self, adapter, --json, --log-level, stderr, stdout, exit code 0 1 2, render table, render json
# STRUCTURE: ▶ ┌argv┐ → ◇ parse ? Refusal→NOT RUN usage : ⊕ configure_logging → ⚡ run_self | run_adapter → ◇ --json ? JSON : table → ⎋ exit 0|1|2

import argparse
import json
import logging
import os
import sys
from typing import List, Optional

import conformlib
from conformlib.report import Refusal, Report, refused

logger = logging.getLogger("conform.cli")

LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")
_LOG_STATE = {"handler": None, "saved_level": None}


# region CLASS_RefusingParser [DOMAIN(8): CommandLine; CONCEPT(9): Refusal, Usage; TECH(5): argparse]
## @purpose An argument parser whose errors become a Refusal instead of a usage text and a process exit, so the report
## and the JSON form carry every usage failure with the exit code 2.
class RefusingParser(argparse.ArgumentParser):

    # region METHOD_error [DOMAIN(8): CommandLine; CONCEPT(9): Refusal; TECH(4): raise]
    ## @purpose Raise Refusal input.usage with argparse's message; never print and never exit.
    def error(self, message: str):
        raise Refusal("input.usage", "argv", message)
    # endregion METHOD_error
# endregion CLASS_RefusingParser


# region FUNC_default_root [DOMAIN(6): CommandLine; CONCEPT(7): Root; TECH(4): os.path]
## @purpose The repository that holds this tool: the parent of the directory of this file, symbolic links resolved, so the
## self mode checks the right tree from any working directory.
## @io None -> str
## @complexity 2
def default_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# endregion FUNC_default_root


# region FUNC_build_parser [DOMAIN(8): CommandLine; CONCEPT(8): Subcommands; TECH(5): argparse]
## @purpose Build the parser of the two subcommands, self and adapter, with the shared --json and --log-level options; the
## subcommand is required.
## @uses RefusingParser
## @io None -> RefusingParser
## @complexity 4
def build_parser() -> RefusingParser:
    parser = RefusingParser(prog="conform", description="Check the meta-framework repository or a harness adapter.")
    sub = parser.add_subparsers(dest="mode", parser_class=RefusingParser, metavar="{self,adapter}")
    sub.required = True
    self_parser = sub.add_parser("self", help="check this repository: its format and the publication scan")
    self_parser.add_argument("--root", default=None, help="repository to check (default: the one holding this tool)")
    self_parser.add_argument("--deny-list", dest="deny_list", default=None,
                             help="file of private words, one per line (required)")
    adapter_parser = sub.add_parser("adapter", help="check a harness adapter against the spec it names")
    adapter_parser.add_argument("adapter", help="path of the adapter JSON file")
    for each in (self_parser, adapter_parser):
        each.add_argument("--json", action="store_true", help="print the report as JSON")
        each.add_argument("--log-level", dest="log_level", default=None, type=str.upper, choices=LOG_LEVELS,
                          help="send LDD log lines to stderr at this level")
    return parser
# endregion FUNC_build_parser


# region FUNC_configure_logging [DOMAIN(8): CommandLine; CONCEPT(8): Logging, Idempotence; TECH(6): logging]
## @purpose Detach the handler and restore the level this function set on its previous call, then, when a level is given,
## attach one stderr handler that prints the bare LDD message. Safe to call any number of times in one process.
## @uses logging
## @io Optional[str] -> None
## @complexity 4
def configure_logging(level: Optional[str]) -> None:
    log = logging.getLogger("conform")
    previous = _LOG_STATE["handler"]
    if previous is not None:
        log.removeHandler(previous)
        _LOG_STATE["handler"] = None
        if _LOG_STATE["saved_level"] is not None:
            log.setLevel(_LOG_STATE["saved_level"])
        _LOG_STATE["saved_level"] = None
    if level is None:
        return
    number = getattr(logging, level)
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(number)
    handler.setFormatter(logging.Formatter("%(message)s"))
    _LOG_STATE["saved_level"] = log.level
    log.setLevel(number)
    log.addHandler(handler)
    _LOG_STATE["handler"] = handler
# endregion FUNC_configure_logging


# region FUNC_render_table [DOMAIN(7): Output; CONCEPT(8): Table, Summary; TECH(4): str]
## @purpose The report as one line per row (status, rule, subject, detail) followed by the summary line.
## @io Report -> str
## @complexity 2
def render_table(report: Report) -> str:
    lines = ["%-7s  %s  %s  %s" % (row.status, row.rule, row.subject, row.detail) for row in report.rows]
    lines.append(report.summary_line())
    return "\n".join(lines)
# endregion FUNC_render_table


# region FUNC_render_json [DOMAIN(7): Output; CONCEPT(8): Json; TECH(4): json]
## @purpose The report as JSON with two-space indent and ASCII only: the same rows, exit code and summary line.
## @io Report -> str
## @complexity 1
def render_json(report: Report) -> str:
    return json.dumps(report.to_dict(), indent=2, ensure_ascii=True)
# endregion FUNC_render_json


# region FUNC__emit [DOMAIN(7): Output; CONCEPT(8): Exit; TECH(4): sys.stdout]
## @purpose Write the report in the requested form to stdout and return its exit code.
## @io (Report, bool) -> int
## @complexity 2
def _emit(report: Report, as_json: bool) -> int:
    text = render_json(report) if as_json else render_table(report)
    sys.stdout.write(text + "\n")
    code = report.exit_code()
    logger.info("[IMP:9][main][EXIT] exit=%d", code)
    return code
# endregion FUNC__emit


# region FUNC_main [DOMAIN(10): CommandLine; CONCEPT(10): ExitContract, Refusal; TECH(6): argparse, logging]
## @purpose Parse the arguments, run the chosen mode once, print the report and return the exit code; a usage error is a
## NOT RUN report in the requested form, never a stack trace or an argparse exit.
## @uses build_parser, configure_logging, conformlib.run_self, conformlib.run_adapter, render_table, render_json
## @io Optional[List[str]] -> int
## @complexity 6
def main(argv: Optional[List[str]] = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    try:
        args = build_parser().parse_args(arguments)
    except Refusal as refusal:
        mode = arguments[0] if arguments and arguments[0] in ("self", "adapter") else "usage"
        return _emit(refused(mode, refusal), "--json" in arguments)
    configure_logging(args.log_level)
    try:
        logger.info("[IMP:4][main][ARGS] mode=%s json=%s log_level=%s", args.mode, args.json, args.log_level)
        if args.mode == "self":
            root = os.path.abspath(args.root) if args.root else default_root()
            report = conformlib.run_self(root, args.deny_list)
        else:
            report = conformlib.run_adapter(args.adapter)
        return _emit(report, args.json)
    finally:
        configure_logging(None)
# endregion FUNC_main


if __name__ == "__main__":
    sys.exit(main())
