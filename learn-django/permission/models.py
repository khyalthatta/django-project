from django.db import models
from django.contrib.auth.models import User


class ProjectPermission(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class UserPermission(models.Model):
    user = models.ForeignKey(User, models.CASCADE,
                             related_name='user_permission')
    permission = models.ForeignKey(
        ProjectPermission, on_delete=models.CASCADE, related_name='user_userpermission')

    def __str__(self):
        return self.user.username
