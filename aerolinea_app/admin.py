from django.contrib import admin
from .models import Pasajero, Vuelo, Aeropuerto

# Register your models here.
admin.site.register(Vuelo)
admin.site.register(Aeropuerto)
admin.site.register(Pasajero)
