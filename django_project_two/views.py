from django.shortcuts import render
from django.urls.conf import path
import datetime

# Create your views here.
def index(request):
    ahora = datetime.datetime.now()
    return render(request, "anionuevo/index.html", {
        "anionuevo": ahora.month == 1 and ahora.day == 1
    })
