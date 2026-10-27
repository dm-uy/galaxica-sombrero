# region MODULE_CONTRACT [DOMAIN(9): ClaudePackage, CodexBridge; CONCEPT(10): Tripwire, PinnedBytes; TECH(7): Python, pytest, hashlib]
## @modulecontract
## @purpose Fail, naming the path, whenever one of the 18 Codex files that the Claude consumer PM profile runs or seeds in place
##   changes, so that a Codex change is never absorbed silently by the Claude package until a reviewer re-pins it with a reason.
## @scope The four Codex C2 scripts, the 13 Codex seed templates and the Codex consumer PM carrier at their repository-relative
##   paths, plus the population of the Codex templates directory; the SCRIPT constants of the three Claude launchers.
## @input The real repository (read-only) and isolated owned copies of the 18 pinned files made with shutil.copy2.
## @output Assertions and a visible IMP:7-10 trajectory printed before them; drift entries of the form path: reason; no file is
##   written outside tmp_path.
## @links [USES_API(8): hashlib.sha256; USES_API(7): shutil.copy2, os.chmod; USES_API(7): ast.parse; USES_API(6): logging;
##   READS_DATA_FROM(9): implementations/codex/references/consumer-pm-profile.md, implementations/codex/skills/pm/scripts,
##   implementations/codex/skills/pm/templates; READS_DATA_FROM(8): implementations/claude/bin/orient, implementations/claude/bin/codemap,
##   implementations/claude/bin/markup-migrate; USES_FIXTURE(7): conftest.repo_root]
## @links_to_spec examples/pm-project/specs/m37-claude-consumer-profile.md Behavior 5, BR-1, AC3
## @invariants
## - The pinned digests are literal baseline facts (SHA-256 of the M37 baseline blobs); no expectation is computed from the live tree.
## - Negative controls change only owned copies and restore complete original bytes and numeric modes before the next control.
## - Every happy-path case rejects all ERROR records; a deliberate drift case requires exactly its own DRIFT record per finding.
## - A symbolic link, directory or absent file at a pinned path is missing; an unpinned entry in the templates directory is an
##   unexpected template, except the ambient git-ignored macOS name .DS_Store.
## @rationale
## Q: Why pin hashes instead of diffing against a Git commit?
## A: QA and Review run on Git-free copies, and one hash over the whole tree could not name the changed path, which AC3 requires.
## Q: Why also watch the templates directory population?
## A: pm-bootstrap seeds from that directory, so a new or removed template changes what the Claude package seeds without touching
##   any of the 18 pinned bytes.
## Q: How is a legitimate Codex change accepted?
## A: A reviewer recomputes the SHA-256 of the changed file, replaces its digest in PINS and replaces the reason for that entry by a
##   dated reason that names the Codex change and the Claude-side check performed (for example the re-run of the launcher tests on
##   Python 3.9 and 3.12); the test never computes its own expectations from the live tree.
## @changes
## LAST_CHANGE: [2.1.0 - Initial M37 tripwire over the 18 Codex files the Claude consumer PM profile depends on.]
## @modulemap
## FUNC 5[Print owned important trace before assertions] => test_claude_consumer_bridge._show
## FUNC 6[SHA-256 hex of a file's bytes] => test_claude_consumer_bridge._digest
## FUNC 10[List every missing, changed or unexpected pinned path] => test_claude_consumer_bridge._bridge_drift
## FUNC 9[Raise an AssertionError that names every drifted path] => test_claude_consumer_bridge._assert_bridge
## FUNC 6[Copy the 18 pinned files into an owned tree] => test_claude_consumer_bridge._owned_bridge_copy
## FUNC 6[List the owned error messages of this module] => test_claude_consumer_bridge._error_messages
## FUNC 9[Require exactly one named drift entry with exactly its own ERROR record] => test_claude_consumer_bridge._expect_drift
## FUNC 8[Require an empty drift and no ERROR record] => test_claude_consumer_bridge._expect_clean
## FUNC 10[The real repository matches all 18 pins] => test_claude_consumer_bridge.test_codex_bridge_pins_hold
## FUNC 10[One byte, an added template, a deleted script or a link is named by path and restored] => test_claude_consumer_bridge.test_bridge_names_one_byte_changes
## FUNC 8[Every pin has a digest and a reason and every launcher script is pinned] => test_claude_consumer_bridge.test_pins_carry_reasons_and_cover_launchers
## @usecases
## - [test_codex_bridge_pins_hold]: Maintainer -> run the root suite on the real tree -> all 18 Codex files equal their pins.
## - [test_bridge_names_one_byte_changes]: Reviewer -> change one byte of a script, a template or the carrier in an owned copy -> the tripwire fails naming that path.
## - [test_pins_carry_reasons_and_cover_launchers]: Reviewer -> read the pin table -> every pin has a reason and every launcher target is pinned.
## @GREP_SUMMARY Claude consumer bridge, tripwire, Codex pins, SHA-256, templates population, one-byte mutation, re-pin with reason, launcher SCRIPT constants
## @STRUCTURE ▶ repository root → ⊕ read 18 pinned files → ◇ digest equals pin ? → ⊕ scan templates directory → ∑ drift list → ◇ empty ? 〈pass : AssertionError naming paths〉 → ⎋ restore owned copy
def _module_contract():
    pass
# endregion MODULE_CONTRACT



import ast
import hashlib
import logging
import os
import pathlib
import shutil
import stat

import pytest

LOGGER = logging.getLogger(__name__)
BASELINE = "M37 baseline ba44b19: accepted C2 bytes"
PINS = {
    "implementations/codex/references/consumer-pm-profile.md": ("2c35f76085f637d5de7693124744f59b24e2b06e560bd1572154329477f11098", "Brownfield receipt clarification 2026-10-27: source/neutral patch identity only; carrier duties unchanged; bridge negative controls and Claude package checks required"),
    "implementations/codex/skills/pm/scripts/codemap.py": ("9d08a9558fa4e88df6f9dc086a6873455c031aee15ecc3d7f584fb17ac63fc6e", BASELINE),
    "implementations/codex/skills/pm/scripts/consumer_files.py": ("a86d3b963e49f9b63c5380ceb19a998f7e91457a6e54c331732f8a781e03ff84", BASELINE),
    "implementations/codex/skills/pm/scripts/markup_migrate.py": ("887b809c466384211caf52ea1027b8fd6ea090eecca4a2beee277302ac066768", BASELINE),
    "implementations/codex/skills/pm/scripts/orient.py": ("46b3afc8b1dd2dd853c415b880ffa21597004d36ef7468ba3feee13c550fe7b4", BASELINE),
    "implementations/codex/skills/pm/templates/AGENTS.md": ("ab8e982bde7c5aade18ae4cae15413f608237a77585ebad6c8a05013a8003813", BASELINE),
    "implementations/codex/skills/pm/templates/CLAUDE.md": ("ac9f6111cd1acb033ed7efd621201ecb09ca2d0efb9990f91d484434ac535c19", BASELINE),
    "implementations/codex/skills/pm/templates/CONVENTIONS.md": ("8a24140f39ae7d9c40fe1f67db102af373366d549c09a476ad696630a8582ab2", BASELINE),
    "implementations/codex/skills/pm/templates/DEC.md": ("fc14ad594074c6f86181d62606e45c1d12d68db1d3d2c65e78788adbd1096b3b", BASELINE),
    "implementations/codex/skills/pm/templates/Doxyfile": ("236ab63eb8b18a9f414cad55990ea5b5c2bb7ec5ad41bc7da1e5df2f8f97e701", BASELINE),
    "implementations/codex/skills/pm/templates/HANDOFF.md": ("8e5de36d2a10767142e7217d28e895c984ceed4c2383e93e33dce6265a90dcdf", BASELINE),
    "implementations/codex/skills/pm/templates/OPEN_QUESTIONS.md": ("38bb6f81d353f7160fafb583fb7b2b0760196ade56a13e96b5a88b3b45861bd4", BASELINE),
    "implementations/codex/skills/pm/templates/RECON.md": ("b1dfa12b50bf16178553341c82f5b42d5a2c8d82267e3f1230747e0f846c8475", BASELINE),
    "implementations/codex/skills/pm/templates/ROADMAP.md": ("029f71bb4df7441a122a3129df33cac9dec63cc226b2a53465122d636d0ee239", BASELINE),
    "implementations/codex/skills/pm/templates/SPEC.md": ("64da4e52d14a53b8821b4874ddd891e8308d7b5c4a6a61243ba76e5ec9fe918e", BASELINE),
    "implementations/codex/skills/pm/templates/TASKS.md": ("53011409e023a115cfbfccd699f49b8adaf0a0505657ad401f08fecad7e44925", BASELINE),
    "implementations/codex/skills/pm/templates/VISION.md": ("49dfbb295449970760fc3f6048467b3da69cdd036f0aa03f321bfafd196d3576", BASELINE),
    "implementations/codex/skills/pm/templates/gitignore": ("e17139c6b1096277073d8b0e80cad1e87f7f8b46c031b24ccef10efdd92029e1", BASELINE),
}
TEMPLATE_DIR = "implementations/codex/skills/pm/templates"
SCRIPT_DIR = "implementations/codex/skills/pm/scripts"
LAUNCHER_DIR = "implementations/claude/bin"
CARRIER = "implementations/codex/references/consumer-pm-profile.md"
AMBIENT = (".DS_Store",)
HEX = frozenset("0123456789abcdef")


# region FUNC__show [DOMAIN(5): Tests; CONCEPT(6): VisibleTrace; TECH(4): print]
## @purpose Expose this module's own important records before the assertions that depend on them (TST-301).
## @uses builtins.print, logging.LogRecord.getMessage
## @io Input: records list of logging.LogRecord, for example caplog.records. Output: None; prints every record of this module's logger whose message carries an importance from 7 to 10.
##   Side effects: stdout lines only. Guarantees: foreign loggers and importance below 7 are never printed. Raises: none for LogRecord input. System importance: 5.
##   Example: a DRIFT record from the tripwire is printed as its bracketed message line.
## @complexity 2
def _show(records):
    # START_BLOCK_BusinessLogic
    for record in records:
        if record.name == LOGGER.name and any("[IMP:%d]" % n in record.getMessage() for n in range(7, 11)):
            print(record.getMessage())
    # END_BLOCK_BusinessLogic
# endregion FUNC__show


# region FUNC__digest [DOMAIN(7): Identity; CONCEPT(7): ByteIdentity; TECH(5): hashlib]
## @purpose Give the SHA-256 of a file's exact bytes, which is the only identity the tripwire compares.
## @uses hashlib.sha256, pathlib.Path.read_bytes
## @io Input: path pathlib.Path of a readable regular file. Output: str of 64 lowercase hexadecimal characters over the file's raw bytes (no newline normalization).
##   Side effects: one file read. Guarantees: deterministic for equal bytes. Raises: OSError for an unreadable file. System importance: 6.
##   Example: the digest of a file holding the three bytes abc is ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad.
## @complexity 1
def _digest(path):
    # START_BLOCK_BusinessLogic
    return hashlib.sha256(path.read_bytes()).hexdigest()
    # END_BLOCK_BusinessLogic
# endregion FUNC__digest


# region FUNC__bridge_drift [DOMAIN(9): CodexBridge; CONCEPT(10): Drift, Population; TECH(6): hashlib, pathlib]
## @purpose List every difference between a tree and the 18 literal pins, so a Codex change is reported by path instead of absorbed.
## @uses test_claude_consumer_bridge._digest, pathlib.Path.iterdir, logging.Logger.info, logging.Logger.error
## @io Input: root pathlib.Path of a repository-shaped tree (the real repository or an owned copy). Output: sorted list of str entries, each path: missing (absent, a link or not a regular file), path: changed (SHA-256 differs) or path: unexpected template (an entry of the templates directory that is not pinned and not ambient); an empty list means the tree matches.
##   Side effects: reads only; one IMP:7 READ record, then one IMP:10 DRIFT record per finding or one IMP:9 VALIDATION_SUCCESS record. Guarantees: findings are independent, none hides another, and each names its repository-relative path.
##   Raises: OSError when a regular pinned file cannot be read. System importance: 10. Example: an owned copy whose orient.py has one flipped byte returns the single entry implementations/codex/skills/pm/scripts/orient.py: changed.
## @complexity 6
def _bridge_drift(root):
    # START_BLOCK_Validation
    LOGGER.info("[IMP:7][_bridge_drift][READ] pinned=%d", len(PINS))
    drift = []
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for relative, (digest, _reason) in sorted(PINS.items()):
        path = root / relative
        if path.is_symlink() or not path.is_file():
            drift.append((relative, "missing"))
        elif _digest(path) != digest:
            drift.append((relative, "changed"))
    templates = root / TEMPLATE_DIR
    if templates.is_dir():
        for entry in sorted(templates.iterdir()):
            relative = TEMPLATE_DIR + "/" + entry.name
            if entry.name not in AMBIENT and relative not in PINS:
                drift.append((relative, "unexpected template"))
    drift.sort()
    # END_BLOCK_BusinessLogic
    # START_BLOCK_ErrorHandling
    for relative, reason in drift:
        LOGGER.error("[IMP:10][_bridge_drift][DRIFT] path=%s reason=%s", relative, reason)
    # END_BLOCK_ErrorHandling
    # START_BLOCK_Result
    if not drift:
        LOGGER.info("[IMP:9][_bridge_drift][VALIDATION_SUCCESS] pinned=%d drift=0", len(PINS))
    return ["%s: %s" % item for item in drift]
    # END_BLOCK_Result
# endregion FUNC__bridge_drift


# region FUNC__assert_bridge [DOMAIN(9): CodexBridge; CONCEPT(9): FailureMessage; TECH(5): AssertionError]
## @purpose Turn a nonempty drift list into one failure whose message names every drifted path.
## @uses test_claude_consumer_bridge._bridge_drift
## @io Input: root pathlib.Path of a repository-shaped tree. Output: None when the tree matches all pins.
##   Side effects: the trace of _bridge_drift. Guarantees: the message is exactly Codex bridge drift: followed by the entries joined with a semicolon and a space. Raises: AssertionError when any drift exists.
##   System importance: 9. Example: after one changed script the message is Codex bridge drift: implementations/codex/skills/pm/scripts/orient.py: changed.
## @complexity 2
def _assert_bridge(root):
    # START_BLOCK_Validation
    drift = _bridge_drift(root)
    # END_BLOCK_Validation
    # START_BLOCK_ErrorHandling
    if drift:
        raise AssertionError("Codex bridge drift: " + "; ".join(drift))
    # END_BLOCK_ErrorHandling
# endregion FUNC__assert_bridge


# region FUNC__owned_bridge_copy [DOMAIN(7): Isolation; CONCEPT(8): OwnedCopy; TECH(5): shutil.copy2]
## @purpose Give a negative control its own writable copy of exactly the 18 pinned files, so no repository byte is ever mutated.
## @uses shutil.copy2, pathlib.Path.mkdir
## @io Input: root pathlib.Path of the real repository; base pathlib.Path that does not exist yet. Output: base, holding the 18 pinned files at their repository-relative paths with their numeric modes.
##   Side effects: creates files under base only. Guarantees: no file other than the pinned 18 is copied, so the templates directory of the copy has exactly 13 entries. Raises: OSError when a pinned source is missing.
##   System importance: 6. Example: the copy of the carrier is base/implementations/codex/references/consumer-pm-profile.md.
## @complexity 2
def _owned_bridge_copy(root, base):
    # START_BLOCK_BusinessLogic
    for relative in PINS:
        target = base / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(root / relative), str(target))
    return base
    # END_BLOCK_BusinessLogic
# endregion FUNC__owned_bridge_copy


# region FUNC__error_messages [DOMAIN(6): Tests; CONCEPT(7): ExpectedOnlyErrors; TECH(4): logging]
## @purpose List the ERROR-level messages that this module's own logger emitted, so a test can demand an exact error population (TST-303).
## @uses logging.LogRecord.getMessage
## @io Input: caplog pytest fixture. Output: list of str messages of records with this module's logger name and level ERROR or above, in emission order.
##   Side effects: none. Guarantees: foreign loggers never count. Raises: none. System importance: 6.
##   Example: after one drifted path the list holds exactly one DRIFT message.
## @complexity 1
def _error_messages(caplog):
    # START_BLOCK_BusinessLogic
    return [r.getMessage() for r in caplog.records if r.name == LOGGER.name and r.levelno >= logging.ERROR]
    # END_BLOCK_BusinessLogic
# endregion FUNC__error_messages


# region FUNC__expect_drift [DOMAIN(9): CodexBridge; CONCEPT(10): ExactDriftEntry; TECH(6): pytest]
## @purpose Require that an owned tree has exactly one drift entry, that its own DRIFT record is the only ERROR record, and that the assertion helper fails with a message naming that path.
## @uses test_claude_consumer_bridge._bridge_drift, test_claude_consumer_bridge._assert_bridge, test_claude_consumer_bridge._error_messages, test_claude_consumer_bridge._show
## @io Input: owned pathlib.Path tree, entry str of the form path: reason, caplog. Output: None after the drift list equals the single entry, the ERROR population equals the one DRIFT record for that path in both calls, and the AssertionError message equals Codex bridge drift: followed by the entry. The caplog is cleared at the end.
##   Side effects: trace output and caplog clearing. Guarantees: an unrelated or duplicate ERROR record fails the check. Raises: AssertionError on any difference.
##   System importance: 9. Example: entry implementations/codex/skills/pm/scripts/orient.py: changed requires the DRIFT record with reason changed for that path.
## @complexity 4
def _expect_drift(owned, entry, caplog):
    # START_BLOCK_Validation
    path, reason = entry.split(": ", 1)
    expected = ["[IMP:10][_bridge_drift][DRIFT] path=%s reason=%s" % (path, reason)]
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    drift = _bridge_drift(owned)
    _show(caplog.records)
    assert drift == [entry]
    assert _error_messages(caplog) == expected
    caplog.clear()
    with pytest.raises(AssertionError) as raised:
        _assert_bridge(owned)
    _show(caplog.records)
    assert str(raised.value) == "Codex bridge drift: " + entry
    assert path in str(raised.value)
    assert _error_messages(caplog) == expected
    caplog.clear()
    # END_BLOCK_BusinessLogic
# endregion FUNC__expect_drift


# region FUNC__expect_clean [DOMAIN(8): CodexBridge; CONCEPT(9): RestoredState; TECH(5): pytest]
## @purpose Require that an owned tree matches all pins again after a control was restored, with no ERROR record at all.
## @uses test_claude_consumer_bridge._bridge_drift, test_claude_consumer_bridge._error_messages
## @io Input: owned pathlib.Path tree and caplog. Output: None after an empty drift list and an empty ERROR population; the caplog is cleared at the end.
##   Side effects: caplog clearing. Guarantees: a half-restored tree fails. Raises: AssertionError on any drift or ERROR record. System importance: 8.
##   Example: after restoring a flipped byte the call passes; before restoring it fails.
## @complexity 2
def _expect_clean(owned, caplog):
    # START_BLOCK_BusinessLogic
    assert _bridge_drift(owned) == []
    assert _error_messages(caplog) == []
    caplog.clear()
    # END_BLOCK_BusinessLogic
# endregion FUNC__expect_clean


# region FUNC_test_codex_bridge_pins_hold [DOMAIN(9): CodexBridge; CONCEPT(10): BaselineBytes; TECH(6): pytest, caplog]
## @purpose Prove that the real repository's 18 Codex files equal their literal baseline pins and that the pin table has the agreed population.
## @uses test_claude_consumer_bridge._assert_bridge, test_claude_consumer_bridge._show, conftest.repo_root
## @io Input: repo_root pathlib.Path fixture and caplog. Output: None after exactly 18 pins (4 scripts, 13 templates, 1 carrier), an empty drift on the real tree, one VALIDATION_SUCCESS record and no ERROR record.
##   Side effects: reads only. Guarantees: a happy path rejects every ERROR record. Raises: AssertionError on any drift, population or trace difference.
##   System importance: 10. Example: changing one byte of templates/Doxyfile in the repository makes this test fail naming that path.
## @complexity 4
def test_codex_bridge_pins_hold(repo_root, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    scripts = [p for p in PINS if p.startswith(SCRIPT_DIR + "/")]
    templates = [p for p in PINS if p.startswith(TEMPLATE_DIR + "/")]
    LOGGER.info("[IMP:9][test_codex_bridge_pins_hold][POPULATION] pins=%d scripts=%d templates=%d", len(PINS), len(scripts), len(templates))
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    _assert_bridge(repo_root)
    _show(caplog.records)
    messages = [r.getMessage() for r in caplog.records if r.name == LOGGER.name]
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert len(PINS) == 18 and len(scripts) == 4 and len(templates) == 13
    assert sum(path == CARRIER for path in PINS) == 1
    assert sum("[IMP:9][_bridge_drift][VALIDATION_SUCCESS] pinned=18 drift=0" in m for m in messages) == 1
    assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
    # END_BLOCK_Result
# endregion FUNC_test_codex_bridge_pins_hold


# region FUNC_test_bridge_names_one_byte_changes [DOMAIN(9): CodexBridge; CONCEPT(10): DiscriminatingMutation, Restoration; TECH(6): pytest, shutil]
## @purpose Prove that a one-byte change in a script, a template or the carrier, an added template, a deleted script, a linked pin and an ambient name are each classified exactly, named by path, and fully restored.
## @uses test_claude_consumer_bridge._owned_bridge_copy, test_claude_consumer_bridge._bridge_drift, test_claude_consumer_bridge._assert_bridge, test_claude_consumer_bridge._show
## @io Input: tmp_path, repo_root and caplog. Output: None after each control yields exactly its own drift entry and exactly one matching ERROR record per drift call, an AssertionError whose message names the path, and a restored copy with identical bytes and numeric modes and an empty drift.
##   Side effects: writes only inside tmp_path. Guarantees: the real repository is never changed; the ambient .DS_Store name produces no drift; no unrelated ERROR record is accepted.
##   Raises: AssertionError when a control is not named exactly or a restoration differs. System importance: 10. Example: flipping the middle byte of the owned orient.py copy gives the single entry implementations/codex/skills/pm/scripts/orient.py: changed.
## @complexity 7
def test_bridge_names_one_byte_changes(tmp_path, repo_root, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    owned = _owned_bridge_copy(repo_root, tmp_path / "owned")
    assert _bridge_drift(owned) == []
    caplog.clear()
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    for relative in ("implementations/codex/skills/pm/scripts/orient.py", TEMPLATE_DIR + "/Doxyfile", CARRIER):
        path = owned / relative
        original = path.read_bytes()
        mode = stat.S_IMODE(os.stat(str(path)).st_mode)
        changed = bytearray(original)
        changed[len(changed) // 2] ^= 0x01
        assert bytes(changed) != original
        path.write_bytes(bytes(changed))
        LOGGER.info("[IMP:8][test_bridge_names_one_byte_changes][MUTATE] path=%s offset=%d", relative, len(changed) // 2)
        _expect_drift(owned, relative + ": changed", caplog)
        path.write_bytes(original)
        os.chmod(str(path), mode)
        assert path.read_bytes() == original and stat.S_IMODE(os.stat(str(path)).st_mode) == mode
        _expect_clean(owned, caplog)
    extra = owned / TEMPLATE_DIR / "EXTRA.md"
    extra.write_text("a seed nobody pinned\n", encoding="utf-8")
    _expect_drift(owned, TEMPLATE_DIR + "/EXTRA.md: unexpected template", caplog)
    extra.unlink()
    _expect_clean(owned, caplog)
    ambient = owned / TEMPLATE_DIR / ".DS_Store"
    ambient.write_bytes(b"ambient")
    _expect_clean(owned, caplog)
    ambient.unlink()
    script = owned / SCRIPT_DIR / "consumer_files.py"
    original = script.read_bytes()
    mode = stat.S_IMODE(os.stat(str(script)).st_mode)
    script.unlink()
    _expect_drift(owned, SCRIPT_DIR + "/consumer_files.py: missing", caplog)
    script.write_bytes(original)
    os.chmod(str(script), mode)
    _expect_clean(owned, caplog)
    template = owned / TEMPLATE_DIR / "TASKS.md"
    original = template.read_bytes()
    mode = stat.S_IMODE(os.stat(str(template)).st_mode)
    elsewhere = tmp_path / "elsewhere.md"
    elsewhere.write_bytes(original)
    template.unlink()
    os.symlink(str(elsewhere), str(template))
    _expect_drift(owned, TEMPLATE_DIR + "/TASKS.md: missing", caplog)
    template.unlink()
    template.write_bytes(original)
    os.chmod(str(template), mode)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    _expect_clean(owned, caplog)
    assert template.read_bytes() == original and not template.is_symlink()
    # END_BLOCK_Result
# endregion FUNC_test_bridge_names_one_byte_changes


# region FUNC_test_pins_carry_reasons_and_cover_launchers [DOMAIN(8): CodexBridge; CONCEPT(9): Coupling, ReasonRecord; TECH(6): ast, pytest]
## @purpose Prove that every pin is a well-formed digest with a nonempty reason and that the script each Claude launcher executes is itself pinned, so a launcher cannot drift away from the tripwire.
## @uses test_claude_consumer_bridge._show, ast.parse, conftest.repo_root
## @io Input: repo_root pathlib.Path fixture. Output: None after all 18 digests are 64 lowercase hexadecimal characters, every reason is a nonempty string, exactly three launchers exist and the module-level SCRIPT constant of each names a pinned Codex script.
##   Side effects: reads the three launcher files. Guarantees: SCRIPT is read with ast and never imported or executed. Raises: AssertionError on a malformed pin, an empty reason, a launcher without SCRIPT or an unpinned target.
##   System importance: 8. Example: bin/markup-migrate declares SCRIPT = markup_migrate.py, whose pin is implementations/codex/skills/pm/scripts/markup_migrate.py.
## @complexity 5
def test_pins_carry_reasons_and_cover_launchers(repo_root, caplog):
    # START_BLOCK_Validation
    caplog.set_level(logging.INFO, logger=LOGGER.name)
    malformed = [p for p, (digest, reason) in PINS.items()
                 if len(digest) != 64 or not set(digest) <= HEX or not isinstance(reason, str) or not reason.strip()]
    launchers = sorted(p for p in (repo_root / LAUNCHER_DIR).iterdir() if p.name not in AMBIENT)
    # END_BLOCK_Validation
    # START_BLOCK_BusinessLogic
    targets = {}
    for launcher in launchers:
        tree = ast.parse(launcher.read_text(encoding="utf-8"))
        values = [n.value.value for n in tree.body if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant)
                  and any(isinstance(t, ast.Name) and t.id == "SCRIPT" for t in n.targets)]
        targets[launcher.name] = values
        LOGGER.info("[IMP:8][test_pins_carry_reasons_and_cover_launchers][LAUNCHER] name=%s script_constants=%d", launcher.name, len(values))
    _show(caplog.records)
    # END_BLOCK_BusinessLogic
    # START_BLOCK_Result
    assert malformed == []
    assert sorted(targets) == ["codemap", "markup-migrate", "orient"]
    assert all(len(values) == 1 and isinstance(values[0], str) for values in targets.values())
    assert all(SCRIPT_DIR + "/" + values[0] in PINS for values in targets.values())
    assert not [r for r in caplog.records if r.levelno >= logging.ERROR]
    # END_BLOCK_Result
# endregion FUNC_test_pins_carry_reasons_and_cover_launchers
