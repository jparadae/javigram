"""Utilizando los forms de Django para la edición del perfil del usuario de Javigram"""

#Django
from django import forms

#Models
from django.contrib.auth.models import User

class RegistroForm(forms.Form):
    """Form de Registro de usuarios en Javigram"""
    username = forms.CharField(max_length= 50, min_length=4)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=10, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=50, min_length=5)
    last_name = forms.CharField(max_length=50, min_length=5)
    email = forms.CharField(max_length=20, min_length=5, widget=forms.EmailInput())
     
    def clean_usuario(self):
        """Funcion que valida si un usuario existe en Javigram"""
        usuario = self.cleaned_data['username']
        usuarioExiste = User.objects.filter(username=usuario).exist()
        if usuarioExiste:
            raise ValidationError("El usuario ya existe en Javigram!") 
            
        return usuario

    def clean(self):
        """clean se utiliza para validar campos que dependen de otros
        como lo es pass y pass_confirm, validando que los campos sean iguales""" 
        cleaned_data = super()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")   
        
        if password != password_confirmation:
            raise ValidationError("Las contraseñas no coinciden, intentalo nuevamente")
        
        return data

class PerfilForm(forms.Form):
    """Forms de Perfil"""
    website = forms.URLField(max_length=200, required=True)
    biografia = forms.CharField(max_length=500, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    img_perfil = forms.ImageField()