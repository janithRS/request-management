from rest_framework.exceptions import APIException

class BaseException(APIException):
    pass

class IdentityException(BaseException):
    pass