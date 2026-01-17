from typing import List, Optional
from uuid import UUID

from src.core.domain.models import Content
from src.core.domain.ports import ClipboardPort

class ClipboardService:
    """
    Core Service handling clipboard operations.
    Acts as the orchestrator between the Client and the Adapters.
    """

    def __init__(self, adapter: ClipboardPort) -> None:
        """
        Args:
            adapter: The specific clipboard adapter implementation to use.
        """
        self._adapter = adapter

    async def read(self) -> Optional[Content]:
        """
        Reads content from the clipboard.
        """
        return await self._adapter.read()

    async def write(self, content: Content) -> None:
        """
        Writes content to the clipboard.
        """
        await self._adapter.write(content)

    async def clear(self) -> None:
        """
        Clears the clipboard.
        """
        await self._adapter.clear()

    async def get_history(self, limit: int = 10) -> List[Content]:
        """
        Retrieves clipboard history.
        """
        return await self._adapter.history(limit=limit)
