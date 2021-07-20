#creo esta nueva url para poder enlazar todas las urls de esta aplicacion con la urls.py del proyecto

from django.urls import path
from . import views
from servicio.views import *


urlpatterns = [
    path('servicios/', views.servicios, name='servicios'),
]