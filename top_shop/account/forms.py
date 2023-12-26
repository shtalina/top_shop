from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Импортируем стандартную модель пользователя

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User  # Используем стандартную модель пользователя
        fields = ('username', 'email', 'phone_number', 'address', 'password1', 'password2')

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')