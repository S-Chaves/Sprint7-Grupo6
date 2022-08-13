from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Nombre de Usuario',
      widget=forms.TextInput(attrs={'class': "form-input", 'placeholder': ' '}))
    dni = forms.CharField(label='DNI',
      widget=forms.TextInput(attrs={'class': "form-input", 'placeholder': ' '}))
    email = forms.CharField(label='Email',
      widget=forms.TextInput(attrs={'class': "form-input", 'placeholder': ' '}))
    password1 = forms.CharField(label='Contraseña',
      widget=forms.PasswordInput(attrs={'class': "form-input", 'placeholder': ' '}))
    password2 = forms.CharField(label='Contraseña (confirmación)',
      widget=forms.PasswordInput(attrs={'class': "form-input", 'placeholder': ' '}))

    class Meta:
        model = User
        fields = [
            'username',
            'dni',
            'email',
            'password1',
            'password2'
            ]