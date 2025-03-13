from domain.schemas.common import BaseEntitySchema
from domain.schemas.order import OrderBaseSchema


class OrderEntity(OrderBaseSchema, BaseEntitySchema):
    pass
