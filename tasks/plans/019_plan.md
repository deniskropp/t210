# Implementation Plan - Task 019: v0.4.0 Linux Clipboard Adapter

## 1. Overview
This plan outlines the implementation of a concrete `LinuxClipboardAdapter` for the Klipper SDK v0.4.0. This will enable actual clipboard interaction on Linux systems using standard command-line tools.

## 2. Technical Approach

### 2.1. Adapter Implementation
*   **Class**: `LinuxClipboardAdapter`
*   **Path**: `src/core/adapters/linux.py`
*   **Dependencies**: `wl-clipboard` (Wayland) OR `xclip`/`xsel` (X11).
*   **Mechanism**: Use `asyncio.create_subprocess_exec` to invoke shell commands.
*   **Tool Detection**: Check for `wl-copy`/`wl-paste` first, then `xclip`, then `xsel`.

### 2.2. Command Mapping
| Operation | Wayland (`wl-clipboard`) | X11 (`xclip`) | X11 (`xsel`) |
| :--- | :--- | :--- | :--- |
| **Read** | `wl-paste` | `xclip -o -selection clipboard` | `xsel -ob` |
| **Write** | `wl-copy` | `xclip -selection clipboard` | `xsel -ib` |
| **Clear** | `wl-copy -c` | `xclip -selection clipboard /dev/null`? | `xsel -cb` |

### 2.3. History Handling
*   Native clipboard tools do not store history.
*   **Strategy**: The adapter's `history()` method will return **empty** for now, or we can implement a simple "session history" by caching writes in a Python list (similar to `InMemoryAdapter`).
*   **Decision**: To verify functionality, we will implement a **Session-based History** inside the adapter: store every item written via the SDK. (Note: This won't capture external copies unless we poll, but it fulfills the interface contract).

### 2.4. Factory Update
*   **File**: `src/klipper_sdk/factory.py`
*   **Logic**:
    -   If `adapter="auto"` and `sys.platform == "linux"`:
    -   Check for tools (`shutil.which`).
    -   If tools found, return `LinuxClipboardAdapter`.
    -   Else, log warning and fallback to `InMemoryAdapter` (or raise error if strict).

## 3. Implementation Steps

### Step 1: Create Linux Adapter
*   **File**: `src/core/adapters/linux.py`
*   **Content**:
    -   Implement `ClipboardPort`.
    -   `__init__`: Detect available tool. Raise `ImportError` or custom exception if none found.
    -   `_run_command(args, input_data)`: Helper for `asyncio.subprocess`.
    -   `read()`: Invoke paste command. Return `Content`.
    -   `write(content)`: Invoke copy command. Append to internal history list.
    -   `clear()`: Invoke clear command. Clear internal history.
    -   `history()`: Return internal list.

### Step 2: Update Factory
*   **File**: `src/klipper_sdk/factory.py`
*   **Changes**:
    -   Import `LinuxClipboardAdapter`.
    -   Add platform detection logic.

### Step 3: Testing
*   **File**: `tests/test_linux_adapter.py`
*   **Strategy**: Mock `asyncio.create_subprocess_exec` to simulate system calls. We do NOT want to overwrite the user's actual clipboard during unit tests.

## 4. Verification
*   Manual test script `examples/linux_demo.py` to verify real clipboard interaction (if user approves running it).
