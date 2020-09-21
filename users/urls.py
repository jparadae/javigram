"""URL Usuarios javigram"""

#From django
from django.urls import path
from django.views.generic import TemplateView
#From users
from users import views

urlpatterns=[

   #Detalle Perfil Usuario 
   
   path(
       route='<str:username>',
       view=TemplateView.as_view(template_name='users/detalle'),
       name='detalle'),

   path(
       route='users/login/', 
       view=views.login_views, 
       name='login'),

   path(
       route='users/logout/', 
       view=views.logout_views, 
       name='logout'),

   path(
       route= 'users/signup/', 
       view=views.register_views, 
       name='signup'),

   path(
       route='users/edit/profile',
       view=views.edit_views, 
       name='editar_perfil'),
  
]
