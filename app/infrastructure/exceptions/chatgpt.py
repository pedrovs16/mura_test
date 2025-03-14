from domain.exceptions.custom_validation import CustomValidationError
from infrastructure.constants.enums.exception_code import GenericErrorCode


class ChatGPTServiceFetchingError(CustomValidationError):
    message = "An error occurred while fetching data from the ChatGPT service"
    code = GenericErrorCode.CHATGPT_ERROR
