from typing import TYPE_CHECKING

from domain.exceptions.custom_validation import CustomValidationError
from infrastructure.api.responses import error_response

if TYPE_CHECKING:
    from fastapi import Request
    from fastapi.responses import JSONResponse


def custom_validation_handler(request: "Request", exc: CustomValidationError) -> "JSONResponse":
    status_code = 422
    message = exc.message
    error_code = exc.code
    return error_response(
        status_code=status_code, content=[{"error_code": error_code, "message": message}]
    )
