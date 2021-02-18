from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Chats, CuentaU, Mensajes

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class CreateCuenta(forms.ModelForm):

    class Meta:
        model = CuentaU
        fields = [
            'username',
            'foto',
            'estado',
        ]
        labels = {'username':'Nombre de usuario','foto':'Foto', 
        'estado':'Estado'}