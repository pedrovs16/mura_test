from typing import TYPE_CHECKING

from domain.entities.order import OrderEntity
from infrastructure.adapters.common.generic_sqlalchemy_adapter import GenericSQLAlchemyAdapter
from infrastructure.api.query_filters.order import OrderFilter
from infrastructure.models.order import Order

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class OrderSQLAlchemyAdapter(GenericSQLAlchemyAdapter):
    def __init__(self, session: "Session"):
        super().__init__(
            session=session, entity=OrderEntity, model=Order, fastapi_filter=OrderFilter
        )
