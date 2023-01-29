from rest_framework import permissions

from exceptions import BadRequest
from exceptions import AccessForbidden
from exceptions import UnauthorizedAccess

from accounts.models import ProjectUser


class IsAuthenticated(permissions.BasePermission):
    """Check if the user is Authenticated."""
    def has_permission(self, request, view):
        user_id = request.META.get('HTTP_USER_ID')
        if not user_id:
            raise BadRequest("Can not find User-id in the request header.")

        try:
            user = ProjectUser.objects.get(id=user_id)
        except:
            raise UnauthorizedAccess("Invalid User-id, please re login")
        view.kwargs['user'] = user

        return True
