from dataclasses import dataclass

from domain.constants.enums.exception_code import ErrorCode


@dataclass
class CustomValidationError(Exception):
    message: str
    code: ErrorCode

    def __init__(self):
        super().__init__(self.message, self.code)

    def __str__(self):
        return self.message
