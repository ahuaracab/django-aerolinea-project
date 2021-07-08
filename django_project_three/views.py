from django.forms.forms import Form
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

#necesitamos tener las tareas en sesiones
# tareas = ["bañarse", "vestirse", "preparar cosas", "salir"]
class FormAltaTarea(forms.Form):
    tarea = forms.CharField(label="Nueva Tarea")

def index(request):
    if "tareas" not in request.session:
        request.session["tareas"] = []
    return render(request, "tareas/index.html", {
        'tareas': request.session["tareas"]
    }) 

def agregar(request):
    if request.method == "POST":
        form = FormAltaTarea(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data["tarea"]
            request.session["tareas"] += [tarea]
            return HttpResponseRedirect(reverse("django_project_three:index"))
        else:
            return render(request, "tareas/agregar.html", {
                "formulario" : form
            })
    return render(request, "tareas/agregar.html", {
        "formulario" : FormAltaTarea()
    })