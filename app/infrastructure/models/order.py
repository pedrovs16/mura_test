from sqlalchemy import BigInteger, Column, String, Text, ForeignKey, Enum
from infrastructure.constants.enums.order import OrderSourceEnum, OrderStatusEnum
from infrastructure.db import Base
from infrastructure.models.common import CommonBaseModel


class Order(Base, CommonBaseModel):
    __tablename__ = "order"

    id = Column(BigInteger, primary_key=True)
    customer_name = Column(String(255), nullable=False)
    email_id = Column(BigInteger, ForeignKey("email.id"), nullable=True)
    phone = Column(String(50), nullable=True)
    location = Column(Text, nullable=True)
    service_requested = Column(Text, nullable=False)
    order_details = Column(Text, nullable=True)  # Parsed AI response
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.PENDING)
    assigned_to = Column(String(255), nullable=True)
    source = Column(Enum(OrderSourceEnum), default=OrderSourceEnum.OTHER)

    def __repr__(self):
        return f"<WorkOrder(id={self.id}, customer={self.customer_name}, status={self.status})>"
