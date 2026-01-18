from typing import List, Optional
from uuid import UUID

from src.core.domain.models import Content
from src.core.domain.ports import ClipboardPort, HistoryPort
from src.core.domain.events import ClipboardEvent, EventType
from src.core.domain.observer import ClipboardObserver

class ClipboardService:
    """
    Core Service handling clipboard operations.
    Acts as the orchestrator between the Client and the Adapters.
    """

    def __init__(self, clipboard_adapter: ClipboardPort, history_adapter: HistoryPort) -> None:
        """
        Args:
            clipboard_adapter: The specific clipboard adapter implementation to use (System IO).
            history_adapter: The specific history adapter implementation to use (Persistence).
        """
        self._clipboard_adapter = clipboard_adapter
        self._history_adapter = history_adapter
        self._observers: List[ClipboardObserver] = []

    def subscribe(self, observer: ClipboardObserver) -> None:
        """
        Subscribe an observer to clipboard events.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: ClipboardObserver) -> None:
        """
        Unsubscribe an observer from clipboard events.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    async def _notify(self, event: ClipboardEvent) -> None:
        """
        Notify all subscribers of an event.
        """
        for observer in self._observers:
            await observer.on_event(event)

    async def read(self) -> Optional[Content]:
        """
        Reads content from the clipboard.
        """
        return await self._clipboard_adapter.read()

    async def write(self, content: Content) -> None:
        """
        Writes content to the clipboard and history.
        """
        await self._clipboard_adapter.write(content)
        await self._history_adapter.add(content)
        await self._notify(ClipboardEvent(type=EventType.CONTENT_CHANGED, data=content))

    async def clear(self) -> None:
        """
        Clears the clipboard and history.
        """
        await self._clipboard_adapter.clear()
        await self._history_adapter.clear()
        await self._notify(ClipboardEvent(type=EventType.HISTORY_CLEARED))

    async def get_history(self, limit: int = 10) -> List[Content]:
        """
        Retrieves clipboard history.
        """
        return await self._history_adapter.get_recent(limit=limit)