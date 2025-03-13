from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field

from infrastructure.api.schemas.common import ModelResponseSchema


class EmailBaseSchema(BaseModel):
    address: Annotated[str, Field(description="Email address of the customer.")]
    to: Annotated[str, Field(description="Email address of the recipient.")]
    subject: Annotated[str, Field(description="Subject of the email.")]
    body: Annotated[str, Field(description="Body of the email.")]
    sent_at: Annotated[datetime, Field(description="Time the email was sent.")]
    reply_to: Annotated[str | None, Field(description="Email address to reply to, nullable.")]


class EmailResponseSchema(EmailBaseSchema, ModelResponseSchema):
    pass


class EmailUpdateRequestSchema(BaseModel):
    address: Annotated[str | None, Field(description="Updated email address of the customer.")]
    to: Annotated[str | None, Field(description="Updated email address of the recipient.")]
    subject: Annotated[str | None, Field(description="Updated subject of the email.")]
    body: Annotated[str | None, Field(description="Updated body of the email.")]
    sent_at: Annotated[datetime | None, Field(description="Updated time the email was sent.")]
    reply_to: Annotated[
        str | None, Field(description="Updated email address to reply to, nullable.")
    ]


class EmailCreateRequestSchema(EmailBaseSchema):
    pass
