"""Utilizando los forms de Django para la edición del perfil del usuario de Javigram"""

#Django
from django import forms

#Models
from django.contrib.auth.models import User
from users.models import UserProfile


"""Aqui ira el formulario de Registro de usuario"""
class RegistroForm(forms.Form):
    """Form sign up user"""
    username = forms.CharField(max_length= 50, min_length=4)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=10, widget=forms.PasswordInput())
    nombre = forms.CharField(max_length=50, min_length=5)
    apellido = forms.CharField(max_length=50, min_length=5)
    email = forms.CharField(max_length=20, min_length=5, widget=forms.EmailInput())
     
    def clean_usuario(self):
        """Funcion que valida si un usuario existe"""
        username = self.cleaned_data['username']
        usuarioExiste = User.objects.filter(username=username).exist()
        if usuarioExiste:
            raise ValidationError("El usuario ya existe!") 
            
        return username

    def clean(self):
        """clean se utiliza para validar campos que dependen de otros
        como lo es pass y pass_confirm, validando que los campos sean iguales""" 
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")   
        
        if password != password_confirmation:
            raise ValidationError("Las contraseñas no coinciden, intentalo nuevamente")
        
        return cleaned_data

    def save(self):
        """Fx que guarda los datos del perfil, data pop elimina elementos al momento de guardar"""
        if self.errors:
            raise ValueError('No se que pasa')
        else:
            cleaned_data = self.cleaned_data
            cleaned_data.pop('password_confirmation')
            usuario = User.objects.create_user(**cleaned_data)
            perfil = UserProfile(users=usuario)
            perfil.save()

        

class PerfilForm(forms.Form):
    """Forms de Perfil"""
    website = forms.URLField(max_length=200, required=True)
    biografia = forms.CharField(max_length=500, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    img_perfil = forms.ImageField()