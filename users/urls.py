from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from django.urls import path

from users.views import (
    UserCreateView,
    email_verification,
    ProfileView,
    RegisterMessageView,
    PasswordRecoveryView,
    PasswordRecoveryMessageView,
)

app_name = UsersConfig.name


urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email_confirm/<str:token>/", email_verification, name="email_confirm"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("register/message/", RegisterMessageView.as_view(), name="register_message"),
    path(
        "password_recovery/", PasswordRecoveryView.as_view(), name="password_recovery"
    ),
    path(
        "password_recovery_message/",
        PasswordRecoveryMessageView.as_view(),
        name="recovery_message",
    ),
    path("profile/", ProfileView.as_view(), name="profile"),
]
