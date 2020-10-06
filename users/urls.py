"""URL Usuarios javigram"""

#From django
from django.urls import path
from django.views.generic import TemplateView
#From users
from users import views

urlpatterns=[

   path(
       route='users/login/', 
       view=views.login_views, 
       name='login'),

   path(
       route='users/salir/', 
       view=views.logout_views, 
       name='salir'),

   path(
       route= 'users/signup/', 
       view=views.RegistroViews.as_view(), 
       name='signup'),

   path(
       route='users/edit/profile',
       view=views.EditarPerfil.as_view(), 
       name='editar_perfil'),

    #Django resuelve por orden las urls
    
    path(
       route='usuario/<str:usuario>/',
       view=views.DetalleUsuario.as_view(),
       name='detalle'),   
  
]
