from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1")


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "last_name",
            "first_name",
            "avatar",
        )
        widgets = {
            "username": forms.TextInput(attrs={"class": "dr-form__input"}),
            "last_name": forms.TextInput(attrs={"class": "dr-form__input"}),
            "first_name": forms.TextInput(attrs={"class": "dr-form__input"}),
            "email": forms.EmailInput(attrs={"class": "dr-form__input"}),
            "avatar": forms.FileInput(attrs={"class": "blockbtn__dfl-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()


class PasswordRecoveryForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
