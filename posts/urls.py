"""URL de posts"""
#From Django
from django.urls import path 

#Pssts
from posts import views

urlpatterns = [
     #path de posts
   path(
       route='', 
       view= views.PostsFeedView.as_view(), 
       name='feed'),

   path(
       route='posts/nuevo/', 
       view=views.CreatePostView.as_view(), 
       name='nuevo_post'),

   path(
       route='posts/<int:pk>/',
       view=views.DetallePostView.as_view(),
       name='detalle'),   

 
]