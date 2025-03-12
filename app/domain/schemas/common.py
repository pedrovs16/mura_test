from datetime import datetime

from pydantic import BaseModel


class BaseEntitySchema(BaseModel):
    id: int | None
    created_at: datetime | None
    updated_at: datetime | None
    deleted_at: datetime | None


class OrderByFilterSchema(BaseModel):
    order_by: list[str] | None = None
