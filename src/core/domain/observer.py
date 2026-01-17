from typing import Protocol
from src.core.domain.events import ClipboardEvent

class ClipboardObserver(Protocol):
    async def on_event(self, event: ClipboardEvent) -> None:
        """
        Handle a clipboard event.
        """
        ...
