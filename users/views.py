"""Vista login de usuario"""

#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

#Forms
from users.forms import PerfilForm, RegistroForm
from django.urls import reverse, reverse_lazy
#model
from django.contrib.auth.models import User

#Posts
from posts.models import Posts
from users.models import UserProfile

class DetalleUsuario(LoginRequiredMixin, DetailView):
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'usuario'
    template_name = 'users/detalle.html'
    context_object_name='user'

    """Trayendo los posts del usuario"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.get_object()
        context['posts'] = Posts.objects.filter(usuario=usuario).order_by('created_at')
        return context


class RegistroViews(FormView):        
    """Vista que recibe un Form"""
    template_name = 'users/signup.html'
    form_class = RegistroForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Guarda la data del form registroviews"""
        form.save()
        return super().form_valid(form)

class EditarPerfil(UpdateView):
    """Se utiliza UpdateView, vista basada en clase"""
    template_name = 'users/edit_profile.html'
    model = UserProfile
    fields = ['website', 'biografia', 'telefono', 'img_perfil']

    def get_object(self):
        """Retorna el perfil del usuario"""
        return self.request.user.userprofile

    def get_success_url(self):
        """Retorna el perfil"""
        usuario = self.object.usuario.username
        return reverse('users:detalle',kwargs={'usuario': usuario})


class LoginView(auth_views.LoginView):

    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):

    template_name = 'users/logout.html'

