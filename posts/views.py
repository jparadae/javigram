#Utils from django
from django.shortcuts import render
from django.http import HttpResponse


#From Utils general
from datetime import datetime

#Definiendo var global
posts = [
    {
        'nombre': 'Pepito Falcon',
        'usuario': 'Papito',
        'timestap': datetime.now().strftime('%b %d, %Y -%H:%M hrs'),
        'imagen_publicada': 'https://sites.google.com/site/thesimpsonsxdddddd/_/rsrc/1375821405412/homero/hommer.jpg?height=320&width=258',
    },
    {
        'nombre': 'Juana Falcon',
        'usuario': 'Papito',
        'timestap': datetime.now().strftime('%b %d, %Y -%H:%M hrs'),
        'imagen_publicada': 'https://sites.google.com/site/thesimpsonsxdddddd/_/rsrc/1375821405412/homero/hommer.jpg?height=320&width=258',
    },
    {
        'nombre': 'Ariel Falcon',
        'usuario': 'Papito',
        'timestap': datetime.now().strftime('%b %d, %Y -%H:%M hrs'),
        'imagen_publicada': 'https://sites.google.com/site/thesimpsonsxdddddd/_/rsrc/1375821405412/homero/hommer.jpg?height=320&width=258',
    }
]

# Create your views here.
def list_posts(request):
    content = []
    for post in posts:
        content.append("""
        <p><strong>{nombre}</strong></p>
        <p><small>{usuario}-<i>{timestap}</i></small></p>
        <figure><img src={imagen_publicada}/></strong>
        """.format(**post))

    return HttpResponse('<br>'.join(content))