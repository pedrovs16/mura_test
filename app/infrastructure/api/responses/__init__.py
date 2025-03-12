from typing import TypedDict

from fastapi.responses import JSONResponse

from domain.constants.enums.exception_code import ErrorCode


class ErrorDetail(TypedDict):
    error_code: ErrorCode
    message: str


def error_response(status_code: int, content: list[ErrorDetail]) -> JSONResponse:
    return JSONResponse(status_code=status_code, content=content)
