from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class ModelResponseSchema(BaseModel):
    id: Annotated[int, Field(description="Unique identifier of the packet.")]
    created_at: Annotated[datetime | None, Field(description="Creation date of the packet.")]
    updated_at: Annotated[datetime | None, Field(description="Updated date of the packet.")]
    deleted_at: Annotated[datetime | None, Field(description="Soft deleted date of the packet.")]
