from datetime import datetime
from uuid import UUID
import pytest
from klipper_sdk.core.models import ClipboardContent, HistoryItem

def test_clipboard_content_creation():
    content = ClipboardContent(
        data="Hello World",
        mime_type="text/plain",
        metadata={"source": "vscode"}
    )
    assert content.data == "Hello World"
    assert content.mime_type == "text/plain"
    assert content.metadata["source"] == "vscode"

def test_clipboard_content_bytes():
    binary_data = b"\x00\x01\x02"
    content = ClipboardContent(
        data=binary_data,
        mime_type="application/octet-stream"
    )
    assert content.data == binary_data

def test_history_item_creation():
    content = ClipboardContent(data="Test", mime_type="text/plain")
    item = HistoryItem(content=content)
    
    assert isinstance(item.id, UUID)
    assert isinstance(item.timestamp, datetime)
    assert item.content == content
    assert item.pinned is False

def test_history_item_defaults():
    content = ClipboardContent(data="Test", mime_type="text/plain")
    item = HistoryItem(content=content, pinned=True)
    assert item.pinned is True

def test_invalid_content():
    with pytest.raises(Exception): # Pydantic validation error
        ClipboardContent(data=123, mime_type="text/plain") # type: ignore
