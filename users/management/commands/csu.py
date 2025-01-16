from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(email='admin2@admin.ru',
                                   first_name='admin_name',
                                   last_name='admin_lastname',
                                   username='admin_acc',
                                   is_staff=True,
                                   is_superuser=True,
                                   )

        user.set_password('admin')
        user.save()
