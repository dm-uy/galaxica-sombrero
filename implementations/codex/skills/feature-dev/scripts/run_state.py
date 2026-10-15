# region MODULE_CONTRACT [DOMAIN(9): NativeMethodology; CONCEPT(9): SourceIdentity, BoundedVerification; TECH(8): Python, StandardLibrary]
## @modulecontract
## @purpose Preserve one parent-owned schema2 run with actual current source identity and honest authority limits.
## @scope Actual co-located bindings, canonical returns, causal Debug, separate response controls, atomic checkpoint and init/show/record CLI.
## @input Explicit owned source/target paths and current canonical records; pytest fixtures supply owned temporary paths for tests. No credentials or provider state.
## @output Importable declared functions, actual CLI answer/diagnostic/exit where applicable, and meaningful test outcomes with actual trace. No fabricated native acceptance.
## @links [USES_API(8): pathlib.Path; USES_API(8): logging; READS_DATA_FROM(9): explicit path inputs; no environment secrets]
## @invariants
## - Current neutral role/phase/scan/gate owners remain controlling; structural checks never prove human authority or role independence.
## - Test fixtures are isolated, deterministic and order-independent; real package sources remain read-only.
## - Private locators/payloads/credentials are absent from source; logs use safe logical classes/counts.
## - Default target inventory follows actual Git ignores with bounded untracked generated exceptions; tracked source always wins.
## - Explicit package inventories remain name-only and Git-independent; no schema/membership changes.
## - Git observations and baseline disable fsmonitor/optional locks and clear ambient GIT_* without logging values.
## @rationale
## Q: Why direct logic and actual CLI tests separately?
## A: Native imports prove bounded logic; real subprocess/file/stream/exit observations prove their actual shipped channel.
## Q: Why preserve unavailable/unsupported limits?
## A: Same-author fixtures and bounded recognizers cannot replace independent source meaning, current maps or actual native smoke.
## @changes
## LAST_CHANGE: [2.4.0 - Exact M30 source/neutral constants only; original algorithms preserved. Earlier:2.2.0 - Exact C2 source/member constants; preserved full original algorithms. Earlier: M25A target Gitignore/tracked priority and hermetic coupled baseline; explicit package/schema unchanged.]
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
## FUNC 9[Observe actual Git without ambient steering or configured fsmonitor execution] => run_state._git_run
## FUNC 9[Select tracked/nonignored paths only at actual Git top-level] => run_state._git_sources
## FUNC 9[Bind tracked-priority Git target or explicit bounded source membership] => run_state.inventory
## FUNC 9[Pin actual complete co-located package, adapter, neutral and spec identities.] => run_state._bindings
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
## - Independent judge: compare actual assertions/source/CLI receipts -> bounded evidence; native acceptance remains separately owned.
## @GREP_SUMMARY native package, actual source identity, current canonical returns, owned fixtures,
##   real CLI streams, causal budget, refusal, Gitignore tracked priority, hermetic observation and no inferred consent
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
import re
import stat
import subprocess
import sys
import uuid

logger = logging.getLogger(__name__)
SCANS = ('green-test-trap', 'quantitative-ac', 'semantic-trace', 'infra-dod', 'side-effect-channel', 'secret-leak', 'real-path-shape', 'discriminating-test')
STATE_FIELDS = {'schema_version','contract_version','run_id','status','phase','target','framework','adapter_path','spec_path','approval','bindings','input_identity','plan','baseline','baseline_candidate','candidate','debug_cap','debug_spent','retry_episodes','retry_limits','accepted','approved_scope','history'}
PACKAGE_GENERATED = {'__pycache__', '.pytest_cache', 'doxygen_output'}
KINDS = {'skill', 'role', 'helper', 'test', 'test-guide', 'config', 'plugin-manifest', 'adapter', 'layout', 'example', 'documentation'}
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

# region FUNC__git_run [DOMAIN(9): NativeMethodology; CONCEPT(10): HermeticGit; TECH(8): subprocess]
## @purpose Observe the selected repository through one read-only Git command without ambient steering or fsmonitor execution.
## @uses subprocess.run, os.environ, logging.Logger.info, logging.Logger.error
## @io project actual directory Path/str; args explicitly assembled read-only Git arguments; text bool defaultFalse.
##   Returns actual CompletedProcess with signed exit and original stdout/stderr, bytes unless text=True. All inherited
##   GIT_* variables are removed; other environment retained; argv disables optional locks and core.fsmonitor. No shell,
##   repository mutation, remote query, configuration write or secret logging. Nonzero Git exit remains an observation;
##   OSError on missing/unlaunchable Git emits own IMP10 before propagation. Example: status reads the selected target
##   despite an ambient GIT_DIR; configured executable fsmonitor never runs. Importance:9.
## @complexity 3
def _git_run(project, args, text=False):
    # START_BLOCK_BusinessLogic
    environment = {key: value for key, value in os.environ.items() if not key.startswith('GIT_')}
    logger.info('[IMP:7][_git_run][READ] operation=%s dropped=%d', args[0], len(os.environ)-len(environment))
    try:
        proc = subprocess.run(['git', '--no-optional-locks', '-c', 'core.fsmonitor=false', '-C', str(project), *args], capture_output=True, text=text, env=environment)
        logger.info('[IMP:9][_git_run][OBSERVED] exit=%d', proc.returncode)
        return proc
    except OSError as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_git_run][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
    # END_BLOCK_BusinessLogic
# endregion FUNC__git_run

# region FUNC__git_sources [DOMAIN(9): NativeMethodology; CONCEPT(10): SourcePopulation; TECH(8): git]
## @purpose Select tracked and nonignored untracked source paths only for the actual Git top-level target.
## @uses run_state._git_run, run_state._relative, pathlib.Path.samefile, os.fsdecode, logging.Logger
## @io root resolved actual directory Path. Returns (tracked set, untracked set) of canonical relative paths, or None
##   for non-Git, subdirectory, or initial unavailable-Git fallback. Confirmed repository listings must both succeed;
##   malformed paths/metadata or corrupt enumeration raises ValueError, later launch errors OSError. Reads actual Git
##   metadata/ignore rules with safe wrapper; no index/config writes. NUL spelling is fsdecoded without normalization.
##   Example: tracked output/source.py survives generated-name policy; ignored untracked .venv is not selected. Importance:9.
## @complexity 6
def _git_sources(root):
    # START_BLOCK_Validation
    logger.info('[IMP:7][_git_sources][CHECK] actual target top-level')
    try:
        top = _git_run(root, ['rev-parse', '--show-toplevel'])
    except OSError:
        logger.warning('[IMP:9][_git_sources][FALLBACK] cause=unavailable-git')
        return None
    try:
        if top.returncode:
            _expect(not ((root/'.git').exists() or (root/'.git').is_symlink()), 'Git metadata cannot be confirmed')
            logger.info('[IMP:9][_git_sources][FALLBACK] cause=non-git')
            return None
        if not root.samefile(Path(os.fsdecode(top.stdout).rstrip('\r\n'))):
            logger.info('[IMP:9][_git_sources][FALLBACK] cause=subdirectory')
            return None
        logger.info('[IMP:9][_git_sources][CONFIRMED] top-level=true')
        # END_BLOCK_Validation
        # START_BLOCK_BusinessLogic
        populations = []
        for arguments in (['ls-files', '--cached', '-z'], ['ls-files', '--others', '--exclude-standard', '-z']):
            listing = _git_run(root, arguments)
            _expect(listing.returncode == 0, 'confirmed Git enumeration failed')
            populations.append({_relative(os.fsdecode(path)) for path in listing.stdout.split(b'\0') if path})
        logger.info('[IMP:9][_git_sources][RESULT] tracked=%d untracked=%d', len(populations[0]), len(populations[1]))
        return tuple(populations)
        # END_BLOCK_BusinessLogic
    except (OSError, ValueError) as error:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][_git_sources][FAIL] kind=%s', type(error).__name__)
        raise
        # END_BLOCK_ErrorHandling
# endregion FUNC__git_sources

# region FUNC_inventory [DOMAIN(9): NativeMethodology; CONCEPT(10): SourceIdentity; TECH(8): Git, Python]
## @purpose Bind actual source bytes/modes with tracked-priority Git selection or an explicit bounded name policy.
## @uses run_state._git_sources, run_state._file, run_state._digest, run_state._expect, os.walk, pathlib.Path.lstat
## @io root actual directory Path/str; excluded optional explicit finite set defaultNone. Returns exactly files/digest/exclusions,
##   sorted complete regular source rows with relative path/type/mode/bytes/SHA256 and canonical digest. Default real Git
##   includes tracked plus nonignored untracked; only UNTRACKED GENERATED directory components, bytecode and .test_attempts
##   are omitted. Tracked generated/ignored names always remain. Missing tracked leaves represent deletion; raced/unreadable
##   retained untracked input refuses. Every retained leaf and parent is nonsymlink. Fallback extends GENERATED with .venv,
##   venv,node_modules plus .DS_Store and tests/.test_counter.json; explicit sets retain original names/bytecode/.test_attempts
##   walk and never consult Git. Reads only; no repository/source mutation. OSError on read/walk, ValueError on unsafe link/
##   path or confirmed Git failure. Example: ignored .venv mutation leaves digest stable; tracked output edit changes it.
##   Importance:9; exclusions describes declared names, not a claim of exact Git-only population.
## @complexity 7
def inventory(root, excluded=None):
    root = Path(root).resolve()
    logger.info('[IMP:7][inventory][READ] source tree')
    rows = []
    try:
        # START_BLOCK_Validation
        _expect(root.is_dir(), 'source directory unavailable')
        selected = _git_sources(root) if excluded is None else None
        names = set(excluded) if excluded is not None else set(GENERATED)
        fallback = excluded is None and selected is None
        if fallback:
            names.update({'.venv', 'venv', 'node_modules'})
        logger.info('[IMP:9][inventory][EXCLUSION] policy=%s names=%d', 'explicit' if excluded is not None else ('git-tracked-priority' if selected is not None else 'bounded-fallback'), len(names))
        # END_BLOCK_Validation
        # START_BLOCK_BusinessLogic
        if selected is not None:
            tracked, untracked = selected
            retained = tracked | {path for path in untracked if not (set(Path(path).parts[:-1]) & names) and not path.endswith(('.pyc', '.pyo')) and Path(path).name != '.test_attempts'}
            for relative in sorted(retained):
                p = root/relative
                for parent in p.parents:
                    if parent == root: break
                    _expect(not parent.is_symlink(), 'source directory link unsupported')
                try:
                    p.lstat()
                except FileNotFoundError:
                    if relative in tracked:
                        logger.info('[IMP:9][inventory][DELETION] tracked=true')
                        continue
                    raise
                row = _file(p)
                row['path'] = relative
                rows.append(row)
        else:
            for folder, dirs, files in os.walk(root, followlinks=False, onerror=lambda error: (_ for _ in ()).throw(error)):
                dirs[:] = sorted(d for d in dirs if d not in names)
                for name in dirs:
                    _expect(not (Path(folder)/name).is_symlink(), 'source directory link unsupported')
                for name in sorted(files):
                    p = Path(folder)/name
                    relative = p.relative_to(root).as_posix()
                    if name.endswith(('.pyc', '.pyo')) or name == '.test_attempts' or (fallback and (name == '.DS_Store' or relative == 'tests/.test_counter.json')):
                        continue
                    row = _file(p)
                    row['path'] = relative
                    rows.append(row)
        rows.sort(key=lambda row: row['path'])
        result = {'files': rows, 'digest': _digest(rows), 'exclusions': sorted(names)}
        logger.info('[IMP:9][inventory][RESULT] count=%d', len(rows))
        return result
        # END_BLOCK_BusinessLogic
    except (OSError, ValueError) as exc:
        # START_BLOCK_ErrorHandling
        logger.error('[IMP:10][inventory][FAIL] kind=%s', type(exc).__name__)
        raise
        # END_BLOCK_ErrorHandling
# endregion FUNC_inventory

# region FUNC__bindings [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Pin actual complete co-located package, adapter, neutral and spec identities.
## @uses run_state.read_json, run_state.inventory, run_state._file, run_state._relative, run_state._digest, run_state._expect
## @io framework directory, adapter exact framework/adapter.json, spec actual file. Returns resolved path records, full73 package rows,71 neutral rows, six core names, layout/adapter/spec byte identities and binding digest. Requires package2.4.0, co-located2.0.0 profile, exact roles/kinds/sorted membership; missing/stub/basic malformed core refuses. Full-content meaning/initial truncation authenticity remains parent judgment; later drift changes locked digest. Raises OSError/ValueError/KeyError/TypeError on unavailable or invalid binding. Reads only; no provider/Git writes. Example: relocated complete co-located tree binds independently of cwd. Importance:9.
## @complexity 9
def _bindings(framework, adapter, spec):
    framework, adapter, spec = Path(framework).resolve(), Path(adapter).resolve(), Path(spec).resolve()
    logger.info('[IMP:7][_bindings][READ] package adapter and effective neutral inputs')
    try:
        _expect(framework.is_dir() and adapter == framework / 'adapter.json', 'framework/adapter binding mismatch')
        layout_path = framework / 'references/package-layout.json'
        layout = read_json(layout_path)
        _expect(layout.get('package') == 'methodology-codex' and layout.get('version') == '3.0.1', 'package identity mismatch')
        _expect(set(layout) == {'package', 'version', 'profile', 'files', 'roles'} and layout.get('profile') == 'colocated-explicit-source', 'unsupported package profile')
        _expect(layout.get('roles') == {role: 'roles/'+role+'.md' for role in ('architect','coder','debugger','qa','reviewer','searcher')}, 'package role locations mismatch')
        declarations = layout.get('files')
        _expect(type(declarations) is list and bool(declarations), 'package file population missing')
        expected = [_relative(row['path']) for row in declarations if type(row) is dict and set(row) == {'path', 'kind'}]
        _expect(len(expected) == len(declarations) and len(set(expected)) == len(expected) == 73 and expected == sorted(expected) and all(row['kind'] in KINDS for row in declarations), 'invalid package member declarations')
        package = inventory(framework, PACKAGE_GENERATED)
        _expect(set(expected) == {row['path'] for row in package['files']}, 'package membership mismatch')
        binding = read_json(adapter)
        _expect(binding.get('spec_root') == '../../', 'co-located spec_root must be ../../')
        neutral = (adapter.parent / _text(binding.get('spec_root'), 'neutral binding missing')).resolve()
        _expect(neutral.is_dir() and neutral == framework.parents[1], 'unsupported detached neutral binding')
        _expect((neutral / 'SPEC_VERSION').read_text().strip() == binding.get('spec_version') == '3.0.1', 'neutral version mismatch')
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
        result = {'framework': str(framework), 'adapter': _file(adapter), 'package': package, 'neutral_root': str(neutral), 'neutral_version': '3.0.1', 'neutral': neutral_rows, 'spec': _file(spec), 'core': list(CORE), 'debug_cap_profile': profile_cap, 'layout': _file(layout_path)}
        result['digest'] = _digest(result)
        logger.info('[IMP:9][_bindings][RESULT] package=%d neutral=%d', len(expected), len(neutral_rows))
        return result
    except (OSError, ValueError, KeyError, TypeError) as exc:
        logger.error('[IMP:10][_bindings][FAIL] kind=%s', type(exc).__name__)
        raise
# endregion FUNC__bindings

# region FUNC__baseline [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Acquire real target repository observations through the hermetic no-lock/no-fsmonitor observer.
## @uses run_state._git_run, logging.Logger.info, logging.Logger.error
## @io project directory Path/str. Returns dict head/branch/status, each with real exit int and stdout/stderr str from the shared no-optional-locks/fsmonitor-disabled Git wrapper with ambient GIT_* removed; a nonrepository retains failed observations rather than invented HEAD. No repository mutations. OSError if process cannot launch. Example: owned non-Git fixture returns nonzero head.exit. Importance:8.
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
## @io state schema2 dict; allow_source_change bool defaultFalse reserved for controlled Architect/Code/Debug acceptance. Returns actual target inventory. Requires current immutable bindings, approval shape/action/spec/scope, bound plan identity and nonnegative cap/spend; unexpected target drift refuses unless caller controls change. No state mutation/writes. OSError/ValueError/KeyError/TypeError signal unavailable/malformed/stale state. Example: schema1 raises read-only historical diagnostic. Importance:9.
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
            _expect(actual == state['candidate'], 'unexpected target candidate change')
        logger.info('[IMP:9][validate_state][RESULT] current identities verified')
        return actual
    except (OSError, ValueError, KeyError, TypeError) as exc:
        logger.error('[IMP:10][validate_state][FAIL] kind=%s', type(exc).__name__)
        raise
# endregion FUNC_validate_state

# region FUNC_initialize [DOMAIN(8): NativeMethodology; CONCEPT(9): Identity, Verification; TECH(7): Python]
## @purpose Create one owned source-bound schema2 run without overwrite or budget reset.
## @uses run_state._bindings, run_state.inventory, run_state._baseline, run_state._file, run_state._digest, run_state.save, pathlib.Path.mkdir
## @io project existing directory, spec real file, approval nonblank parent provenance reference, safe alphanumeric/underscore/hyphen run_id, max_debug plain int0..4 default4; keyword-only framework/adapter actual co-located binding and plan declared contained path. Returns (absolute state Path, schema2 dict). Pins full immutable inputs and original target inventory; binds existing plan or records pending exactly once; creates only .methodology/runs/run_id and checkpoint after validation. Raises ValueError for invalid scope/types/extension/duplicate run; OSError on unavailable input/checkpoint. Authentic human consent is parent judgment. Example: max_debug0 initializes with debug_spent0 and cannot enter repair. Importance:9.
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
        state = {'schema_version': 2, 'contract_version': 'methodology-codex/2.0.0', 'run_id': run_id, 'status': 'RUNNING', 'phase': 'bootstrap', 'target': str(project), 'framework': str(Path(framework).resolve()), 'adapter_path': str(Path(adapter).resolve()), 'spec_path': str(spec), 'approval': {'reference': approval, 'action': 'execute approved specification', 'spec': bindings['spec']['sha256'], 'scope': str(project)}, 'bindings': bindings, 'input_identity': '', 'plan': {'path': str(plan), 'status': 'bound' if plan.exists() else 'pending'}, 'baseline': _baseline(project), 'baseline_candidate': copy.deepcopy(candidate), 'candidate': candidate, 'debug_cap': max_debug, 'debug_spent': 0, 'retry_episodes': {'response-correction': 0, 'extraction': 0, 'transport': 0, 'test-session': 0}, 'accepted': {}, 'approved_scope': [], 'retry_limits': {'response-correction': 1, 'extraction': 0, 'transport': 0, 'test-session': 0}, 'history': [{'kind': 'initialized', 'time': _stamp(), 'plan': 'bound' if plan.exists() else 'pending', 'debug_delta': 0}]}
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
