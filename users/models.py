from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = models.CharField(max_length=100, verbose_name="Никнейм")
    email = models.EmailField(unique=True, verbose_name="Почта")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия", **NULLABLE)
    first_name = models.CharField(max_length=100, verbose_name="Имя", **NULLABLE)
    avatar = models.ImageField(
        upload_to="users/avatar/", verbose_name="Аватар", **NULLABLE
    )
    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.username} {self.last_name} {self.first_name} {self.email} "
