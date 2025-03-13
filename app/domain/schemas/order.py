from datetime import datetime

from pydantic import BaseModel

from domain.schemas.common import OrderByFilterSchema
from infrastructure.constants.enums.order import OrderSourceEnum, OrderStatusEnum


class OrderBaseSchema(BaseModel):
    customer_name: str
    email_id: int | None = None
    phone: str | None
    location: str | None
    service_requested: str
    order_details: str | None
    status: OrderStatusEnum = OrderStatusEnum.PENDING
    assigned_to: str | None
    source: OrderSourceEnum = OrderSourceEnum.OTHER


class OrderCreateSchema(OrderBaseSchema):
    pass


class OrderUpdateSchema(BaseModel):
    customer_name: str | None = None
    email_id: int | None = None
    phone: str | None = None
    location: str | None = None
    service_requested: str | None = None
    order_details: OrderStatusEnum | None = None
    status: OrderStatusEnum | None = None
    source: OrderSourceEnum | None = None


class OrderFilterSchema(OrderByFilterSchema):
    id__in: list[int] | None = None
    customer_name: str | None = None
    email_id: int | None = None
    phone: str | None = None
    location: str | None = None
    service_requested: str | None = None
    status: OrderStatusEnum | None = None
    source: OrderSourceEnum | None = None
