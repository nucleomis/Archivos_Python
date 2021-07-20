from django.shortcuts import render
from tienda.models import *
# Create your views here.

def tienda(request):

    post = Producto.objects.all()

    return render(request, "tienda.html", {"posts": post})


def categoriapro (request, categoria_id):

    categorias = CategoriaPro.objects.all()

    cat = CategoriaPro.objects.get(id=categoria_id)

    producto = Producto.objects.filter(categoria= cat)

    return render(request, "categoriapro.html", {"categoria":cat, "producto":producto, "categorias": categorias})

def descripcion(request, producto_id):

    producto = Producto.objects.get(id=producto_id)

    return render(request, "descripcion.html")