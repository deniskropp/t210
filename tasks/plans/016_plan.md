# Implementation Plan - Task 016: v0.3.0 Event System & Monitoring

## 1. Overview
This plan outlines the implementation of the Event System and Monitoring capabilities for the Klipper SDK v0.3.0. This addition will enable real-time applications by allowing clients to react to clipboard changes (write, clear) without polling.

## 2. Architecture: The Observer Pattern

We will implement the **Observer Pattern** within the `ClipboardService`.

-   **Subject**: `ClipboardService` (manages the state and list of observers).
-   **Observer**: New `ClipboardObserver` interface (abstract base class).
-   **Event**: New `ClipboardEvent` model to encapsulate event details.

### Component Interactions
1.  Client registers an observer (callback or object) via `KlipperClient`.
2.  `KlipperClient` delegates subscription to `ClipboardService`.
3.  When `ClipboardService.write()` or `clear()` is called:
    -   Operation is performed on the Adapter.
    -   `ClipboardService` iterates through subscribers and calls their `on_event` method.

## 3. Detailed Implementation Steps

### Step 1: Define Domain Models & Interfaces
*   **Action**: Create `src/core/domain/events.py`.
*   **Content**:
    -   `EventType` (Enum): `CONTENT_CHANGED`, `HISTORY_CLEARED`, `ERROR`.
    -   `ClipboardEvent` (Pydantic Model): `type: EventType`, `timestamp: datetime`, `data: Optional[Content]`.
*   **Action**: Update `src/core/domain/ports.py` (or create `src/core/domain/observer.py`).
*   **Content**:
    -   `ClipboardObserver` (Protocol/ABC): `async def on_event(self, event: ClipboardEvent) -> None`.

### Step 2: Enhance ClipboardService (Subject)
*   **File**: `src/core/service/service.py`
*   **Changes**:
    -   Add `_observers: List[ClipboardObserver]` to `__init__`.
    -   Implement `subscribe(observer: ClipboardObserver)`.
    -   Implement `unsubscribe(observer: ClipboardObserver)`.
    -   Implement `_notify(event: ClipboardEvent)`.
    -   **Triggering**:
        -   In `write()`: `await self._notify(ClipboardEvent(type=CONTENT_CHANGED, data=content))`
        -   In `clear()`: `await self._notify(ClipboardEvent(type=HISTORY_CLEARED))`

### Step 3: Enhance KlipperClient (Facade)
*   **File**: `src/klipper_sdk/client/client.py`
*   **Changes**:
    -   Add `monitor()` method (Async Generator) that yields events?
    -   OR add simple `add_event_listener(callback)` method that wraps a function into an `Observer`.
    -   *Decision*: We will support `add_event_listener(callback)` for simplicity and flexibility.

### Step 4: Testing
*   **File**: `tests/test_events.py`
*   **Scope**:
    -   Verify callbacks are fired on `write`.
    -   Verify callbacks are fired on `clear`.
    -   Verify `unsubscribe` stops updates.
    -   Ensure non-blocking behavior (async).

## 4. Verification & Documentation
-   Run `pytest` to ensure 100% pass rate.
-   Update `docs/api/client.md` to include new event methods.
-   Update `examples/monitor.py` to demonstrate the new feature.
