from fastapi import APIRouter

from infrastructure.api.routers.order import router as order_router
from infrastructure.api.routers.email import router as email_router

router = APIRouter()

routers = [order_router, email_router]

for r in routers:
    router.include_router(r)
