from typing import TYPE_CHECKING

from domain.entities.email import EmailEntity
from infrastructure.adapters.common.generic_sqlalchemy_adapter import GenericSQLAlchemyAdapter
from infrastructure.api.query_filters.email import EmailFilter
from infrastructure.models.email import Email

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class EmailSQLAlchemyAdapter(GenericSQLAlchemyAdapter):
    def __init__(self, session: "Session"):
        super().__init__(
            session=session, entity=EmailEntity, model=Email, fastapi_filter=EmailFilter
        )
