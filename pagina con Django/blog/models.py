from django.db import models
from django.contrib.auth.models import User #esta importacio la utilizo para poder usar los usuarios como autores de los post


# Create your models here.


class Categorias(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_creado = models.DateField(auto_now_add = True)
    fecha_actualizado = models.DateField(auto_now_add= True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre    

class Post(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length= 40)
    imagen = models.ImageField(upload_to = 'blog', null=True, blank=True) #upload_to lo utlizo para guardar una subcarpeta dentro de la direccion asignada en settings
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categorias)
    fecha_creado = models.DateField(auto_now_add = True)
    fecha_actualizado = models.DateField(auto_now_add= True)

    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo

