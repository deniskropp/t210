from typing import List, Optional
from src.core.domain.ports import ClipboardPort
from src.core.domain.models import Content

class InMemoryClipboardAdapter(ClipboardPort):
    """
    In-memory implementation of ClipboardPort.
    Useful for testing and development without side effects.
    """
    def __init__(self) -> None:
        self._current: Optional[Content] = None

    async def read(self) -> Optional[Content]:
        return self._current

    async def write(self, content: Content) -> None:
        self._current = content

    async def clear(self) -> None:
        self._current = None