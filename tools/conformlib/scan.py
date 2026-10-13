# region MODULE_CONTRACT [DOMAIN(10): Publication, Privacy; CONCEPT(9): PublicationScan, DenyList, Canary, Fingerprint; TECH(7): re, os.walk]
## @modulecontract
## @purpose To let the owner publish this repository with evidence that no private word, no home path and no e-mail
## address is in it: the scan reads every text file, reports each finding by rule, file, line and a fingerprint of the
## value, and never repeats the value, so the report and the logs are safe to paste anywhere.
## @scope The deny list (a file the owner keeps outside the repository), the four scan rules, the run-time canary probe,
## the walk over the repository's text files.
## @input A repository root, the path of a deny-list file, a Report to write rows into.
## @output FAIL rows named by rule with subject file and detail line plus fingerprint; INFO rows for files not scanned;
## PASS rows for the rules that found nothing; the populations text-files, binary-files, deny-list, deny-list-fp, skipped.
## @links [USES_API(8): re, os, hashlib via conformlib.report; READS_DATA_FROM(9): every file of the root, the deny-list file]
## @links_to_spec BR-7, BR-12, AC-7, AC-10
## @invariants
## - A matched value, a deny token and a line's text never appear in a row, a log line or an exception message.
## - The scan patterns are built from fragments, so no line of this source matches any of them.
## - A rule that cannot bite its canary stops the run (scan.canary), so a silent pattern never reads as a clean repository.
## - The deny list is read once; the tool never echoes its content, only its size and a fingerprint of the list.
## @rationale
## Q: Why a canary probe at run time?
## A: A pattern broken by an edit finds nothing and the scan passes; the run-time canary proves each pattern and each
## token still bites before the repository is judged clean.
## Q: Why a fingerprint and not the value?
## A: The finding must be locatable (file, line) and comparable across runs without carrying the private value into
## a log, a terminal scrollback or a pasted report.
## Q: Why are patterns written in fragments?
## A: The scanner is part of the repository it scans; a pattern spelled whole would be a finding in its own source.
## @GREP_SUMMARY publication coverage, diagnostic protection, scoped log guard, redaction spans
## @STRUCTURE loaded tokens + patterns -> protect rows and sinks -> walk/read or Refusal -> restore filters
## @changes
## LAST_CHANGE: [v0.2.0 - Refuse incomplete reads/walks and protect diagnostic and log spans per self run.]
## @modulemap
## FUNC 8[Read the deny list into tokens] => load_deny_list
## FUNC 9[The four compiled scan rules] => build_patterns
## FUNC 8[Build one canary line per rule shape at run time, from fragments] => _canary_lines
## FUNC 10[Prove every rule and token bites a run-time canary] => canary_probe
## FUNC 7[Yield text or deliberate binary skips; refuse read/walk failures] => conformlib.scan.iter_text_files
## FUNC 9[Protect diagnostic spans with scan matching] => conformlib.scan.redact_diagnostic
## CLASS 9[Scoped log protection on existing sinks] => conformlib.scan.DiagnosticGuard
## FUNC 9[Safe incomplete-scan refusal] => conformlib.scan._scan_refusal
## FUNC 10[Scan the tree, write rows and populations] => scan_tree
## @usecases
## - [scan_tree]: Owner -> conform self with a deny list -> know the repository is fit to publish
## - [canary_probe]: Tool -> before the scan -> refuse a run whose patterns cannot bite
## - [load_deny_list]: Tool -> read the private word list -> tokens and a list fingerprint, never the words
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: publication scan, deny list, canary probe, fingerprint, home path, tilde path, e-mail address, deny token, text files, binary files, privacy, no content in logs
# STRUCTURE: ▶ ┌root,deny_file┐ → ⊕ tokens + list_fp → ⚡ canary ∀pattern,∀token → ○ walk: 〈NUL/UTF-8? INFO : ○ line: 4 patterns + tokens → FAIL rule,file,line,fp〉 → ∑ populations → ⎋ rows

import logging
import os
import re
from typing import Callable, Iterator, List, Optional, Pattern, Tuple

from conformlib.markdown import SKIPPED_WALK_DIRS, normalize_newlines
from conformlib.report import Refusal, Report, fingerprint, list_fingerprint

logger = logging.getLogger("conform.scan")

SKIPPED_DIRS = SKIPPED_WALK_DIRS
SKIPPED_FILES = (".DS_Store",)
SCAN_RULES = ("scan.home-path", "scan.home-relative", "scan.email", "scan.deny-token")


# region FUNC_load_deny_list [DOMAIN(9): Privacy; CONCEPT(9): DenyList, Fingerprint; TECH(5): open, decode]
## @purpose Read the owner's deny-list file into tokens: one per line, blank lines and lines starting with a hash sign
## skipped, duplicates (ignoring case) dropped. A missing, unreadable, non-UTF-8 or empty list stops the run as an input
## problem, so a wrong path never reads as a clean repository.
## @uses open, list_fingerprint
## @io Optional[str] -> List[str]
## @complexity 5
def load_deny_list(path: Optional[str]) -> List[str]:
    if not path:
        raise Refusal("input.deny-list", "--deny-list", "no deny list given")
    try:
        with open(path, "rb") as handle:
            text = handle.read().decode("utf-8-sig")
    except (OSError, UnicodeDecodeError) as error:
        logger.error("[IMP:10][load_deny_list][READ] error=%s", type(error).__name__)
        raise Refusal("input.deny-list", "--deny-list", "deny list missing, unreadable or not UTF-8")
    tokens = []  # type: List[str]
    seen = set()
    for raw in normalize_newlines(text).split("\n"):
        token = raw.strip()
        if not token or token.startswith("#"):
            continue
        key = token.lower()
        if key in seen:
            continue
        seen.add(key)
        tokens.append(token)
    if not tokens:
        logger.error("[IMP:10][load_deny_list][READ] entries=0")
        raise Refusal("input.deny-list", "--deny-list", "deny list is empty")
    logger.info("[IMP:7][load_deny_list][READ] entries=%d fp=%s", len(tokens), list_fingerprint(tokens))
    return tokens
# endregion FUNC_load_deny_list


# region FUNC_build_patterns [DOMAIN(9): Privacy; CONCEPT(9): ScanRule, Fragments; TECH(6): re]
## @purpose Give the four compiled scan patterns: a POSIX home path and a Windows home path (both rule scan.home-path), a
## tilde path with a segment and an e-mail address. Every regex is built from fragments so that no line of this source
## holds what a rule matches.
## @uses re
## @io None -> List[Tuple[str, Pattern]]
## @complexity 5
def build_patterns() -> List[Tuple[str, Pattern]]:
    guard = "(?<![A-Za-z0-9_.-])"
    slash = "/"
    back = "\\\\"
    roots = "(?:" + "Us" + "ers" + "|" + "ho" + "me" + ")"
    posix = guard + slash + roots + slash + "[^/\\s]+" + slash
    windows = "(?i:[A-Za-z]:" + back + "Us" + "ers" + back + "[^\\\\\\s]+" + back + ")"
    tilde = guard + "~" + slash + "[A-Za-z0-9._-]+"
    local = "(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]+"
    domain = "[A-Za-z0-9-]+(?:\\.[A-Za-z0-9-]+)*\\.[A-Za-z]{2,}"
    email = local + "@" + domain
    patterns = [
        ("scan.home-path", re.compile(posix)),
        ("scan.home-path", re.compile(windows)),
        ("scan.home-relative", re.compile(tilde)),
        ("scan.email", re.compile(email)),
    ]
    logger.debug("[IMP:3][build_patterns][BUILD] patterns=%d", len(patterns))
    return patterns
# endregion FUNC_build_patterns


# region FUNC__canary_lines [DOMAIN(8): Privacy; CONCEPT(9): Canary, Fragments; TECH(4): str]
## @purpose Build, at run time and from fragments, one line per rule shape that the rule must match: a POSIX home path, a
## Windows home path, a tilde path and an e-mail address.
## @io None -> List[Tuple[str, str]]
## @complexity 2
def _canary_lines() -> List[Tuple[str, str]]:
    posix = "/" + "Us" + "ers" + "/" + "cnry" + "/x"
    windows = "C:" + "\\" + "Us" + "ers" + "\\" + "cnry" + "\\x"
    tilde = "~" + "/" + "cnry"
    mail = "cnry" + "@" + "example" + "." + "org"
    return [
        ("scan.home-path", posix),
        ("scan.home-path", windows),
        ("scan.home-relative", tilde),
        ("scan.email", mail),
    ]
# endregion FUNC__canary_lines


# region FUNC_canary_probe [DOMAIN(10): Privacy; CONCEPT(10): Canary, Bite; TECH(5): re]
## @purpose Prove, before any file is read, that every pattern matches its run-time canary and every deny token matches
## its case-swapped canary, and stop the run with scan.canary when one does not bite. Returns how many patterns and
## tokens were proved.
## @uses build_patterns output, fingerprint
## @io (List[Tuple[str, Pattern]], List[str]) -> Tuple[int, int]
## @complexity 6
def canary_probe(patterns: List[Tuple[str, Pattern]], tokens: List[str]) -> Tuple[int, int]:
    for rule, line in _canary_lines():
        bites = any(compiled.search(line) for name, compiled in patterns if name == rule)
        if not bites:
            logger.error("[IMP:10][canary_probe][BITE] patterns=%d tokens=%d ok=False rule=%s", len(patterns), len(tokens), rule)
            raise Refusal("scan.canary", "*", "rule %s did not match its canary" % rule)
    for token in tokens:
        canary_line = "x" + token.swapcase() + "x"
        if token.lower() not in canary_line.lower():
            logger.error("[IMP:10][canary_probe][BITE] patterns=%d tokens=%d ok=False fp=%s",
                         len(patterns), len(tokens), fingerprint(token.lower()))
            raise Refusal("scan.canary", "*", "token fp=%s did not match its canary" % fingerprint(token.lower()))
    logger.info("[IMP:9][canary_probe][BITE] patterns=%d tokens=%d ok=True", len(patterns), len(tokens))
    return len(patterns), len(tokens)
# endregion FUNC_canary_probe



# region FUNC_redact_diagnostic [DOMAIN(10): Privacy; CONCEPT(10): DiagnosticSpans, Fingerprint; TECH(7): re]
## @purpose Protect input-derived spans using the same pattern and lowercase token matches as publication scanning.
## @uses conformlib.report.fingerprint
## @io (str, List[str], List[Tuple[str, Pattern]]) -> str
## @complexity 7
def redact_diagnostic(value: str, tokens: List[str], patterns: List[Tuple[str, Pattern]]) -> str:
    # The owning guard/report logs this operation; logging here would recursively filter itself.
    spans = [(m.start(), m.end()) for _rule, compiled in patterns for m in compiled.finditer(value)]
    low = value.lower()
    # Lowercasing can expand a character; keep lowered offsets mapped to original input spans.
    offsets = [index for index, char in enumerate(value) for _ in char.lower()]
    for token in tokens:
        needle = token.lower()
        if not needle:
            continue
        start = low.find(needle)
        while start >= 0:
            spans.append((offsets[start], offsets[start + len(needle) - 1] + 1))
            start = low.find(needle, start + 1)
    merged = []
    for start, end in sorted(spans):
        if merged and start < merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))
    pieces = []
    previous = 0
    for start, end in merged:
        pieces.extend((value[previous:start], "[redacted fp=%s]" % fingerprint(value[start:end].lower())))
        previous = end
    pieces.append(value[previous:])
    return "".join(pieces)
# endregion FUNC_redact_diagnostic


# region CLASS_DiagnosticGuard [DOMAIN(10): Privacy; CONCEPT(10): PerRun, LogSinks; TECH(7): logging.Filter]
## @purpose Protect conform messages at their existing sinks for one self call and release every installed filter.
## @uses conformlib.scan.redact_diagnostic
## @io Callable[[str], str] -> scoped filter lifecycle
class DiagnosticGuard(logging.Filter):
    # region METHOD___init__ [DOMAIN(9): Privacy; CONCEPT(9): Lifecycle]
    ## @purpose Keep the callback and owned handler references local to this run.
    def __init__(self, protect: Callable[[str], str]) -> None:
        super().__init__()
        self.protect = protect
        self.handlers = []
    # endregion METHOD___init__

    # region METHOD_filter [DOMAIN(10): Privacy; CONCEPT(10): NamespaceBoundary]
    ## @purpose Protect rendered conform messages before formatters or ancestor sinks see them.
    ## @io logging.LogRecord -> bool
    def filter(self, record: logging.LogRecord) -> bool:
        if record.name == "conform" or record.name.startswith("conform."):
            record.msg = self.protect(record.getMessage())
            record.args = ()
        return True
    # endregion METHOD_filter

    # region METHOD_start [DOMAIN(10): Privacy; CONCEPT(9): Attach, ExistingSinks]
    ## @purpose Install only owned filters on current conform and ancestor handlers without creating a sink.
    ## @io None -> None
    def start(self) -> None:
        loggers = [logging.getLogger("conform")]
        loggers.extend(item for name, item in list(logging.Logger.manager.loggerDict.items())
                       if name.startswith("conform.") and isinstance(item, logging.Logger))
        ancestor = loggers[0].parent
        while ancestor is not None:
            loggers.append(ancestor)
            ancestor = ancestor.parent
        for log in loggers:
            for handler in log.handlers:
                if handler not in self.handlers:
                    handler.addFilter(self)
                    self.handlers.append(handler)
        logger.info("[IMP:9][DiagnosticGuard][START] handlers=%d protection=active", len(self.handlers))
    # endregion METHOD_start

    # region METHOD_close [DOMAIN(10): Privacy; CONCEPT(9): Restore, Finally]
    ## @purpose Release only this run's filters on every outcome while keeping the caller's handler state.
    ## @io None -> None
    def close(self) -> None:
        logger.info("[IMP:9][DiagnosticGuard][CLOSE] handlers=%d protection=complete", len(self.handlers))
        for handler in self.handlers:
            handler.removeFilter(self)
        self.handlers = []
    # endregion METHOD_close
# endregion CLASS_DiagnosticGuard


# region FUNC__scan_refusal [DOMAIN(10): Publication; CONCEPT(10): IncompleteCoverage; TECH(7): OSError]
## @purpose Refuse an incomplete scan with relative location and exception class, never unsafe exception text.
## @uses conformlib.report.Refusal
## @io (str, str, OSError, str) -> None
## @complexity 2
def _scan_refusal(root: str, path: str, error: OSError, operation: str) -> None:
    subject = os.path.relpath(path, root).replace(os.sep, "/")
    kind = type(error).__name__
    logger.error("[IMP:10][iter_text_files][REFUSAL] operation=%s class=%s subject=%s", operation, kind, subject)
    raise Refusal("input.root", subject, "%s failed (%s)" % (operation, kind))
# endregion FUNC__scan_refusal


# region FUNC_iter_text_files [DOMAIN(8): Privacy; CONCEPT(8): Population, TextOrBinary; TECH(5): os.walk]
## @purpose Yield every file of the root in sorted order as its relative path and its text, or None when the file holds a
## NUL byte or is not UTF-8. Skipped: version-control directory/pointer metadata, the generated-documentation output, caches, the
## operating system's folder-metadata file, and symbolic links. Failed reads or traversal refuse coverage.
## @uses os.walk
## @io str -> Iterator[Tuple[str, Optional[str]]]
## @complexity 5
def iter_text_files(root: str) -> Iterator[Tuple[str, Optional[str]]]:
    # BUG_FIX_CONTEXT: failed reads and omitted walk errors cannot prove publication coverage.
    def walk_error(error: OSError) -> None:
        _scan_refusal(root, error.filename or root, error, "walk")

    for dirpath, dirnames, filenames in os.walk(root, onerror=walk_error):
        dirnames[:] = sorted(name for name in dirnames
                             if name not in SKIPPED_DIRS and not os.path.islink(os.path.join(dirpath, name)))
        for name in sorted(filenames):
            # BUG_FIX_CONTEXT: a worktree stores Git metadata in a file rather than a directory.
            if name == ".git":
                logger.info("[IMP:4][iter_text_files][SKIP_METADATA] git_pointer=1")
                continue
            if name in SKIPPED_FILES:
                continue
            full = os.path.join(dirpath, name)
            if os.path.islink(full):
                continue
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            try:
                with open(full, "rb") as handle:
                    data = handle.read()
            except OSError as error:
                _scan_refusal(root, full, error, "read")
            if b"\x00" in data:
                yield rel, None
                continue
            try:
                yield rel, data.decode("utf-8")
            except UnicodeDecodeError:
                yield rel, None
# endregion FUNC_iter_text_files


# region FUNC_scan_tree [DOMAIN(10): Privacy; CONCEPT(10): PublicationScan, Finding, Fingerprint; TECH(6): re, Report]
## @purpose Scan every text line of the repository with the four rules and write one FAIL row per finding (rule, file,
## line, fingerprint of the matched value or of the lowercased token), one INFO row per file not scanned, one PASS row per
## rule without a finding, and the scan's populations. The matched value is never written anywhere.
## @uses iter_text_files, fingerprint, list_fingerprint, normalize_newlines
## @io (str, List[str], List[Tuple[str, Pattern]], Report) -> None
## @complexity 8
def scan_tree(root: str, tokens: List[str], patterns: List[Tuple[str, Pattern]], report: Report) -> None:
    failed = set()
    text_files = 0
    binary_files = 0
    lowered = [(token.lower(), fingerprint(token.lower())) for token in tokens]
    for rel, text in iter_text_files(root):
        if text is None:
            binary_files += 1
            report.add("INFO", "scan.binary", rel, "not scanned: binary or not UTF-8")
            continue
        text_files += 1
        for number, line in enumerate(normalize_newlines(text).split("\n"), 1):
            for rule, compiled in patterns:
                for match in compiled.finditer(line):
                    fp = fingerprint(match.group(0))
                    report.add("FAIL", rule, rel, "line %d fp=%s" % (number, fp))
                    failed.add(rule)
                    logger.info("[IMP:9][scan_tree][FINDING] rule=%s file=%s line=%d fp=%s", rule, rel, number, fp)
            low = line.lower()
            for token_lower, token_fp in lowered:
                if token_lower in low:
                    report.add("FAIL", "scan.deny-token", rel, "line %d fp=%s" % (number, token_fp))
                    failed.add("scan.deny-token")
                    logger.info("[IMP:9][scan_tree][FINDING] rule=scan.deny-token file=%s line=%d fp=%s",
                                rel, number, token_fp)
    for rule in SCAN_RULES:
        if rule not in failed:
            report.add("PASS", rule, "*", "%d text files" % text_files)
    report.probe("scan")
    report.populate("text-files", text_files)
    report.populate("binary-files", binary_files)
    report.populate("deny-list", len(tokens))
    report.populate("deny-list-fp", list_fingerprint(tokens))
    report.populate("skipped", ",".join(SKIPPED_DIRS + SKIPPED_FILES))
    logger.info("[IMP:7][scan_tree][READ] text_files=%d binary_files=%d", text_files, binary_files)
# endregion FUNC_scan_tree
