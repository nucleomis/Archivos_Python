#creo esta nueva url para poder enlazar todas las urls de esta aplicacion con la urls.py del proyecto

from django.urls import path
from proyectowebapp.views import *


urlpatterns = [
    path('', inicio, name='inicio'),
]

