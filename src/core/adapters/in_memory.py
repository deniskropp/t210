from typing import List, Optional
from src.core.domain.ports import ClipboardPort
from src.core.domain.models import Content

class InMemoryClipboardAdapter(ClipboardPort):
    """
    In-memory implementation of ClipboardPort.
    Useful for testing and development without side effects.
    """
    def __init__(self):
        self._storage: List[Content] = []
        self._current: Optional[Content] = None

    async def read(self) -> Optional[Content]:
        return self._current

    async def write(self, content: Content) -> None:
        self._current = content
        self._storage.append(content)

    async def clear(self) -> None:
        self._current = None
        # Note: History is preserved in this simple impl, or could be cleared too.
        # Strict clear usually means current content is gone.

    async def history(self, limit: int = 10) -> List[Content]:
        return sorted(
            self._storage, 
            key=lambda c: c.metadata.created_at, 
            reverse=True
        )[:limit]
