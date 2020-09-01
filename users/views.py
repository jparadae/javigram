"""Vista login de usuario"""

#Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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
