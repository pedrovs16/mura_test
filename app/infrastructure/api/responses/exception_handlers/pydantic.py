from typing import TYPE_CHECKING

from pydantic import ValidationError

from infrastructure.api.responses import error_response
from infrastructure.constants.enums.exception_code import GenericErrorCode

if TYPE_CHECKING:
    from fastapi import Request
    from fastapi.responses import JSONResponse


def pydantic_validation_exception_handler(
    request: "Request", exc: ValidationError
) -> "JSONResponse":
    expected_errors_content = []

    for error in exc.errors():
        if error["type"] == "value_error":
            detail = {"error_code": GenericErrorCode.INVALID_VALUE, "message": error["msg"]}
            expected_errors_content.append(detail)

    if expected_errors_content:
        return error_response(status_code=400, content=expected_errors_content)
    raise exc
