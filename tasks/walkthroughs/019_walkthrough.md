# Walkthrough - Task 019: v0.4.0 Planning

## Goal
Design the `LinuxClipboardAdapter` to enable real clipboard interaction on Linux.

## Achievements
1.  **Technical Strategy**: Decided to use `asyncio.subprocess` to wrap standard Linux tools (`wl-clipboard`, `xclip`, `xsel`).
2.  **Architecture**: Designed `LinuxClipboardAdapter` to implement `ClipboardPort`.
3.  **History Handling**: Decided on a "Session History" approach (in-memory cache of writes) to satisfy the `history()` interface contract without complex persistence for now.
4.  **Factory Logic**: Defined the auto-detection logic for `src/klipper_sdk/factory.py`.
5.  **Plan Created**: `tasks/plans/019_plan.md`.

## Next Steps
-   **Task 020**: Execute the implementation of `LinuxClipboardAdapter`.
