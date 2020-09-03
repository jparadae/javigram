"""Utilizando los forms de Django para la edición del perfil del usuario de Javigram"""

#Django
from django import forms

class PerfilForms(forms.Form):

    website = forms.CharField(label='Website', max_length=100)