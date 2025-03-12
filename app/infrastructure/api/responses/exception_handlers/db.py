import re
from typing import TYPE_CHECKING

from psycopg2.errors import ForeignKeyViolation, UniqueViolation
from sqlalchemy.exc import IntegrityError, NoResultFound

from infrastructure.api.responses import error_response
from infrastructure.constants.enums.exception_code import GenericErrorCode

if TYPE_CHECKING:
    from fastapi import Request
    from fastapi.responses import JSONResponse


def no_result_found_exception_handler(request: "Request", exc: NoResultFound) -> "JSONResponse":
    error_code = GenericErrorCode.NOT_FOUND
    message = "The instance does not exist."
    return error_response(status_code=404, content=[{"error_code": error_code, "message": message}])


def integrity_exception_handler(request: "Request", exc: IntegrityError) -> "JSONResponse":
    if isinstance(exc.orig, UniqueViolation):
        return _handle_unique_violation(exc)

    if isinstance(exc.orig, ForeignKeyViolation):
        return _handle_foreign_key_violation(exc)

    raise exc


def _handle_unique_violation(e: IntegrityError):
    error_code = GenericErrorCode.UNIQUE_VIOLATION

    match = re.search(r"\((.*?)\)", e.orig.diag.message_detail)
    fields_with_duplicates = match.group(1)
    message = f"An instance with the same '{fields_with_duplicates}' already exists."

    return error_response(status_code=409, content=[{"error_code": error_code, "message": message}])


def _handle_foreign_key_violation(e: IntegrityError):
    error_code = GenericErrorCode.FOREIGN_KEY_VIOLATION

    match = re.search(r"\((.*?)\)=\((.*?)\)", e.orig.diag.message_detail)
    field, value = match.group(1), match.group(2)
    message = f"{field} '{value}' does not exist"
    return error_response(status_code=422, content=[{"error_code": error_code, "message": message}])
