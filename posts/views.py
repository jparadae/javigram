#Utils from django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import DetailView

#Forms
from posts.forms import PostForm

#Models
from posts.models import Posts
from users.models import User

#From Utils general
from datetime import datetime

# Create your views here.

class PostsFeedView(LoginRequiredMixin, ListView):
    """Retorna todos los posts publicados"""
    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('created_at')
    paginate_by = 10
    context_object_name = 'posts'


class DetallePost(LoginRequiredMixin, DetailView):
    queryset = Posts.objects.all()
    template_name = 'posts/detalle.html'
    context_object_name='posts'

    



""" Se depreca por usar ListView
@login_required
def list_posts(request):
    posts = Posts.objects.all().order_by('created_at')
    
    return render(request, 'posts/feed.html', {'posts': posts})"""

@login_required
def nuevo_post(request):
    """Para crear un nuevo post en javigram"""
    form_post = PostForm(request.POST or None)

    if request.method == 'POST':
        form_post = PostForm(request.POST, request.FILES)
        if form_post.is_valid():
            print(form_post.cleaned_data)
            form_post.save()
            return redirect('posts:feed')
        else:
            form_post = PostForm()

    return render(
        request = request,
        template_name = 'posts/nuevo_post.html',
        context={
            'usuario': request.user,
            'perfil' : request.user.userprofile,
            'form_post': form_post
            }
        )
    
    