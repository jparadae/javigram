#Modelos de Posts

#Django
from django.db import models

#Utilidades

"""class User(models.Model):
    """Creando Modelo Usuario"""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    cumpleanio = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True) #C/vez que se crea una instancia de usuario, añade la fecha
    updated_at = models.DateTimeField(auto_now=True) #C/vez que se modifica añade la fecha actual

    #Modificando la tabla para saber si el usuario es admin, por default no
    es_admin = models.BooleanField(default=False) """

