"""URL Usuarios javigram"""

#From django
from django.urls import path
from django.views.generic import TemplateView
#From users
from users import views

urlpatterns=[

   path(
       route='usuario/<str:usuario>/',
       view=views.DetalleUsuario.as_view(),
       name='detalle'),

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
       view=views.register_views, 
       name='signup'),

   path(
       route='users/edit/profile',
       view=views.edit_views, 
       name='editar_perfil'),
  
]
