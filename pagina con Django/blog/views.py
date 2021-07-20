from django.shortcuts import render
from blog.models import *
from django.contrib.auth.models import User
# Create your views here.

def blog(request):

    post = Post.objects.all()

    return render(request, 'blog.html', {"posts":post})


def categoria (request, categoria_id):

    cat = Categorias.objects.get(id=categoria_id)

    post = Post.objects.filter(categorias= cat)

    return render(request, "categoria.html", {"categoria":cat, "posts":post})
    

def autor(request, autor_id):

    aut = User.objects.get(id = autor_id)

    post = Post.objects.filter(autor = aut)

    return render( request, "autor.html", {"autor": aut, "posts": post})