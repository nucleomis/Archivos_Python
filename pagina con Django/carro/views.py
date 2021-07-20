from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect
# Create your views here.

def agregar_producto(request, id_producto):

    carro = Carro(request)

    id = id_producto

    producto  = Producto.objects.get(id)    

    carro.agregar(producto = producto)

    return redirect('tienda')

def eliminar_producto(request, id_producto):

    carro = Carro(request)

    id = id_producto

    producto  = Producto.objects.get(id)    

    carro.eliminar(producto = producto)

    return redirect('tienda')

def restar_producto(request, id_producto):

    carro = Carro(request)

    id = id_producto

    producto  = Producto.objects.get(id)    

    carro.restar(producto = producto)

    return redirect('tienda')

def guardar_producto(request, id_producto):

    carro = Carro(request)

    id = id_producto

    producto  = Producto.objects.get(id)    

    carro.guardar(producto = producto)

    return redirect('tienda')

def limpiar_producto(request):
    carro = Carro(request)

    carro.limpiar()

    return redirect('tienda')