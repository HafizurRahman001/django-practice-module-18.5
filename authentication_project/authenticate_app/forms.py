from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class SignUPForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class UpdateUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','email']