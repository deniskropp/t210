from datetime import datetime
from typing import Any, Dict, Union
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

class ClipboardContent(BaseModel):
    """
    Represents the content of a clipboard item.
    """
    data: Union[str, bytes] = Field(..., description="The actual clipboard content.")
    mime_type: str = Field(..., description="MIME type of the content (e.g., 'text/plain').")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata (source app, timestamp).")

class HistoryItem(BaseModel):
    """
    Represents an item in the clipboard history.
    """
    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the history item.")
    timestamp: datetime = Field(default_factory=datetime.now, description="Time of capture.")
    content: ClipboardContent = Field(..., description="The content of the item.")
    pinned: bool = Field(default=False, description="Whether the item is pinned in history.")
