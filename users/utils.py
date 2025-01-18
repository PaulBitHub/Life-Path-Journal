from django.core.mail import send_mail
from string import ascii_letters, digits
from random import choices

from config.settings import EMAIL_HOST_USER


def send_email_confirm(url, email):
    send_mail(
        subject="Подтвержение регистрации в магазине МЕЧТА",
        message=f"Для подтверждения регистрации, перейдите по ссылке {url}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
    )


def send_email_reset_password(password, email):
    send_mail(
        subject="Сброс пароля в магазине МЕЧТА",
        message=f"Новый пароль {password}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
    )


def generate_random_password():
    data = ascii_letters + digits
    return "".join(choices(data, k=8))
