import asyncio
import pytest
from uuid import uuid4

from klipper_sdk.client.client import KlipperClient
from klipper_sdk.core.models import ClipboardContent

@pytest.fixture
def client():
    return KlipperClient()

@pytest.mark.asyncio
async def test_client_set_get_content(client):
    content = ClipboardContent(data="Hello Client", mime_type="text/plain")
    assert await client.set_content(content) is True
    
    fetched = await client.get_content()
    assert fetched.data == "Hello Client"
    assert fetched.mime_type == "text/plain"

@pytest.mark.asyncio
async def test_client_clear(client):
    content = ClipboardContent(data="To be cleared", mime_type="text/plain")
    await client.set_content(content)
    
    assert await client.clear() is True
    fetched = await client.get_content()
    # Depending on implementation, might return None or empty content.
    # Our implementation returns empty text/plain if None.
    assert fetched.data == ""

@pytest.mark.asyncio
async def test_client_history_auto_add(client):
    content1 = ClipboardContent(data="Item 1", mime_type="text/plain")
    content2 = ClipboardContent(data="Item 2", mime_type="text/plain")
    
    await client.set_content(content1)
    await client.set_content(content2)
    
    history = await client.get_recent()
    assert len(history) == 2
    assert history[0].content.data == "Item 2"
    assert history[1].content.data == "Item 1"

@pytest.mark.asyncio
async def test_client_history_management(client):
    content = ClipboardContent(data="Delete Me", mime_type="text/plain")
    await client.set_content(content)
    
    history = await client.get_recent()
    item_id = history[0].id
    
    # Get Item
    item = await client.get_item(item_id)
    assert item is not None
    assert item.content.data == "Delete Me"
    
    # Delete Item
    assert await client.delete_item(item_id) is True
    assert await client.get_item(item_id) is None
    
    # Clear History
    await client.set_content(content)
    assert await client.clear_history() is True
    assert len(await client.get_recent()) == 0

@pytest.mark.asyncio
async def test_client_monitor(client):
    content_to_send = ClipboardContent(data="Streamed", mime_type="text/plain")
    
    async def produce():
        await asyncio.sleep(0.1)
        await client.set_content(content_to_send)

    async def consume():
        async for item in client.monitor():
            assert item.data == "Streamed"
            break
    
    await asyncio.gather(produce(), consume())
