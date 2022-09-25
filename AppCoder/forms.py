from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class FormularioCurso (forms.Form):
    
    curso = forms.CharField()
    camada = forms.IntegerField()


class FormularioProfe(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    profesion = forms.CharField()


class FormularioRegistro(UserCreationForm):

    email = forms.EmailField(label="Ingrese su correo")
    password1 = forms.CharField(label="Ingrese una constraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repita la constraseña", widget = forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username" , "email" , "password1" , "password2"] # debe haber tantos campos como variables cree anteriormente y se debe respetar el orden