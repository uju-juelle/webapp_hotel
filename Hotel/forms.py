from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserEmailForm(UserCreationForm):
    class Meta:
        email = forms.EmailField()
        model = User
        fields = ["email"]