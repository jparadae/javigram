"""Middleware para un usuario que no tiene completos los datos del perfil de usuario como img_profile y bio"""
#Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileUserCompleteMiddleware:
    """Si un usuario no tiene completo los datos del perfil es redirigido a users/edit/profile para
    completar los datos y seguir utilizando javigram"""


    def __init__(self, get_response):
        """
          Middleware de inicialización
        """    
        self.get_response = get_response

    def __call__(self, request):
        """
        1. Valido que un usuario no este ingresando como anonimo
        """    
        if not request.user.is_anonymous:
            """if not request.user.userprofile:
                print('No tiene nada Perfil, entonces lo envio a crear uno')
                return redirect('edit_profile')
            else:
                print('si tiene, entonces ')"""
            perfil = request.user.userprofile
            if not perfil.img_perfil or not perfil.biografia:
                if request.path not in [reverse('edit_profile'), reverse('logout')]:
                    return redirect('edit_profile')
        response = self.get_response(request)
        return response


    