#creo esta nueva url para poder enlazar todas las urls de esta aplicacion con la urls.py del proyecto

from django.urls import path
from . import views
from blog.views import *


urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('autor/<int:autor_id>/', views.autor, name='autor'),
]