from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from pydantic import BaseModel

TCreateSchema = TypeVar("TCreateSchema", bound=BaseModel)
TUpdateSchema = TypeVar("TUpdateSchema", bound=BaseModel)
TFilterSchema = TypeVar("TFilterSchema", bound=BaseModel)
TEntity = TypeVar("TEntity", bound=BaseModel)


class GenericDataPort(Generic[TCreateSchema, TUpdateSchema, TFilterSchema, TEntity], ABC):
    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def create(self, data: TCreateSchema, *, save: bool = True) -> TEntity:
        pass

    @abstractmethod
    def create_batch(self, data: list[TCreateSchema], *, save: bool = True) -> list[TEntity]:
        pass

    @abstractmethod
    def update(self, id: int, data: TUpdateSchema, *, save: bool = True) -> TEntity:
        pass

    @abstractmethod
    def delete(self, id: int, *, soft: bool = True, save: bool = True):
        pass

    @abstractmethod
    def delete_batch(self, ids: list[int], *, soft: bool = True, save: bool = True):
        pass

    @abstractmethod
    def get(self, id: int) -> TEntity:
        pass

    @abstractmethod
    def filter(self, filters: TFilterSchema | None, deleted: bool = False) -> list[TEntity]:
        pass
