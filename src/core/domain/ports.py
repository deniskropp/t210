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
        Clears the clipboard content.
        """
        pass

    @abstractmethod
    async def history(self, limit: int = 10) -> List[Content]:
        """
        Retrieves the history of clipboard entries.
        Args:
            limit: Maximum number of entries to return.
        """
        pass
