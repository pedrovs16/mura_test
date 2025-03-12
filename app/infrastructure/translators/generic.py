from typing import TypeVar

from sqlalchemy import Column

from infrastructure.db import Base

Entity = TypeVar("Entity")


def convert_model_to_entity(model_instance: Base, entity_class: type[Entity]) -> Entity:
    entity_dict = {}

    for key, value in model_instance.__table__.columns.items():
        # skip private attributes and callables (methods)
        if key.startswith("_") or callable(value):
            continue

        if isinstance(value, Column):
            column_value = getattr(model_instance, key)
            entity_dict[key] = column_value

    return entity_class(**entity_dict)


def convert_models_to_entities(
    model_instances: list[Base], entity_class: type[Entity]
) -> list[Entity]:
    entities = []

    for model_instance in model_instances:
        entities.append(convert_model_to_entity(model_instance, entity_class))

    return entities
