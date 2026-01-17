import asyncio
from typing import AsyncGenerator, List, Optional
from uuid import UUID

from src.core.domain.models import Content
from src.core.service.service import ClipboardService

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

    # Note: Monitoring logic to be re-implemented when Observer pattern is added to Service.
    # For now, we omit it to keep scope clean or can add a placeholder if needed.
    # monitor() removed for now as per plan to focus on core operations first.
