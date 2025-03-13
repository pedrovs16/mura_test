from fastapi_filter.contrib.sqlalchemy import Filter

from domain.schemas.order import OrderFilterSchema
from infrastructure.api.query_filters.common import PaginatedFilter
from infrastructure.models.order import Order


class OrderFilter(OrderFilterSchema, Filter):
    class Config:
        extra = "ignore"

    class Constants(Filter.Constants):
        model = Order


class PaginatedOrderFilter(OrderFilter, PaginatedFilter):
    pass
