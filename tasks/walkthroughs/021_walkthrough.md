# Walkthrough - Task 021: Release v0.4.0

## Goal
Release v0.4.0 of the Klipper SDK, enabling Linux platform support.

## Achievements
1.  **Version Update**: Updated `pyproject.toml` to `0.4.0`.
2.  **Changelog**: Updated `docs/CHANGELOG.md` to include v0.4.0 features (`LinuxClipboardAdapter`, Auto-detection).
3.  **Status**: Updated `tasks/status.md`.

## Release Notes (v0.4.0)
This release makes the SDK functional on Linux systems by integrating with standard clipboard tools (`wl-clipboard`, `xclip`, `xsel`) via `asyncio`. The `ClientFactory` now attempts to auto-detect the environment, falling back to `InMemoryAdapter` only if necessary.

## Next Steps
-   Consider v0.5.0 features: Persistent storage (SQLite adapter) or Windows/macOS support.
