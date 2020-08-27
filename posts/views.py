#Utils from django
from django.shortcuts import render

#From Utils general
from datetime import datetime

#Definiendo var global
posts = [
    {
        'titulo' : 'Andando1',
        'usuario':  {
        'nombre': 'Macarena Falcon',
        'avatar': 'https://i.pinimg.com/originals/19/87/90/198790eb7e08830027c1ae1686496c72.png',
        },
        'timestap': datetime.now().strftime('%b %d, %Y -%H:%M hrs'),
        'imagen_publicada': 'https://serturista.com/wp-content/uploads/2010/09/cerro-san-cristobal-1.jpg',
    },
    {
        'titulo' : 'Papito',
        'usuario':  {
        'nombre': 'Alex Falcon',
        'avatar': 'https://images.vexels.com/media/users/3/140748/isolated/preview/5b078a59390bb4666df98b49f1cdedd0-perfil-masculino-avatar-by-vexels.png',
        },
        'timestap': datetime.now().strftime('%b %d, %Y -%H:%M hrs'),
        'imagen_publicada': 'https://www.researchgate.net/profile/Juan_Manuel_Del_Castillo/publication/330880053/figure/fig3/AS:726348431638529@1550186369549/Figura-6-Maqueta-del-cerro-Cuncacucho-con-la-fortaleza-en-la-cima-y-el-tambo-inca-al.png',
    },
    {
        'titulo' : 'Bob',
        'usuario':  {
        'nombre': 'Patricio Falcon',
        'avatar': 'https://cdn.pixabay.com/photo/2020/07/14/13/07/icon-5404125_960_720.png',
        },
        'timestap': datetime.now().strftime('%b %d, %Y -%H:%M hrs'),
        'imagen_publicada': 'https://laderasur.com/content/uploads/2019/12/cerro-provincia-por-gabriel-fuentes-5.jpg',
    }
]

# Create your views here.
def list_posts(request):
    return render(request, 'feed.html', {'posts': posts})