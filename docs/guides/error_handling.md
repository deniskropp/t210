# Error Handling Guide

The Klipper SDK uses a consistent exception hierarchy to help you handle errors gracefully.

## Exception Hierarchy

All exceptions inherit from `KlipperSDKError`.

- `KlipperSDKError`
    - `ClipboardError` (Generic clipboard failure)
    - `AdapterError` (Underlying adapter failure)
    - `ValidationError` (Invalid data/content)

## Handling Exceptions

```python
from src.shared.exceptions import KlipperSDKError

try:
    await client.get_content()
except KlipperSDKError as e:
    print(f"Oops, something went wrong: {e}")
```

## Debugging

If you encounter issues:
1.  Check that your platform is supported (currently `InMemory` is default, `Wayland`/`X11` coming soon).
2.  Enable logging (standard Python logging).
