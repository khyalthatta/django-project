from django.contrib import admin

from .models import UserPermission, ProjectPermission

admin.site.register(UserPermission)
admin.site.register(ProjectPermission)
