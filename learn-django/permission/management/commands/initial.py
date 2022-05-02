from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        admin, _ = Group.objects.get_or_create(name='Admin')
        instructor, _ = Group.objects.get_or_create(name="Instructor")
        student, _ = Group.objects.get_or_create(name="Student")

        try:
            user = User.objects.get(id=1, is_superuser=True)
            user.groups.add(admin)

        except:
            pass

        print("Groups Added Successfully")
