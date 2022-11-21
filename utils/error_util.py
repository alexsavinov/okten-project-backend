from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from enums.error_enum import ErrorEnum


def custom_error_handler(exc: Exception, content) -> Response:
    handlers = {
        'JwtException': _jwt_validate_error,
        'SendEmailException': _sendemail_error
    }
    exc_class = exc.__class__.__name__
    if exc_class in handlers:
        function = handlers[exc_class]
        return function(exc, content)
    response = exception_handler(exc, content)
    return response


def _jwt_validate_error(exc: Exception, content: dict) -> Response:
    print('_jwt_validate_error:')
    print(exc)
    print(content)
    return Response(ErrorEnum.JWT.msg, ErrorEnum.JWT.code)


def _sendemail_error(exc: Exception, content: dict) -> Response:
    # print("_sendemail_error -- exc: ", exc)
    # print("_sendemail_error -- content: ", content)

    # Error 11001 connecting to redis:6379
    return Response(str(exc), status=status.HTTP_503_SERVICE_UNAVAILABLE)
