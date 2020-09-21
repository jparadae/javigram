"""javigram URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from javigram import views as local_views
from posts import views as views_post
from users import views as views_user


urlpatterns = [
   path('admin/', admin.site.urls),
   
   ##vistas basadas en class
   path('', include(('posts.urls','posts'), namespace='posts')),

   #Paths de users
   path('users', include(('users.urls', 'users'), namespace='users')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
