from abc import ABC, abstractmethod
from typing import AsyncGenerator, List, Optional
from uuid import UUID

from klipper_sdk.core.models import ClipboardContent, HistoryItem

class IClipboard(ABC):
    """
    Interface for direct clipboard interactions.
    """

    @abstractmethod
    async def get_content(self, mime_type: Optional[str] = None) -> ClipboardContent:
        """
        Retrieve the current content of the clipboard.

        Args:
            mime_type: Optional specific MIME type to request.

        Returns:
            ClipboardContent object containing the data.
        """
        pass

    @abstractmethod
    async def set_content(self, content: ClipboardContent) -> bool:
        """
        Set the content of the clipboard.

        Args:
            content: The ClipboardContent object to set.

        Returns:
            True if successful, False otherwise.
        """
        pass

    @abstractmethod
    async def clear(self) -> bool:
        """
        Clear the clipboard content.

        Returns:
            True if successful, False otherwise.
        """
        pass

    @abstractmethod
    async def monitor(self) -> AsyncGenerator[ClipboardContent, None]:
        """
        Monitor the clipboard for changes.

        Yields:
            ClipboardContent objects as they change.
        """
        pass

class IHistory(ABC):
    """
    Interface for clipboard history management.
    """

    @abstractmethod
    async def get_recent(self, limit: int = 10) -> List[HistoryItem]:
        """
        Retrieve recent clipboard history items.

        Args:
            limit: Maximum number of items to retrieve.

        Returns:
            List of HistoryItem objects.
        """
        pass

    @abstractmethod
    async def get_item(self, id: UUID) -> Optional[HistoryItem]:
        """
        Retrieve a specific history item by ID.

        Args:
            id: Unique identifier of the item.

        Returns:
            HistoryItem if found, None otherwise.
        """
        pass

    @abstractmethod
    async def delete_item(self, id: UUID) -> bool:
        """
        Delete a specific history item.

        Args:
            id: Unique identifier of the item.

        Returns:
            True if successful, False otherwise.
        """
        pass

    @abstractmethod
    async def clear_history(self) -> bool:
        """
        Clear the entire clipboard history.

        Returns:
            True if successful, False otherwise.
        """
        pass
