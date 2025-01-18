from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Создание администратора
        self.create_admin_user(
            email="admin@admin.ru",
            first_name="AdminName",
            last_name="AdminLastname",
            username="admin_acc",
            password="admin",
        )

        # Создание обычного пользователя
        self.create_regular_user(
            email="user1@example.com",
            first_name="User",
            last_name="One",
            username="user_one",
            password="userpassword1",
        )

        self.create_regular_user(
            email="user2@example.com",
            first_name="User",
            last_name="Two",
            username="user_two",
            password="userpassword2",
        )

    def create_admin_user(self, email, first_name, last_name, username, password):
        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(password)
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Admin user {username} created successfully.")
        )

    def create_regular_user(self, email, first_name, last_name, username, password):
        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            is_staff=False,
            is_superuser=False,
        )
        user.set_password(password)
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Regular user {username} created successfully.")
        )
