# KlipperClient API Reference

The `KlipperClient` is the main entry point for the SDK. It provides a high-level, asynchronous interface for clipboard operations.

## Class: `KlipperClient`

**Path**: `src.klipper_sdk.client.client.KlipperClient`

### Initialization

```python
def __init__(self, service: ClipboardService) -> None:
```

- **service**: An instance of `ClipboardService`. Use `src.klipper_sdk.factory.create_client` to instantiate easily.

### Methods

#### `get_content`

```python
async def get_content(self) -> Optional[Content]
```

Retrieves the current content from the clipboard.

- **Returns**: `Content` object if clipboard is not empty, else `None`.

#### `set_content`

```python
async def set_content(self, content: Content) -> None
```

Writes content to the clipboard.

- **Args**:
    - `content`: A `Content` object (use `Content.from_text(...)` helper).

#### `clear`

```python
async def clear(self) -> None
```

Clears the clipboard content.

#### `get_recent`

```python
async def get_recent(self, limit: int = 10) -> List[Content]
```

Retrieves recent clipboard history.

- **Args**:
    - `limit` (int): Maximum number of entries to return. Default is 10.
- **Returns**: List of `Content` objects.
