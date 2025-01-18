from django import forms

from diary.models import Diary


class DiaryForm(forms.ModelForm):
    cd_date = forms.DateField(
        localize=True,
        widget=forms.DateInput(
            format="%Y-%m-%d", attrs={"class": "dr-form__input_date", "type": "date"}
        ),
    )

    class Meta:
        model = Diary
        exclude = ("owner",)
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "drpc-title input_diary", "placeholder": "Привет!"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "drpc text",
                    "placeholder": "Напиши что-нибудь интересное...",
                    "rows": 2,
                }
            ),
            "image": forms.FileInput(attrs={"class": "blockbtn__dfl-input"}),
        }
