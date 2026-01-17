# Implementation Plan - Task 018: Release v0.3.0

## 1. Overview
This plan covers the steps to release version 0.3.0 of the Klipper SDK, which introduces the Event System.

## 2. Release Steps

### Step 1: Update Version
*   **File**: `pyproject.toml`
*   **Action**: Change `version` from `0.2.0` to `0.3.0`.

### Step 2: Update Changelog
*   **File**: `docs/CHANGELOG.md`
*   **Action**:
    -   Mark `v0.2.0` as released (remove "In Development").
    -   Add `v0.3.0` section with details about the Event System.
    -   Features:
        -   Event System (Observer Pattern).
        -   Real-time monitoring capabilities.
        -   `KlipperClient.add_event_listener` / `remove_event_listener`.
        -   `ClipboardService.subscribe` / `unsubscribe`.
        -   `EventType` and `ClipboardEvent` models.

### Step 3: Verify Build (Simulation)
*   **Action**: Run a build command (e.g., `pip install build && python -m build`) to ensure the package builds correctly. (We'll simulate this or run it if `build` tool is available). *Self-correction: I'll check if `build` is installed, otherwise I'll just verify `pyproject.toml` validity.*

### Step 4: Update Project Status
*   **File**: `tasks/status.md`
*   **Action**: Update status to reflect v0.3.0 release.

## 3. Verification
-   Check `pyproject.toml` content.
-   Check `docs/CHANGELOG.md` content.
