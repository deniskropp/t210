import pytest
import asyncio
from src.core.service.service import ClipboardService
from src.core.adapters.in_memory import InMemoryClipboardAdapter
from src.core.domain.ports import HistoryPort
from src.klipper_sdk.client.client import KlipperClient
from src.core.domain.events import ClipboardEvent, EventType
from src.core.domain.models import Content

class MockHistoryAdapter(HistoryPort):
    async def add(self, content): pass
    async def get_recent(self, limit=10): return []
    async def clear(self): pass

@pytest.fixture
def service():
    adapter = InMemoryClipboardAdapter()
    history = MockHistoryAdapter()
    return ClipboardService(adapter, history_adapter=history)

@pytest.fixture
def client(service):
    return KlipperClient(service)

@pytest.mark.asyncio
async def test_event_on_write(client):
    received_events = []
    
    async def callback(event: ClipboardEvent):
        received_events.append(event)
        
    client.add_event_listener(callback)
    
    content = Content.from_text("test", source_app="test_app")
    await client.set_content(content)
    
    assert len(received_events) == 1
    assert received_events[0].type == EventType.CONTENT_CHANGED
    assert received_events[0].data == content

@pytest.mark.asyncio
async def test_event_on_clear(client):
    received_events = []
    
    async def callback(event: ClipboardEvent):
        received_events.append(event)
        
    client.add_event_listener(callback)
    
    await client.clear()
    
    assert len(received_events) == 1
    assert received_events[0].type == EventType.HISTORY_CLEARED
    assert received_events[0].data is None

@pytest.mark.asyncio
async def test_unsubscribe(client):
    received_events = []
    
    async def callback(event: ClipboardEvent):
        received_events.append(event)
        
    observer = client.add_event_listener(callback)
    
    content = Content.from_text("test1")
    await client.set_content(content)
    assert len(received_events) == 1
    
    client.remove_event_listener(observer)
    
    await client.set_content(content)
    assert len(received_events) == 1  # Should not increase