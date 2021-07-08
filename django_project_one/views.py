from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse('<h1 style="color: red">Hola mundo!</h1>')

def harry(request):
    return HttpResponse('Hola Harry')

def hermione(request):
    return HttpResponse('Hola Hermione')

def saludar(request, nombre):
    return HttpResponse(f'Hola {nombre.capitalize()}')

def plantilla(request):
    return render(request, 'hola/block_uno.html')

def saludar_plantilla(request, nombre):
    return render(request, 'hola/saludar_plantilla.html', {
        "nombre": nombre.capitalize()
    })
