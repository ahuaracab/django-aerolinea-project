from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola, name="hola"),
    path('harry', views.harry, name="harry"), #solo el nombre de la función de view debe ir en views.harry
    path('hermione', views.hermione, name="hermione"),
    path('saludar/<str:nombre>', views.saludar, name="saludar"),
    path('plantilla', views.plantilla, name="plantilla"),
    path('saludar_plantilla/<str:nombre>', views.saludar_plantilla, name="saludar_plantilla")    
]