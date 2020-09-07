"""javigram URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from javigram import views as local_views
from posts import views as views_post
from users import views as views_user


urlpatterns = [
   path('admin/', admin.site.urls),
   
   path('hola/', local_views.hola_mundo, 'hola_mundo'),
   path('sorted/', local_views.orden_numeros, name ='orden_numeros'),
   path('saludo/<str:nombre>/<int:edad>/', local_views.saludo, name='saludos'),

   #path de posts
   path('', views_post.list_posts, name='feed'),
   path('posts/nuevo/', views_post.nuevo_post, name='nuevo_post'),

   #Paths de users
   path('users/login/', views_user.login_views, name='login'),
   path('users/logout/', views_user.logout_views, name='logout'),
   path('users/signup/', views_user.register_views, name='signup'),
   path('users/edit/profile', views_user.edit_views, name='editar_perfil'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
