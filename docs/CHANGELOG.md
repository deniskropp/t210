# Changelog

## v0.5.0

### Features
- **SQLite Persistence**: Introduced `SQLiteStorage` adapter for persistent history management.
- **Dual-Port Architecture**: Separated `ClipboardPort` (System) and `HistoryPort` (Storage).
- **Schema Enforcement**: Added strict SQL schema with versioning for the history database.
- **Auto-Persist**: Updated `KlipperClient` factory to use SQLite storage by default in `auto` mode.

## v0.4.0

### Features
- **Linux Support**: Added `LinuxClipboardAdapter` using `wl-clipboard` (Wayland) or `xclip`/`xsel` (X11).
- **Auto-Detection**: Updated `ClientFactory` to automatically detect and use the Linux adapter on compatible systems.
- **Async Process**: Implemented non-blocking clipboard operations using `asyncio.subprocess`.

## v0.3.0

### Features
- **Event System**: Implemented Observer Pattern in `ClipboardService`.
- **Real-time Monitoring**: Added `add_event_listener` and `remove_event_listener` to `KlipperClient`.
- **Domain Events**: Introduced `ClipboardEvent` and `EventType` models.
- **Service Layer**: Added subscription management (`subscribe`, `unsubscribe`) to `ClipboardService`.

## v0.2.0

### Features
- Introduced **Hexagonal Architecture**.
- Separated `Core Domain` (Models/Ports) from `Adapters`.
- Implemented `ClipboardService` as the central orchestrator.
- Refactored `KlipperClient` to be a facade.
- Added `InMemoryAdapter` for testing.
- Added `ClientFactory` for easy instantiation.

### Breaking Changes
- Removed `klipper_sdk.core.models` and `klipper_sdk.core.interfaces`. Use `src.core.domain` instead.

## v0.1.0
- Initial Proof of Concept (Stub implementation).
