from django.shortcuts import render, HttpResponse
from servicio.models import *

# Create your views here.

def inicio(request):

    return render(request, 'inicio.html')
