# region MODULE_CONTRACT [DOMAIN(9): ToolBinding, SessionOrientation; CONCEPT(9): InPlaceBinding, BlockedNotDegraded; TECH(7): Python, StandardLibrary, ClaudeCodeSessionStartHook]
## @modulecontract
## @purpose Tell the arriving root, at every session start, whether the methodology-claude package is bound in place to its neutral methodology checkout and which durable project records exist, so that no role or skill runs on a missing, stale or detached binding.
## @scope Binding verification (adapter, neutral version, package layout identity, six core owner cards), presence of the target project records, and one SessionStart additional-context answer. Read-only: no file is written and the session never fails.
## @input Hook payload JSON on stdin with the optional field cwd (empty or invalid text counts as an empty object); environment CLAUDE_PLUGIN_ROOT, CLAUDE_PROJECT_DIR and METHODOLOGY_HOOK_LOG; the package and neutral files on disk.
## @output Exactly one JSON object on stdout with hookSpecificOutput, hookEventName SessionStart and additionalContext of at most 1500 characters; exit status 0 in every case. A diagnostic trace goes to stderr only when METHODOLOGY_HOOK_LOG is set.
## @links [USES_API(8): Claude Code SessionStart hook output contract; USES_API(7): pathlib.Path; USES_API(7): json; USES_API(6): logging; READS_DATA_FROM(9): adapter.json, references/package-layout.json, SPEC_VERSION at the neutral root, the six core owner cards; READS_DATA_FROM(7): environment CLAUDE_PLUGIN_ROOT, CLAUDE_PROJECT_DIR, METHODOLOGY_HOOK_LOG; READS_DATA_FROM(5): file presence of AGENTS.md, CLAUDE.md, VISION.md, ROADMAP.md, TASKS.md, HANDOFF.md in the target project]
## @invariants
## - The module never writes a file and never reads the content of a target project record, only whether it exists.
## - The process always exits with status 0 and always prints exactly one JSON object; an internal error becomes a BLOCKED context that names only the error type.
## - A binding problem is always collected completely: every failed check contributes its own reason, none stops the others.
## - A missing or different neutral checkout is BLOCKED; the module never looks for another installed copy.
## - The context text never exceeds 1500 characters and never contains the content of a project record.
## @rationale
## Q: Why check the binding at every session start and not only once?
## A: The package is loaded in place from a checkout; a checkout can move, change version or lose files between sessions, and a role that reads a stale owner acts on rules that no longer exist. The check is cheap and read-only.
## Q: Why report BLOCKED and never fall back to another installed copy?
## A: A fallback copy may be older than the package that points at it; the roles would then follow rules their carriers do not describe. A stopped run is recoverable, a silently wrong run is not.
## Q: Why presence only for project records?
## A: Orientation needs to know which records exist so the root can read them deliberately under the orient check; copying private content into every session start context would be unrequested disclosure.
## @changes
## LAST_CHANGE: [1.1.0 - Exact M30 package source constant; executable functions unchanged. Earlier:1.0.0 - Initial in-place binding check and project record presence for the first native Claude Code package.]
## @modulemap
## FUNC 2[Attach full module documentation with no runtime effects] => session_start._module_contract
## FUNC 6[Resolve the package root from the environment or the script location] => session_start.resolve_package_root
## FUNC 6[Parse the hook payload, treating bad input as an empty object] => session_start._parse_payload
## FUNC 7[Read one JSON object file, or report that it cannot be used] => session_start._read_json_object
## FUNC 7[Read the status field of a neutral card front matter] => session_start._card_status
## FUNC 8[Check adapter spec_root and spec_version] => session_start._check_adapter
## FUNC 9[Check SPEC_VERSION at the neutral root against the adapter] => session_start._check_neutral_version
## FUNC 8[Check the package layout identity] => session_start._check_layout
## FUNC 9[Check the six core owners exist as draft cards] => session_start._check_core_owners
## FUNC 10[Collect every binding failure for a package root] => session_start.check_binding
## FUNC 7[Report which target project records exist] => session_start.orient_project
## FUNC 7[Pick the target project directory] => session_start._project_dir
## FUNC 9[Render the bounded session context text] => session_start.render_context
## FUNC 5[Attach the opt-in stderr trace handler] => session_start._configure_logging
## FUNC 9[Hook entry point: answer with one JSON object and exit 0] => session_start.main
## @usecases
## - [main]: Claude Code (SessionStart) -> checks the co-located checkout -> context states the bound neutral version and the reading duty.
## - [main]: Claude Code (SessionStart) -> finds a detached or stale package -> context states BLOCKED with every reason.
## - [orient_project]: Arriving root -> learns which records exist -> reads them deliberately under the orient check.
## @GREP_SUMMARY SessionStart hook, binding check, colocated-in-place, spec_version, SPEC_VERSION, package-layout, core owners, draft card, BLOCKED, additionalContext, project record presence, orient, read-only, never fails
## @STRUCTURE ▶ ┌stdin payload + env┐ → ◇ parse payload → ⚡ check_binding ┌adapter + SPEC_VERSION + layout + 6 cards┐ → ○ orient_project ∋record presence → ◇ render_context 〈ok ? bound + duty : BLOCKED + reasons〉 → ⟦one JSON object⟧ → ⎋ exit 0
def _module_contract():
    pass
# endregion MODULE_CONTRACT

import json
import logging
import os
import sys
from pathlib import Path

logger = logging.getLogger("session_start")
logger.addHandler(logging.NullHandler())

PACKAGE_NAME = "methodology-claude"
PACKAGE_VERSION = "2.1.1"
PACKAGE_PROFILE = "colocated-in-place"
SPEC_ROOT = "../../"
CORE_OWNERS = ("concepts/principles.md", "roles/_base.md", "code/exoskeleton.md", "code/ldd.md", "code/doxygen.md", "code/tests.md")
PROJECT_RECORDS = ("VISION.md", "ROADMAP.md", "TASKS.md", "HANDOFF.md")
MAX_CONTEXT = 1500
CLIP_MARK = " [truncated]"
HOOK_LOG_ENV = "METHODOLOGY_HOOK_LOG"


# region FUNC_resolve_package_root [DOMAIN(8): ToolBinding; CONCEPT(8): PackageLocation; TECH(6): pathlib, environment]
## @purpose Locate the package that this hook belongs to, so the binding check examines the same checkout the session loaded.
## @uses pathlib.Path, os.path.realpath
## @io Input: environ mapping of str to str (CLAUDE_PLUGIN_ROOT is read when present and nonempty); script_file str path of this module. Output: Path to the physical package root, symlinks resolved.
##   Side effects: none; the path is not required to exist. Guarantees: a nonempty CLAUDE_PLUGIN_ROOT wins, otherwise the parent of the directory that holds script_file.
##   Raises: TypeError for a non-str script_file when no environment value is present. System importance: 8. Example: with no environment value, a script at package/hooks/session_start.py resolves to package.
## @complexity 2
def resolve_package_root(environ, script_file):
    # START_BLOCK_BusinessLogic
    configured = environ.get("CLAUDE_PLUGIN_ROOT", "")
    if configured:
        logger.info("[IMP:6][resolve_package_root][ENVIRONMENT] package root taken from CLAUDE_PLUGIN_ROOT")
        return Path(os.path.realpath(configured))
    logger.info("[IMP:6][resolve_package_root][LOCATION] package root taken from the script location")
    return Path(os.path.realpath(script_file)).parent.parent
    # END_BLOCK_BusinessLogic
# endregion FUNC_resolve_package_root


# region FUNC__parse_payload [DOMAIN(7): HookPayload; CONCEPT(7): TolerantParsing; TECH(6): json]
## @purpose Turn the raw hook payload text into a dictionary without ever failing, because a session start must not depend on payload quality.
## @uses json.loads
## @io Input: text str (any content, possibly empty). Output: dict; the parsed object when text is a JSON object, otherwise an empty dict.
##   Side effects: trace records only. Guarantees: never raises for str input; non-object JSON and invalid JSON give an empty dict.
##   Raises: none for str input. System importance: 6. Example: a payload with only a cwd field returns a dict holding that field; the text "not json" returns an empty dict.
## @complexity 3
def _parse_payload(text):
    # START_BLOCK_Validation
    if not isinstance(text, str) or not text.strip():
        logger.info("[IMP:5][_parse_payload][EMPTY] no payload text; using an empty object")
        return {}
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    try:
        value = json.loads(text)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_ErrorHandling
    except (ValueError, RecursionError) as error:
        logger.info("[IMP:6][_parse_payload][INVALID] kind=%s; using an empty object", type(error).__name__)
        return {}
    # END_BLOCK_ErrorHandling
    if not isinstance(value, dict):
        logger.info("[IMP:6][_parse_payload][NOT_OBJECT] kind=%s; using an empty object", type(value).__name__)
        return {}
    logger.info("[IMP:6][_parse_payload][ACCEPT] fields=%d", len(value))
    return value
# endregion FUNC__parse_payload


# region FUNC__read_json_object [DOMAIN(8): ToolBinding; CONCEPT(7): SafeRead; TECH(7): pathlib, json]
## @purpose Read one JSON object file for the binding check and report plainly when it cannot be used, so the caller records a reason instead of crashing.
## @uses pathlib.Path.read_text, json.loads
## @io Input: path Path of a file. Output: dict when the file is readable UTF-8 JSON holding an object, otherwise None.
##   Side effects: one file read; an IMP:10 trace record naming the file and the error class, never the content. Guarantees: never raises for OSError, undecodable bytes or invalid JSON.
##   Raises: none for a Path input. System importance: 8. Example: a missing adapter.json returns None and logs READ_FAILURE; a file holding the text [1] returns None and logs NOT_OBJECT.
## @complexity 3
def _read_json_object(path):
    # START_BLOCK_BusinessLogic
    try:
        logger.info("[IMP:7][_read_json_object][READ] file=%s", path.name)
        value = json.loads(path.read_text(encoding="utf-8"))
    # END_BLOCK_BusinessLogic
    # START_BLOCK_ErrorHandling
    except (OSError, ValueError, RecursionError) as error:
        logger.error("[IMP:10][_read_json_object][READ_FAILURE] file=%s kind=%s", path.name, type(error).__name__)
        return None
    # END_BLOCK_ErrorHandling
    if not isinstance(value, dict):
        logger.error("[IMP:10][_read_json_object][NOT_OBJECT] file=%s kind=%s", path.name, type(value).__name__)
        return None
    return value
# endregion FUNC__read_json_object


# region FUNC__card_status [DOMAIN(8): NeutralCard; CONCEPT(8): CardStatus; TECH(6): front matter]
## @purpose Read the status of a neutral owner card, so a stub or damaged owner is not mistaken for a complete one.
## @uses pathlib.Path.open
## @io Input: path Path of a Markdown file. Output: str status value (for example draft or stub) when the file starts with a front matter block holding a status key, otherwise None.
##   Side effects: one bounded read of the first 4096 characters; an IMP:10 record on read failure. Guarantees: never raises for OSError or undecodable bytes; the file body is not interpreted.
##   Raises: none for a Path input. System importance: 7. Example: a file beginning with a front matter block that holds the line status: draft returns draft; a file without front matter returns None.
## @complexity 4
def _card_status(path):
    # START_BLOCK_BusinessLogic
    try:
        logger.info("[IMP:7][_card_status][READ] file=%s", path.name)
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            head = handle.read(4096)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_ErrorHandling
    except OSError as error:
        logger.error("[IMP:10][_card_status][READ_FAILURE] file=%s kind=%s", path.name, type(error).__name__)
        return None
    # END_BLOCK_ErrorHandling
    lines = head.splitlines()
    if not lines or lines[0].strip() != "---":
        logger.info("[IMP:6][_card_status][NO_FRONT_MATTER] file=%s", path.name)
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        key, separator, value = line.partition(":")
        if separator and key.strip() == "status":
            return value.strip()
    return None
# endregion FUNC__card_status


# region FUNC__check_adapter [DOMAIN(9): ToolBinding; CONCEPT(9): AdapterIdentity; TECH(7): json]
## @purpose Confirm that the adapter resolves the neutral root two levels above the package and names the neutral version it was written for.
## @uses session_start._read_json_object
## @io Input: package_root Path. Output: tuple of (list of reason str, adapter spec_version str or None). The reason list is empty exactly when adapter.json is readable, spec_root equals the string ../../ and spec_version is a nonempty string.
##   Side effects: one file read and trace records. Guarantees: every failed condition contributes its own reason; a missing adapter gives one reason and no version.
##   Raises: none. System importance: 9. Example: a copy of the package without adapter.json returns one reason about adapter.json and None.
## @complexity 4
def _check_adapter(package_root):
    # START_BLOCK_Validation
    adapter = _read_json_object(package_root / "adapter.json")
    if adapter is None:
        logger.error("[IMP:10][_check_adapter][ADAPTER_UNUSABLE] adapter.json cannot be used")
        return ["adapter.json is missing, unreadable or not a JSON object"], None
    reasons = []
    if adapter.get("spec_root") != SPEC_ROOT:
        reasons.append("adapter spec_root is not %s" % SPEC_ROOT)
        logger.error("[IMP:10][_check_adapter][SPEC_ROOT_MISMATCH] expected=%s", SPEC_ROOT)
    version = adapter.get("spec_version")
    if not isinstance(version, str) or not version.strip():
        reasons.append("adapter spec_version is missing")
        logger.error("[IMP:10][_check_adapter][SPEC_VERSION_MISSING] adapter names no neutral version")
        version = None
    # END_BLOCK_Validation
    if not reasons:
        logger.info("[IMP:9][_check_adapter][ADAPTER_VALID] spec_root=%s spec_version=%s", SPEC_ROOT, version.strip())
    return reasons, (version.strip() if version else None)
# endregion FUNC__check_adapter


# region FUNC__check_neutral_version [DOMAIN(9): ToolBinding; CONCEPT(9): NeutralVersion; TECH(6): pathlib]
## @purpose Confirm that the neutral checkout above the package exists and has the version the adapter expects, so the roles read the rules they were written for.
## @uses pathlib.Path.read_text
## @io Input: neutral_root Path; adapter_version str or None. Output: tuple of (list of reason str, SPEC_VERSION text str or None). The text is stripped of surrounding whitespace.
##   Side effects: one file read and trace records. Guarantees: a missing or empty SPEC_VERSION gives a reason and no version; a version that differs from a known adapter_version gives a reason that names both; with adapter_version None only readability is judged.
##   Raises: none. System importance: 9. Example: SPEC_VERSION holding 2.0.0 against adapter 1.0.0 returns one reason naming both and 2.0.0.
## @complexity 4
def _check_neutral_version(neutral_root, adapter_version):
    # START_BLOCK_Validation
    path = neutral_root / "SPEC_VERSION"
    try:
        logger.info("[IMP:7][_check_neutral_version][READ] file=SPEC_VERSION")
        text = path.read_text(encoding="utf-8").strip()
    except (OSError, ValueError) as error:
        logger.error("[IMP:10][_check_neutral_version][READ_FAILURE] kind=%s", type(error).__name__)
        return ["SPEC_VERSION is missing at the neutral root"], None
    if not text:
        logger.error("[IMP:10][_check_neutral_version][EMPTY] SPEC_VERSION holds no version")
        return ["SPEC_VERSION at the neutral root is empty"], None
    if adapter_version is not None and text != adapter_version:
        logger.error("[IMP:10][_check_neutral_version][VERSION_MISMATCH] neutral=%s adapter=%s", text[:32], adapter_version[:32])
        return ["SPEC_VERSION %s differs from adapter spec_version %s" % (text[:32], adapter_version[:32])], text
    # END_BLOCK_Validation
    logger.info("[IMP:9][_check_neutral_version][VERSION_MATCH] neutral=%s", text[:32])
    return [], text
# endregion FUNC__check_neutral_version


# region FUNC__check_layout [DOMAIN(8): ToolBinding; CONCEPT(8): PackageIdentity; TECH(7): json]
## @purpose Confirm that the package declares the identity this hook was written for (name, version and in-place profile), so a foreign or renamed package is not bound by accident.
## @uses session_start._read_json_object
## @io Input: package_root Path. Output: tuple of (list of reason str, declared package version str or None). The reason list is empty exactly when references/package-layout.json is a readable object with package methodology-claude, version 1.1.0 and profile colocated-in-place.
##   Side effects: one file read and trace records. Guarantees: each mismatching key contributes its own reason with the found value clipped to 40 characters; an unusable file gives one reason.
##   Raises: none. System importance: 8. Example: a layout declaring profile installed-copy returns one reason naming the found profile.
## @complexity 4
def _check_layout(package_root):
    # START_BLOCK_Validation
    layout = _read_json_object(package_root / "references" / "package-layout.json")
    if layout is None:
        logger.error("[IMP:10][_check_layout][LAYOUT_UNUSABLE] package-layout.json cannot be used")
        return ["references/package-layout.json is missing, unreadable or not a JSON object"], None
    reasons = []
    for key, expected in (("package", PACKAGE_NAME), ("version", PACKAGE_VERSION), ("profile", PACKAGE_PROFILE)):
        found = layout.get(key)
        if found != expected:
            reasons.append("package-layout %s is %s, expected %s" % (key, str(found)[:40], expected))
            logger.error("[IMP:10][_check_layout][IDENTITY_MISMATCH] key=%s", key)
    # END_BLOCK_Validation
    if not reasons:
        logger.info("[IMP:9][_check_layout][LAYOUT_VALID] package=%s version=%s profile=%s", PACKAGE_NAME, PACKAGE_VERSION, PACKAGE_PROFILE)
    version = layout.get("version")
    return reasons, (version if isinstance(version, str) else None)
# endregion FUNC__check_layout


# region FUNC__check_core_owners [DOMAIN(9): ToolBinding; CONCEPT(9): CoreOwners, DraftCard; TECH(6): pathlib, front matter]
## @purpose Confirm that the six core owners every role must read in full exist as complete (draft) cards at the neutral root, so no role starts on a missing or stub owner.
## @uses session_start._card_status
## @io Input: neutral_root Path. Output: list of reason str; empty exactly when each of the six core owner paths is a regular file whose card status is draft.
##   Side effects: six bounded reads and trace records. Guarantees: every missing or non-draft owner contributes its own reason that names the relative path (and the found status); the check never reads past the card head.
##   Raises: none. System importance: 9. Example: a stub status in code/ldd.md returns one reason naming code/ldd.md and the status stub.
## @complexity 4
def _check_core_owners(neutral_root):
    # START_BLOCK_Validation
    reasons = []
    for relative in CORE_OWNERS:
        path = neutral_root / relative
        if not path.is_file():
            reasons.append("core owner missing: %s" % relative)
            logger.error("[IMP:10][_check_core_owners][OWNER_MISSING] owner=%s", relative)
            continue
        status = _card_status(path)
        if status != "draft":
            reasons.append("core owner card is not status draft: %s (status %s)" % (relative, status if status else "absent"))
            logger.error("[IMP:10][_check_core_owners][OWNER_NOT_DRAFT] owner=%s", relative)
    # END_BLOCK_Validation
    if not reasons:
        logger.info("[IMP:9][_check_core_owners][OWNERS_VALID] count=%d", len(CORE_OWNERS))
    return reasons
# endregion FUNC__check_core_owners


# region FUNC_check_binding [DOMAIN(10): ToolBinding; CONCEPT(10): InPlaceBinding, CompleteReasons; TECH(7): pathlib]
## @purpose Decide whether the package is bound in place to a matching neutral checkout, and collect every failure so the owner can repair the checkout in one pass.
## @uses session_start._check_adapter, session_start._check_neutral_version, session_start._check_layout, session_start._check_core_owners, os.path.realpath
## @io Input: package_root str or Path of the package (symlinks are resolved, the neutral root is two levels above the resolved path). Output: tuple of (ok bool, reasons list of str, facts dict with str values for package_root, neutral_root, spec_version, package_version where known).
##   Side effects: file reads and trace records; no writes. Guarantees: ok is True exactly when reasons is empty; all four sub-checks always run; facts always holds package_root and neutral_root.
##   Raises: none for a str or Path input. System importance: 10 for the session binding. Example: the real co-located package returns (True, [], facts) with spec_version 1.0.0; the same package copied alone returns False with the SPEC_VERSION and six owner reasons.
## @complexity 5
def check_binding(package_root):
    # START_BLOCK_Validation
    root = Path(os.path.realpath(str(package_root)))
    neutral_root = root.parent.parent
    logger.info("[IMP:6][check_binding][INIT] four binding checks start")
    adapter_reasons, adapter_version = _check_adapter(root)
    version_reasons, neutral_version = _check_neutral_version(neutral_root, adapter_version)
    layout_reasons, package_version = _check_layout(root)
    owner_reasons = _check_core_owners(neutral_root)
    reasons = adapter_reasons + version_reasons + layout_reasons + owner_reasons
    # END_BLOCK_Validation
    # START_BLOCK_Result
    facts = {"package_root": str(root), "neutral_root": str(neutral_root)}
    if neutral_version:
        facts["spec_version"] = neutral_version
    if package_version:
        facts["package_version"] = package_version
    if reasons:
        logger.error("[IMP:10][check_binding][BLOCKED] reasons=%d", len(reasons))
    else:
        logger.info("[IMP:9][check_binding][BOUND] package=%s version=%s neutral=%s", PACKAGE_NAME, package_version, neutral_version)
    return (not reasons), reasons, facts
    # END_BLOCK_Result
# endregion FUNC_check_binding


# region FUNC__present [DOMAIN(6): ProjectRecords; CONCEPT(6): PresenceOnly; TECH(5): pathlib]
## @purpose Answer whether one project record file exists without ever reading it.
## @uses pathlib.Path.is_file
## @io Input: path Path. Output: bool; True exactly for an existing regular file (links followed), False for anything else including an unreadable directory entry.
##   Side effects: one stat call. Guarantees: never raises for OSError; the content is never opened.
##   Raises: none. System importance: 5. Example: an existing VISION.md returns True; a missing one returns False.
## @complexity 2
def _present(path):
    try:
        return path.is_file()
    except OSError as error:
        logger.info("[IMP:6][_present][PROBE_FAILURE] kind=%s", type(error).__name__)
        return False
# endregion FUNC__present


# region FUNC_orient_project [DOMAIN(8): SessionOrientation; CONCEPT(8): RecordPresence; TECH(6): pathlib]
## @purpose Show the arriving root which durable records the target project has, so it can read them deliberately under the orient check.
## @uses session_start._present
## @io Input: project_dir str or Path of the target project. Output: dict with project_dir str, agents_md bool, claude_md bool and records dict of record name to bool for VISION.md, ROADMAP.md, TASKS.md and HANDOFF.md; records is empty when AGENTS.md is absent.
##   Side effects: up to six stat calls and trace records; no content is read, nothing is written. Guarantees: the four record names are probed only next to an existing AGENTS.md.
##   Raises: none for a str or Path input. System importance: 7. Example: a directory with AGENTS.md and TASKS.md returns agents_md True and records with TASKS.md True and the other three False.
## @complexity 3
def orient_project(project_dir):
    # START_BLOCK_BusinessLogic
    base = Path(project_dir)
    agents = _present(base / "AGENTS.md")
    claude = _present(base / "CLAUDE.md")
    logger.info("[IMP:7][orient_project][PROBE] agents_md=%s claude_md=%s", agents, claude)
    records = {name: _present(base / name) for name in PROJECT_RECORDS} if agents else {}
    # END_BLOCK_BusinessLogic
    logger.info("[IMP:6][orient_project][RESULT] records_probed=%d", len(records))
    return {"project_dir": str(base), "agents_md": agents, "claude_md": claude, "records": records}
# endregion FUNC_orient_project


# region FUNC__project_dir [DOMAIN(7): SessionOrientation; CONCEPT(7): TargetProject; TECH(6): environment]
## @purpose Choose the target project directory the session was started in.
## @uses os.getcwd
## @io Input: payload dict (field cwd used when it is a nonempty str); environ mapping (CLAUDE_PROJECT_DIR used when nonempty). Output: str directory path; payload cwd first, then CLAUDE_PROJECT_DIR, then the process working directory.
##   Side effects: none beyond the working directory query. Guarantees: the result is a nonempty str. Raises: OSError when no working directory exists and no value is supplied. System importance: 7. Example: a payload with cwd set returns that value even when CLAUDE_PROJECT_DIR is set.
## @complexity 2
def _project_dir(payload, environ):
    cwd = payload.get("cwd")
    if isinstance(cwd, str) and cwd:
        return cwd
    configured = environ.get("CLAUDE_PROJECT_DIR", "")
    if configured:
        return configured
    return os.getcwd()
# endregion FUNC__project_dir


# region FUNC__state_word [DOMAIN(5): ContextText; CONCEPT(5): Wording; TECH(4): str]
## @purpose Give presence flags one stable wording in the context text.
## @uses builtins.str
## @io Input: flag bool. Output: the str present for True and absent for False. Side effects: none. Guarantees: only those two values. Raises: none. System importance: 4. Example: _state_word(True) returns present.
## @complexity 1
def _state_word(flag):
    return "present" if flag else "absent"
# endregion FUNC__state_word


# region FUNC__record_line [DOMAIN(7): ContextText; CONCEPT(7): RecordPresenceLine; TECH(5): str]
## @purpose Turn the orientation dict into the one sentence that tells the root which project records exist.
## @uses session_start._state_word
## @io Input: orientation dict as returned by session_start.orient_project, or None. Output: str sentence ending with a period; empty str when orientation is None.
##   Side effects: none. Guarantees: only file names and presence words appear, never record content. Raises: KeyError for a dict missing the orient_project keys. System importance: 7. Example: an orientation with AGENTS.md only names the project directory, AGENTS.md present, CLAUDE.md absent and that no adopted records exist next to it.
## @complexity 3
def _record_line(orientation):
    if not orientation:
        return ""
    line = "Project %s: AGENTS.md %s, CLAUDE.md %s" % (orientation["project_dir"], _state_word(orientation["agents_md"]), _state_word(orientation["claude_md"]))
    if orientation["agents_md"]:
        line += "; next to AGENTS.md: " + ", ".join("%s %s" % (name, _state_word(found)) for name, found in orientation["records"].items())
    else:
        line += "; no adopted records to orient from"
    return line + "."
# endregion FUNC__record_line


# region FUNC__clip [DOMAIN(5): ContextText; CONCEPT(5): Bound; TECH(4): str]
## @purpose Keep a text inside a character limit with a visible truncation mark.
## @uses builtins.len
## @io Input: text str; limit int at least 0. Output: str of at most limit characters; the text itself when it fits, otherwise its beginning followed by the truncation mark (or only the beginning when the limit is shorter than the mark).
##   Side effects: none. Guarantees: len of the result never exceeds limit. Raises: none. System importance: 5. Example: _clip of a 2000 character text with limit 1500 returns 1500 characters ending with the mark.
## @complexity 2
def _clip(text, limit):
    if len(text) <= limit:
        return text
    if limit <= len(CLIP_MARK):
        return text[:max(limit, 0)]
    return text[:limit - len(CLIP_MARK)] + CLIP_MARK
# endregion FUNC__clip


# region FUNC_render_context [DOMAIN(9): SessionOrientation; CONCEPT(9): BoundedContext, BlockedStatement; TECH(6): str]
## @purpose Compose the one bounded text the session receives, either the bound statement with the reading duty or the BLOCKED statement with every reason.
## @uses session_start._record_line, session_start._clip
## @io Input: ok bool; reasons list of str; facts dict as returned by session_start.check_binding (may be empty); orientation dict or None. Output: str of at most 1500 characters.
##   Side effects: none. Guarantees: the bound text holds the sentence methodology-claude 1.0.0 bound in place to neutral methodology and the neutral version at the absolute neutral root, the duty to read references/claude-runtime.md and the six core owners in full, and the orient pointer; the BLOCKED text holds the reasons and the instruction never to fall back to another installed copy, with reasons clipped before the instruction is.
##   Raises: KeyError for ok True with facts lacking package_root, neutral_root or spec_version. System importance: 9. Example: ok False with reasons naming a missing SPEC_VERSION returns a text starting methodology-claude binding BLOCKED.
## @complexity 5
def render_context(ok, reasons, facts, orientation):
    # START_BLOCK_BusinessLogic
    records = _record_line(orientation)
    if ok:
        text = ("%s %s bound in place to neutral methodology %s at %s. "
                "Before any methodology role or skill work, read %s/references/claude-runtime.md and the six core owners in full; Orient by checks/orient.md. "
                "The core owners under the neutral root: %s."
                % (PACKAGE_NAME, facts.get("package_version", PACKAGE_VERSION), facts["spec_version"], facts["neutral_root"],
                   facts["package_root"], ", ".join(CORE_OWNERS)))
        text = _clip(text + (" " + records if records else ""), MAX_CONTEXT)
        logger.info("[IMP:9][render_context][BOUND_TEXT] chars=%d", len(text))
        return text
    head = "%s binding BLOCKED: " % PACKAGE_NAME
    tail = "; do not run methodology roles until the co-located checkout is restored; never fall back to another installed copy."
    items = list(reasons)
    if facts.get("neutral_root"):
        items.append("neutral root checked: %s" % facts["neutral_root"])
    room = MAX_CONTEXT - len(head) - len(tail)
    joined = _clip("; ".join(items), room)
    leftover = room - len(joined)
    suffix = (" " + records) if records and len(records) + 1 <= leftover else ""
    # END_BLOCK_BusinessLogic
    text = head + joined + tail + suffix
    logger.error("[IMP:10][render_context][BLOCKED_TEXT] reasons=%d chars=%d", len(reasons), len(text))
    return text
# endregion FUNC_render_context


# region FUNC__configure_logging [DOMAIN(5): Diagnostics; CONCEPT(5): OptInTrace; TECH(5): logging, stderr]
## @purpose Keep the hook silent on stderr by default and attach a plain trace handler only when the owner asks for it.
## @uses logging.StreamHandler, logging.getLevelName
## @io Input: environ mapping; METHODOLOGY_HOOK_LOG selects the level by name (DEBUG, INFO, WARNING, ERROR) and any other nonempty value means INFO. Output: the attached logging.Handler, or None when the variable is unset or empty.
##   Side effects: attaches one handler writing bare messages to stderr and lowers the logger level. Guarantees: unset means no output at all, because the module logger carries a null handler. Raises: none. System importance: 5. Example: METHODOLOGY_HOOK_LOG=1 attaches a handler at INFO.
## @complexity 3
def _configure_logging(environ):
    setting = environ.get(HOOK_LOG_ENV, "")
    if not setting:
        return None
    level = logging.getLevelName(setting.upper())
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)
    logger.setLevel(level if isinstance(level, int) else logging.INFO)
    return handler
# endregion FUNC__configure_logging


# region FUNC_main [DOMAIN(9): ClaudeCodeHooks; CONCEPT(9): NeverFailSession, SingleJsonAnswer; TECH(7): json, stdin, stdout]
## @purpose Answer the SessionStart event with exactly one JSON object that carries the binding statement and the project record presence, and exit 0 whatever happens.
## @uses session_start.resolve_package_root, session_start._parse_payload, session_start.check_binding, session_start.orient_project, session_start._project_dir, session_start.render_context, session_start._configure_logging, json.dumps
## @io Input: stdin text stream (default sys.stdin), stdout text stream (default sys.stdout), environ mapping (default os.environ), script_file str (default the path of this module). Output: int 0 always; writes one JSON line with hookSpecificOutput holding hookEventName SessionStart and additionalContext.
##   Side effects: reads files and the environment, writes the answer to stdout, writes a trace to stderr only when METHODOLOGY_HOOK_LOG is set; removes the handler it attached. Guarantees: exactly one JSON object is written; a closed or unreadable standard input counts as an empty payload; an internal error produces a BLOCKED context that names only the error type.
##   Raises: none; every error is converted to the BLOCKED answer. System importance: 9. Example: an empty stdin in the real checkout writes the bound sentence and returns 0.
## @complexity 5
def main(stdin=None, stdout=None, environ=None, script_file=None):
    env = os.environ if environ is None else environ
    stream = sys.stdout if stdout is None else stdout
    handler = _configure_logging(env)
    try:
        # START_BLOCK_BusinessLogic
        try:
            source = sys.stdin if stdin is None else stdin
            text = source.read() if source is not None else ""
        except (OSError, ValueError) as error:
            logger.info("[IMP:6][main][STDIN_UNREADABLE] kind=%s; using an empty payload", type(error).__name__)
            text = ""
        payload = _parse_payload(text)
        logger.info("[IMP:4][main][INIT] session start check begins")
        package_root = resolve_package_root(env, __file__ if script_file is None else script_file)
        ok, reasons, facts = check_binding(package_root)
        orientation = orient_project(_project_dir(payload, env))
        context = render_context(ok, reasons, facts, orientation)
        # END_BLOCK_BusinessLogic
    # START_BLOCK_ErrorHandling
    except Exception as error:
        logger.error("[IMP:10][main][FAIL] kind=%s", type(error).__name__)
        context = render_context(False, ["internal error (%s)" % type(error).__name__], {}, None)
    # END_BLOCK_ErrorHandling
    try:
        stream.write(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": context}}) + "\n")
        stream.flush()
        logger.info("[IMP:9][main][ANSWERED] chars=%d", len(context))
    except Exception as error:
        logger.error("[IMP:10][main][WRITE_FAILURE] kind=%s", type(error).__name__)
    finally:
        if handler is not None:
            logger.removeHandler(handler)
    return 0
# endregion FUNC_main


if __name__ == "__main__":
    sys.exit(main())
