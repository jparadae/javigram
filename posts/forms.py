"""Nuevo posts en javigram"""

#Django 
from django.forms import ModelForm

#From Posts
from posts.models import Posts

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['usuario','perfil','titulo', 'img_posts']

