# Configuration Guide

The Klipper SDK is designed to work out-of-the-box with sensible defaults, but it can be configured for specific needs.

## Factory Configuration

The easiest way to configure the client is via the `create_client` factory:

```python
from src.klipper_sdk.factory import create_client

# Auto-detect adapter (default)
client = create_client(adapter="auto")

# Force In-Memory adapter (useful for testing)
client = create_client(adapter="in_memory")
```

## Environment Variables

*Coming Soon*: Future versions will support configuring adapters via environment variables, e.g.:

```bash
export KLIPPER_ADAPTER=wayland
```
