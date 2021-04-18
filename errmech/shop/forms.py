from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'input login__input', 'autocomplete': 'off'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'input login__input'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'input login__input'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'input login__input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'input login__input', 'autocomplete': 'none'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'input login__input'}))
