from dataclasses import dataclass

from domain.ports.common.generic_data_port import (
    GenericDataPort,
    TCreateSchema,
    TEntity,
    TFilterSchema,
    TUpdateSchema,
)


@dataclass
class CreateUseCase:
    data_port: GenericDataPort

    def execute(self, data: TCreateSchema) -> TEntity:
        return self.data_port.create(data, save=True)


@dataclass
class CreateBatchUseCase:
    data_port: GenericDataPort

    def execute(self, data: list[TCreateSchema]) -> list[TEntity]:
        return self.data_port.create_batch(data, save=True)


@dataclass
class UpdateUseCase:
    data_port: GenericDataPort

    def execute(self, id: int, data: TUpdateSchema) -> TEntity:
        return self.data_port.update(id, data, save=True)


@dataclass
class DeleteUseCase:
    data_port: GenericDataPort

    def execute(self, id: int, soft: bool = True):
        self.data_port.delete(id, soft=soft, save=True)


@dataclass
class GetUseCase:
    data_port: GenericDataPort

    def execute(self, id: int) -> TEntity:
        return self.data_port.get(id)


@dataclass
class FilterUseCase:
    data_port: GenericDataPort

    def execute(self, filters: TFilterSchema, deleted: bool = False) -> list[TEntity]:
        return self.data_port.filter(filters=filters, deleted=deleted)
