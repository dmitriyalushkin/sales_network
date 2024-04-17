from rest_framework.permissions import BasePermission


class IsUserOrActive(BasePermission):
    ''' Является ли пользователь активным '''

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return request.user == view.get_object.user
