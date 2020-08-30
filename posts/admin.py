#Registrando el modelo posts en el admin de Django

from django.contrib import admin
from posts.models import Posts

"""Registrando el modelo Perfil de la forma tradicional al admin de django
admin.site.register(Posts)
"""
# Register your models here.
@admin.register(Posts)
class Posts(admin.ModelAdmin):
    """"
    Clase que lista más opciones de un perfil que las de default de django,
    tambien genera listas desplegables para editar inmediatamente sin tener que acceder al elemento
    list_editable = dentro de los elementos de la lista da la opcion de editar sin tener que acceder
    al elemento.
    search_field= busca entre el modelo usuario que extiende del auth de django
    list_filter = proporciona un filtro al modelo registrado 
    fieldset = dispone los campos a mostrar en el admin de perfilusuario segun la doc de django
    """
    list_display = ('pk', 'usuario', 'titulo', 'created_at')
    list_editable =  ('usuario', 'titulo')
