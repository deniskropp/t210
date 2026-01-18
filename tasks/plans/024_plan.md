# Implementation Plan - Task 024: Release v0.5.0

## Objective
Release version 0.5.0 of the Klipper SDK, featuring SQLite-based history persistence.

## Steps

1.  **Version Bump**:
    *   Update `pyproject.toml`: Change version to `0.5.0`.
    *   Update `src/__init__.py` (if version is stored there, usually not, but check `src/klipper_sdk/__init__.py`).

2.  **Changelog Update**:
    *   Update `docs/CHANGELOG.md`.
    *   Add entry for `[0.5.0] - 2026-01-18`.
    *   Highlights:
        *   Added `SQLiteStorage` adapter for persistent history.
        *   Implemented `HistoryPort` interface.
        *   Updated `KlipperClient` factory to use SQLite by default in `auto` mode.
        *   Added `aiosqlite` dependency.

3.  **Status Update**:
    *   Update `tasks/status.md` to reflect `v0.5.0` release.

4.  **Verification**:
    *   Run tests one last time to ensure clean release state.
