import asyncio
from typing import AsyncGenerator, List, Optional
from uuid import UUID, uuid4

from klipper_sdk.core.interfaces import IClipboard, IHistory
from klipper_sdk.core.models import ClipboardContent, HistoryItem

class KlipperClient(IClipboard, IHistory):
    """
    Concrete implementation of the Klipper SDK Client.
    Currently acts as an in-memory clipboard manager for demonstration/stubbing purposes.
    In the future, this will delegate to a network connection.
    """

    def __init__(self) -> None:
        self._current_content: Optional[ClipboardContent] = None
        self._history: List[HistoryItem] = []
        self._monitor_queues: List[asyncio.Queue[ClipboardContent]] = []

    # --- IClipboard Implementation ---

    async def get_content(self, mime_type: Optional[str] = None) -> ClipboardContent:
        if self._current_content is None:
            # Return empty text content if nothing is set
            return ClipboardContent(data="", mime_type="text/plain")
        
        # In a real implementation, we might convert formats here based on mime_type
        return self._current_content

    async def set_content(self, content: ClipboardContent) -> bool:
        self._current_content = content
        
        # Add to history
        history_item = HistoryItem(content=content)
        self._history.insert(0, history_item)
        
        # Notify monitors
        for queue in self._monitor_queues:
            await queue.put(content)
            
        return True

    async def clear(self) -> bool:
        self._current_content = None
        return True

    async def monitor(self) -> AsyncGenerator[ClipboardContent, None]:
        queue: asyncio.Queue[ClipboardContent] = asyncio.Queue()
        self._monitor_queues.append(queue)
        try:
            while True:
                content = await queue.get()
                yield content
        finally:
            self._monitor_queues.remove(queue)

    # --- IHistory Implementation ---

    async def get_recent(self, limit: int = 10) -> List[HistoryItem]:
        return self._history[:limit]

    async def get_item(self, id: UUID) -> Optional[HistoryItem]:
        for item in self._history:
            if item.id == id:
                return item
        return None

    async def delete_item(self, id: UUID) -> bool:
        initial_len = len(self._history)
        self._history = [item for item in self._history if item.id != id]
        return len(self._history) < initial_len

    async def clear_history(self) -> bool:
        self._history.clear()
        return True
