from typing import TYPE_CHECKING, TypeVar

from fastapi_filter.contrib.sqlalchemy import Filter

from domain.ports.common.generic_data_port import (
    GenericDataPort,
    TCreateSchema,
    TEntity,
    TFilterSchema,
    TUpdateSchema,
)
from infrastructure.api.query_filters.common import DeleteBatchFilter
from infrastructure.db import Base
from infrastructure.translators.generic import convert_model_to_entity, convert_models_to_entities

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

TFastAPIFilter = TypeVar("TFastAPIFilter", bound=Filter)
TModel = TypeVar("TModel", bound=Base)  # SQLAlchemy Model


class GenericSQLAlchemyAdapter(GenericDataPort):
    def __init__(
        self, session: "Session", entity: TEntity, model: TModel, fastapi_filter: TFastAPIFilter
    ):
        self.session = session
        self.entity = entity
        self.model = model
        self.fastapi_filter = fastapi_filter

    def cancel(self):
        self.session.rollback()

    def save(self):
        self.session.commit()

    def create(self, data: TCreateSchema, *, save: bool = True) -> TEntity:
        model_instance = self.model(**data.dict(exclude_none=True))
        self.session.add(model_instance)

        if save:
            self.session.commit()
        else:
            # instanciate the object with a PK but does not persist the changes in the DB
            self.session.flush()

        self.session.refresh(model_instance)
        return convert_model_to_entity(model_instance=model_instance, entity_class=self.entity)

    def create_batch(self, data: list[TCreateSchema], *, save: bool = True) -> list[TEntity]:
        model_instances = [self.model(**item.dict(exclude_none=True)) for item in data]
        self.session.add_all(model_instances)

        if save:
            self.session.commit()
        else:
            self.session.flush()

        for model_instance in model_instances:
            self.session.refresh(model_instance)
        return convert_models_to_entities(model_instances=model_instances, entity_class=self.entity)

    def update(self, id: int, data: TUpdateSchema, *, save: bool = True) -> TEntity:
        model_instance = self._get_model_instance(id)
        for field, value in data.dict(exclude_none=True).items():
            setattr(model_instance, field, value)

        if save:
            self.session.commit()
            self.session.refresh(model_instance)

        return convert_model_to_entity(model_instance=model_instance, entity_class=self.entity)

    def delete(self, id: int, *, soft: bool = True, save: bool = True):
        model_instance = self._get_model_instance(id)
        if soft:
            model_instance.delete()
        else:
            self.session.delete(model_instance)

        if save:
            self.session.commit()

    def delete_batch(self, ids: list[int] | None = None, *, soft: bool = True, save: bool = True):
        if ids is None:
            ids = []
        filter_params = DeleteBatchFilter(id__in=ids) if ids else Filter()
        model_instances = self.filter(filter_params)
        for model_instance in model_instances:
            self.delete(id=model_instance.id, soft=soft, save=save)
        return ids

    def get(self, id: int) -> TEntity:
        model_instance = self._get_model_instance(id)
        return convert_model_to_entity(model_instance=model_instance, entity_class=self.entity)

    def filter(self, filters: TFilterSchema | None, deleted: bool = False) -> list[TEntity]:
        filtered_query = self.fastapi_filter()
        if filters:
            filtered_query = self.fastapi_filter(**filters.dict(exclude_none=True))
        query = self.session.query(self.model).execution_options(include_deleted=deleted)
        query = filtered_query.filter(query)
        query = filtered_query.sort(query)
        return convert_models_to_entities(model_instances=query.all(), entity_class=self.entity)

    def _get_model_instance(self, id) -> TModel | None:
        return self.session.query(self.model).filter(self.model.id == id).one()
