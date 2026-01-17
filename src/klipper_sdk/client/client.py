import asyncio
from typing import AsyncGenerator, List, Optional, Callable, Awaitable
from uuid import UUID

from src.core.domain.models import Content
from src.core.service.service import ClipboardService
from src.core.domain.observer import ClipboardObserver
from src.core.domain.events import ClipboardEvent

class CallbackObserver(ClipboardObserver):
    """
    Helper to wrap a callback function as an Observer.
    """
    def __init__(self, callback: Callable[[ClipboardEvent], Awaitable[None]]):
        self._callback = callback

    async def on_event(self, event: ClipboardEvent) -> None:
        await self._callback(event)

class KlipperClient:
    """
    Public-facing client for the Klipper SDK.
    Delegates operations to the internal ClipboardService.
    """

    def __init__(self, service: ClipboardService) -> None:
        """
        Args:
            service: The configured ClipboardService instance.
        """
        self._service = service

    async def get_content(self) -> Optional[Content]:
        """
        Retrieves the current content from the clipboard.
        """
        return await self._service.read()

    async def set_content(self, content: Content) -> None:
        """
        Sets content to the clipboard.
        """
        await self._service.write(content)

    async def clear(self) -> None:
        """
        Clears the clipboard content.
        """
        await self._service.clear()

    async def get_recent(self, limit: int = 10) -> List[Content]:
        """
        Retrieves recent clipboard history.
        """
        return await self._service.get_history(limit=limit)

    def add_event_listener(self, callback: Callable[[ClipboardEvent], Awaitable[None]]) -> ClipboardObserver:
        """
        Registers a callback to be invoked on clipboard events.
        Returns the observer instance which can be used to unsubscribe.
        """
        observer = CallbackObserver(callback)
        self._service.subscribe(observer)
        return observer

    def remove_event_listener(self, observer: ClipboardObserver) -> None:
        """
        Unsubscribes a previously registered observer.
        """
        self._service.unsubscribe(observer)
