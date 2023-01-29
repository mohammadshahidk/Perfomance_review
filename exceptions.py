"""Exceptions which used in Apps."""

from rest_framework.exceptions import APIException


class BadRequest(APIException):
    """Request method is invalid."""

    status_code = 400
    default_detail = 'Request details are invalid.'
    default_code = 'bad_request'


class UnauthorizedAccess(APIException):
    """user Authorization failed."""

    status_code = 401
    default_detail = 'User is not authorized to access.'
    default_code = 'unauthorized_access'


class AccessForbidden(APIException):
    """User is not allowed to access."""

    status_code = 403
    default_detail = 'User access is forbidden.'
    default_code = 'access_forbidden'
