#creo esta nueva url para poder enlazar todas las urls de esta aplicacion con la urls.py del proyecto

from django.urls import path
from . import views
from tienda.views import *


urlpatterns = [
    path('tienda/', views.tienda, name='tienda'),
    path('categoriapro/<int:categoria_id>/', views.categoriapro, name='categoriapro'),
    path('descripcion/<int:producto_id>/', views.descripcion, name='descripcion'),
]