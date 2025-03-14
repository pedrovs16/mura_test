from dataclasses import dataclass

from domain.ports.ai import AIIntegrationPort
from domain.ports.common.generic_data_port import GenericDataPort, TCreateSchema, TEntity
from domain.schemas.order import OrderCreateSchema


@dataclass
class ReceiveEmailUseCase:
    email_data_port: GenericDataPort
    order_data_port: GenericDataPort
    ai_port: AIIntegrationPort

    def execute(self, data: TCreateSchema) -> TEntity:
        email_entity = self.email_data_port.create(data)
        ai_response = self.ai_port.generate_text(email_entity.body)
        order_dict = {**ai_response, "email_id": email_entity.id, "email": email_entity.body}
        self.order_data_port.create(OrderCreateSchema(**order_dict))
        return email_entity
