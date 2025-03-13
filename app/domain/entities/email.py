from domain.schemas.common import BaseEntitySchema
from domain.schemas.email import EmailBaseSchema


class EmailEntity(EmailBaseSchema, BaseEntitySchema):
    pass
