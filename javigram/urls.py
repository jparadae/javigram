"""javigram URL Configuration"""
from django.contrib import admin
from django.urls import path
from javigram import views as local_views

from posts import views as views_post
urlpatterns = [
   # path('admin/', admin.site.urls),
   path('hola/', local_views.hola_mundo),
   path('sorted/', local_views.orden_numeros),
   path('saludo/<str:nombre>/<int:edad>/', local_views.saludo),

   #path de posts
   path('posts/', views_post.list_posts)
]
