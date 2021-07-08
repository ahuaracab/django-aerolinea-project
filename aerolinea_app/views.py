from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Pasajero, Vuelo
from django.urls import reverse 

# Create your views here.
def index(request):
    return render(request, 'vuelos/index.html', {
        "lista_vuelos": Vuelo.objects.all()
    })

def vuelo(request, vuelo_id):
    vuelo = Vuelo.objects.get(id=vuelo_id)
    pasajeros = vuelo.pasajeros.all()
    no_son_pasajeros = Pasajero.objects.exclude(vuelos=vuelo).all()
    return render(request, "vuelos/vuelo.html", {
        "vuelo" : vuelo,
        "pasajeros": pasajeros,
        "no_son_pasajeros": no_son_pasajeros
    }) 

def reserva(request, vuelo_id):

    if request.method == "POST":
        vuelo = Vuelo.objects.get(pk=vuelo_id)
        pasajero_id = int(request.POST["pasajero"])
        pasajero = Pasajero.objects.get(pk=pasajero_id)
        pasajero.vuelos.add(vuelo)
        return HttpResponseRedirect(reverse("aerolinea_app:vuelo", args=(vuelo.id,)))
