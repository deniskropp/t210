# Changelog

## v0.2.0 (In Development)

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
