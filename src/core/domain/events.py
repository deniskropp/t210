from enum import Enum
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field
from src.core.domain.models import Content

class EventType(str, Enum):
    CONTENT_CHANGED = "CONTENT_CHANGED"
    HISTORY_CLEARED = "HISTORY_CLEARED"
    ERROR = "ERROR"

class ClipboardEvent(BaseModel):
    type: EventType
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    data: Optional[Content] = None
