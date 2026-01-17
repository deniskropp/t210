from datetime import datetime, timezone
from uuid import UUID
import pytest
from src.core.domain.models import Content, Metadata

def test_content_creation_from_text():
    content = Content.from_text("Hello World", source_app="vscode")
    
    assert content.data == "Hello World"
    assert content.metadata.content_type == "text/plain"
    assert content.metadata.source_app == "vscode"
    assert isinstance(content.metadata.id, UUID)
    assert isinstance(content.metadata.created_at, datetime)

def test_content_manual_creation():
    meta = Metadata(content_type="application/json")
    content = Content(data='{"key": "value"}', metadata=meta)
    
    assert content.data == '{"key": "value"}'
    assert content.metadata.content_type == "application/json"
    assert content.metadata.id is not None

def test_metadata_defaults():
    meta = Metadata(content_type="text/plain")
    assert meta.id is not None
    assert meta.created_at is not None
    assert meta.source_app is None

def test_validation_error():
    # Pydantic v2 validation
    with pytest.raises(Exception): 
        Metadata(content_type=123) # type: ignore
