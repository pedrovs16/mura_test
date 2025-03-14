from fastapi import Depends, Response, status
from fastapi_filter import FilterDepends
from fastapi_pagination import Page, Params, paginate
from fastapi_pagination.utils import disable_installed_extensions_check
from fastapi_restful.cbv import cbv
from fastapi_restful.inferring_router import InferringRouter

from domain.entities.order import OrderEntity
from domain.schemas.order import OrderCreateSchema, OrderFilterSchema, OrderUpdateSchema
from domain.use_cases.generic_crud import (
    CreateUseCase,
    DeleteUseCase,
    FilterUseCase,
    GetUseCase,
    UpdateUseCase,
)
from infrastructure.adapters.data.order_sqlalchemy_adapter import OrderSQLAlchemyAdapter
from infrastructure.api.query_filters.order import PaginatedOrderFilter
from infrastructure.api.routers.base import BaseRouter

router = InferringRouter(prefix="/orders", tags=["Orders"])
disable_installed_extensions_check()


@cbv(router)
class OrderRouter(BaseRouter):
    @router.post("/", status_code=status.HTTP_201_CREATED, response_model=OrderEntity)
    async def post_order(self, body: OrderCreateSchema) -> OrderEntity:
        return CreateUseCase(data_port=OrderSQLAlchemyAdapter(self.session)).execute(body)

    @router.put("/{id}", status_code=status.HTTP_200_OK, response_model=OrderEntity)
    async def put_order(self, id: int, body: OrderUpdateSchema) -> OrderEntity:
        return UpdateUseCase(data_port=OrderSQLAlchemyAdapter(self.session)).execute(id, body)

    @router.delete("/{id}", status_code=status.HTTP_200_OK)
    async def delete_order(self, id: int, soft_delete: bool = False):
        return DeleteUseCase(data_port=OrderSQLAlchemyAdapter(self.session)).execute(
            id, soft_delete
        )

    @router.get("/{id}", status_code=status.HTTP_200_OK, response_model=OrderEntity)
    async def get_order(self, id: int) -> OrderEntity:
        return GetUseCase(data_port=OrderSQLAlchemyAdapter(self.session)).execute(id)

    @router.get("/", status_code=status.HTTP_200_OK, response_model=Page[OrderEntity])
    async def filter_orders(
        self,
        response: Response,
        params: Params = Depends(),
        filters: PaginatedOrderFilter = FilterDepends(PaginatedOrderFilter),
    ) -> Page[OrderEntity]:
        non_paginated_filters = OrderFilterSchema(**filters.dict(exclude_none=True))
        entries = FilterUseCase(data_port=OrderSQLAlchemyAdapter(self.session)).execute(
            non_paginated_filters
        )
        paginated_data = paginate(entries, params)
        first = 0
        last = len(paginated_data.items) - 1
        total = paginated_data.total
        response.headers["Content-Range"] = f"orders {first}-{last}/{total}"
        return paginated_data
