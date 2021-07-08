from django.urls import path
from . import views

app_name = "aerolinea_app"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:vuelo_id>/', views.vuelo, name = 'vuelo'),
    path('<int:vuelo_id>/reserva', views.reserva, name = 'reserva')
]
