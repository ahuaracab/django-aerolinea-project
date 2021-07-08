from django.urls import path
from . import views

app_name = "django_project_three"

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar', views.agregar, name='agregar')
]