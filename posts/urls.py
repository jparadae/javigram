"""URL de posts"""
#From Django
from django.urls import path 

#Pssts
from posts import views

urlpatterns = [
     #path de posts
   path(
       route='', 
       view= views.list_posts, 
       name='feed'),

   path(
       route='posts/nuevo/', 
       view=views.nuevo_post, 
       name='nuevo_post'),
]