import pytest
from src.klipper_sdk.factory import create_client
from src.core.domain.models import Content

@pytest.fixture
def client():
    # Use 'in_memory' for predictable testing
    return create_client(adapter="in_memory")

@pytest.mark.asyncio
async def test_client_set_get_content(client):
    content = Content.from_text("Hello Client")
    await client.set_content(content)
    
    fetched = await client.get_content()
    assert fetched.data == "Hello Client"
    assert fetched.metadata.content_type == "text/plain"

@pytest.mark.asyncio
async def test_client_clear(client):
    content = Content.from_text("To be cleared")
    await client.set_content(content)
    
    await client.clear()
    fetched = await client.get_content()
    assert fetched is None

@pytest.mark.asyncio
async def test_client_history_auto_add(client):
    content1 = Content.from_text("Item 1")
    content2 = Content.from_text("Item 2")
    
    await client.set_content(content1)
    await client.set_content(content2)
    
    history = await client.get_recent(limit=10)
    # Note: InMemoryAdapter sorts history by created_at. 
    # Since we create them almost instantly, order depends on system clock resolution.
    # We check membership instead of strict order for robustness in this simple test.
    data_in_history = [item.data for item in history]
    assert "Item 1" in data_in_history
    assert "Item 2" in data_in_history
    assert len(history) == 2

# Legacy tests for specific delete/item_get are removed as they were part of the 
# old client's internal logic, not the generic Service interface yet.
# We focus on the core Service Layer contract: read/write/clear/history.
