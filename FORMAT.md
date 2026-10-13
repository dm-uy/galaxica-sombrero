---
id: format
title: The format of the neutral files
status: draft
---

# The format of the neutral files

This file governs the format of every neutral file of the repository, and its norms apply to this file itself. The terms
MUST, MUST NOT, SHOULD, SHOULD NOT and MAY mean what they mean in standards writing: MUST and MUST NOT are absolute,
SHOULD and SHOULD NOT hold unless there is a stated reason, and MAY is optional.

<!-- anchor: format.neutral-files -->

## Neutral files

A neutral file is a Markdown file that states the methodology in words no harness owns. The norms below tell a tool how to
read such a file, and a person how to write one.

- **FMT-1** MUST: Every Markdown file of the repository is a neutral file and follows this format, except `README.md` and `CHANGELOG.md` at the root, the files under `tests/` and `examples/`, and the typed implementation-package namespace `implementations/`. Implementation packages use their own declared format and independently validated complete inventory; this neutral-membership separation does not exclude any intended public member from publication/privacy checks. Ordinary Markdown outside those declared exceptions remains governed by this format.

<!-- anchor: format.card -->

## The card

The card is the first thing a tool reads. It is deliberately flat, so that a few lines of code can read it. A card looks like
this:

```markdown
---
id: roles.qa
title: QA
status: stub
---
```

- **FMT-2** MUST: A neutral file opens with a card: its first line is `---`, and a later line `---` closes it.
- **FMT-3** MUST: A card is flat: every line between its two `---` lines is one `key: value` pair at the start of the line, with no indentation, no list and no nesting; a tool reads it without a YAML parser.
- **FMT-4** MUST: A card carries the keys `id`, `title` and `status`, each with a non-empty value.
- **FMT-5** MUST: `id` is dotted lowercase: segments of lowercase letters, digits and hyphens, each opening with a letter, joined by dots (for example `roles.qa`); it is unique across the repository.
- **FMT-6** MUST: `status` is `stub`, `draft` or `stable`.
- **FMT-7** MAY: A card carries `skill-name` and `skill-when` together: the name under which a harness packages the file as a skill, and when that skill is called.
- **FMT-8** MUST NOT: A card carries a key other than `id`, `title`, `status`, `skill-name` and `skill-when`, or one key twice; a new key is a change of this format.

<!-- anchor: format.anchor -->

## Anchors and sections

An anchor names a section. A harness that vendors a file compares and overrides by anchor, never by heading. An anchor
line looks like this:

```markdown
<!-- anchor: roles.qa.scans -->
```

- **FMT-9** MUST: An anchor is a line that holds only `<!-- anchor: <id> -->`, where the id is dotted lowercase as in FMT-5.
- **FMT-10** MUST: An anchor id is unique across the repository.
- **FMT-11** MUST: A section runs from its anchor line to the next anchor line, or to the end of the file.
- **FMT-12** MUST NOT: A tool or a harness locates a section by its heading, its number or its line: headings are not anchors, and an anchor survives a renamed heading.

<!-- anchor: format.norm -->

## Norms

A norm is the smallest unit a check can hold a file to. A norm line, inside an anchored section, looks like this:

```markdown
<!-- anchor: roles.qa.scans -->

- **QA-5** MUST: The QA role runs every scan before the suite.
```

- **FMT-13** MUST: A norm is a list item that opens with its id in bold, a space, its level and a colon, as in the example of this section.
- **FMT-14** MUST: A norm id is upper-case letters, a hyphen and a number (for example `QA-5`) and is unique across the repository.
- **FMT-15** MUST: A norm's level is `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT` or `MAY`.
- **FMT-16** MUST: Every norm lies inside an anchored section.

<!-- anchor: format.calls -->

## Adaptation points and parameters

A call keeps the neutral text free of any harness's own words. In the running text a call is shown in a code span or a
fenced block; a call written outside both is a live call and must resolve. A call looks like this:

```markdown
Run the check with {{cap:check-runner}} and report to {{param:owner-label}}.
```

A declaration in a registry looks like this:

```markdown
- **cap:worktree** An isolated working copy for parallel or isolated work.
```

- **FMT-17** MUST: The neutral text names a runtime specific only through a call, written in ASCII: `{{cap:<name>}}` for an adaptation point and `{{param:<name>}}` for a parameter, where the name is lowercase letters, digits and hyphens opening with a letter.
- **FMT-18** MUST: `runtime/capabilities.md` declares each capability as a list item that opens with `cap:<name>` in bold, followed by its meaning.
- **FMT-19** MUST: `runtime/parameters.md` declares each parameter as a list item that opens with `param:<name>` in bold, followed by its meaning.
- **FMT-20** MUST: Every call resolves to a declaration.

<!-- anchor: format.version -->

## Versions

The methodology is versioned as one unit, in the file `SPEC_VERSION`, and the changelog records each version.

- **FMT-21** MUST: `SPEC_VERSION` holds one semantic version, `MAJOR.MINOR.PATCH`; the first version is `0.1.0`.
- **FMT-22** MUST: `CHANGELOG.md` has an entry for the version in `SPEC_VERSION`: a heading line that reads `## ` and the version.
- **FMT-23** MUST: Removing a norm, or changing its meaning, raises MAJOR.
- **FMT-24** MUST: Adding a norm or a file raises MINOR.
- **FMT-25** MUST: A wording change that keeps every meaning raises PATCH.

<!-- anchor: format.adapter -->

## Adapters

An adapter is the file in which a harness accounts for every neutral file, every capability and every parameter. Its
fields, its schema and its checks are described in `runtime/adapters.md`.

- **FMT-26** MUST: A harness keeps its adapter as one JSON file in its own repository or in its owned declared implementation package under this repository's typed `implementations/` namespace, valid against `runtime/adapter.schema.json`. Co-location preserves the same pointwise contract and does not make the neutral checker a validator of native package semantics.
- **FMT-27** MUST: An adapter holds `harness`, `owner`, `spec_version` and `spec_root`; `spec_root`, every `via` and every vendored `path` are absolute or relative to the directory of the adapter file.
- **FMT-28** MUST: `parameters` maps every declared parameter to a non-empty value.
- **FMT-29** MUST: `capabilities` maps every declared capability to an object with a non-empty `mechanism`, a non-empty `fallback`, or both.
- **FMT-30** MUST: `files` maps the path of every neutral file to one entry whose `mode` is `reference`, `vendored` or `not-applied`.
- **FMT-31** MUST: When a `reference` entry names `via`, that harness file exists and names the neutral file's id or path.
- **FMT-32** MUST: A `vendored` entry holds `path`, the harness's copy, and `sha256`, the SHA-256 of the neutral file's bytes with line endings normalised to LF at the time of the copy, in lowercase hex; `overrides` is optional.
- **FMT-33** MUST: Every anchored section of a vendored copy that no override names equals the neutral section byte for byte after line endings are normalised; the text before the first anchor is not compared.
- **FMT-34** MUST: An override holds `anchor`, `reason`, `owner`, and an ISO date `until` or a `trigger`; its anchor exists in the neutral file; a `trigger` is checked for presence only.
- **FMT-35** MUST NOT: An override's `until` lies in the past.
- **FMT-36** MUST: A `not-applied` entry holds a non-empty `reason`.
- **FMT-37** SHOULD: An adapter's `spec_version` equals `SPEC_VERSION`; an older one is reported as a warning.
- **FMT-38** SHOULD: A vendored copy is refreshed when the neutral file's hash changes; until then conform reports it stale, as a warning.

<!-- anchor: format.examples -->

## Examples in the text

The examples in this file show syntax. A reader that took them for live syntax would find anchors, norms and calls that
do not exist.

- **FMT-39** MUST: Anchors, norms, calls and declarations inside a fenced code block are examples and are not read; calls inside an inline code span are examples too.
