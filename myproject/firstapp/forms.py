from django import forms
from .models import Clothe

class ClotheForm(forms.ModelForm):
    class Meta:
        model = Clothe
        fields = [
            'name',
            'description',
            'price',
            'size',
            'photo',
            'is_exists',
            'category',
            'collections'
        ]
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'text-input'}),
            'description': forms.Textarea(attrs={'class': 'text-input'}),
            'price': forms.NumberInput(attrs={'class': 'num-input'}),
            'size': forms.NumberInput(attrs={'class': 'num-input'}),
            'photo': forms.FileInput(attrs={'class': 'file-input'}),
            'is_exists': forms.CheckboxInput(attrs={'class': 'checkbox-input'}),
            'category': forms.Select(attrs={'class': 'select-input'}),
            'collections': forms.SelectMultiple(attrs={'class': 'select-input'})
        }

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'text-input'}),
        min_length=8
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'text-input'}),
        min_length=8
    )

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'text-input'}),
        min_length=8
    )
    email = forms.CharField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'text-input'}),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'text-input'}),
        min_length=8
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'text-input'}),
        min_length=8
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']