from fastapi_filter.contrib.sqlalchemy import Filter


class PaginatedFilter(Filter):
    page: int = 1
    size: int = 50


class DeleteBatchFilter(Filter):
    id__in: list[int | None]
