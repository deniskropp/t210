# Implementation Plan - v0.5.0 SQLite Persistence

## 1. Architectural Strategy
We will adopt a **Dual Port** strategy to separate "System Clipboard" interaction from "History Persistence".

*   **Current State**: `ClipboardService` -> `ClipboardPort` (handles IO + history).
*   **Target State**: `ClipboardService` -> (`ClipboardPort` + `HistoryPort`).

### Rationale
*   **Separation of Concerns**: OS operations (Linux/Windows/Mac) are distinct from Storage operations (SQLite/JSON/Cloud).
*   **Testability**: We can mock storage independent of the OS clipboard.
*   **Scalability**: Easier to swap SQLite for another backend later.

## 2. Changes

### 2.1 Dependencies
*   Add `aiosqlite` to `pyproject.toml`.

### 2.2 Domain Layer (`src/core/domain/`)
*   **New Port**: `src/core/domain/ports.py` (or `storage_ports.py` if preferred, but `ports.py` is fine for now).
    *   Define `HistoryPort` abstract base class.
    *   Methods: `add(content: Content)`, `get_recent(limit: int)`, `clear()`.
*   **Refactor `ClipboardPort`**:
    *   Remove `history()` method (it belongs to `HistoryPort` now).

### 2.3 Service Layer (`src/core/service/service.py`)
*   Update `ClipboardService.__init__` to accept `history_adapter: HistoryPort`.
*   Update `write()`:
    1.  Call `clipboard_adapter.write(content)`.
    2.  Call `history_adapter.add(content)`.
*   Update `get_history()`:
    *   Delegate to `history_adapter.get_recent()`.

### 2.4 Infrastructure Layer (`src/core/adapters/`)
*   **New Adapter**: `src/core/adapters/sqlite_storage.py`.
    *   Implements `HistoryPort`.
    *   Uses `aiosqlite`.
    *   Schema (Strict Enforcement):
        ```sql
        CREATE TABLE main (uuid char(40) PRIMARY KEY, added_time REAL NOT NULL CHECK (added_time > 0), last_used_time REAL CHECK (last_used_time > 0), mimetypes TEXT NOT NULL, text NTEXT, starred BOOLEAN);
        CREATE TABLE aux (uuid char(40) NOT NULL, mimetype TEXT NOT NULL, data_uuid char(40) NOT NULL, PRIMARY KEY (uuid, mimetype));
        CREATE TABLE version (db_version INT NOT NULL);
        ```
    *   Database Path: Use `XDG_DATA_HOME` via `src/shared/config.py` (need to ensure config supports this).

### 2.5 Factory & Usage
*   Update `src/klipper_sdk/factory.py` to instantiate the SQLite adapter and inject it into the Service.

## 3. Verification
*   **Tests**:
    *   `test_sqlite_adapter.py`: Verify DB creation, inserts, and queries.
    *   `test_service.py`: Verify interactions between Service, ClipboardPort, and HistoryPort.
*   **Manual**:
    *   Run `examples/history.py` (needs update) to verify persistence across restarts.

## 4. Execution Steps
1.  **Dependencies**: Update `pyproject.toml`.
2.  **Domain**: Define `HistoryPort`, update `ClipboardPort`.
3.  **Infrastructure**: Implement `SQLiteStorage`.
4.  **Service**: Integrate `HistoryPort` into `ClipboardService`.
5.  **Wiring**: Update `Factory`.
6.  **Verify**: Run tests.
