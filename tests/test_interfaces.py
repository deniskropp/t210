import pytest
from typing import AsyncGenerator, List, Optional
from uuid import UUID
from klipper_sdk.core.interfaces import IClipboard, IHistory
from klipper_sdk.core.models import ClipboardContent, HistoryItem

class MockClipboard(IClipboard):
    async def get_content(self, mime_type: Optional[str] = None) -> ClipboardContent:
        return ClipboardContent(data="mock", mime_type="text/plain")
    
    async def set_content(self, content: ClipboardContent) -> bool:
        return True
    
    async def clear(self) -> bool:
        return True
    
    async def monitor(self) -> AsyncGenerator[ClipboardContent, None]:
        yield ClipboardContent(data="mock", mime_type="text/plain")

class MockHistory(IHistory):
    async def get_recent(self, limit: int = 10) -> List[HistoryItem]:
        return []

    async def get_item(self, id: UUID) -> Optional[HistoryItem]:
        return None

    async def delete_item(self, id: UUID) -> bool:
        return True

    async def clear_history(self) -> bool:
        return True

@pytest.mark.asyncio
async def test_clipboard_interface_implementation():
    mock = MockClipboard()
    assert await mock.set_content(ClipboardContent(data="test", mime_type="text/plain")) is True
    content = await mock.get_content()
    assert content.data == "mock"

    async for item in mock.monitor():
        assert item.data == "mock"
        break

@pytest.mark.asyncio
async def test_history_interface_implementation():
    mock = MockHistory()
    assert await mock.clear_history() is True
    items = await mock.get_recent()
    assert items == []

def test_cannot_instantiate_abstract_clipboard():
    with pytest.raises(TypeError):
        class IncompleteClipboard(IClipboard):
            pass
        IncompleteClipboard() # type: ignore

def test_cannot_instantiate_abstract_history():
    with pytest.raises(TypeError):
        class IncompleteHistory(IHistory):
            pass
        IncompleteHistory() # type: ignore
