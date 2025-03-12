from fastapi import APIRouter

from infrastructure.api.routers.order import router as order_router

router = APIRouter()

routers = [order_router]

for r in routers:
    router.include_router(r)
