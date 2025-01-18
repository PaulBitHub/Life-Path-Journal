import secrets

from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm, PasswordRecoveryForm
from users.models import User
from users.utils import send_email_confirm


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:register_message")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_email_confirm(url, user.email)

        messages.success(
            self.request,
            "Ссылка для подтверждения вашего email была отправлена на указанный адрес.",
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Профиль"
        return context


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()

    messages.success(
        request, "Ваш email был успешно подтвержден! Теперь вы можете войти в систему."
    )
    return redirect(reverse("users:login"))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Профиль"
        return context


class RegisterMessageView(TemplateView):
    template_name = "users/register_message.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Профиль"
        return context


class PasswordRecoveryMessageView(TemplateView):
    template_name = "users/password_recovery_message.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Профиль"
        return context


class PasswordRecoveryView(TemplateView):
    model = User
    template_name = "users/password_recovery_form.html"
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy("users:recovery_message")

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        token = secrets.token_hex(10)
        user.set_password(token)
        user.save()

        host = self.request.get_host()
        url = f"http://{host}/users/login/"

        send_mail(
            "Восстановление пароля",
            f"Ваш новый пароль {token}, перейдите по ссылке {url}",
            EMAIL_HOST_USER,
            [user.email],
        )
        return HttpResponseRedirect("/users/password_recovery_message/")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Восстановление пароля"
        return context
