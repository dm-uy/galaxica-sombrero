# Smoke specification — package inventory report

A small, useful greenfield task for exercising this package end to end in an owned, empty target directory. It is a template: an approval that runs it must be a real owner decision naming this file and the target; the template itself grants nothing.

## Goal

Write a Python 3.9 standard-library CLI `inventory.py` in the target that reads a Claude package layout (`references/package-layout.json`) and the package files it declares, and writes a deterministic JSON report.

## Inputs

- `--package PATH`: the package root (for example the absolute path of `implementations/claude`).
- `--output PATH`: where to write the report; its parent directory must exist.

## Behavior

- BR-1: Read the layout; for every declared file record `path`, `kind`, byte `size` and `sha256` of the actual bytes, sorted by path. The layout file itself is listed like any member; no self-hash is asserted inside it.
- BR-2: Derive counts: total files, skills (`kind` skill), roles (`kind` role), helpers (`kind` helper), and check that the declared `roles` map points at existing role files.
- BR-3: Write the report as UTF-8 JSON with sorted keys and print one summary line `files=<n> skills=<n> roles=<n> helpers=<n>` to stdout.
- BR-4: Refuse with exit code 2 and a one-line reason on stderr, writing no report, when the layout is malformed, a declared file is missing, or a declared path escapes the package (absolute, `..`, symbolic link).

## Acceptance criteria

| Id | Criterion |
|---|---|
| AC-1 | On the real package the report lists every declared member with its true size and SHA-256; counts equal the layout's (for this package: 64 files, 28 skills, 6 roles, 7 helpers). |
| AC-2 | The three refusal cases exit 2, write nothing and name the cause. |
| AC-3 | Tests use real temporary package copies, print the important trace before asserting, and the expected values are derived from the input bytes, not duplicated constants. |
| AC-4 | The CLI and tests carry the semantic exoskeleton and LDD; `doxygen Doxyfile` in the target builds silently. |

## Scope

MAY EDIT (exact target-relative files; no directories, no trailing slashes): `inventory.py`, `tests/test_inventory.py`, `tests/test_guide.md`, `Doxyfile`, `README.md`. The Architect lists any further file it needs individually in its own MAY EDIT before Code starts. The development plan lies at the path the root dictates and the run footprint `.methodology/` (run logs, evidence and the final report under `.methodology/evidence/<run id>/`) is excluded from the candidate, so neither is listed. DO NOT TOUCH: anything outside the target; the package is read-only input.
