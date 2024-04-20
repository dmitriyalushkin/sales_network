from rest_framework.permissions import BasePermission


class IsUserOrActive(BasePermission):
    ''' Является ли пользователь активным '''

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return request.user == view.get_object.user


class CustomUpdatePermission(BasePermission):
    ''' Пользователь не может обновлять задолженность '''

    def has_permission(self, request, view):
        if view.action == 'update' and view.kwargs['arrears'] != request.user.arrears:
            return False
        return True
