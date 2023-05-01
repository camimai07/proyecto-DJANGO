from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')

def index(request):
    # if(request.method=='GET'):
    #     titulo = 'titulo cuando accedo por GET'
    # else:
    #     titulo = 'Titulo cuando accedo por otro metodo'

    return render(request, 'publica/sitio/index.html')
    # return HttpResponse(f"""
    # <h1>PROYECTO DJANGO - CODO A CODO</h1>
    # <p>{titulo}</p>
    # """)



#def cabecera(request):
#    return render(request, 'publica/sitio/cabecera.html')
def libros(request):
    return render(request, 'publica/sitio/libros.html')

def nosotros(request):
    return render(request, 'publica/sitio/nosotros.html')

def login(request):
    return render(request, 'publica/admin/login.html')

def registro(request):
    return render(request, 'publica/admin/registro.html')

def admin(request):
    return render(request, 'publica/admin/index.html')


def saludar(request,nombre):
    return HttpResponse(f"""
    <h1>Hola {nombre}</h>
    <p>Estoy haciendo una prueba</p>
    """)
