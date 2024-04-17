from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='petrov@sky.pro',
            first_name='Petr',
            last_name='Petrov',
            is_staff=True,
            is_superuser=True,
            is_active=False
        )

        user.set_password('123456')
        user.save()
