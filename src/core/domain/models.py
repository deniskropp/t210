from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, Field

class Metadata(BaseModel):
    """
    Metadata associated with a clipboard entry.
    """
    model_config = ConfigDict(strict=True)

    id: UUID = Field(default_factory=uuid4, description="Unique identifier for the entry")
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Timestamp of creation (UTC)"
    )
    source_app: Optional[str] = Field(default=None, description="Application that generated the content")
    content_type: str = Field(description="MIME type or simple type description (text/plain, etc.)")

class Content(BaseModel):
    """
    Represents a clipboard content item.
    """
    model_config = ConfigDict(strict=True)

    data: str = Field(description="The actual content data (text or serialized) ")
    metadata: Metadata = Field(description="Associated metadata")

    @classmethod
    def from_text(cls, text: str, source_app: str | None = None) -> "Content":
        """Factory method to create content from simple text."""
        return cls(
            data=text,
            metadata=Metadata(
                content_type="text/plain",
                source_app=source_app
            )
        )
