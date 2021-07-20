"""tiendaonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tienda.views import tienda
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto/', include('proyectowebapp.urls')),
    path('servicio/', include('servicio.urls')),
    path('', include('blog.urls')),
    path('', include('contacto.urls')),
    path('', include('tienda.urls')),
    path('', include('carro.urls')),
    
    #con include() hago un subdirectorio para poder importar el urls de la aplicacion al urls del proyecto

] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    #con este metodo incluto todos los documentos como imagenes y demas en la carperta static

