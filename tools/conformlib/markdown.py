# region MODULE_CONTRACT [DOMAIN(9): NeutralFiles, Format; CONCEPT(9): Card, Anchor, Norm, Call, Declaration, Fence; TECH(8): re, os.walk, hashlib]
## @modulecontract
## @purpose To read a neutral file in exactly one way for both modes of conform: its flat card, its anchors and sections,
## its norms, its adaptation-point calls and its registry declarations, while never reading an example that sits inside
## a fenced block or a code span. It also decides which files are neutral and hashes a file with its line endings
## normalised, so a vendored copy can be compared by hash.
## @scope The card, fence-aware anchors, sections, norms, calls, declarations, the neutral-file set, the LF-normalised hash.
## @input A repository root (a directory) or one file's relative path and text.
## @output Parsed records with the issues the reader itself found, and the neutral tree of a root.
## @links [USES_API(8): re, os, hashlib; READS_DATA_FROM(9): every neutral Markdown file of the root]
## @links_to_spec BR-1, BR-5, BR-6
## @invariants
## - Nothing inside a fenced block, and no call inside an inline code span, is ever read as live syntax.
## - Line endings are normalised to LF before a card is read, a section is compared or a hash is taken.
## - The reader records issues; it never decides a status. The checks turn issues into rows.
## @rationale
## Q: Why one reader for both modes?
## A: A vendored copy is compared section by section with the neutral file; if the self mode and the adapter mode read
## anchors differently, a copy could pass one and fail the other.
## Q: Why is the neutral-file set defined by exclusion?
## A: A new content directory then cannot escape the card rule until a list is edited.
## @changes
## LAST_CHANGE: [v1.0.0 - Separate the typed root implementation namespace from neutral membership only; shared publication traversal and parser semantics retained.]
## @modulemap
## CLASS 8[A file's flat card] => Card
## CLASS 10[Everything the reader found in one file] => Parsed
## FUNC 6[CRLF and CR to LF] => normalize_newlines
## FUNC 8[Read the flat card at the top of a file] => parse_card
## FUNC 10[Read anchors, sections, norms, calls and declarations] => parse_markdown
## FUNC 8[The relative paths of the neutral files of a root] => list_neutral_files
## FUNC 9[Parse every neutral file of a root] => load_neutral_tree
## FUNC 8[SHA-256 of bytes with LF line endings] => normalized_sha256
## @usecases
## - [parse_markdown]: Check (any rule) -> read a file -> anchors, norms and calls without examples
## - [list_neutral_files]: Self mode -> walk the root -> the set the card rule covers
## - [normalized_sha256]: Adapter mode -> hash a neutral file -> compare with a vendored entry
def _module_contract():
    pass
# endregion MODULE_CONTRACT
# GREP_SUMMARY: markdown reader, card, flat front matter, anchor, section, norm, call, cap param, declaration, fence, code span, neutral files, sha256, LF normalisation
# STRUCTURE: ▶ ┌path,text┐ → ⊕ normalize LF → ◇ line1 = --- ? card : none → ○ line: 〈fence? skip〉 → ◇ anchor | norm | declaration | call → ⟦Parsed + issues⟧ → ⎋ tree

import hashlib
import logging
import os
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from conformlib.report import Refusal

logger = logging.getLogger("conform.markdown")

SKIPPED_WALK_DIRS = (".git", "doxygen_output", "__pycache__", ".pytest_cache")
NEUTRAL_ROOT_EXCLUDED_FILES = ("README.md", "CHANGELOG.md")
NEUTRAL_ROOT_EXCLUDED_DIRS = ("tests", "examples", "implementations")

CARD_LINE = re.compile(r"^([a-z][a-z0-9-]*):(?: (.*))?$")
ID_RE = re.compile(r"^[a-z][a-z0-9-]*(\.[a-z][a-z0-9-]*)*$")
NAME_RE = re.compile(r"^[a-z][a-z0-9-]*$")
NORM_ID_RE = re.compile(r"^[A-Z]+-[0-9]+$")
_ANCHOR_CANDIDATE = re.compile(r"^<!--\s*anchor:")
_ANCHOR_LINE = re.compile(r"^<!-- anchor: (\S+) -->$")
_BOLD_ITEM = re.compile(r"^\s*- \*\*([^*]+)\*\*(.*)$")
_LEVEL_TAIL = re.compile(r"^ (MUST NOT|MUST|SHOULD NOT|SHOULD|MAY):")
_LEVEL_SHAPED = re.compile(r"^ (MUST|SHOULD|MAY)\b")
_DECLARATION = re.compile(r"^\s*- \*\*(cap|param):([^*]*)\*\*(.*)$")
_CODE_SPAN = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
_BRACE_GROUP = re.compile(r"\{\{([^{}]*)\}\}")
_CALL_CANDIDATE = re.compile(r"^(cap|param)\s*:")
_CALL_EXACT = re.compile(r"^(cap|param):([a-z][a-z0-9-]*)$")
_FENCE_OPEN = re.compile(r"^(`{3,}|~{3,})")
REGISTRY_FILES = {"runtime/capabilities.md": "cap", "runtime/parameters.md": "param"}


# region CLASS_Card [DOMAIN(8): NeutralFiles; CONCEPT(9): Card; TECH(5): dataclass]
## @purpose The flat card of a file: its key-value pairs in file order, each with its line, so a check can see a missing,
## an unknown or a repeated key without a YAML parser.
@dataclass
class Card:
    pairs: List[Tuple[str, str, int]] = field(default_factory=list)

    # region METHOD_get [DOMAIN(5): NeutralFiles; CONCEPT(6): Lookup]
    ## @purpose The value of the first pair with a key, or None when the key is absent.
    def get(self, key: str) -> Optional[str]:
        for k, v, _line in self.pairs:
            if k == key:
                return v
        return None
    # endregion METHOD_get

    # region METHOD_keys [DOMAIN(5): NeutralFiles; CONCEPT(6): Lookup]
    ## @purpose The keys in file order, repeats included.
    def keys(self) -> List[str]:
        return [k for k, _v, _line in self.pairs]
    # endregion METHOD_keys
# endregion CLASS_Card


# region CLASS_Parsed [DOMAIN(9): NeutralFiles; CONCEPT(10): Anchor, Section, Norm, Call, Declaration; TECH(5): dataclass]
## @purpose Everything the reader found in one file: the card, the anchors with their lines, the section texts, the norms,
## the live calls, the registry declarations and the issues the reader raised (rule, line, detail).
@dataclass
class Parsed:
    path: str
    text: str
    card: Optional[Card] = None
    anchors: List[Tuple[str, int]] = field(default_factory=list)
    sections: Dict[str, str] = field(default_factory=dict)
    norms: List[Tuple[str, str, int]] = field(default_factory=list)
    calls: List[Tuple[str, str, int]] = field(default_factory=list)
    declarations: List[Tuple[str, str, str, int]] = field(default_factory=list)
    issues: List[Tuple[str, int, str]] = field(default_factory=list)
# endregion CLASS_Parsed


# region FUNC_normalize_newlines [DOMAIN(6): NeutralFiles; CONCEPT(7): LineEndings; TECH(4): str.replace]
## @purpose Make CRLF and lone CR into LF, so a card, a section and a hash read the same on every platform.
## @io str -> str
## @complexity 1
def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")
# endregion FUNC_normalize_newlines


# region FUNC_parse_card [DOMAIN(8): NeutralFiles; CONCEPT(9): Card; TECH(5): re]
## @purpose Read the flat card at the top of a file: line 1 is the opening rule, the next rule line closes it, and every
## line between is one key-value pair at column 0. Returns the card (None when absent or unclosed), the index of the first
## body line and the issues found.
## @uses re
## @io List[str] -> (Optional[Card], int, List[(rule, line, detail)])
## @complexity 4
def parse_card(lines: List[str]) -> Tuple[Optional[Card], int, List[Tuple[str, int, str]]]:
    issues = []  # type: List[Tuple[str, int, str]]
    if not lines or lines[0] != "---":
        issues.append(("card.present", 1, "no card"))
        return None, 0, issues
    close = None
    for index in range(1, len(lines)):
        if lines[index] == "---":
            close = index
            break
    if close is None:
        issues.append(("card.present", 1, "card not closed"))
        return None, 0, issues
    card = Card()
    for index in range(1, close):
        match = CARD_LINE.match(lines[index])
        if match is None:
            issues.append(("card.flat", index + 1, "card line is not key: value at column 0"))
            continue
        card.pairs.append((match.group(1), (match.group(2) or "").strip(), index + 1))
    return card, close + 1, issues
# endregion FUNC_parse_card


# region FUNC_parse_markdown [DOMAIN(10): NeutralFiles; CONCEPT(10): Anchor, Section, Norm, Call, Declaration, Fence; TECH(6): re]
## @purpose Read one neutral file into a Parsed record, in one pass and with one fence rule, so the self mode and the adapter
## mode see the same anchors, sections, norms, calls and declarations, and never see an example inside a fenced block.
## @uses re, parse_card, normalize_newlines
## @io (str, str) -> Parsed
## @complexity 8
def parse_markdown(path: str, text: str) -> Parsed:
    # === LOG DRIVEN DEVELOPMENT 2.0 (LDD) ===
    # The reader logs one trace line per file at IMP:2 (counts only, never text).
    text = normalize_newlines(text)
    lines = text.split("\n")
    card, body_start, card_issues = parse_card(lines)
    parsed = Parsed(path=path, text=text, card=card, issues=list(card_issues))
    registry_kind = REGISTRY_FILES.get(path)
    body_end = len(lines)
    if lines and lines[-1] == "":
        body_end -= 1
    fence_char = ""
    fence_len = 0
    anchor_indexes = []  # type: List[Tuple[str, int]]
    for index in range(body_start, len(lines)):
        number = index + 1
        line = lines[index]
        stripped = line.lstrip()
        if fence_char:
            run = len(stripped) - len(stripped.lstrip(fence_char))
            if run >= fence_len:
                fence_char = ""
                fence_len = 0
            continue
        opener = _FENCE_OPEN.match(stripped)
        if opener is not None:
            fence_char = opener.group(1)[0]
            fence_len = len(opener.group(1))
            continue
        if _ANCHOR_CANDIDATE.match(stripped):
            exact = _ANCHOR_LINE.match(line)
            if exact is not None and ID_RE.match(exact.group(1)):
                parsed.anchors.append((exact.group(1), number))
                anchor_indexes.append((exact.group(1), index))
            else:
                parsed.issues.append(("anchor.syntax", number, "anchor line is not exactly an anchor with a valid id"))
            continue
        bold = _BOLD_ITEM.match(line)
        if bold is not None:
            item_id = bold.group(1)
            rest = bold.group(2)
            if NORM_ID_RE.match(item_id):
                level = _LEVEL_TAIL.match(rest)
                if level is None:
                    parsed.issues.append(("norm.level", number, "norm level is not one of the five followed by a colon"))
                    parsed.norms.append((item_id, "", number))
                else:
                    parsed.norms.append((item_id, level.group(1), number))
                if not anchor_indexes:
                    parsed.issues.append(("norm.anchored", number, "norm before the first anchor of its file"))
            elif _LEVEL_SHAPED.match(rest):
                parsed.issues.append(("norm.id", number, "level-shaped item whose bold id is not a norm id"))
        if registry_kind is not None:
            declared = _DECLARATION.match(line)
            if declared is not None:
                prefix = declared.group(1)
                name = declared.group(2)
                meaning = declared.group(3).lstrip(" :-").strip()
                if prefix != registry_kind or not NAME_RE.match(name):
                    parsed.issues.append(("registry.syntax", number, "declaration with a bad name or the other registry's prefix"))
                else:
                    parsed.declarations.append((prefix, name, meaning, number))
                    if not meaning:
                        parsed.issues.append(("registry.meaning", number, "declaration with no meaning"))
        clean = _CODE_SPAN.sub("", line)
        for group in _BRACE_GROUP.finditer(clean):
            inner = group.group(1)
            if not _CALL_CANDIDATE.match(inner.strip()):
                continue
            exact_call = _CALL_EXACT.match(inner)
            if exact_call is None:
                parsed.issues.append(("call.syntax", number, "call-shaped text with a bad name"))
            else:
                parsed.calls.append((exact_call.group(1), exact_call.group(2), number))
    for position, (anchor_id, start) in enumerate(anchor_indexes):
        end = anchor_indexes[position + 1][1] if position + 1 < len(anchor_indexes) else body_end
        parsed.sections.setdefault(anchor_id, "\n".join(lines[start:end]))
    logger.debug("[IMP:2][parse_markdown][READ] path=%s anchors=%d norms=%d calls=%d issues=%d",
                 path, len(parsed.anchors), len(parsed.norms), len(parsed.calls), len(parsed.issues))
    return parsed
# endregion FUNC_parse_markdown


# region FUNC_list_neutral_files [DOMAIN(8): NeutralFiles; CONCEPT(9): NeutralFileSet; TECH(5): os.walk]
## @purpose Decide which files the card rule covers: every Markdown file of the root except README.md and CHANGELOG.md at
## the root and the declared tests/examples/typed implementations namespaces; ordinary new content stays governed.
## Implementation packages owe their own inventory validation and complete public privacy coverage; shared walk skips are unchanged.
## @uses os.walk
## @io str -> List[str]
## @complexity 4
def list_neutral_files(root: str) -> List[str]:
    found = []  # type: List[str]
    for dirpath, dirnames, filenames in os.walk(root):
        at_root = os.path.normpath(dirpath) == os.path.normpath(root)
        dirnames[:] = sorted(
            name for name in dirnames
            if name not in SKIPPED_WALK_DIRS and not (at_root and name in NEUTRAL_ROOT_EXCLUDED_DIRS)
        )
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            if at_root and name in NEUTRAL_ROOT_EXCLUDED_FILES:
                continue
            full = os.path.join(dirpath, name)
            if os.path.islink(full):
                continue
            found.append(os.path.relpath(full, root).replace(os.sep, "/"))
    found.sort()
    logger.debug("[IMP:3][list_neutral_files][WALK] neutral_files=%d", len(found))
    return found
# endregion FUNC_list_neutral_files


# region FUNC_load_neutral_tree [DOMAIN(9): NeutralFiles; CONCEPT(9): Tree, Parse; TECH(6): open, decode]
## @purpose Read and parse every neutral file of a root in sorted order, so a check has the whole repository as data and
## a file that cannot be read stops the run as an input problem instead of passing unseen.
## @uses list_neutral_files, parse_markdown
## @io str -> Dict[str, Parsed]
## @complexity 4
def load_neutral_tree(root: str) -> Dict[str, Parsed]:
    tree = {}  # type: Dict[str, Parsed]
    total = 0
    for rel in list_neutral_files(root):
        full = os.path.join(root, *rel.split("/"))
        try:
            with open(full, "rb") as handle:
                data = handle.read()
            text = data.decode("utf-8")
        except (OSError, UnicodeDecodeError) as error:
            logger.error("[IMP:10][load_neutral_tree][READ] file=%s error=%s", rel, type(error).__name__)
            raise Refusal("input.root", rel, "neutral file unreadable or not UTF-8")
        total += len(data)
        tree[rel] = parse_markdown(rel, text)
    logger.info("[IMP:7][load_neutral_tree][READ] files=%d bytes=%d", len(tree), total)
    return tree
# endregion FUNC_load_neutral_tree


# region FUNC_normalized_sha256 [DOMAIN(8): NeutralFiles; CONCEPT(9): Hash, LineEndings; TECH(5): hashlib]
## @purpose Give the lowercase hex SHA-256 of a file's bytes after CRLF and CR became LF, so a copy made on another
## platform compares equal to the neutral file.
## @uses hashlib
## @io bytes -> str
## @complexity 2
def normalized_sha256(data: bytes) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()
# endregion FUNC_normalized_sha256
