from typing import TYPE_CHECKING

from infrastructure.api.responses import error_response
from infrastructure.constants.enums.exception_code import GenericErrorCode

if TYPE_CHECKING:
    from fastapi import Request
    from fastapi.responses import JSONResponse


def unexpected_exception_handler(request: "Request", exc: Exception) -> "JSONResponse":
    error_code = GenericErrorCode.UNEXPECTED_ERROR
    message = "An unexpected error occured. Please contact the administrator."
    return error_response(status_code=500, content=[{"error_code": error_code, "message": message}])
