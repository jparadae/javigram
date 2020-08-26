
#Django
from django.http import HttpResponse

#Utilidades
from datetime import datetime
import json

def hola_mundo(request):
    """ Fx que Retorna la hora del servidor"""
    now = datetime.now().strftime('%b %d, %Y -%H:%M hrs')
    return HttpResponse('La hora del servidor es {now}'.format(now=str(now)))

def orden_numeros(request):
    """Fx que retorna numeros ordenados en formato json"""
    #Imprimiendo el objeto request
    print(request)
    """importando debbuger pdb de python
    import pdb ; pdb.set_trace()"""
    numeros = [int(i) for i in request.GET['numeros'].split(',')]
    numeros_ordenados = sorted(numeros)
    data = {
        'status' : 'ok',
        'numeros ordenados' : numeros_ordenados,
        'message' : 'Numeros enteros ordenados exitosamente'
    }

    return HttpResponse(json.dumps(data), content_type='application/json') 


def saludo(request, nombre, edad):    
    """Fx que valida si eres mayor de edad para entrar a javigram"""
    if edad < 18:
        message = 'Lo siento {}, no estas autorizado a ingresar'.format(nombre)
    else:
        message = 'Bienvenido {}, a Javigram'.format(nombre)
    return HttpResponse(str(message))   

