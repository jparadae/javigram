# Modelo Perfil Usuario, extiendo del model usuario.

#From Django
from django.db import models
from django.contrib.auth.models import User

#Utilidades

class UserProfile(models.Model):
    """Esta clase extiende del modelo de Usuario, utilizando proxy,
    model para añadir otros datos necesario para crear el perfil del usuario"""

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    website = models.URLField(max_length=200,blank=True)
    biografia = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    img_perfil = models.ImageField(upload_to='users/picture', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Retorno el nombre del usuario"""
        return self.usuario.username
    
    


