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
   
   path('hola/', local_views.hola_mundo),
   path('sorted/', local_views.orden_numeros),
   path('saludo/<str:nombre>/<int:edad>/', local_views.saludo),

   #path de posts
   path('posts/', views_post.list_posts, name='feed'),
   #Paths de users
   path('users/login/', views_user.login_views, name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
