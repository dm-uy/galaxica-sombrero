# region MODULE_CONTRACT [DOMAIN(9): NativeMethodology; CONCEPT(9): SourceIdentity, BoundedVerification, InPlacePlugin; TECH(8): Python, StandardLibrary]
## @modulecontract
## @purpose Preserve one parent-owned schema2 run of the Claude Code package with actual current source identity and honest authority limits.
## @scope Actual in-place plugin bindings (profile colocated-in-place, agents carriers, neutral owners resolved two levels above the package), the target candidate identity and its exclusion policy (git ignore rules, declared fallback list), canonical returns, causal Debug, separate response controls, atomic checkpoint and init/show/record CLI.
## @input Explicit owned source/target paths and current canonical records; pytest fixtures supply owned temporary paths for tests. No credentials or provider state.
## @output Importable declared functions, actual CLI answer/diagnostic/exit where applicable, and meaningful test outcomes with actual trace. No fabricated native acceptance.
## @links [USES_API(8): pathlib.Path; USES_API(8): logging; USES_API(8): subprocess for read-only git rev-parse, ls-files, branch and status through one hermetic wrapper; READS_DATA_FROM(9): explicit path inputs and the declared package layout; READS_DATA_FROM(8): the target's own git ignore rules; no environment secrets]
## @links_to_spec M22 specification section 2 Mechanics; requirements BR-3 and BR-4; flow/run-state.md STATE-102 and STATE-501; code/tests.md TST-501
## @invariants
## - Current neutral role/phase/scan/gate owners remain controlling; structural checks never prove human authority or role independence.
## - The package identity is methodology-claude 1.0.0 with the colocated-in-place profile and the run contract methodology-claude/1.0.0; the state contract is schema2 and matches the sibling package helper except that the candidate record carries one added key, exclusion_mode, which candidate comparison ignores.
## - The package member count is whatever the declared layout lists and must equal the actual package inventory; no literal count is trusted.
## - Debug allowance is a nonnegative plain integer, zero is valid, the default is four, and an adapter extension above four is BLOCKED.
## - For a target that is the top level of its own git work tree the candidate is tracked plus untracked non-ignored content (STATE-102) minus the generated directory names: what git reports as ignored is excluded, and an ignored directory is skipped wholesale, with no descent and no link refusal inside it.
## - The generated directory names (.git, .methodology, __pycache__, .pytest_cache, doxygen_output, output) are excluded by name in every target mode, git included: a deliberate superset of STATE-102 limited to regenerable build and cache outputs, kept so that no target that worked before the repair regresses. No other name is excluded in git mode.
## - The fallback exclusion list (the generated names plus the Anti-Loop counter names and further regenerable caches) is a heuristic for a target without usable git rules: not a repository, git not launchable, or a subdirectory of a larger repository whose foreign ignore rules could blind the candidate. Git targets use git's own ignore rules on top of the generated names, never the heuristic part of that list.
## - A confirmed repository whose ignore enumeration fails is refused, never downgraded to the fallback list.
## - Candidate content still refuses links and nonregular members; an unignored new file still changes the digest. Bytecode files and the legacy .test_attempts file stay skipped in every mode.
## - An inventory taken with an explicit exclusion set (the package binding) never consults git, so package identity cannot vary with a repository ignore file. The explicit names are matched against directory names and file names alike; the package set holds the regenerable caches and the ambient .DS_Store file, which are never package members.
## - Every git call goes through one wrapper (_git_run) and is hermetic: read only, no optional locks, core.fsmonitor forced off so a program configured in the target repository never runs, and the repository-redirecting environment of the caller (GIT_DIR, GIT_WORK_TREE, GIT_INDEX_FILE, GIT_OBJECT_DIRECTORY, GIT_ALTERNATE_OBJECT_DIRECTORIES, GIT_COMMON_DIR, GIT_NAMESPACE, GIT_CEILING_DIRECTORIES, GIT_DISCOVERY_ACROSS_FILESYSTEM) dropped, so the target is always judged by its own repository and index. Content filters a repository configures (filter.NAME.clean, for example git-lfs) are deliberately not disabled: the status observation needs them to judge clean content, and git runs them only for a tracked file whose stat data changed; the ls-files enumeration that defines the candidate never runs them. Hooks and core.hooksPath are irrelevant to these read commands.
## - A package membership refusal names up to three missing and up to three undeclared relative paths, so the offender is visible without a second probe.
## - Private locators/payloads/credentials are absent from source; logs use safe logical classes/counts.
## @rationale
## Q: Why a second copy of the state helper rather than a shared one?
## A: The sibling package helper is outside this package's scope; a shared extraction would change that package and is a separate decision. This copy binds its own identity and keeps the state contract unchanged apart from the recorded exclusion mode, so either runtime reads the same ledger shape.
## Q: Why take the member count from the declared layout?
## A: The layout already declares the exact member list and the helper compares it with the real inventory in both directions; a second literal count could only drift from it.
## Q: Why preserve unavailable/unsupported limits?
## A: Same-author fixtures and bounded recognizers cannot replace independent source meaning, current maps or actual native smoke.
## Q: Why do git's ignore rules, and not a fixed name list, define the candidate of a git target?
## A: STATE-102 defines the candidate as tracked plus untracked non-ignored content, TST-501 makes the Anti-Loop counter an ignored file owned by session hooks and FINAL-202 calls the Doxygen map ignored output. A fixed list alone can neither know a project's ignored map directory nor stay small enough to hide no real directory; a red suite run or a map build must not look like authored change, and a new unignored file must. Only the regenerable build and cache names stay excluded by name (see the next question).
## Q: Why must the target be the work-tree top level, and why is a failing enumeration refused?
## A: A target below a larger repository would inherit that repository's ignore rules, and a catch-all rule above it would blind the whole candidate; such a target uses the declared fallback instead. Once the target is confirmed as a repository, silently weakening to the heuristic would change the identity basis unnoticed, so the failure is refused with a diagnostic.
## Q: Why are the generated directory names still excluded by name in a git target that does not ignore them?
## A: Before the repair doxygen_output, output, __pycache__ and .pytest_cache were never candidate content; making them depend on a project's ignore file would turn a Doxygen build or a test run during Code into a change outside the scope for every git project that has not ignored its map or cache output, a regression of working targets. The superset is deliberate and limited to regenerable build and cache outputs; it is a documented departure from exact STATE-102 (FINAL-202 expects such output to be ignored anyway), not a general name list.
## Q: Why does every git call force core.fsmonitor off and drop the caller's repository-redirecting environment?
## A: Round 3 reproduced two failures. git ls-files --others --ignored and git status run the program a target repository configures as core.fsmonitor, so observing a repository executed code it owns; and an inherited GIT_DIR or GIT_INDEX_FILE made the enumeration read a foreign index, which silently dropped a tracked file from the candidate (fail open). A command-line -c value outranks repository, environment and global configuration, and removing the redirecting variables makes git discover the repository of the target path itself.
## @changes
## LAST_CHANGE: [1.0.0 - Neutral1.1.0 compatibility; Claude Code package binding of the schema2 helper: package methodology-claude, profile colocated-in-place, roles under agents, hook-config and workflow member kinds, member count from the declared layout. Debug repair of independent Review round 2: the target candidate follows git ignore rules (STATE-102) with a declared fallback list otherwise, the candidate records exclusion_mode, ignored trees are skipped before any link check, candidate comparison uses files and digest, and the generated directory names stay excluded by name in git mode as a deliberate superset. Debug repair of independent Review and QA round 3: every git call is hermetic (core.fsmonitor off, repository-redirecting environment dropped), the package exclusion covers the ambient .DS_Store file, and the package membership refusal names the offending paths.]
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => run_state._module_contract
## FUNC 4[Stamp a chronological observation in UTC.] => run_state._stamp
## FUNC 9[Expose and enforce one named structural invariant.] => run_state._expect
## FUNC 9[Validate a nonempty plain logical string without exposing its value.] => run_state._text
## FUNC 9[Reject invalid numeric allowance/counter types before spending.] => run_state._plain_integer
## FUNC 9[Parse the declared textual Debug cap without ambiguous coercion.] => run_state._decimal_cap
## FUNC 9[Reject duplicate JSON keys without silently overwriting control data.] => run_state._unique_object
## FUNC 9[Reject nonfinite constants forbidden by the actual JSON record contract.] => run_state._reject_constant
## FUNC 8[Read one real complete JSON object with duplicate-key refusal.] => run_state.read_json
## FUNC 8[Derive reproducible identity from complete canonical JSON data.] => run_state._digest
## FUNC 9[Bind actual regular source bytes and numeric mode without following links.] => run_state._file
## FUNC 9[Refuse escaping and noncanonical relative source paths.] => run_state._relative
## FUNC 9[Run one read-only git command hermetically: no optional locks, core.fsmonitor off, repository-redirecting environment dropped.] => run_state._git_run
## FUNC 9[Learn which untracked paths git reports as ignored for a repository-top-level target, or decline to the fallback list.] => run_state._git_ignored
## FUNC 9[Account complete regular source membership and byte/mode identity under git ignore rules, the declared fallback list or an explicit exclusion set.] => run_state.inventory
## FUNC 7[Compose the package membership refusal naming up to three missing and three undeclared paths.] => run_state._membership_diagnostic
## FUNC 9[Pin actual complete in-place package, adapter, neutral and spec identities.] => run_state._bindings
## FUNC 8[Acquire real target repository observations without optional Git locks.] => run_state._baseline
## FUNC 9[Refuse incomplete, unsupported or wrongly typed local ledger data before storage or replay.] => run_state._state_shape
## FUNC 9[Permit refusal chronology only on a complete correctly located existing schema2 ledger.] => run_state._diagnostic_ready
## FUNC 9[Refuse unsupported schema or stale locked inputs/target before continuation.] => run_state.validate_state
## FUNC 9[Create one owned source-bound schema2 run without overwrite or budget reset.] => run_state.initialize
## FUNC 9[Require real readable evidence contained by the assigned target.] => run_state._artifact
## FUNC 9[Validate every actual nonempty contained evidence reference.] => run_state._evidence
## FUNC 9[Refuse missing or wrong plain types in declared required payload fields.] => run_state._typed_fields
## FUNC 9[Validate current successful Code map evidence without claiming its semantics.] => run_state._doxygen
## FUNC 9[Validate canonical phase-dependent return evidence and all eight named QA rows.] => run_state._payload
## FUNC 9[Accept only the explicit scoped authored delta within saved Architect authority.] => run_state._source_change
## FUNC 9[Accept one parent event without partial input mutation and charge repair before dispatch.] => run_state.advance
## FUNC 9[Checkpoint a complete owned state atomically and clean only its temporary file.] => run_state.save
## FUNC 9[Deliver the helper real CLI answer and honest diagnostics through their own channels.] => run_state.main
## @usecases
## - Parent/test: inspect real current inputs -> accept scoped current outcome or refuse unsafe/malformed/stale input.
## - Root orchestrator: init, record each verified phase return, show to resume -> one single-writer ledger with cumulative Debug spend.
## - Independent judge: compare actual assertions/source/CLI receipts -> bounded evidence; native acceptance remains separately owned.
## @GREP_SUMMARY Claude Code package, run state, hermetic git, core.fsmonitor, GIT_DIR, GIT_INDEX_FILE, .DS_Store, package membership diagnostic, schema2 ledger, in-place plugin binding, actual source identity,
##   current canonical returns, causal Debug budget, eight named scans, real CLI streams, refusal and no inferred consent,
##   candidate identity, git ignore rules, ls-files, Anti-Loop counter, fallback exclusion list, exclusion mode
## @STRUCTURE ▶ explicit owned inputs → ◇ validate actual shape and identity → ○ bounded operation
##   → ⊕ actual observation/assertions → ⎋ current result or honest refusal
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import logging
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import stat
import subprocess
import sys
import unicodedata
import uuid

logger = logging.getLogger(__name__)
SCANS = ('green-test-trap', 'quantitative-ac', 'semantic-trace', 'infra-dod', 'side-effect-channel', 'secret-leak', 'real-path-shape', 'discriminating-test')
STATE_FIELDS = {'schema_version','contract_version','run_id','status','phase','target','framework','adapter_path','spec_path','approval','bindings','input_identity','plan','baseline','baseline_candidate','candidate','debug_cap','debug_spent','retry_episodes','retry_limits','accepted','approved_scope','history'}
PACKAGE_GENERATED = {'__pycache__', '.pytest_cache', 'doxygen_output', '.DS_Store'}
# PACKAGE_GENERATED is matched against directory and file names alike: the ambient macOS .DS_Store file is ignored by repositories and never published, so it is never a package member.
GIT_REDIRECTING = ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_OBJECT_DIRECTORY', 'GIT_ALTERNATE_OBJECT_DIRECTORIES', 'GIT_COMMON_DIR', 'GIT_NAMESPACE', 'GIT_CEILING_DIRECTORIES', 'GIT_DISCOVERY_ACROSS_FILESYSTEM')
# GIT_REDIRECTING lists the inherited variables that point git at another repository, index, object store or discovery boundary; _git_run drops them from the child environment.
GIT_PROGRAMLESS = ('--no-optional-locks', '-c', 'core.fsmonitor=false')
# GIT_PROGRAMLESS is the fixed argument prefix of every git call: no optional locks, and the repository-configured core.fsmonitor program is switched off (a command-line value outranks repository, environment and global configuration).
KINDS = {'skill', 'role', 'helper', 'test', 'test-guide', 'config', 'plugin-manifest', 'adapter', 'layout', 'example', 'documentation', 'hook-config', 'workflow'}
PACKAGE_NAME = 'methodology-claude'
PACKAGE_VERSION = '1.0.0'
PACKAGE_PROFILE = 'colocated-in-place'
CONTRACT_VERSION = 'methodology-claude/1.0.0'
ROLES = ('architect', 'coder', 'debugger', 'qa', 'reviewer', 'searcher')
CORE = ('concepts/principles.md', 'roles/_base.md', 'code/exoskeleton.md', 'code/ldd.md', 'code/doxygen.md', 'code/tests.md')
TERMINAL = {'SUCCESS', 'SPEC_BLOCKED', 'VISUAL_GATE_FAIL', 'ESCALATED', 'BLOCKED', 'ERROR', 'ESCALATED_FINALIZE'}
PHASE_ROLES = {'bootstrap': {'searcher'}, 'architect': {'architect'}, 'code': {'coder'}, 'qa': {'qa'}, 'review': {'reviewer'}, 'debug': {'debugger'}, 'finalize': {'architect', 'root'}}
STATUS = {'bootstrap': {'SUCCESS', 'BLOCKED'}, 'architect': {'SUCCESS', 'BLOCKED'}, 'code': {'SUCCESS', 'BUG_REPORT', 'BLOCKED'}, 'qa': {'SUCCESS', 'BUG_REPORT', 'BLOCKED'}, 'review': {'SUCCESS', 'BUG_REPORT', 'BLOCKED'}, 'debug': {'FIXED', 'BLOCKED'}, 'finalize': {'SUCCESS', 'BLOCKED', 'ESCALATED_FINALIZE'}}
COMMON = {'phase', 'role', 'status', 'summary', 'runId', 'inputIdentity', 'candidateIdentity', 'contractVersion', 'evidence'}
FIELDS = {
    'bootstrap': {'isEmpty', 'classificationHint', 'fileCount', 'files', 'recommendations', 'mapEvidence', 'limitations', 'reason'},
    'architect': {'classification', 'projectType', 'taskType', 'planPath', 'featureSlices', 'mayEdit', 'doNotTouch', 'acceptanceCriteria', 'specDeficiencies', 'specBlocked', 'visualGate', 'blockReason', 'businessRequirementsPath', 'limitations', 'reason'},
    'code': {'artifacts', 'testGuidePath', 'testSummary', 'deviations', 'measurements', 'logs', 'doxygen', 'detectedUi', 'classifierEvidence', 'externalIdsVerified', 'bugReport', 'reason', 'limitations'},
    'qa': {'testSummary', 'scans', 'findings', 'limitations', 'bugReport', 'reason'},
    'review': {'findings', 'limitations', 'diffEvidence', 'scopeJudgment', 'bugReport', 'reason'},
    'debug': {'rootCause', 'fix', 'filesTouched', 'postFixAudit', 'testSummary', 'regressionEvidence', 'origin', 'reason', 'limitations'},
    'finalize': {'report', 'classification', 'planPath', 'testsPath', 'logPath', 'doxygenPath', 'testSummary', 'acceptanceEvidence', 'qaEvidence', 'reviewEvidence', 'liveEvidence', 'blastRadius', 'scopeDeviations', 'limitations', 'reason', 'requiredRepair'}
}
GENERATED = {'.git', '.methodology', '__pycache__', '.pytest_cache', 'doxygen_output', 'output'}
# GENERATED is excluded by name in every target mode (a deliberate superset of git's ignore rules, limited to regenerable build and cache outputs).
# Fallback exclusion list: GENERATED plus a declared heuristic for a target without usable git ignore rules; a git target adds git's own rules instead.
FALLBACK_DIRS = GENERATED | {'.ruff_cache', '.mypy_cache', 'node_modules', '.venv', 'venv', 'htmlcov'}
FALLBACK_FILES = {'.test_counter.json', '.test_attempts', '.coverage'}


# region FUNC__stamp [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Stamp a chronological observation in UTC.
## @uses datetime.datetime.now, datetime.timezone.utc
## @io No arguments. Returns str in ISO8601 UTC format, e.g. 2026-10-09T00:00:00+00:00. No external writes or logger sink; clock observation only. No input validation/error path. Importance:4.
## @complexity 5
def _stamp():
    return datetime.now(timezone.utc).isoformat()
# endregion FUNC__stamp

# region FUNC__expect [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Expose and enforce one named structural invariant.
## @uses logging.Logger.info, logging.Logger.error
## @io condition bool-like expression and label safe str controlled by this module; no user payload. Returns None on true; raises ValueError(label) on false after own IMP10 REJECT; true emits IMP9 ACCEPT. No file writes. Example: _expect(True, "known check") returns None. Importance:9.
## @complexity 5
def _expect(condition, label):
    if not condition:
        logger.error('[IMP:10][_expect][REJECT] invariant=%s', label)
        raise ValueError(label)
    logger.info('[IMP:9][_expect][ACCEPT] invariant=%s', label)
# endregion FUNC__expect

# region FUNC__text [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Validate a nonempty plain logical string without exposing its value.
## @uses run_state._expect, logging.Logger.info, logging.Logger.error
## @io value object; label safe logical str. Returns original plain str with nonblank content; never coerces. Raises ValueError for non-str or blank; own safe failure trace. No I/O except caller-configured logger. Example: _text("phase", "field") returns "phase". Importance:9.
## @complexity 5
def _text(value, label):
    # START_BLOCK_Validation
    try:
        _expect(type(value) is str and bool(value.strip()), label)
        logger.info('[IMP:9][_text][VALID] nonempty logical field')
        return value



    except (OSError, ValueError, KeyError, TypeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_text][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
# endregion FUNC__text

# region FUNC__plain_integer [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Reject invalid numeric allowance/counter types before spending.
## @uses run_state._expect, logging.Logger.info, logging.Logger.error
## @io value object, label safe str, minimum plain int default0. Returns original plain int at least minimum; bool and fractional/string values rejected with ValueError. No counter mutation or file writes; own safe validation/failure trace. Example: _plain_integer(0, "cap") returns0; True raises. Importance:9.
## @complexity 5
def _plain_integer(value, label, minimum=0):
    # START_BLOCK_Validation
    try:
        _expect(type(value) is int and value >= minimum, label)
        logger.info('[IMP:9][_plain_integer][VALID] minimum=%d', minimum)
        return value



    except (OSError, ValueError, KeyError, TypeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_plain_integer][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
# endregion FUNC__plain_integer

# region FUNC__decimal_cap [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Parse the declared textual Debug cap without ambiguous coercion.
## @uses re.fullmatch, run_state._expect, builtins.int, logging.Logger.info, logging.Logger.error
## @io value plain str in exact unsigned decimal spelling: 0 or a nonzero ASCII digit followed by ASCII digits. Returns nonnegative plain int; signs, leading zeros, whitespace and fractional syntax raise ValueError with owning safe failure trace. No writes or consent inference; values above4 remain separately unsupported at init/binding. Example: 0 accepted, +4 and 04 refused. Importance:9.
## @complexity 5
def _decimal_cap(value):
    logger.info('[IMP:4][_decimal_cap][START] strict decimal allowance spelling')
    try:
        _expect(type(value) is str and re.fullmatch(r'0|[1-9][0-9]*',value) is not None, 'Debug text requires canonical unsigned decimal spelling')
        number=int(value)
        logger.info('[IMP:9][_decimal_cap][RESULT] canonical decimal parsed')
        return number
    except (ValueError,TypeError) as error:
        logger.error('[IMP:10][_decimal_cap][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC__decimal_cap

# region FUNC__unique_object [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Reject duplicate JSON keys without silently overwriting control data.
## @uses run_state._expect, logging.Logger.info, logging.Logger.error
## @io pairs finite list of key/value tuples supplied by json parser. Returns insertion-preserving dict; duplicate keys raise ValueError before accepting a parsed object. No input mutation or writes; safe key count/error-class trace only. Example: [("a",1)] becomes {"a":1}; repeated a refuses. Importance:9.
## @complexity 5
def _unique_object(pairs):
    # START_BLOCK_Validation
    try:
        result = {}
        for key, value in pairs:
            _expect(key not in result, 'duplicate JSON key')
            result[key] = value
        logger.info('[IMP:9][_unique_object][VALID] keys=%d', len(result))
        return result



    except (OSError, ValueError, KeyError, TypeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_unique_object][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
# endregion FUNC__unique_object

# region FUNC__reject_constant [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Reject nonfinite constants forbidden by the actual JSON record contract.
## @uses logging.Logger.error
## @io value parser-supplied constant string. Always emits owning IMP10 then raises ValueError without echoing its text. No writes or partial object acceptance. Example: NaN in a record is rejected before state processing. Importance:9.
## @complexity 5
def _reject_constant(value):
    logger.error('[IMP:10][_reject_constant][FAIL] nonfinite JSON literal refused')
    raise ValueError('nonfinite JSON literal')
# endregion FUNC__reject_constant

# region FUNC_read_json [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Read one real complete JSON object with duplicate-key refusal.
## @uses json.loads, pathlib.Path.read_text, run_state._unique_object, run_state._reject_constant, run_state._expect
## @io path str or Path to permitted readable UTF8 JSON. Returns dict; object_pairs_hook checks every nested object. Raises OSError for absent/unreadable file, UnicodeError for invalid UTF8, ValueError for malformed/duplicate/nonobject JSON. No writes; actual file-read and safe class trace. Example: a file containing {"a":1} yields that object. Importance:8.
## @complexity 5
def read_json(path):
    logger.info('[IMP:7][read_json][READ] JSON artifact')
    try:
        value = json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=_unique_object, parse_constant=_reject_constant)
        _expect(type(value) is dict, 'JSON root requires object')
        logger.info('[IMP:9][read_json][RESULT] validated object')
        return value
    except (OSError, UnicodeError, ValueError) as exc:
        logger.error('[IMP:10][read_json][FAIL] kind=%s', type(exc).__name__)
        raise
# endregion FUNC_read_json

# region FUNC__digest [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Derive reproducible identity from complete canonical JSON data.
## @uses json.dumps, hashlib.sha256
## @io value JSON-serializable object. Returns lowercase 64-character SHA256 of UTF8 sorted-key compact JSON; no mutation, I/O or clock. TypeError for unsupported value. Example: same ordered mappings with reordered keys yield equal identity. Importance:8.
## @complexity 5
def _digest(value):
    data = json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()
    return hashlib.sha256(data).hexdigest()
# endregion FUNC__digest

# region FUNC__file [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Bind actual regular source bytes and numeric mode without following links.
## @uses pathlib.Path.lstat, pathlib.Path.read_bytes, stat.S_ISREG, stat.S_IMODE, hashlib.sha256, run_state._expect
## @io path str/Path to regular nonsymlink file. Returns dict path absolute resolved str, type regular, mode nonnegative numeric permission bits, bytes nonnegative int and actual SHA256 str. OSError on read/lstat failure; ValueError on nonregular/link. Reads all bytes; writes nothing; safe count/class trace. Example: one-byte owned file produces bytes1 and its actual digest. Importance:9.
## @complexity 5
def _file(path):
    p = Path(path)
    logger.info('[IMP:7][_file][READ] regular input identity')
    try:
        info = p.lstat()
        _expect(stat.S_ISREG(info.st_mode), 'input must be a regular nonsymlink file')
        data = p.read_bytes()
        logger.info('[IMP:9][_file][RESULT] bytes=%d', len(data))
        return {'path': str(p.resolve()), 'type': 'regular', 'mode': stat.S_IMODE(info.st_mode), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    except (OSError, ValueError) as exc:
        logger.error('[IMP:10][_file][FAIL] kind=%s', type(exc).__name__)
        raise
# endregion FUNC__file

# region FUNC__relative [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Refuse escaping and noncanonical relative source paths.
## @uses pathlib.PurePosixPath, run_state._text, run_state._expect
## @io value plain nonempty str in canonical POSIX relative spelling. Returns unchanged value; absolute, dot, dot-dot, normalization differences refuse with ValueError. No traversal/writes; own trace. Example: "a b/file.py" accepted, "../file.py" refused. Importance:9.
## @complexity 5
def _relative(value):
    # START_BLOCK_Validation
    try:
        value = _text(value, 'relative path required')
        p = PurePosixPath(value)
        _expect(not p.is_absolute() and '..' not in p.parts and '.' not in p.parts and str(p) == value and bool(p.parts), 'unsafe relative path')
        logger.info('[IMP:9][_relative][VALID] canonical relative path')
        return value



    except (OSError, ValueError, KeyError, TypeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_relative][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
# endregion FUNC__relative

# region FUNC__git_run [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, HermeticGit; TECH(7): Python, git, subprocess]
## @purpose Observe a target repository through git without letting the repository or the caller's environment steer the observation: no program the repository configures runs, and no inherited variable points git at a foreign repository or index.
## @uses subprocess.run, os.environ, run_state.GIT_PROGRAMLESS, run_state.GIT_REDIRECTING, logging.Logger.info
## @io project actual directory str/Path passed to git -C; args list of git arguments after the fixed prefix; text bool keyword-only, default False for bytes output. Returns the CompletedProcess of git --no-optional-locks -c core.fsmonitor=false -C project args, started with the caller environment minus every GIT_REDIRECTING variable, with stdout and stderr captured and the real exit code kept. Raises OSError when git cannot be launched, which each caller handles in its own way. Reads only: no repository writes, no optional locks, no repository-configured fsmonitor program. Content filters are not disabled (see the module invariant). Example: with GIT_DIR pointing at another repository, ls-files for a target still reads the target own index.
## @complexity 4
def _git_run(project, args, *, text=False):
    # START_BLOCK_BusinessLogic
    # BUG_FIX_CONTEXT: Review and QA round 3 showed two non-hermetic effects of the former bare calls. A target repository configuring core.fsmonitor had its program executed by git ls-files --others and git status (observation ran repository-owned code); an inherited GIT_DIR or GIT_INDEX_FILE made the ignore enumeration read a foreign index, which silently dropped a tracked file from the candidate (fail open).
    # Previous: subprocess.run(['git', '--no-optional-locks', '-C', root] + args) with the inherited environment. Problem: repository and caller state decided what ran and which index was read.
    # Fix: one wrapper for every call adds -c core.fsmonitor=false (command-line configuration outranks every other source) and removes the repository-redirecting variables, so git discovers the repository of the path itself.
    environment = {key: value for key, value in os.environ.items() if key not in GIT_REDIRECTING}
    proc = subprocess.run(['git'] + list(GIT_PROGRAMLESS) + ['-C', str(project)] + list(args), capture_output=True, text=text, env=environment)
    logger.info('[IMP:7][_git_run][READ] command=%s exit=%d dropped_variables=%d', args[0], proc.returncode, len(os.environ.keys() & set(GIT_REDIRECTING)))
    return proc
    # END_BLOCK_BusinessLogic
# endregion FUNC__git_run

# region FUNC__git_ignored [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, GitIgnoreRules; TECH(7): Python, git, subprocess]
## @purpose Learn exactly which untracked paths git itself reports as ignored for a target that is the top level of its own repository, so the candidate identity is tracked plus untracked non-ignored content (STATE-102).
## @uses run_state._git_run, os.path.samefile, os.fsdecode, posixpath.normpath, unicodedata.normalize, run_state._expect, logging.Logger.info, logging.Logger.error
## @io root resolved existing directory Path. Returns None when the declared fallback list must apply: git cannot be launched, root is not inside a work tree, or root is not the work-tree top level (a subdirectory would inherit foreign ignore rules). Otherwise returns a frozenset of NFC-normalized POSIX paths relative to root, one per ignored untracked file, link or wholly ignored directory, without a trailing slash; the single entry . means the whole root is ignored. A confirmed repository whose enumeration fails raises ValueError after the owning IMP10 trace, never a silent downgrade; a launch failure of the second git call raises OSError. Reads only: git rev-parse and ls-files through the hermetic wrapper (no optional locks, core.fsmonitor off, repository-redirecting environment dropped), no repository writes. Example: a repository ignoring docs/api/xml/ yields a set holding docs/api/xml.
## @complexity 6
def _git_ignored(root):
    logger.info('[IMP:7][_git_ignored][READ] git ignore rules of the target')
    try:
        # START_BLOCK_Validation
        try:
            top = _git_run(root, ['rev-parse', '--show-toplevel'])
        except OSError as error:
            logger.info('[IMP:8][_git_ignored][GIT_UNAVAILABLE] kind=%s; declared fallback list applies', type(error).__name__)
            return None
        if top.returncode != 0 or not top.stdout.strip():
            logger.info('[IMP:8][_git_ignored][NO_WORK_TREE] git reports no usable work tree for the target; declared fallback list applies')
            return None
        try:
            same = os.path.samefile(os.fsdecode(top.stdout.rstrip(b'\n')), root)
        except OSError:
            same = False
        if not same:
            logger.info('[IMP:8][_git_ignored][NOT_TOPLEVEL] target lies below a larger work tree; foreign ignore rules are not applied, declared fallback list applies')
            return None
        logger.info('[IMP:9][_git_ignored][VALIDATION_SUCCESS] target is the work-tree top level; git ignore rules apply')
        # END_BLOCK_Validation
        # START_BLOCK_BusinessLogic
        listing = _git_run(root, ['ls-files', '--others', '--ignored', '--exclude-standard', '--directory', '-z'])
        _expect(listing.returncode == 0, 'git ignore enumeration failed')
        ignored = frozenset(unicodedata.normalize('NFC', posixpath.normpath(os.fsdecode(raw))) for raw in listing.stdout.split(b'\0') if raw)
        logger.info('[IMP:9][_git_ignored][RESULT] ignored_paths=%d', len(ignored))
        return ignored
        # END_BLOCK_BusinessLogic
    except (OSError, ValueError) as exc:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_git_ignored][FAIL] kind=%s', type(exc).__name__)
        raise
        # END_BLOCK_ErrorHandling
# endregion FUNC__git_ignored

# region FUNC_inventory [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python, git]
## @purpose Account complete regular source membership and byte/mode identity: for a target, tracked plus untracked non-ignored content under git's own ignore rules or the declared fallback list; for an explicit exclusion set, the plain name-based population the package binding needs.
## @uses os.walk, pathlib.Path.relative_to, unicodedata.normalize, run_state._git_ignored, run_state._file, run_state._digest, run_state._expect
## @io root actual directory str/Path; excluded None for a target or a finite set of names for an explicit name-only inventory (PACKAGE_GENERATED for the package, GENERATED as before); the names are matched against directory names and file names alike, so the package set drops the ambient .DS_Store file as well as the regenerable caches. A target whose root is a git work-tree top level uses mode git: the GENERATED names (.git, .methodology, __pycache__, .pytest_cache, doxygen_output, output) are excluded by name, plus what git reports as ignored, and an ignored directory is skipped wholesale without descent or link refusal; any other target uses mode fallback with FALLBACK_DIRS (GENERATED plus caches) and FALLBACK_FILES, a documented heuristic. Bytecode files and .test_attempts are skipped in every mode. Returns files sorted by relative path with type/mode/bytes/SHA256, digest over full rows, sorted exclusions, and for a target also exclusion_mode git or fallback; an explicit set returns exactly the original three keys. Walk/read errors raise OSError; links/nonregular members of candidate content and a failing git enumeration raise ValueError. Reads files only; no writes. Deleted/new/modified differences follow row comparison. Example: an ignored tests/.test_counter.json never changes the digest, adding an unignored x.py does.
## @complexity 7
def inventory(root, excluded=None):
    root = Path(root).resolve()
    logger.info('[IMP:7][inventory][READ] source tree')
    rows = []
    skipped = 0
    try:
        _expect(root.is_dir(), 'source directory unavailable')
        # START_BLOCK_ExclusionPolicy
        # BUG_FIX_CONTEXT: Review round 2 reproduced candidate drift from git-ignored files (the hook-owned Anti-Loop counter bumped by a red QA run, a Doxygen map under an ignored directory, an in-project virtual environment with links).
        # Previous: every file under the target was hashed except six fixed directory names, and any link anywhere was refused. Problem: the identity was not STATE-102 (tracked plus untracked non-ignored), so ordinary tool output was refused as an unexpected candidate change and Debug was never entered.
        # Fix: a target that is the top level of its git work tree excludes what git reports as ignored and skips ignored trees before any link check; other targets use the declared heuristic fallback list; an explicit exclusion set keeps its original name-only behavior for the package binding.
        # BUG_FIX_CONTEXT: Review and QA round 3 reproduced an init and record failure caused by an ambient macOS .DS_Store file inside the package (ignored by the repository, never published): the explicit name set was matched against directory names only, so the file counted as an undeclared package member.
        # Previous: file_names was empty in names mode. Problem: PACKAGE_GENERATED could never exclude a file. Fix: the explicit names are matched against file names too; the package set now holds .DS_Store.
        # Second note (root decision): the first form of the fix dropped the GENERATED names (doxygen_output, output, __pycache__, .pytest_cache) in git mode, so a git project that does not ignore its Doxygen output or caches would have started failing at Code. They stay excluded by name in git mode too, a deliberate superset of STATE-102 limited to regenerable build and cache outputs.
        if excluded is not None:
            mode, ignored, dir_names, file_names, exclusions = 'names', frozenset(), set(excluded), set(excluded), sorted(excluded)
        else:
            ignored = _git_ignored(root)
            if ignored is None:
                mode, ignored, dir_names, file_names, exclusions = 'fallback', frozenset(), FALLBACK_DIRS, FALLBACK_FILES, sorted(FALLBACK_DIRS | FALLBACK_FILES)
            else:
                mode, dir_names, file_names, exclusions = 'git', GENERATED, set(), sorted(GENERATED)
        logger.info('[IMP:8][inventory][EXCLUSION] mode=%s git_ignored_paths=%d', mode, len(ignored))
        # END_BLOCK_ExclusionPolicy
        # START_BLOCK_Walk
        walk = [] if '.' in ignored else os.walk(root, followlinks=False, onerror=lambda error: (_ for _ in ()).throw(error))
        for folder, dirs, files in walk:
            prefix = '' if folder == str(root) else Path(folder).relative_to(root).as_posix() + '/'
            kept = []
            for name in sorted(dirs):
                if name in dir_names or (ignored and unicodedata.normalize('NFC', prefix + name) in ignored):
                    skipped += 1
                else:
                    kept.append(name)
            dirs[:] = kept
            for name in kept:
                _expect(not (Path(folder) / name).is_symlink(), 'source directory link unsupported')
            for name in sorted(files):
                p = Path(folder) / name
                if name.endswith(('.pyc', '.pyo')) or name == '.test_attempts' or name in file_names or (ignored and unicodedata.normalize('NFC', prefix + name) in ignored):
                    skipped += 1
                    continue
                row = _file(p)
                row['path'] = p.relative_to(root).as_posix()
                rows.append(row)
        # END_BLOCK_Walk
        rows.sort(key=lambda row: row['path'])
        result = {'files': rows, 'digest': _digest(rows), 'exclusions': exclusions}
        if excluded is None:
            result['exclusion_mode'] = mode
        logger.info('[IMP:9][inventory][RESULT] count=%d mode=%s skipped=%d', len(rows), mode, skipped)
        return result
    except (OSError, ValueError) as exc:
        logger.error('[IMP:10][inventory][FAIL] kind=%s', type(exc).__name__)
        raise
# endregion FUNC_inventory

# region FUNC__membership_diagnostic [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, PackageMembership; TECH(7): Python]
## @purpose Let the refusal of a package whose tree and layout disagree name the offending members, so a maintainer sees the file at once instead of a pathless mismatch.
## @uses builtins.sorted, builtins.len
## @io missing and undeclared collections of relative path str (declared but absent; present but undeclared). Returns the label str package membership mismatch followed, when anything differs, by a colon and the missing and undeclared groups in that order, each naming the first three sorted paths and, beyond three, the count of the rest; with no difference the bare label, so the accepted-invariant trace keeps its former text. Pure: no I/O, no clock. Example: undeclared holding stray.txt yields package membership mismatch: undeclared stray.txt.
## @complexity 3
def _membership_diagnostic(missing, undeclared):
    groups = []
    for kind, paths in (('missing', sorted(missing)), ('undeclared', sorted(undeclared))):
        if paths:
            groups.append(kind + ' ' + ', '.join(paths[:3]) + (' and %d more' % (len(paths) - 3) if len(paths) > 3 else ''))
    return 'package membership mismatch' + (': ' + '; '.join(groups) if groups else '')
# endregion FUNC__membership_diagnostic

# region FUNC__bindings [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Pin actual complete in-place package, adapter, neutral and spec identities.
## @uses run_state.read_json, run_state.inventory, run_state._membership_diagnostic, run_state._file, run_state._relative, run_state._digest, run_state._expect
## @io framework directory, adapter exact framework/adapter.json, spec actual file. Returns resolved path records, one package row per declared layout member (count taken from the layout, never a literal),71 neutral rows, six core names, layout/adapter/spec byte identities and binding digest. Requires package methodology-claude version1.0.0, profile colocated-in-place, roles under agents, exact kinds/sorted membership equal to the actual inventory in both directions (the refusal names up to three missing and three undeclared relative paths; the ambient .DS_Store file is not a member); missing/stub/basic malformed core refuses. Full-content meaning/initial truncation authenticity remains parent judgment; later drift changes locked digest. Raises OSError/ValueError/KeyError/TypeError on unavailable or invalid binding. Reads only; no provider/Git writes. Example: relocated complete in-place tree binds independently of cwd. Importance:9.
## @complexity 9
def _bindings(framework, adapter, spec):
    framework, adapter, spec = Path(framework).resolve(), Path(adapter).resolve(), Path(spec).resolve()
    logger.info('[IMP:7][_bindings][READ] package adapter and effective neutral inputs')
    try:
        _expect(framework.is_dir() and adapter == framework / 'adapter.json', 'framework/adapter binding mismatch')
        layout_path = framework / 'references/package-layout.json'
        layout = read_json(layout_path)
        _expect(layout.get('package') == PACKAGE_NAME and layout.get('version') == PACKAGE_VERSION, 'package identity mismatch')
        _expect(set(layout) == {'package', 'version', 'profile', 'files', 'roles'} and layout.get('profile') == PACKAGE_PROFILE, 'unsupported package profile')
        _expect(layout.get('roles') == {role: 'agents/'+role+'.md' for role in ROLES}, 'package role locations mismatch')
        declarations = layout.get('files')
        _expect(type(declarations) is list and bool(declarations), 'package file population missing')
        expected = [_relative(row['path']) for row in declarations if type(row) is dict and set(row) == {'path', 'kind'}]
        _expect(len(expected) == len(declarations) and len(set(expected)) == len(expected) and expected == sorted(expected) and all(row['kind'] in KINDS for row in declarations), 'invalid package member declarations')
        logger.info('[IMP:9][_bindings][LAYOUT] profile=%s declared=%d', PACKAGE_PROFILE, len(expected))
        package = inventory(framework, PACKAGE_GENERATED)
        # BUG_FIX_CONTEXT: the membership refusal carried no path, so an ambient .DS_Store (round 3) could only be found by a second probe.
        # Previous: _expect(set(expected) == actual, 'package membership mismatch'). Fix: compute both differences and name up to three offenders of each kind in the label.
        actual = {row['path'] for row in package['files']}
        missing, undeclared = set(expected) - actual, actual - set(expected)
        _expect(not missing and not undeclared, _membership_diagnostic(missing, undeclared))
        binding = read_json(adapter)
        _expect(binding.get('spec_root') == '../../', 'co-located spec_root must be ../../')
        neutral = (adapter.parent / _text(binding.get('spec_root'), 'neutral binding missing')).resolve()
        _expect(neutral.is_dir() and neutral == framework.parents[1], 'unsupported detached neutral binding')
        _expect((neutral / 'SPEC_VERSION').read_text().strip() == binding.get('spec_version') == '1.1.0', 'neutral version mismatch')
        profile_cap = _decimal_cap(binding['parameters']['debug-entry-cap'])
        _expect(profile_cap <= 4, 'BLOCKED: adapter Debug extension unsupported')
        declared = binding.get('files')
        _expect(type(declared) is dict and len(declared) == 71, 'neutral owner population mismatch')
        for relative, rule in declared.items():
            _relative(relative)
            _expect(type(rule) is dict and rule.get('mode') in {'reference', 'vendored', 'not-applied'}, 'invalid adapter file binding')
            if rule.get('via'):
                via = (adapter.parent / rule['via']).resolve()
                _expect(via.is_relative_to(framework), 'adapter via outside package')
                _file(via)
        for relative in CORE:
            _expect(relative in declared and declared[relative]['mode'] == 'reference', 'required core reference missing')
            content = (neutral / relative).read_text()
            _expect(content.startswith('---\n') and '\nstatus: draft\n' in content and len(content.splitlines()) > 20, 'required core missing/stub/basic structure invalid; full-content judgment belongs to parent')
        registry = (neutral / 'checks/qa-scans.md').read_text()
        _expect(set(re.findall(r'^\| ([a-z]+(?:-[a-z]+)+) \|', registry, re.M)) == set(SCANS), 'current named scan registry mismatch')
        neutral_rows = [_file(neutral / _relative(relative)) for relative in sorted(declared)]
        for row, relative in zip(neutral_rows, sorted(declared)):
            row['path'] = relative
        result = {'framework': str(framework), 'adapter': _file(adapter), 'package': package, 'neutral_root': str(neutral), 'neutral_version': '1.1.0', 'neutral': neutral_rows, 'spec': _file(spec), 'core': list(CORE), 'debug_cap_profile': profile_cap, 'layout': _file(layout_path)}
        result['digest'] = _digest(result)
        logger.info('[IMP:9][_bindings][RESULT] package=%d neutral=%d', len(expected), len(neutral_rows))
        return result
    except (OSError, ValueError, KeyError, TypeError) as exc:
        logger.error('[IMP:10][_bindings][FAIL] kind=%s', type(exc).__name__)
        raise
# endregion FUNC__bindings

# region FUNC__baseline [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Acquire real target repository observations without optional Git locks.
## @uses run_state._git_run, logging.Logger.info, logging.Logger.error
## @io project directory Path/str. Returns dict head/branch/status, each with real exit int and stdout/stderr str from the hermetic git wrapper (no optional locks, core.fsmonitor off, repository-redirecting environment dropped); a nonrepository retains failed observations rather than invented HEAD. No repository mutations. OSError if process cannot launch. Example: owned non-Git fixture returns nonzero head.exit. Importance:8.
## @complexity 5
def _baseline(project):
    # START_BLOCK_Validation
    try:
        logger.info('[IMP:7][_baseline][READ] actual repository facts')
        rows = {}
        for key, args in [('head', ['rev-parse', 'HEAD']), ('branch', ['branch', '--show-current']), ('status', ['status', '--porcelain=v1', '-z', '-uall'])]:
            proc = _git_run(project, args, text=True)
            rows[key] = {'exit': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}
        logger.info('[IMP:9][_baseline][RESULT] repository=%s', rows['head']['exit'] == 0)
        return rows



    except (OSError, ValueError, KeyError, TypeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_baseline][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
# endregion FUNC__baseline

# region FUNC__state_shape [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Refuse incomplete, unsupported or wrongly typed local ledger data before storage or replay.
## @uses run_state._expect, run_state._text, run_state._plain_integer
## @io state object. Returns None for the complete declared schema2 field surface, exact phase/status, plain nonnegative cap/spend and distinct supported retry units/profile. Unknown/missing fields or invalid types raise ValueError/KeyError/TypeError after owning safe failure trace. No live filesystem/authority authentication or writes; stale accepted bindings can still be retained diagnostically. Example: absent history refuses without fabricated replacement. Importance:9.
## @complexity 5
def _state_shape(state):
    logger.info('[IMP:4][_state_shape][START] complete ledger structure')
    try:
        _expect(type(state) is dict and type(state.get('schema_version')) is int and state.get('schema_version')==2, 'unsupported state schema; historical records are read-only')
        _expect(STATE_FIELDS <= set(state) <= STATE_FIELDS | {'debug_origin'}, 'incomplete or unknown state fields')
        _expect(type(state['schema_version']) is int and state['schema_version']==2, 'unsupported state schema; historical records are read-only')
        _expect(state['phase'] in PHASE_ROLES and state['status'] in TERMINAL | {'RUNNING'}, 'invalid state phase/status')
        for key in ('target','framework','adapter_path','spec_path','run_id','input_identity','contract_version'):
            _text(state[key], 'state logical identity missing')
        for key in ('approval','bindings','plan','baseline','baseline_candidate','candidate','retry_episodes','retry_limits','accepted'):
            _expect(type(state[key]) is dict, 'invalid state object '+key)
        _expect(type(state['history']) is list and type(state['approved_scope']) is list, 'invalid state chronology/scope')
        _plain_integer(state['debug_cap'], 'invalid Debug cap')
        _plain_integer(state['debug_spent'], 'invalid Debug spent')
        _expect(0 <= state['debug_spent'] <= state['debug_cap'] <= 4, 'invalid or unsupported Debug allowance')
        units={'response-correction','extraction','transport','test-session'}
        _expect(set(state['retry_episodes']) == set(state['retry_limits']) == units, 'retry unit population mismatch')
        for unit in units:
            _plain_integer(state['retry_episodes'][unit], 'invalid retry episode')
            _plain_integer(state['retry_limits'][unit], 'invalid retry limit')
        _expect(state['retry_limits']=={'response-correction':1,'extraction':0,'transport':0,'test-session':0}, 'unsupported retry profile')
        logger.info('[IMP:9][_state_shape][RESULT] complete structural ledger')
    except (ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][_state_shape][FAIL] kind=%s',type(error).__name__)
        raise
# endregion FUNC__state_shape

# region FUNC__diagnostic_ready [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Permit refusal chronology only on a complete correctly located existing schema2 ledger.
## @uses run_state._state_shape, pathlib.Path, logging.Logger.info, logging.Logger.error
## @io state object and resolved CLI state Path. Returns bool; true requires complete structural state and exact owned target/run destination. Invalid/old/incomplete shape emits safe own failure and returns False, never fabricates a replacement. No writes or human-authenticity claim. Example: historical schema1 returns False. Importance:9.
## @complexity 5
def _diagnostic_ready(state,path):
    try:
        _state_shape(state)
        eligible=path == Path(state['target'])/'.methodology/runs'/state['run_id']/'state.json'
        logger.info('[IMP:9][_diagnostic_ready][RESULT] eligible=%s',eligible)
        return eligible
    except (ValueError,KeyError,TypeError) as error:
        logger.error('[IMP:10][_diagnostic_ready][FAIL] kind=%s; no replacement ledger',type(error).__name__)
        return False
# endregion FUNC__diagnostic_ready

# region FUNC_validate_state [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Refuse unsupported schema or stale locked inputs/target before continuation.
## @uses run_state._bindings, run_state._file, run_state.inventory, run_state._digest, run_state._text, run_state._plain_integer, run_state._expect
## @io state schema2 dict; allow_source_change bool defaultFalse reserved for controlled Architect/Code/Debug acceptance. Returns actual target inventory. Requires current immutable bindings, approval shape/action/spec/scope, bound plan identity and nonnegative cap/spend; unexpected target drift, judged by the file population and digest of the candidate (git-ignored content is not candidate content), refuses unless caller controls change. No state mutation/writes. OSError/ValueError/KeyError/TypeError signal unavailable/malformed/stale state. Example: schema1 raises read-only historical diagnostic. Importance:9.
## @complexity 5
def validate_state(state, *, allow_source_change=False):
    logger.info('[IMP:4][validate_state][START] current schema and identity')
    try:
        _state_shape(state)
        _expect(type(state) is dict and state.get('schema_version') == 2 and type(state.get('schema_version')) is int, 'unsupported state schema; historical records are read-only')
        _expect(state.get('phase') in PHASE_ROLES and state.get('status') in TERMINAL | {'RUNNING'}, 'invalid state phase/status')
        _text(state['run_id'], 'run identity missing')
        _plain_integer(state['debug_cap'], 'invalid Debug cap')
        _expect(state['debug_cap'] <= 4, 'BLOCKED: above-default Debug extensions unsupported')
        _plain_integer(state['debug_spent'], 'invalid Debug spent')
        _expect(state['debug_spent'] <= state['debug_cap'], 'Debug spend exceeds allowance')
        _expect(type(state['history']) is list and type(state['accepted']) is dict, 'state chronology missing')
        _expect(type(state['approval']) is dict, 'approval provenance missing')
        for key in ('reference', 'action', 'spec', 'scope'):
            _text(state['approval'].get(key), 'approval provenance missing')
        _expect(state['approval']['action'] == 'execute approved specification' and state['approval']['scope'] == state['target'] and state['approval']['spec'] == state['bindings']['spec']['sha256'], 'approval action/spec/scope mismatch')
        current = _bindings(state['framework'], state['adapter_path'], state['spec_path'])
        _expect(current == state['bindings'], 'immutable input identity changed')
        _expect(state['input_identity'] == _digest({'bindings': current['digest'], 'plan': state['plan']}), 'input identity mismatch')
        if state['plan']['status'] == 'bound':
            _expect(_file(state['plan']['path']) == state['plan']['identity'], 'bound plan changed')
        else:
            _expect(state['plan']['status'] == 'pending' and state['phase'] in {'bootstrap', 'architect'}, 'invalid pending plan')
        actual = inventory(state['target'])
        if not allow_source_change:
            # BUG_FIX_CONTEXT: the whole-record comparison would also compare the exclusion bookkeeping (mode and name list), refuse any ledger recorded before exclusion_mode existed and turn a change of basis into a content verdict.
            # Previous: actual == state['candidate']. Problem: identity is the file population and its digest; the bookkeeping keys are not content.
            # Fix: compare the files and the digest only, which is the same verdict for every ledger of one basis.
            recorded = state['candidate']
            _expect(actual['digest'] == recorded.get('digest') and actual['files'] == recorded.get('files'), 'unexpected target candidate change')
        logger.info('[IMP:9][validate_state][RESULT] current identities verified')
        return actual
    except (OSError, ValueError, KeyError, TypeError) as exc:
        logger.error('[IMP:10][validate_state][FAIL] kind=%s', type(exc).__name__)
        raise
# endregion FUNC_validate_state

# region FUNC_initialize [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Create one owned source-bound schema2 run without overwrite or budget reset.
## @uses run_state._bindings, run_state.inventory, run_state._baseline, run_state._file, run_state._digest, run_state.save, pathlib.Path.mkdir
## @io project existing directory, spec real file, approval nonblank parent provenance reference, safe alphanumeric/underscore/hyphen run_id, max_debug plain int0..4 default4; keyword-only framework/adapter actual co-located binding and plan declared contained path. Returns (absolute state Path, schema2 dict). Pins full immutable inputs and the original target inventory (git-ignored content excluded, exclusion_mode recorded); binds existing plan or records pending exactly once; creates only .methodology/runs/run_id and checkpoint after validation. Raises ValueError for invalid scope/types/extension/duplicate run; OSError on unavailable input/checkpoint. Authentic human consent is parent judgment. Example: max_debug0 initializes with debug_spent0 and cannot enter repair. Importance:9.
## @complexity 5
def initialize(project, spec, approval, run_id, max_debug=4, *, framework, adapter, plan):
    logger.info('[IMP:4][initialize][START] bind owned run')
    try:
        # START_BLOCK_Validation
        project, spec, plan = Path(project).resolve(), Path(spec).resolve(), Path(plan).resolve()
        _expect(project.is_dir() and spec.is_file(), 'target/spec unavailable')
        _expect(plan.is_relative_to(project), 'plan must be inside target')
        _expect(re.fullmatch(r'[A-Za-z0-9_-]+', _text(run_id, 'run id missing')) is not None, 'unsafe run id')
        _plain_integer(max_debug, 'invalid Debug cap')
        _expect(max_debug <= 4, 'BLOCKED: above-default Debug extensions unsupported')
        _text(approval, 'authentic parent approval reference required')
        bindings = _bindings(framework, adapter, spec)
        _expect(max_debug <= bindings['debug_cap_profile'], 'requested Debug cap exceeds declared adapter allowance')
        candidate = inventory(project)
        logger.info('[IMP:9][initialize][VALIDATION_SUCCESS] cap=%d', max_debug)
        # END_BLOCK_Validation
        # START_BLOCK_BusinessLogic
        state = {'schema_version': 2, 'contract_version': CONTRACT_VERSION, 'run_id': run_id, 'status': 'RUNNING', 'phase': 'bootstrap', 'target': str(project), 'framework': str(Path(framework).resolve()), 'adapter_path': str(Path(adapter).resolve()), 'spec_path': str(spec), 'approval': {'reference': approval, 'action': 'execute approved specification', 'spec': bindings['spec']['sha256'], 'scope': str(project)}, 'bindings': bindings, 'input_identity': '', 'plan': {'path': str(plan), 'status': 'bound' if plan.exists() else 'pending'}, 'baseline': _baseline(project), 'baseline_candidate': copy.deepcopy(candidate), 'candidate': candidate, 'debug_cap': max_debug, 'debug_spent': 0, 'retry_episodes': {'response-correction': 0, 'extraction': 0, 'transport': 0, 'test-session': 0}, 'accepted': {}, 'approved_scope': [], 'retry_limits': {'response-correction': 1, 'extraction': 0, 'transport': 0, 'test-session': 0}, 'history': [{'kind': 'initialized', 'time': _stamp(), 'plan': 'bound' if plan.exists() else 'pending', 'debug_delta': 0}]}
        if plan.exists():
            state['plan']['identity'] = _file(plan)
        state['input_identity'] = _digest({'bindings': bindings['digest'], 'plan': state['plan']})
        folder = project / '.methodology' / 'runs' / run_id
        _expect(folder.resolve().is_relative_to(project) and not folder.exists(), 'run exists or escapes target; no overwrite/reset')
        folder.mkdir(parents=True, exist_ok=False)
        path = folder / 'state.json'
        save(path, state)
        logger.info('[IMP:9][initialize][RESULT] initialized schema2')
        return path, state
        # END_BLOCK_BusinessLogic
    except (OSError, ValueError, KeyError, TypeError) as exc:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][initialize][FAIL] kind=%s', type(exc).__name__)
        raise
        # END_BLOCK_ErrorHandling
# endregion FUNC_initialize

# region FUNC__artifact [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Require real readable evidence contained by the assigned target.
## @uses run_state._text, run_state._file, run_state._expect, pathlib.Path.resolve
## @io state dict with target absolute path; value nonblank path str. Returns regular-file identity from full bytes/mode. ValueError on outside/missing/nonregular evidence, OSError on unreadable bytes. No writes; resolves containment then reads. Example: target/.methodology/evidence.txt accepted, sibling file refuses. Importance:9.
## @complexity 5
def _artifact(state, value):
    # START_BLOCK_Validation
    try:
        p = Path(_text(value, 'artifact reference missing')).resolve()
        _expect(p.is_relative_to(Path(state['target'])) and p.is_file(), 'artifact outside target or absent')
        identity = _file(p)
        logger.info('[IMP:9][_artifact][RESULT] real contained artifact')
        return identity



    except (OSError, ValueError, KeyError, TypeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_artifact][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
# endregion FUNC__artifact

# region FUNC__evidence [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Validate every actual nonempty contained evidence reference.
## @uses run_state._artifact, run_state._expect
## @io state schema2 target binding; values nonempty list of artifact path strings. Returns ordered list of full file identities. ValueError for empty/non-list/unsafe/absent artifacts; OSError on read error. Reads only, does not mutate list. Example: [owned evidence path] returns one verified identity. Importance:9.
## @complexity 5
def _evidence(state, values):
    # START_BLOCK_Validation
    try:
        _expect(type(values) is list and bool(values), 'nonempty evidence list required')
        rows = [_artifact(state, value) for value in values]
        logger.info('[IMP:9][_evidence][RESULT] count=%d', len(rows))
        return rows



    except (OSError, ValueError, KeyError, TypeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_evidence][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
# endregion FUNC__evidence

# region FUNC__typed_fields [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Refuse missing or wrong plain types in declared required payload fields.
## @uses run_state._expect, run_state._text
## @io result dict, fields dict of logical key to exact builtin type. Returns None; str fields must be nonblank except output which may be empty. ValueError for missing/wrong/plain-bool-as-int types. No mutation/files; safe field count/failure trace. Example: {"exitCode":0} with {"exitCode":int} accepted. Importance:9.
## @complexity 5
def _typed_fields(result, fields):
    # START_BLOCK_Validation
    try:
        for key, kind in fields.items():
            _expect(key in result and type(result[key]) is kind, 'missing or invalid '+key)
            if kind is str and key not in {'output'}:
                _text(result[key], 'empty '+key)
        logger.info('[IMP:9][_typed_fields][RESULT] fields=%d', len(fields))



    except (OSError, ValueError, KeyError, TypeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_typed_fields][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
# endregion FUNC__typed_fields

# region FUNC__doxygen [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Validate current successful Code map evidence without claiming its semantics.
## @uses run_state._typed_fields, run_state._evidence, run_state._artifact, run_state._expect, pathlib.Path.exists, pathlib.Path.read_text, re.search
## @io state with latest accepted candidate/input identity; value dict command/exitCode/output/evidence/mapPath/candidateIdentity/inputIdentity. Returns None for exit0/current real map evidence, or the precisely declared NOT_APPLICABLE record with current identities, actual contained path/exact quote/evidence and bounded explicit-denial recognition. Parent judges real controlling authority/applicability; absence, missing tool/config and generic waiver do not discharge map. ValueError on stale/failed/missing record or invalid prohibition; OSError on evidence read. Reads only; full XML associations and genuine production execution remain parent checks. Example: empty successful command output is valid. Importance:9.
## @complexity 5
def _doxygen(state, value):
    # START_BLOCK_Validation
    try:
        _expect(type(value) is dict, 'Doxygen record required')
        if value.get('status')=='NOT_APPLICABLE':
            _expect(set(value)=={'status','reason','prohibition','evidence','candidateIdentity','inputIdentity'}, 'explicit Doxygen prohibition record required')
            _typed_fields(value, {'reason':str,'prohibition':dict,'evidence':list,'candidateIdentity':str,'inputIdentity':str})
            _expect(value['inputIdentity']==state['input_identity'] and value['candidateIdentity']==state['candidate']['digest'], 'stale Doxygen prohibition identity')
            rule=value['prohibition']
            _expect(set(rule)=={'path','quote'}, 'contained quoted host-rule proof required')
            _artifact(state,rule.get('path'))
            quote=_text(rule.get('quote'),'explicit written prohibition quote missing')
            content=Path(rule['path']).read_text(encoding='utf-8')
            _expect(quote in content and 'doxygen' in quote.lower() and re.search(r'(?i)forbid|prohibit|must not|do not|запрещ|не запуск',quote) is not None, 'quote lacks bounded explicit Doxygen denial evidence; absence is not prohibition')
            _evidence(state,value['evidence'])
            _expect(str(Path(rule['path']).resolve()) in {str(Path(p).resolve()) for p in value['evidence']}, 'prohibition rule must be in actual evidence population')
            logger.info('[IMP:9][_doxygen][PROHIBITION_VALID] contained exact quote; true authority/applicability belongs to parent')
            return
        _expect(set(value) <= {'command','exitCode','output','evidence','mapPath','candidateIdentity','inputIdentity','status'} and value.get('status','PASS')=='PASS', 'unknown Doxygen build record fields/status')
        _typed_fields(value, {'command': str, 'exitCode': int, 'output': str, 'evidence': list, 'mapPath': str, 'candidateIdentity': str, 'inputIdentity': str})
        _expect(value['exitCode'] == 0 and value['inputIdentity'] == state['input_identity'] and value['candidateIdentity'] == state['candidate']['digest'], 'stale/failed Doxygen record')
        _evidence(state, value['evidence'])
        p = Path(value['mapPath']).resolve()
        _expect(p.is_relative_to(Path(state['target'])) and p.exists(), 'Doxygen map unavailable')
        logger.info('[IMP:9][_doxygen][RESULT] current successful map record')



    except (OSError, ValueError, KeyError, TypeError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_doxygen][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_Validation
# endregion FUNC__doxygen

# region FUNC__payload [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Validate canonical phase-dependent return evidence and all eight named QA rows.
## @uses run_state._typed_fields, run_state._evidence, run_state._artifact, run_state._doxygen, run_state._expect, run_state._text
## @io state current schema2; result existing canonical role dict. Returns None after exact known-field/status-dependent validation; QA scans is exactly eight id/status/reason/evidence list rows, findings structured; SUCCESS cannot contain FAIL/BLOCKED. All phase payloads retain actual defined types/artifacts. Accepted Code prohibition is revalidated using unchanged whole-rule identity and current candidate; Finalize may omit doxygenPath only under that valid conditional exception. ValueError/KeyError/TypeError on malformed fields and OSError on evidence access. Reads only, no input mutation; semantic applicability/consent/native independence is parent-owned. Example: ordinal "1" scan refuses. Importance:9. Complexity9 reflects distinct required payload and applicability branches, kept explicit to prevent permissive dispatch.
## @complexity 9
def _payload(state, result):
    phase, status = result['phase'], result['status']
    logger.info('[IMP:4][_payload][START] phase=%s status=%s', phase, status)
    try:
        _expect(set(result) <= COMMON | FIELDS[phase], 'unknown role return field')
        inherited=state['accepted'].get('code',{}).get('doxygen')
        prohibited=type(inherited) is dict and inherited.get('status')=='NOT_APPLICABLE'
        if prohibited:
            _expect(_file(inherited['prohibition']['path'])==state['accepted']['code']['prohibition_identity'], 'accepted host prohibition changed; renewed parent judgment required')
            current=copy.deepcopy(inherited)
            current['candidateIdentity']=state['candidate']['digest']
            _doxygen(state,current)
        _evidence(state, result['evidence'])
        if status in {'BLOCKED', 'ESCALATED_FINALIZE'}:
            _typed_fields(result, {'reason': str, 'limitations': list})
            if status == 'ESCALATED_FINALIZE':
                _typed_fields(result, {'requiredRepair': str})
        elif status == 'BUG_REPORT':
            report = result.get('bugReport')
            _expect(type(report) is dict and set(report) == {'goal', 'actual', 'logAnalysis', 'dataAnalysis', 'hypothesis', 'recommendation'}, 'populated six-field bugReport required')
            _typed_fields(report, {key: str for key in report})
        if phase == 'qa':
            _typed_fields(result, {'testSummary': str, 'scans': list, 'findings': list, 'limitations': list})
            rows = result['scans']
            _expect(len(rows) == 8 and all(type(row) is dict for row in rows), 'eight named scan rows required')
            _expect({row.get('id') for row in rows} == set(SCANS), 'scan identity population mismatch')
            for row in rows:
                _expect(set(row) == {'id', 'status', 'reason', 'evidence'}, 'malformed scan row')
                _text(row['reason'], 'scan reason missing')
                _expect(row['status'] in {'PASS', 'FAIL', 'N/A', 'BLOCKED'}, 'invalid scan status')
                _evidence(state, row['evidence'])
            if status == 'SUCCESS':
                _expect(all(row['status'] in {'PASS', 'N/A'} for row in rows), 'QA cannot pass failed/blocked scan')
            for finding in result['findings']:
                _expect(type(finding) is dict and {'scan', 'code', 'severity', 'message', 'evidence'} <= set(finding) <= {'scan', 'code', 'severity', 'message', 'evidence', 'path', 'line'}, 'malformed finding')
                _expect(finding['scan'] in SCANS and finding['severity'] in {'LOW', 'MEDIUM', 'HIGH'}, 'finding identity/severity mismatch')
                _text(finding['code'], 'finding code missing')
                _text(finding['message'], 'finding message missing')
                _evidence(state, finding['evidence'])
        if status == 'SUCCESS' or status == 'FIXED':
            if phase == 'bootstrap':
                _typed_fields(result, {'isEmpty': bool, 'classificationHint': str, 'fileCount': int, 'files': list, 'recommendations': list})
                _plain_integer(result['fileCount'], 'invalid fileCount')
                _expect(result['classificationHint'] in {'GREENFIELD', 'BROWNFIELD'} and result['fileCount'] == len(result['files']), 'bootstrap inventory mismatch')
                for row in result['files']:
                    _typed_fields(row, {key: str for key in ('path', 'summary', 'structure', 'relevance')})
                if 'mapEvidence' in result:
                    _evidence(state, result['mapEvidence'])
            elif phase == 'architect':
                _typed_fields(result, {'classification': str, 'projectType': str, 'taskType': str, 'planPath': str, 'featureSlices': list, 'mayEdit': list, 'doNotTouch': list, 'acceptanceCriteria': list, 'specDeficiencies': list, 'specBlocked': bool, 'visualGate': dict})
                _expect(not result['specBlocked'], 'SPEC_BLOCKED: Architect human deficiency')
                _expect(str(Path(result['planPath']).resolve()) == state['plan']['path'], 'dictated plan mismatch')
                _artifact(state, result['planPath'])
                for row in result['featureSlices']:
                    _typed_fields(row, {'id': str, 'description': str, 'files': list, 'ui': bool})
                for row in result['acceptanceCriteria']:
                    _typed_fields(row, {'id': str, 'text': str, 'measurable': bool})
                    _expect(not row['measurable'] or 'threshold' in row, 'measurable threshold missing')
                v = result['visualGate']
                _typed_fields(v, {'status': str, 'output': str, 'componentNodes': int, 'testsOnly': bool})
                _plain_integer(v['componentNodes'], 'invalid component count')
                active = v['componentNodes'] >= 3 and not v['testsOnly']
                _expect(v['status'] in {'PASS', 'NOT_APPLICABLE', 'SKIPPED'}, 'VISUAL_GATE_FAIL: visual outcome')
                if v['status'] == 'PASS':
                    _typed_fields(v, {'command': str, 'exitCode': int, 'scannedNodes': int, 'evidence': list})
                    _expect(v['exitCode'] == 0 and type(v['scannedNodes']) is int and v['scannedNodes'] >= 1, 'visual PASS lacks actual nodes')
                    _evidence(state, v['evidence'])
                else:
                    _expect(not active, 'required visual gate cannot be waived')
                    _text(v.get('reason'), 'visual exclusion reason missing')
            elif phase == 'code':
                _typed_fields(result, {'artifacts': list, 'testGuidePath': str, 'testSummary': str, 'deviations': list, 'measurements': list, 'logs': list, 'doxygen': dict})
                _evidence(state, result['artifacts'])
                _artifact(state, result['testGuidePath'])
                _evidence(state, result['logs'])
                _doxygen(state, result['doxygen'])
            elif phase == 'review':
                _typed_fields(result, {'findings': list, 'limitations': list, 'diffEvidence': list, 'scopeJudgment': str})
                _evidence(state, result['diffEvidence'])
            elif phase == 'debug':
                _typed_fields(result, {'rootCause': str, 'fix': str, 'filesTouched': list, 'postFixAudit': str, 'testSummary': str, 'regressionEvidence': list, 'origin': str})
                _expect(result['origin'] == state['debug_origin']['phase'], 'Debug cause origin mismatch')
                _evidence(state, result['regressionEvidence'])
                for value in result['filesTouched']:
                    touched=Path(_text(value,'touched path missing')).resolve()
                    _expect(touched.is_relative_to(Path(state['target'])), 'touched path outside target')
                    if touched.exists():
                        _file(touched)
            elif phase == 'finalize':
                _typed_fields(result, {'report': str, 'classification': str, 'planPath': str, 'testsPath': str, 'logPath': str, 'testSummary': str, 'acceptanceEvidence': list, 'qaEvidence': list, 'reviewEvidence': list, 'liveEvidence': list, 'blastRadius': dict, 'scopeDeviations': list, 'limitations': list})
                if 'doxygenPath' in result:
                    _artifact(state,result['doxygenPath'])
                else:
                    _expect(prohibited, 'applicable Finalize Doxygen path missing')
                for key in ('report', 'planPath', 'testsPath', 'logPath'):
                    _artifact(state, result[key])
                for key in ('acceptanceEvidence', 'qaEvidence', 'reviewEvidence', 'liveEvidence'):
                    _evidence(state, result[key])
                _expect(set(result['blastRadius']) == {'added', 'modified', 'deleted', 'untracked'} and all(type(x) is list for x in result['blastRadius'].values()), 'blast-radius inventory missing')
                _expect(state['accepted'].get('qa', {}).get('candidate') == state['candidate']['digest'] and state['accepted'].get('review', {}).get('candidate') == state['candidate']['digest'], 'Finalize requires current QA and Review')
        logger.info('[IMP:9][_payload][RESULT] role payload verified structurally')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        logger.error('[IMP:10][_payload][FAIL] kind=%s', type(exc).__name__)
        raise
# endregion FUNC__payload

# region FUNC__source_change [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Accept only the explicit scoped authored delta within saved Architect authority.
## @uses run_state._relative, run_state._evidence, run_state._expect
## @io state latest accepted candidate/approved_scope; actual newly derived inventory; context sourceChange dict with mayEdit relative path list and real artifacts absolute path list; result Code artifacts or Debug filesTouched including actual observed removed paths, or declared known-effect parent correction. Partial Code BUG_REPORT/BLOCKED or Debug BLOCKED preserve observed bytes without success. Returns old/new digests and sorted changed paths. Code artifact list must match context; Debug touched paths must belong to observed approved source while real resulting artifacts remain separately verified. ValueError for outside scope or mismatched Code artifact lists; OSError on evidence. Reads only; parent authenticity remains external. Example: new source.py permitted, added spec.md outside scope refuses. Importance:9.
## @complexity 5
def _source_change(state, actual, context, result):
    logger.info('[IMP:4][_source_change][START] expected authored candidate delta')
    try:
        permission = context.get('sourceChange')
        _expect(type(permission) is dict and set(permission) == {'mayEdit', 'artifacts'}, 'parent sourceChange scope required')
        _expect(type(permission['mayEdit']) is list and type(permission['artifacts']) is list, 'invalid sourceChange population')
        allowed = {_relative(p) for p in permission['mayEdit']}
        before = {r['path']: r for r in state['candidate']['files']}
        after = {r['path']: r for r in actual['files']}
        changed = {p for p in before.keys() | after.keys() if before.get(p) != after.get(p)}
        _expect(changed <= allowed, 'candidate changes outside parent sourceChange scope')
        if result.get('kind')=='control':
            _evidence(state,result['evidence'])
        elif result['phase']=='code':
            if result['status']=='SUCCESS' or 'artifacts' in result:
                _expect(permission['artifacts'] == result.get('artifacts'), 'sourceChange artifacts disagree with Code result')
            if result['status'] in {'BUG_REPORT','BLOCKED'}:
                _evidence(state,result['evidence'])
        else:
            touched={Path(_text(value,'touched path missing')).resolve().relative_to(Path(state['target'])).as_posix() for value in result.get('filesTouched',[])}
            _expect(touched <= allowed and touched <= before.keys() | after.keys(), 'Debug touched paths outside observed approved source')
        _expect(allowed <= set(state['approved_scope']), 'sourceChange exceeds approved Architect scope')
        _evidence(state, permission['artifacts'])
        logger.info('[IMP:9][_source_change][RESULT] changed=%d', len(changed))
        return {'old': state['candidate']['digest'], 'new': actual['digest'], 'changed': sorted(changed)}
    except (ValueError, KeyError, TypeError) as exc:
        logger.error('[IMP:10][_source_change][FAIL] kind=%s', type(exc).__name__)
        raise
# endregion FUNC__source_change

# region FUNC_advance [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Accept one parent event without partial input mutation and charge repair before dispatch.
## @uses copy.deepcopy, run_state.validate_state, run_state._payload, run_state._source_change, run_state._digest, run_state._file
## @io state schema2 dict and role wrapper {kind:role,result:canonical envelope,context:optional sourceChange} or declared response-correction control. Returns new state only. Normal route includes accepted Review; Code SUCCESS, parent-scoped partial BUG_REPORT/BLOCKED and investigated known-effect response controls, plus Debug FIXED/BLOCKED, can retain actual authorized target bytes without falsely accepting phase completion; partial Code failure never marks Code accepted; pending Architect binds declared plan once into input digest. Shared Code/QA/Review repair spend is pre-entry; cap0/exhaustion refuses repair, retries are distinct; terminal and old/stale/malformed input refuses. ValueError/KeyError/TypeError/OSError leave original state byte-equivalent. No direct writes; owning success/failure/entry trace. Example: valid QA moves to Review, never directly Finalize. Importance:9. Complexity9 is explicit phase/status/identity/counter routing rather than a permissive generic switch.
## @complexity 9
def advance(state, result):
    logger.info('[IMP:4][advance][START] validate one parent-owned event')
    try:
        # START_BLOCK_Validation
        _expect(type(result) is dict, 'parent record wrapper required')
        kind = result.get('kind')
        _expect(kind in {'role', 'control'}, 'record kind must be role/control')
        role = result.get('result') if kind == 'role' else None
        parent_change = state.get('phase') in {'code','debug'} and type(result.get('context')) is dict and 'sourceChange' in result['context']
        changing = (kind == 'control' and parent_change) or (kind == 'role' and type(role) is dict and ((state.get('phase') in {'code', 'debug'} and role.get('status') in {'SUCCESS', 'FIXED'}) or (parent_change and role.get('status') in {'BUG_REPORT','BLOCKED'}) or (state.get('phase') == 'architect' and state.get('plan', {}).get('status') == 'pending' and role.get('status') == 'SUCCESS')))
        actual = validate_state(state, allow_source_change=changing)
        _expect(state['status'] == 'RUNNING', 'terminal run cannot advance; owner continuation required')
        updated = copy.deepcopy(state)
        event = {'time': _stamp(), 'kind': kind, 'phase': state['phase'], 'debug_delta': 0}
        if kind == 'control':
            _expect({'kind','event','phase','reason','evidence','unknownEffect'} <= set(result) <= {'kind','event','phase','reason','evidence','unknownEffect','context'}, 'malformed parent control')
            _expect(result['event'] == 'response-correction' and result['phase'] == state['phase'], 'unsupported control episode')
            _expect(type(result['unknownEffect']) is bool and not result['unknownEffect'], 'unknown effect requires investigation before replay')
            _text(result['reason'], 'control reason missing')
            _evidence(state, result['evidence'])
            if changing:
                context=result['context']
                _expect(type(context) is dict and set(context)=={'sourceChange'}, 'malformed control binding context')
                event['source_change']=_source_change(state,actual,context,result)
                event['source_change']['disposition']='partial-observed-no-phase-success'
                updated['candidate']=actual
                updated['accepted'].pop('qa',None)
                updated['accepted'].pop('review',None)
            else:
                _expect(not result.get('context'), 'sourceChange only valid for authored phase control')
            updated['retry_episodes']['response-correction'] += 1
            event.update(control=copy.deepcopy(result))
            if updated['retry_episodes']['response-correction'] > 1:
                updated['status'] = 'ESCALATED_FINALIZE' if state['phase'] == 'finalize' else 'BLOCKED'
            updated['history'].append(event)
            logger.info('[IMP:9][advance][CONTROL_RESULT] response attempt=%d', updated['retry_episodes']['response-correction'])
            return updated
        _expect(set(result) <= {'kind', 'result', 'context'} and type(role) is dict, 'malformed role wrapper')
        _expect(COMMON <= set(role), 'canonical envelope missing fields')
        for key in ('summary', 'runId', 'inputIdentity', 'candidateIdentity', 'contractVersion'):
            _text(role[key], 'empty envelope '+key)
        phase, status = state['phase'], role['status']
        _expect(role['phase'] == phase and role['role'] in PHASE_ROLES[phase] and status in STATUS[phase], 'role/phase/status mismatch')
        _expect(role['runId'] == state['run_id'] and role['inputIdentity'] == state['input_identity'] and role['contractVersion'] == state['contract_version'], 'role locked identity mismatch')
        context = result.get('context', {})
        _expect(type(context) is dict and set(context) <= {'sourceChange'}, 'unknown binding context')
        if changing and phase in {'code', 'debug'}:
            event['source_change'] = _source_change(state, actual, context, role)
            updated['candidate'] = actual
            updated['accepted'].pop('qa', None)
            updated['accepted'].pop('review', None)
        elif changing:
            before = {r['path']: r for r in state['candidate']['files']}
            after = {r['path']: r for r in actual['files']}
            changed = {p for p in before.keys() | after.keys() if before.get(p) != after.get(p)}
            _expect(changed <= {Path(state['plan']['path']).relative_to(Path(state['target'])).as_posix()}, 'unexpected change while binding pending plan')
            updated['plan'] = {'path': state['plan']['path'], 'status': 'bound', 'identity': _file(state['plan']['path'])}
            updated['candidate'] = actual
            event['input_identity_bound'] = {'old': state['input_identity'], 'new': _digest({'bindings': state['bindings']['digest'], 'plan': updated['plan']})}
            updated['input_identity'] = event['input_identity_bound']['new']
            event['plan_bound'] = updated['plan']['identity']
        else:
            _expect(not context, 'sourceChange only valid on authored candidate acceptance')
        _expect(role['candidateIdentity'] == updated['candidate']['digest'], 'role candidate identity mismatch')
        _payload(updated, role)
        logger.info('[IMP:9][advance][VALIDATION_SUCCESS] phase=%s status=%s', phase, status)
        # END_BLOCK_Validation
        # START_BLOCK_BusinessLogic
        event['result'] = copy.deepcopy(role)
        if status in {'BLOCKED', 'ESCALATED_FINALIZE'}:
            updated['status'] = status
        elif status == 'BUG_REPORT':
            _expect(updated['plan']['status'] == 'bound' and bool(updated['approved_scope']), 'pre-design/scope-free repair forbidden')
            updated['accepted'].pop('qa', None)
            updated['accepted'].pop('review', None)
            updated['debug_origin'] = {'phase': phase, 'report': copy.deepcopy(role['bugReport']), 'evidence': copy.deepcopy(role['evidence']), 'candidate': updated['candidate']['digest']}
            if updated['debug_spent'] >= updated['debug_cap']:
                updated['status'] = 'ESCALATED'
            else:
                updated['debug_spent'] += 1
                updated['phase'] = 'debug'
                event['debug_delta'] = 1
                event['attempt'] = updated['debug_spent']
                logger.info('[IMP:9][advance][DEBUG_ENTRY] origin=%s spent=%d cap=%d', phase, updated['debug_spent'], updated['debug_cap'])
        else:
            if phase == 'architect':
                scope = []
                for value in role['mayEdit']:
                    candidate_path = Path(_text(value, 'scope path missing'))
                    relative = candidate_path.resolve().relative_to(Path(state['target'])).as_posix() if candidate_path.is_absolute() else value
                    scope.append(_relative(relative))
                _expect(bool(scope), 'Architect approved scope missing')
                updated['approved_scope'] = scope
            updated['accepted'][phase] = {'candidate': updated['candidate']['digest'], 'evidence': copy.deepcopy(role['evidence']), 'role': role['role']}
            if phase=='code':
                updated['accepted']['code']['doxygen']=copy.deepcopy(role['doxygen'])
                if role['doxygen'].get('status')=='NOT_APPLICABLE':
                    updated['accepted']['code']['prohibition_identity']=_file(role['doxygen']['prohibition']['path'])
            updated['phase'] = {'bootstrap': 'architect', 'architect': 'code', 'code': 'qa', 'qa': 'review', 'review': 'finalize', 'debug': 'qa', 'finalize': 'finalize'}[phase]
            if phase == 'finalize':
                updated['status'] = 'SUCCESS'
        updated['retry_episodes']['response-correction'] = 0
        updated['history'].append(event)
        logger.info('[IMP:9][advance][RESULT] next=%s terminal=%s', updated['phase'], updated['status'])
        return updated
        # END_BLOCK_BusinessLogic
    except (OSError, ValueError, KeyError, TypeError) as exc:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][advance][FAIL] kind=%s', type(exc).__name__)
        raise
        # END_BLOCK_ErrorHandling
# endregion FUNC_advance

# region FUNC_save [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Checkpoint a complete owned state atomically and clean only its temporary file.
## @uses json.dumps, pathlib.Path.write_text, pathlib.Path.replace, pathlib.Path.unlink, uuid.uuid4, run_state._expect
## @io path exact existing target/.methodology/runs/run_id/state.json; state schema2 JSON-compatible dict. Returns None after UTF8 complete temp sibling write/replace. Wrong destination/schema or nonfinite/unserializable data raises ValueError/TypeError; I/O raises OSError; existing checkpoint is retained until replacement. No Git or target source writes. Separately constructed safe refusal events retain accepted fields. Example: state write round-trips complete history/counters. Importance:9.
## @complexity 5
def save(path, state):
    logger.info('[IMP:4][save][START] atomic checkpoint')
    temporary = None
    try:
        # START_BLOCK_Validation
        path = Path(path).resolve()
        _state_shape(state)
        expected = Path(state['target']) / '.methodology/runs' / state['run_id'] / 'state.json'
        _expect(path == expected and path.parent.is_dir(), 'unsafe checkpoint destination')
        data = json.dumps(state, indent=2, ensure_ascii=False, allow_nan=False)+'\n'
        logger.info('[IMP:9][save][VALIDATION_SUCCESS] complete JSON encoded')
        # END_BLOCK_Validation
        # START_BLOCK_BusinessLogic
        temporary = path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp')
        logger.info('[IMP:7][save][WRITE] temporary sibling then replace')
        temporary.write_text(data, encoding='utf-8')
        temporary.replace(path)
        logger.info('[IMP:9][save][RESULT] complete checkpoint persisted')
        # END_BLOCK_BusinessLogic
    except (OSError, ValueError, KeyError, TypeError) as exc:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][save][FAIL] kind=%s', type(exc).__name__)
        raise
        # END_BLOCK_ErrorHandling
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
# endregion FUNC_save

# region FUNC_main [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Deliver the helper real CLI answer and honest diagnostics through their own channels.
## @uses argparse.ArgumentParser, logging.basicConfig, json.dumps, run_state.initialize, run_state.advance, run_state.save, run_state.read_json, run_state.validate_state
## @io argv optional list[str], defaults process arguments. State CLI init/show/record returns int0 for accepted operation and2 for refusal. stdout contains only declared answer/report; stderr contains safe owning INFO/ERROR diagnostics. State show validates without writes; record may append a safe cause event only to an initialized correctly located schema2 ledger, preserving progress/counters. No agent/Git dispatch. CLI catches documented input/I/O errors, argparse invalid arguments exits2. Example: show --state owned_state verifies same-run identity without resetting counters. Importance:9.
## @complexity 9
def main(argv=None):
    logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(message)s')
    logger.info('[IMP:4][main][START] state CLI')
    parser = argparse.ArgumentParser(description='Validate source-bound schema2 state; parent owns authority and transitions.')
    commands = parser.add_subparsers(dest='action', required=True)
    init = commands.add_parser('init')
    for key in ('project', 'spec', 'approval', 'framework', 'adapter', 'plan', 'run-id'):
        init.add_argument('--'+key, required=True)
    init.add_argument('--max-debug', type=_decimal_cap, default=4)
    for action in ('show', 'record'):
        command = commands.add_parser(action)
        command.add_argument('--state', required=True)
        if action == 'record':
            command.add_argument('--result', required=True)
    try:
        args = parser.parse_args(argv)
    except SystemExit as error:
        if error.code == 0:
            logger.info('[IMP:9][main][HELP] declared usage delivered')
        else:
            logger.error('[IMP:10][main][ARGUMENT_REFUSAL] invalid CLI arguments')
        return error.code
    path, original = None, None
    try:
        if args.action == 'init':
            path, state = initialize(args.project, args.spec, args.approval, args.run_id, args.max_debug, framework=args.framework, adapter=args.adapter, plan=args.plan)
        else:
            path = Path(args.state).resolve()
            original = read_json(path)
            _state_shape(original)
            expected = Path(original.get('target', '')) / '.methodology/runs' / original.get('run_id', '') / 'state.json'
            _expect(path == expected, 'state file ownership/containment mismatch')
            if args.action == 'show':
                validate_state(original)
                state = original
            else:
                state = advance(original, read_json(args.result))
                save(path, state)
        logger.info('[IMP:9][main][RESULT] accepted action=%s', args.action)
        print(json.dumps({'state_file': str(path), 'state': state}, ensure_ascii=False, allow_nan=False))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        logger.error('[IMP:10][main][REFUSAL] action=%s kind=%s', args.action, type(exc).__name__)
        # Only append a safe diagnostic to the actual already initialized schema2 ledger.
        if args.action == 'record' and _diagnostic_ready(original,path):
            diagnostic = copy.deepcopy(original)
            diagnostic['history'].append({'time': _stamp(), 'kind': 'refused', 'phase': original.get('phase'), 'cause': type(exc).__name__, 'reason': str(exc), 'debug_delta': 0})
            try:
                save(path, diagnostic)
            except (OSError, ValueError, KeyError, TypeError) as failure:
                logger.error('[IMP:10][main][DIAGNOSTIC_FAILURE] kind=%s', type(failure).__name__)
        print('methodology state: '+str(exc), file=sys.stderr)
        return 2
# endregion FUNC_main

if __name__ == '__main__':
    sys.exit(main())
