from datetime import datetime

from pydantic import BaseModel


class BaseEntity(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
