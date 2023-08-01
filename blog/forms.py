from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register(UserCreationForm):
    username = forms.CharField(label='Ваше имя',  widget=forms.TextInput(attrs={'class': 'col-lg-4 offset-lg-1'}))
    surname = forms.CharField(label='Ваша фамилия', widget=forms.TextInput(attrs={'class': 'col-lg-4 offset-lg-1'}))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'col-lg-4 offset-lg-1'}))

    class Meta:
        model = User
        fields = ('username', 'surname','phone')