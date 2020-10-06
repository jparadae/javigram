"""Vista login de usuario"""

#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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





"""Se Depreca por RegisterView Función que registra a un usuario en Javigram"""
"""
def register_views(request):
   
    form = RegistroForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('login')
        else:
            form = RegistroForm()

    return render(
    request = request,
    template_name='users/signup.html', 
    context={'form': form})  
"""

# Create your views here.
def login_views(request):
    """
    Función que valida si un usuario esta logeado en Javigram, mediante un post,  utilizando el method authenticate de django
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) 
        print(username, password, request)
        if user:
            login(request, user)
            return redirect('posts:feed')
         # A backend authenticated the credentials
        else:
            return render(request, 'users/login.html', {'error': 'Credenciales de usuario invalidas'})
         # No backend authenticated the credentials

    return render(request, 'users/login.html') 

"""vista para editar los perfiles de usuarios incompletos, utilizando los forms de django
     -Se instancia al perfil para ser editado 
"""

"""    

@login_required
def edit_views(request):
    
    try:
        perfil = request.user.userprofile
    except:
        print("Ocurrio un error baby")
        perfil = None
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            datos_formulario = form.cleaned_data
            perfil.website = datos_formulario['website']
            perfil.biografia = datos_formulario['biografia']
            perfil.telefono = datos_formulario['telefono']
            perfil.img_perfil = datos_formulario['img_perfil']
            perfil.save()
            url = reverse('users:detalle', kwargs={'usuario': request.user.username})
            return redirect(url)
    else:
        form = PerfilForm()   
       
    
    return render(request, 'users/edit_profile.html', 
    context={
     'perfil': perfil,
     'user' : request.user,
     'form' : form
    })
"""
@login_required
def logout_views(request):
    logout(request)
    return render(request, 'users/login.html')