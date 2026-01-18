from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.domain.models import Content

class ClipboardPort(ABC):
    """
    Port (Interface) for Clipboard Adapters.
    Encapsulates all interaction with the underlying system clipboard.
    """

    @abstractmethod
    async def read(self) -> Optional[Content]:
        """
        Reads the current content from the clipboard.
        Returns:
            Content object or None if empty/error.
        """
        pass

    @abstractmethod
    async def write(self, content: Content) -> None:
        """
        Writes content to the clipboard.
        Args:
            content: The content object to write.
        """
        pass

    @abstractmethod
    async def clear(self) -> None:
        """
        Clears the system clipboard content.
        """
        pass


class HistoryPort(ABC):
    """
    Port (Interface) for History Persistence Adapters.
    Encapsulates all interaction with the long-term storage (DB).
    """

    @abstractmethod
    async def add(self, content: Content) -> None:
        """
        Adds a new entry to the history.
        Args:
            content: The content object to add.
        """
        pass

    @abstractmethod
    async def get_recent(self, limit: int = 10) -> List[Content]:
        """
        Retrieves recent history entries.
        Args:
            limit: Maximum number of entries to return.
        """
        pass

    @abstractmethod
    async def clear(self) -> None:
        """
        Clears the history storage.
        """
        pass