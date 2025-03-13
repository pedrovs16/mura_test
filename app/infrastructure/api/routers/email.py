from fastapi import Depends, Response, status
from fastapi_filter import FilterDepends
from fastapi_pagination import Page, Params, paginate
from fastapi_restful.cbv import cbv
from fastapi_restful.inferring_router import InferringRouter

from domain.entities.email import EmailEntity
from domain.schemas.email import EmailCreateSchema, EmailFilterSchema, EmailUpdateSchema
from domain.use_cases.generic_crud import (
    CreateUseCase,
    DeleteUseCase,
    FilterUseCase,
    GetUseCase,
    UpdateUseCase,
)
from infrastructure.adapters.data.email_sqlalchemy_adapter import EmailSQLAlchemyAdapter
from infrastructure.api.query_filters.email import PaginatedEmailFilter
from infrastructure.api.routers.base import BaseRouter

router = InferringRouter(prefix="/emails", tags=["Emails"])


@cbv(router)
class EmailRouter(BaseRouter):
    @router.post("/", status_code=status.HTTP_201_CREATED, response_model=EmailEntity)
    async def post_email(self, body: EmailCreateSchema) -> EmailEntity:
        return CreateUseCase(data_port=EmailSQLAlchemyAdapter(self.session)).execute(body)

    @router.put("/{id}", status_code=status.HTTP_200_OK, response_model=EmailEntity)
    async def put_email(self, id: int, body: EmailUpdateSchema) -> EmailEntity:
        return UpdateUseCase(data_port=EmailSQLAlchemyAdapter(self.session)).execute(id, body)

    @router.delete("/{id}", status_code=status.HTTP_200_OK)
    async def delete_email(self, id: int, soft_delete: bool = False):
        return DeleteUseCase(data_port=EmailSQLAlchemyAdapter(self.session)).execute(
            id, soft_delete
        )

    @router.get("/{id}", status_code=status.HTTP_200_OK, response_model=EmailEntity)
    async def get_email(self, id: int) -> EmailEntity:
        return GetUseCase(data_port=EmailSQLAlchemyAdapter(self.session)).execute(id)

    @router.get("/", status_code=status.HTTP_200_OK, response_model=Page[EmailEntity])
    async def filter_emails(
        self,
        response: Response,
        params: Params = Depends(),
        filters: PaginatedEmailFilter = FilterDepends(PaginatedEmailFilter),
    ) -> Page[EmailEntity]:
        non_paginated_filters = EmailFilterSchema(**filters.dict(exclude_none=True))
        entries = FilterUseCase(data_port=EmailSQLAlchemyAdapter(self.session)).execute(
            non_paginated_filters
        )
        paginated_data = paginate(entries, params)
        first = 0
        last = len(paginated_data.items) - 1
        total = paginated_data.total
        response.headers["Content-Range"] = f"emails {first}-{last}/{total}"
        return paginated_data
