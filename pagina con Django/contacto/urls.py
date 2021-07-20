#creo esta nueva url para poder enlazar todas las urls de esta aplicacion con la urls.py del proyecto

from django.urls import path
from . import views
from contacto.views import *


urlpatterns = [
    path('contacto/', views.contacto, name='contacto'),
]
    