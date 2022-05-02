from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view, *args, **kwargs):
        if request.user.is_superuser:
            return True
        return False


class CodePermission(BasePermission):
    def has_permission(self, request, view):
        if not self.required_permissions:
            return False

        if not request.user.is_authenticated:
            return False

        user_codes = request.user.user_permission.all(
        ).values_list('permission__code', flat=True)
        for code in self.required_permissions:
            if code not in user_codes:
                return False

        return True


def project_permission(required_permissions):
    return type('Permission', (CodePermission,), dict(required_permissions=required_permissions))
