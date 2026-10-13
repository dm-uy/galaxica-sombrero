# region MODULE_CONTRACT [DOMAIN(8): Verdict, Report; CONCEPT(9): ExitContract, Fingerprint, Refusal; TECH(7): dataclasses, hashlib, logging]
## @modulecontract
## @purpose To give both modes of conform one verdict model: rows with a status, a rule, a subject and a detail, the
## populations and probes a run covered, the exit contract (0 pass, 1 fail, 2 not run) and the fingerprints that let a
## finding be located without ever printing the value that triggered it.
## @scope Rows, refusals, populations, probes, the summary line, the JSON-ready dictionary, fingerprints.
## @input Calls from the checks: add, populate, probe.
## @output A Report whose exit_code, summary_line and to_dict the frontend renders.
## @links [USES_API(7): hashlib, dataclasses, logging]
## @links_to_spec BR-7, BR-8
## @invariants
## - The exit code is 2 when any row is NOT RUN, else 1 when any row is FAIL, else 0.
## - A row's rule, subject and detail never hold two consecutive spaces and never a line break.
## - A fingerprint and a log line never carry the value they describe.
## @rationale
## Q: Why one Report for both modes?
## A: The table, the JSON object and the exit code must be the same for a self run and an adapter run; one model
## renders both and the frontend holds no check logic.
## @GREP_SUMMARY verdict, Row, Report, Refusal, exit code 0 1 2, NOT RUN, summary line, population, probes, fingerprint, sha256
## @STRUCTURE ▶ ┌mode┐ → ⊕ add rows ⚡ → ○ populate + probe → ◇ exit: NOT RUN ? 2 : FAIL ? 1 : 0 → ∑ summary_line → ⟦to_dict⟧ → ⎋ render
## @changes
## LAST_CHANGE: [v0.2.0 - Optional per-report diagnostic protection shared by rows, populations and refusals.]
## @modulemap
## CLASS 9[A single verdict line] => Row
## CLASS 8[The check could not run] => Refusal
## FUNC 5[Keep a table value free of line breaks and double spaces] => squeeze
## CLASS 10[The verdict of one run] => Report
## FUNC 7[Length and hash prefix of a value] => fingerprint
## FUNC 7[Fingerprint of a whole token list] => list_fingerprint
## FUNC 8[A one-row NOT RUN report] => refused
## @usecases
## - [Report]: Check (any rule) -> add a row -> the frontend prints table and exit code
## - [fingerprint]: Scan (a finding) -> fingerprint the match -> the reader finds it without seeing it
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: verdict, Row, Report, Refusal, exit code 0 1 2, NOT RUN, summary line, population, probes, fingerprint, sha256
# STRUCTURE: ▶ ┌mode┐ → ⊕ add rows ⚡ → ○ populate + probe → ◇ exit: NOT RUN ? 2 : FAIL ? 1 : 0 → ∑ summary_line → ⟦to_dict⟧ → ⎋ render

import hashlib
import logging
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Optional

logger = logging.getLogger("conform.report")

STATUSES = ("PASS", "WARN", "FAIL", "INFO", "NOT RUN")

_COUNT_KEYS = {"PASS": "pass", "WARN": "warn", "FAIL": "fail", "INFO": "info", "NOT RUN": "not-run"}


# region CLASS_Row [DOMAIN(8): Verdict; CONCEPT(8): Row; TECH(6): dataclass]
## @purpose One finding of a run, frozen so that a rendered table and a JSON object cannot drift apart.
@dataclass(frozen=True)
class Row:
    status: str
    rule: str
    subject: str
    detail: str
# endregion CLASS_Row


# region CLASS_Refusal [DOMAIN(8): Verdict; CONCEPT(9): Refusal, NotRun; TECH(5): Exception]
## @purpose The signal that a check could not run at all (unreadable input, missing registry): the frontend turns it into
## one NOT RUN row and exit 2 instead of a partial verdict.
class Refusal(Exception):
    # region METHOD___init__ [DOMAIN(8): Verdict; CONCEPT(8): Refusal, Construction]
    ## @purpose Keep the rule, the subject and the reason of the refusal for the row the frontend prints.
    def __init__(self, rule: str, subject: str, reason: str) -> None:
        super().__init__(reason)
        self.rule = rule
        self.subject = subject
        self.reason = reason
    # endregion METHOD___init__
# endregion CLASS_Refusal


# region FUNC_squeeze [DOMAIN(5): Verdict; CONCEPT(6): Normalisation; TECH(4): str.split]
## @purpose Keep a table line parseable: a value holds no line break and no run of two spaces.
## @io str -> str
## @complexity 2
def squeeze(value: str) -> str:
    return " ".join(str(value).split())
# endregion FUNC_squeeze


# region CLASS_Report [DOMAIN(9): Verdict, Report; CONCEPT(10): ExitContract, Population, Probes; TECH(6): dataclass rows]
## @purpose The verdict of one run of either mode: the rows, the populations and probes it covered, and the derived exit
## code, counts, summary line and JSON-ready dictionary.
class Report:
    # region METHOD___init__ [DOMAIN(6): Verdict; CONCEPT(6): Construction]
    ## @purpose Start an empty verdict for a mode (self, adapter or usage).
    def __init__(self, mode: str, protect: Optional[Callable[[str], str]] = None) -> None:
        self.protect = protect
        self.mode = mode
        self.rows = []  # type: List[Row]
        self.population = {}  # type: Dict[str, object]
        self.probes = []  # type: List[str]
    # endregion METHOD___init__

    # region METHOD_add [DOMAIN(7): Verdict; CONCEPT(8): Row; TECH(5): squeeze]
    ## @purpose Append a row with optional diagnostic protection before normalization; status and rule remain trusted.
    ## @io (str, str, str, str) -> None
    def add(self, status: str, rule: str, subject: str, detail: str) -> None:
        if status not in STATUSES:
            raise ValueError("unknown status " + status)
        if self.protect is not None:
            subject, detail = self.protect(str(subject)), self.protect(str(detail))
            logger.debug("[IMP:3][Report_add][PROTECT] fields=2")
        self.rows.append(Row(status, squeeze(rule), squeeze(subject), squeeze(detail)))
        if status in ("FAIL", "NOT RUN"):
            logger.info("[IMP:6][Report_add][ROW] status=%s rule=%s", status, squeeze(rule))
    # endregion METHOD_add

    # region METHOD_populate [DOMAIN(6): Verdict; CONCEPT(7): Population]
    ## @purpose Record counts or optionally protected string data in the existing key order.
    ## @io (str, object) -> None
    def populate(self, key: str, value: object) -> None:
        if self.protect is not None and not isinstance(value, int):
            value = self.protect(str(value))
            logger.debug("[IMP:3][Report_populate][PROTECT] fields=1")
        self.population[key] = value if isinstance(value, int) else squeeze(str(value))
    # endregion METHOD_populate

    # region METHOD_probe [DOMAIN(6): Verdict; CONCEPT(7): Probes]
    ## @purpose Record that a probe ran, once, in the order it first ran.
    def probe(self, name: str) -> None:
        if name not in self.probes:
            self.probes.append(name)
    # endregion METHOD_probe

    # region METHOD_has [DOMAIN(5): Verdict; CONCEPT(6): Query]
    ## @purpose Tell whether the report holds a row of a status, optionally of one rule.
    def has(self, status: str, rule: str = "") -> bool:
        return any(r.status == status and (not rule or r.rule == rule) for r in self.rows)
    # endregion METHOD_has

    # region METHOD_exit_code [DOMAIN(8): Verdict; CONCEPT(10): ExitContract]
    ## @purpose The exit contract: 2 when any row is NOT RUN, else 1 when any row is FAIL, else 0.
    def exit_code(self) -> int:
        if self.has("NOT RUN"):
            return 2
        if self.has("FAIL"):
            return 1
        return 0
    # endregion METHOD_exit_code

    # region METHOD_counts [DOMAIN(6): Verdict; CONCEPT(7): Counts]
    ## @purpose Count the rows of each status under the summary's lowercase keys.
    def counts(self) -> Dict[str, int]:
        result = {key: 0 for key in _COUNT_KEYS.values()}
        for row in self.rows:
            result[_COUNT_KEYS[row.status]] += 1
        return result
    # endregion METHOD_counts

    # region METHOD_summary_line [DOMAIN(8): Verdict; CONCEPT(9): Summary]
    ## @purpose The one summary line of both output forms: mode, exit, counts, population and probes.
    def summary_line(self) -> str:
        counts = self.counts()
        population = " ".join(k + "=" + str(v) for k, v in self.population.items()) or "none"
        probes = ",".join(self.probes) or "none"
        return (
            "SUMMARY  mode=%s  exit=%d  pass=%d warn=%d fail=%d info=%d not-run=%d  population: %s  probes: %s"
            % (
                self.mode,
                self.exit_code(),
                counts["pass"],
                counts["warn"],
                counts["fail"],
                counts["info"],
                counts["not-run"],
                population,
                probes,
            )
        )
    # endregion METHOD_summary_line

    # region METHOD_to_dict [DOMAIN(8): Verdict; CONCEPT(9): Json; TECH(5): dict]
    ## @purpose The dictionary the JSON form serialises: the same rows, the same summary line and the same exit code.
    def to_dict(self) -> dict:
        return {
            "mode": self.mode,
            "exit": self.exit_code(),
            "rows": [
                {"status": r.status, "rule": r.rule, "subject": r.subject, "detail": r.detail} for r in self.rows
            ],
            "summary": {
                "line": self.summary_line(),
                "counts": self.counts(),
                "population": dict(self.population),
                "probes": list(self.probes),
            },
        }
    # endregion METHOD_to_dict
# endregion CLASS_Report


# region FUNC_fingerprint [DOMAIN(8): Publication; CONCEPT(9): Fingerprint; TECH(7): sha256]
## @purpose Let a finding be located and matched without printing the value: its length and the first 8 hex of its hash.
## @uses hashlib
## @io str -> str
## @complexity 2
def fingerprint(value: str) -> str:
    return "%d:%s" % (len(value), hashlib.sha256(value.encode("utf-8")).hexdigest()[:8])
# endregion FUNC_fingerprint


# region FUNC_list_fingerprint [DOMAIN(8): Publication; CONCEPT(8): Fingerprint, DenyList; TECH(7): sha256]
## @purpose Identify a deny list by the first 12 hex of the hash of its sorted lowercased tokens, so a report names which
## list ran without naming a token.
## @uses hashlib
## @io Iterable[str] -> str
## @complexity 2
def list_fingerprint(tokens: Iterable[str]) -> str:
    joined = "\n".join(sorted(t.lower() for t in tokens))
    return hashlib.sha256(joined.encode("utf-8")).hexdigest()[:12]
# endregion FUNC_list_fingerprint


# region FUNC_refused [DOMAIN(8): Verdict; CONCEPT(9): Refusal, NotRun; TECH(5): Report]
## @purpose Turn a refusal into the report of a run that could not start: one NOT RUN row, no population, no probes.
## @io (str, Refusal, Optional[Callable]) -> Report
## @complexity 2
def refused(mode: str, refusal: Refusal, protect: Optional[Callable[[str], str]] = None) -> Report:
    report = Report(mode, protect=protect)
    report.add("NOT RUN", refusal.rule, refusal.subject, refusal.reason)
    logger.error("[IMP:10][refused][REFUSAL] rule=%s", squeeze(refusal.rule))
    return report
# endregion FUNC_refused
