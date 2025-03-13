from datetime import datetime

from pydantic import BaseModel

from domain.schemas.common import OrderByFilterSchema


class EmailBaseSchema(BaseModel):
    address: str
    to: str
    subject: str
    body: str
    sent_at: datetime
    reply_to: str | None = None


class EmailCreateSchema(EmailBaseSchema):
    pass


class EmailUpdateSchema(BaseModel):
    address: str | None = None
    to: str | None = None
    subject: str | None = None
    body: str | None = None
    sent_at: datetime | None = None
    reply_to: str | None = None


class EmailFilterSchema(OrderByFilterSchema):
    address: str | None = None
    to: str | None = None
    subject: str | None = None
    body: str | None = None
    sent_at: datetime | None = None
    reply_to: str | None = None
