from typing import Annotated

from pydantic import BaseModel, Field

from infrastructure.api.schemas.common import ModelResponseSchema
from infrastructure.constants.enums.order import OrderSourceEnum, OrderStatusEnum


class OrderBaseSchema(BaseModel):
    customer_name: Annotated[str, Field(description="Name of the customer placing the order.")]
    email_id: Annotated[int | None, Field(description="Email id of the customer email, nullable.")]
    phone: Annotated[int | None, Field(description="Phone number of the customer, nullable.")]
    location: Annotated[str | None, Field(description="Location of the customer.")]
    service_requested: Annotated[str, Field(description="Service requested by the customer.")]
    order_details: Annotated[str | None, Field(description="Details of the order, nullable.")]
    status: Annotated[
        OrderStatusEnum, Field(description="Current status of the order.", default="Pending")
    ]
    assigned_to: Annotated[
        str | None, Field(description="Name of the person assigned to the order, nullable.")
    ]
    source: Annotated[OrderSourceEnum, Field(description="Source of the order.", default="Other")]


class OrderResponseSchema(OrderBaseSchema, ModelResponseSchema):
    pass


class OrderUpdateRequestSchema(BaseModel):
    customer_name: Annotated[
        str | None, Field(description="Updated name of the customer placing the order.")
    ]
    email_id: Annotated[str | None, Field(description="Updated email id of the customer email.")]
    phone: Annotated[
        str | None, Field(description="Updated phone number of the customer, nullable.")
    ]
    location: Annotated[str | None, Field(description="Updated location of the customer.")]
    service_requested: Annotated[
        str | None, Field(description="Updated service requested by the customer.")
    ]
    order_details: Annotated[
        str | None, Field(description="Updated details of the order, nullable.")
    ]
    status: Annotated[OrderStatusEnum | None, Field(description="Updated status of the order.")]
    assigned_to: Annotated[
        str | None, Field(description="Updated name of the person assigned to the order, nullable.")
    ]
    source: Annotated[OrderSourceEnum | None, Field(description="Updated source of the order.")]


class OrderCreateRequestSchema(OrderBaseSchema):
    pass
