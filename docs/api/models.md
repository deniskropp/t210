# Domain Models API Reference

These models represent the core data structures used throughout the Klipper SDK.

**Path**: `src.core.domain.models`

## Class: `Content`

Represents a clipboard item.

```python
class Content(BaseModel):
    data: str
    metadata: Metadata
```

### Methods

#### `from_text`

```python
@classmethod
def from_text(cls, text: str, source_app: str | None = None) -> "Content"
```

Factory method to create content from simple text.

- **Args**:
    - `text`: The string content.
    - `source_app`: Optional name of the source application.

## Class: `Metadata`

Metadata associated with a clipboard entry.

```python
class Metadata(BaseModel):
    id: UUID
    created_at: datetime
    source_app: Optional[str]
    content_type: str
```

- **id**: Unique identifier (auto-generated).
- **created_at**: Timestamp (UTC, auto-generated).
- **source_app**: Originating application (optional).
- **content_type**: MIME type (e.g., "text/plain").
