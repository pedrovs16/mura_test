from fastapi_filter.contrib.sqlalchemy import Filter

from domain.schemas.email import EmailFilterSchema
from infrastructure.api.query_filters.common import PaginatedFilter
from infrastructure.models.email import Email


class EmailFilter(EmailFilterSchema, Filter):
    class Config:
        extra = "ignore"

    class Constants(Filter.Constants):
        model = Email


class PaginatedEmailFilter(EmailFilter, PaginatedFilter):
    pass
