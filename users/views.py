"""Vista login de usuario"""

#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from django.contrib.auth.models import User

from django.db.utils import IntegrityError
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
            return redirect('feed')
         # A backend authenticated the credentials
        else:
            return render(request, 'users/login.html', {'error': 'Credenciales de usuario invalidas'})
         # No backend authenticated the credentials

    return render(request, 'users/login.html') 

def register_views(request):
    """Función que registra a un usuario en Javigram"""
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['password']
        password_confirmation = request.POST['confirma_password']
        print(username, password, password_confirmation)
        if password != password_confirmation:
            return render(request,'users/signup.html', {'error':'Las constraseñas no coinciden'})
        try:
            user = User.objects.create_user(username=username, password=password)  
        except IntegrityError: 
            return render(request, 'users/signup.html', {'error': 'El nombre de usuario ya existe, intente otro por favor'})    

        user.nombre = request.POST['nombre']
        user.apellido = request.POST['apellido']
        user.email = request.POST['email']
        user.save()

        perfil_usr = UserProfile(usuario=user) 
        perfil_usr.save()
        return redirect('login')  
    return render(request, 'users/signup.html')    

@login_required
def logout_views(request):
    logout(request)
    return render(request, 'users/login.html')