# region MODULE_CONTRACT [DOMAIN(10): Conformance, PluginApi; CONCEPT(9): SelfMode, Boundary, Refusal; TECH(6): logging]
## @modulecontract
## @purpose To give the frontend, a test or another agent one call per mode of conform that always returns a Report and
## never prints, exits or raises: a refusal or an unexpected error becomes a NOT RUN row, so the caller has one shape to
## render and one exit code to return.
## @scope The public entry points of the backend package and the package's logging default.
## @input A repository root and a deny-list path (self mode); an adapter path (adapter mode).
## @output A Report whose rows, populations, probes and exit code the caller renders.
## @links [USES_API(8): conformlib.markdown, conformlib.selfcheck, conformlib.scan, conformlib.adapter, conformlib.report; READS_DATA_FROM(9): the root, the deny-list file, the adapter file and the spec root it names]
## @links_to_spec BR-5, BR-6, BR-7, BR-8, AC-5, AC-6, AC-7, AC-8
## @invariants
## - run_self and run_adapter return a Report on every input; an exception never leaves them.
## - An unexpected exception becomes one NOT RUN internal.error row that names only the exception class.
## - The package attaches a NullHandler to the conform logger, so nothing reaches stderr unless the frontend asks for it.
## @rationale
## Q: Why catch every exception at this boundary?
## A: The exit contract is three values; a traceback would give a fourth, and a caller that reads exit 2 as "could not
## run" must never see a raw crash that looks like a verdict.
## Q: Why is the refusal order fixed here?
## A: A wrong root or an empty deny list must never read as a clean repository; each refusal ends the run before any
## file is judged.
## @GREP_SUMMARY conformlib plugin api, run_self, run_adapter, refusal order, internal error boundary, NullHandler, exit contract
## @STRUCTURE ▶ ┌root,deny_list┐ → ◇ refusals: root → deny list → neutral files → canary → ⊕ tree → ⚡ format probes → ⚡ scan → ∑ verdict → ⎋ Report (never raises) ‖ run_adapter: ┌adapter┐ → ⊕ load_adapter → ⊕ spec_root → ⊕ load_spec ⚡ refusals → ⚡ structure → ◇ version → ◇ parameters → ◇ capabilities → ○ files → ∑ verdict → ⎋ Report (never raises)
## @changes
## LAST_CHANGE: [v0.2.0 - Per-self diagnostic protection before parsing, shared refusals and guaranteed log restoration.]
## @modulemap
## FUNC 10[Run the self mode over a root with a deny list] => run_self
## FUNC 10[Run the adapter mode over an adapter file] => run_adapter
## @usecases
## - [run_self]: Maintainer -> conform self -> a verdict on the repository's format and publication safety
## - [run_adapter]: Harness maintainer -> conform adapter -> a verdict on whether the adapter keeps the contract
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: conformlib plugin api, run_self, run_adapter, refusal order, internal error boundary, NullHandler, exit contract
# STRUCTURE: ▶ ┌root,deny_list┐ → ◇ refusals: root → deny list → neutral files → canary → ⊕ tree → ⚡ format probes → ⚡ scan → ∑ verdict → ⎋ Report (never raises) ‖ run_adapter: ┌adapter┐ → ⊕ load_adapter → ⊕ spec_root → ⊕ load_spec ⚡ refusals → ⚡ structure → ◇ version → ◇ parameters → ◇ capabilities → ○ files → ∑ verdict → ⎋ Report (never raises)

import logging
import os
from typing import Optional

from conformlib.adapter import (
    check_capabilities,
    check_files,
    check_parameters,
    check_spec_version,
    check_structure,
    load_adapter,
    load_spec,
    record_population,
    resolve_spec_root,
)
from conformlib.markdown import list_neutral_files, load_neutral_tree
from conformlib.report import Refusal, Report, refused
from conformlib.scan import DiagnosticGuard, build_patterns, canary_probe, load_deny_list, redact_diagnostic, scan_tree
from conformlib.selfcheck import run_format_checks

logging.getLogger("conform").addHandler(logging.NullHandler())
logger = logging.getLogger("conform.api")

__all__ = ["run_self", "run_adapter"]


# region FUNC_run_self [DOMAIN(10): Conformance; CONCEPT(10): SelfMode, Refusal, Verdict; TECH(6): Report]
## @purpose Judge the repository at a root against its own format and against the publication scan, and return the
## Report: refusals first (root, deny list, neutral files, canary), then the format probes, then the scan. Never raises.
## @uses conformlib.scan.DiagnosticGuard, conformlib.scan.redact_diagnostic, load_deny_list, build_patterns, canary_probe, load_neutral_tree, run_format_checks, scan_tree, refused
## @io (str, Optional[str]) -> Report
## @complexity 8
def run_self(root: str, deny_list: Optional[str]) -> Report:
    report = Report("self")
    protect = None
    guard = None
    try:
        if not root or not os.path.isdir(root):
            raise Refusal("input.root", "--root", "root is missing or not a directory")
        tokens = load_deny_list(deny_list)
        patterns = build_patterns()
        # BUG_FIX_CONTEXT: protect before neutral parsing and preserve the same policy on early refusals.
        protect = lambda value: redact_diagnostic(value, tokens, patterns)
        guard = DiagnosticGuard(protect)
        guard.start()
        report = Report("self", protect=protect)
        if not list_neutral_files(root):
            raise Refusal("input.root", "--root", "no neutral file under the root")
        proved_patterns, proved_tokens = canary_probe(patterns, tokens)
        report.probe("scan.canary")
        report.add("PASS", "scan.canary", "*",
                   "%d patterns and %d tokens bite their canaries" % (proved_patterns, proved_tokens))
        tree = load_neutral_tree(root)
        run_format_checks(root, tree, report)
        scan_tree(root, tokens, patterns, report)
        counts = report.counts()
        logger.info("[IMP:9][run_self][VERDICT] exit=%d fail=%d warn=%d neutral_files=%s",
                    report.exit_code(), counts["fail"], counts["warn"], report.population.get("neutral-files", "0"))
        return report
    except Refusal as refusal:
        logger.error("[IMP:10][run_self][REFUSAL] rule=%s", refusal.rule)
        return refused("self", refusal, protect=protect)
    except Exception as error:  # noqa: BLE001 - the boundary turns any crash into a NOT RUN row
        logger.error("[IMP:10][run_self][INTERNAL] function=run_self class=%s", type(error).__name__)
        return refused("self", Refusal("internal.error", "*", type(error).__name__), protect=protect)
    finally:
        if guard is not None:
            guard.close()
# endregion FUNC_run_self


# region FUNC_run_adapter [DOMAIN(10): Conformance; CONCEPT(10): AdapterMode, Refusal, Verdict; TECH(6): Report]
## @purpose Judge an adapter file against the spec it names, and return the Report: refusals first (the adapter, the
## spec root, the schema), then the structure, the version, the parameters, the capabilities and the files with their
## modes. Never raises.
## @uses load_adapter, resolve_spec_root, load_spec, check_structure, check_spec_version, check_parameters, check_capabilities, check_files, refused
## @io str -> Report
## @complexity 8
def run_adapter(adapter_path: str) -> Report:
    report = Report("adapter")
    try:
        adapter = load_adapter(adapter_path)
        adapter_dir = os.path.dirname(os.path.abspath(adapter_path))
        spec_root = resolve_spec_root(adapter, adapter_dir)
        spec = load_spec(spec_root)
        invalid = check_structure(adapter, spec.schema, report)
        report.probe("structure")
        record_population(adapter, spec, report)
        check_spec_version(adapter, spec, invalid, report)
        check_parameters(adapter, spec, invalid, report)
        check_capabilities(adapter, spec, invalid, report)
        check_files(adapter, adapter_dir, spec, invalid, report)
    except Refusal as refusal:
        logger.error("[IMP:10][run_adapter][REFUSAL] rule=%s", refusal.rule)
        return refused("adapter", refusal)
    except Exception as error:  # noqa: BLE001 - the boundary turns any crash into a NOT RUN row
        logger.error("[IMP:10][run_adapter][INTERNAL] function=run_adapter class=%s", type(error).__name__)
        return refused("adapter", Refusal("internal.error", "*", type(error).__name__))
    counts = report.counts()
    logger.info("[IMP:9][run_adapter][VERDICT] exit=%d fail=%d warn=%d neutral_files=%s",
                report.exit_code(), counts["fail"], counts["warn"], report.population.get("neutral-files", "0"))
    return report
# endregion FUNC_run_adapter
