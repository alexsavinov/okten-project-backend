from enum import Enum

from rest_framework import status


class ErrorEnum(Enum):
    JWT = ('Token invalid or expired', status.HTTP_400_BAD_REQUEST)

    def __init__(self, msg, code=status.HTTP_400_BAD_REQUEST) -> None:
        self.msg = msg
        self.code = code
