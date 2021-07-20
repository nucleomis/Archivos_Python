#creo esta nueva url para poder enlazar todas las urls de esta aplicacion con la urls.py del proyecto

from django.urls import path
from carro import views
from carro.views import *


urlpatterns = [
    path('carro/', views.agregar_producto, name='carro'),
]