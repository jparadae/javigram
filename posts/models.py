#Modelos de Posts

#Django
from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
#Utilidades

class Posts(models.Model):
    """Creando Modelo posts
    Este extendera del modelo de usuario, y del modelo Profile, y 
    si un usuario es eliminado se eliminará en cascada el contenido de posts
    -Será registrado en el admin de django de forma custom
    """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    perfil = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    titulo = models.CharField(max_length=255)
    img_posts = models.ImageField(upload_to='posts/img_posts', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True) #C/vez que se crea una instancia de usuario, añade la fecha
    updated_at = models.DateTimeField(auto_now=True) #C/vez que se modifica añade la fecha actual
    
    def __str__(self):
        """Fx string que retorna el titulo de la img posteada"""      
        return '{} por @{}'.format(self.titulo, self.usuario.username)


