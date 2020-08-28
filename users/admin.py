#Registrando el modelo PerfilUsuario en el Admin de Django

#From Django
from django.contrib import admin
from users.models import UserProfile

"""Registrando el modelo Perfil de la forma tradicional al admin de django
admin.site.register(UserProfile)
"""

#Registrando el Perfil en el admin de django de forma custom
@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    """"
    Clase que lista más opciones de un perfil que las de default de django,
    tambien genera listas desplegables para editar inmediatamente sin tener que acceder al elemento
    list_editable = dentro de los elementos de la lista da la opcion de editar sin tener que acceder
    al elemento.
    search_field= busca entre el modelo usuario que extiende del auth de django
    list_filter = proporciona un filtro al modelo registrado 
    """
    list_display = ('pk','usuario', 'website')
    list_links_display = ('usuario')
    list_editable =('usuario','website')
    search_fields = ('usuario__first_name', 'usuario__last_name', 'usuario__username')
    list_filter = ('created_at', 'updated_at')