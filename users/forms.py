"""Utilizando los forms de Django para la edición del perfil del usuario de Javigram"""

#Django
from django import forms

class RegistroForm(forms.Form):
    """Form de Registro de usuarios en Javigram"""
    usuario = forms.CharField(max_length= 200)
    password = forms.CharField(max_length=10, min_length=5)
    password_confirmation = forms.CharField(max_length=10, min_length=5)

class PerfilForm(forms.Form):
    """Forms de Perfil"""
    website = forms.URLField(max_length=200, required=True)
    biografia = forms.CharField(max_length=500, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    img_perfil = forms.ImageField()