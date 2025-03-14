from logging import config, getLogger

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, NoResultFound

from config import settings
from domain.exceptions.custom_validation import CustomValidationError
from infrastructure.api.responses.exception_handlers import unexpected_exception_handler
from infrastructure.api.responses.exception_handlers.api import request_validation_exception_handler
from infrastructure.api.responses.exception_handlers.custom_validation import (
    custom_validation_handler,
)
from infrastructure.api.responses.exception_handlers.db import (
    integrity_exception_handler,
    no_result_found_exception_handler,
)
from infrastructure.api.responses.exception_handlers.pydantic import (
    pydantic_validation_exception_handler,
)
from infrastructure.api.routers import index
from infrastructure.exceptions.chatgpt import ChatGPTServiceFetchingError

# setup loggers
config.fileConfig("logging.conf", disable_existing_loggers=False)

# get root logger
logger = getLogger(__name__)
logger.info(f"Start of app : {__name__}")


def create_app() -> FastAPI:
    app = FastAPI(title=settings.APP_NAME)
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
    app.include_router(index.router)

    return app


app = create_app()


app.add_exception_handler(Exception, unexpected_exception_handler)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(ValidationError, pydantic_validation_exception_handler)
app.add_exception_handler(NoResultFound, no_result_found_exception_handler)
app.add_exception_handler(IntegrityError, integrity_exception_handler)
app.add_exception_handler(CustomValidationError, custom_validation_handler)
app.add_exception_handler(ChatGPTServiceFetchingError, custom_validation_handler)
