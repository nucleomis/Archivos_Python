from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length= 40)
    imagen = models.ImageField(upload_to = 'servicios') #upload_to lo utlizo para guardar una subcarpeta dentro de la direccion asignada en settings
    fecha_creado = models.DateField(auto_now_add = True)
    fecha_actualizado = models.DateField(auto_now_add= True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo