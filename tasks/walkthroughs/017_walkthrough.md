# Walkthrough - Task 017: v0.3.0 Event System Implementation

## Goal
Implement the Event System and Monitoring capabilities for the Klipper SDK v0.3.0, enabling real-time clipboard observation.

## Achievements
1.  **Domain Models**: Created `src/core/domain/events.py` defining `EventType` and `ClipboardEvent` with timezone-aware timestamps.
2.  **Observer Protocol**: Created `src/core/domain/observer.py` defining the `ClipboardObserver` protocol.
3.  **Core Service Update**: Enhanced `ClipboardService` in `src/core/service/service.py` to support `subscribe`, `unsubscribe`, and `_notify`. Implemented event triggering in `write()` and `clear()`.
4.  **Client API Update**: Updated `KlipperClient` in `src/klipper_sdk/client/client.py` to expose `add_event_listener` and `remove_event_listener` using a `CallbackObserver` wrapper.
5.  **Testing**: Created `tests/test_events.py` verifying all scenarios (write, clear, unsubscribe) with 100% pass rate.
6.  **Documentation & Examples**: Updated `docs/api/client.md` and `examples/monitor.py` to reflect the new capabilities.

## Verification
-   `python -m pytest tests/test_events.py` passed.
-   `python -m examples.monitor` executed successfully, demonstrating real-time event reception.

## Next Steps
-   Prepare for v0.3.0 release (Task 018).
