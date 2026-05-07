# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Sublime Text LSP plugin that downloads and manages the Ruff language server binary. The plugin inherits from `AbstractPlugin` in the LSP package; language server communication is handled there.

## Setup

Use `uv` (not pip) to manage dependencies:

```
uv sync --all-groups   # install all deps including dev tools
```

## Dev Commands

| Command | What it does |
|---------|-------------|
| `make ci-check` | mypy type check + ruff lint + ruff format diff (what CI runs) |
| `make ci-fix` | ruff check --fix + ruff format (safe auto-fixes) |
| `make ci-fix-unsafe` | same as above but with --unsafe-fixes |

Run `make ci-check` before declaring any change done.

## Code Style

- Line length: 120
- isort: force-single-line imports
- ruff preview mode enabled — see `pyproject.toml [tool.ruff]` for full rule set

## Gotchas

- **Server version** (`plugin/constants.py`) is managed by Renovate — do not edit it manually.
- **No tests** — this project intentionally has no test suite; do not add test scaffolding.
- Python 3.14+ is required (`requires-python = ">=3.14"` in `pyproject.toml`).
