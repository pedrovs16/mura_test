from typing import TYPE_CHECKING

from fastapi.exceptions import RequestValidationError

from infrastructure.api.responses import error_response
from infrastructure.constants.enums.exception_code import GenericErrorCode

if TYPE_CHECKING:
    from fastapi import Request
    from fastapi.responses import JSONResponse


def request_validation_exception_handler(
    request: "Request", exc: RequestValidationError
) -> "JSONResponse":
    content = []
    # try catching generic (format/type related) errors
    for error in exc.errors():
        message = error["msg"]

        if error["type"] == "value_error.jsondecode":
            error_code = GenericErrorCode.INVALID_JSON
        else:
            problematic_field = error["loc"][1]
            message = f"{problematic_field}: {message}"

            if error["type"] == "value_error.missing":
                error_code = GenericErrorCode.MISSING_FIELD
            else:
                error_code = GenericErrorCode.INVALID_VALUE

        detail = {"error_code": error_code, "message": message}

        content.append(detail)
    return error_response(status_code=400, content=content)
