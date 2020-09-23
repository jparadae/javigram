"""Vista login de usuario"""

#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

#Forms
from users.forms import PerfilForm, RegistroForm
from django.urls import reverse
#model
from django.contrib.auth.models import User

class DetalleUsuario(DetailView):
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'usuario'
    template_name = 'users/detalle.html'


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



def register_views(request):
    """Función que registra a un usuario en Javigram"""
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
    

@login_required
def edit_views(request):
    """vista para editar los perfiles de usuarios incompletos, utilizando los forms de django
     -Se instancia al perfil para ser editado 
    """
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

@login_required
def logout_views(request):
    logout(request)
    return render(request, 'users/login.html')