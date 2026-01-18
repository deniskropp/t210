import pytest
import aiosqlite
import os
from src.core.adapters.sqlite_storage import SQLiteStorage
from src.core.domain.models import Content

@pytest.mark.asyncio
async def test_sqlite_adapter_basics(tmp_path):
    db_file = tmp_path / "test.db"
    adapter = SQLiteStorage(db_path=str(db_file))
    
    # Check init
    await adapter.initialize()
    assert db_file.exists()
    
    # Check add
    content = Content.from_text("Hello World")
    await adapter.add(content)
    
    # Check retrieve
    recent = await adapter.get_recent()
    assert len(recent) == 1
    assert recent[0].data == "Hello World"
    assert recent[0].metadata.id == content.metadata.id
    
    # Check clear
    await adapter.clear()
    recent = await adapter.get_recent()
    assert len(recent) == 0

@pytest.mark.asyncio
async def test_lazy_init(tmp_path):
    db_file = tmp_path / "lazy.db"
    adapter = SQLiteStorage(db_path=str(db_file))
    
    # Should init automatically
    content = Content.from_text("Lazy")
    await adapter.add(content)
    
    assert db_file.exists()
    recent = await adapter.get_recent()
    assert len(recent) == 1
