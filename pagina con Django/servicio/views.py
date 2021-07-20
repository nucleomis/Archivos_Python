from django.shortcuts import render
from servicio.models import *
# Create your views here.

def servicios(request):

    servicios = Servicio.objects.all()

    return render(request, "servicio/servicio.html", {"servicios": servicios})