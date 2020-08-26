#Utils from django
from django.shortcuts import render

#From Utils general
from datetime import datetime

#Definiendo var global
posts = [
    {
        'titulo' : 'Andando1',
        'usuario':  {
        'nombre': 'Pepito Falcon',
        'avatar': '',
        },
        'timestap': datetime.now().strftime('%b %d, %Y -%H:%M hrs'),
        'imagen_publicada': 'https://sites.google.com/site/thesimpsonsxdddddd/_/rsrc/1375821405412/homero/hommer.jpg?height=320&width=258',
    },
    {
        'titulo' : 'Papito',
        'usuario':  {
        'nombre': 'Alex Falcon',
        'avatar': '',
        },
        'timestap': datetime.now().strftime('%b %d, %Y -%H:%M hrs'),
        'imagen_publicada': 'https://sites.google.com/site/thesimpsonsxdddddd/_/rsrc/1375821405412/homero/hommer.jpg?height=320&width=258',
    },
    {
        'titulo' : 'Bob',
        'usuario':  {
        'nombre': 'Patricio Falcon',
        'avatar': '',
        },
        'timestap': datetime.now().strftime('%b %d, %Y -%H:%M hrs'),
        'imagen_publicada': 'https://sites.google.com/site/thesimpsonsxdddddd/_/rsrc/1375821405412/homero/hommer.jpg?height=320&width=258',
    }
]

# Create your views here.
def list_posts(request):
    return render(request, 'feed.html', {'posts': posts})