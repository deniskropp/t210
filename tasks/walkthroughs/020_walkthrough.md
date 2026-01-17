# Walkthrough - Task 020: v0.4.0 Implementation

## Goal
Implement the `LinuxClipboardAdapter` to allow real system clipboard interaction on Linux.

## Achievements
1.  **Implemented Adapter**: Created `src/core/adapters/linux.py` which:
    -   Auto-detects `wl-clipboard`, `xclip`, or `xsel`.
    -   Uses `asyncio.subprocess` for non-blocking I/O.
    -   Implements a session-based history (in-memory cache of writes).
2.  **Updated Factory**: Modified `src/klipper_sdk/factory.py` to auto-load the Linux adapter when running on Linux and tools are available.
3.  **Tested**: Created and passed `tests/test_linux_adapter.py` verifying tool detection, read, and write operations using mocks.

## Verification
-   Tests passed (4/4).
-   Code adheres to async standards and Project structure.

## Next Steps
-   Release v0.4.0 (Task 021).
