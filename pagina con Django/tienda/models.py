from os import truncate
from django.db import models

# Create your models here.

#para crear la base de datos: 
#python mange.py makemigration

#para crear el codigo para crear las tablas en la base de datos:
#python manage.py sqlmigrate (nombre de la app) (numero de operacion(que se muestra al hacer el makemigratior))

#para crear las tablas en la base de datos: 
#despues de hacer la migracion, ingresar:
#python manage.py migrate


#metodos:
#-------crear tabla----:
#instanciar la clase en una variable
#Articulo.objects.create(atributo1=..., atributo2=...,etc)

#metodo 2:
#instanciar la clase ej: art1=Articulos()
#darle los valores y despues ejecutar el comando ej:
#art1.save()

#------actualizar:
#ej: 
#art1= Articulo.objects.get(id=1)
#art1.nombre= "marijuana"
#art1.save()

#-------borrar:
#ej:
#art1= Articulo.objects.get(id=1)
#art1.delete()

#------consultar lista:
#ej:
#lista = Articulos.objects.all()
#despues se puede obtener la lista con alguna estuctura repetitiva
#o podes obtener la lista en forma de lista completa de la sig manera
#lista.query.__str__()

#--------consultar por criterio o referencia:
#estas consultas devuelven una lista
#ej:
#Articulos.object.filter(nombre="mesa")
#ej2:
# Articulos.object.filter(seccion="electronica", nombre = "lampara")
#ej3: 
# Articulos.object.filter(nombre="mesa" precio<50)
#para representar este valor ">" en la shell se utiliza __gte
#para representar este valor "<" en la shell se utiliza __lte
#*Para ordenar por un valor en especial equivaliente en sql a orderby
#se usa:
#Articulos.object.filter(nombre="mesa" precio<50).orden_by("precio")
#este metodo ordena de menor a mayor....
#para ordenar de mayor a menor:
#Articulos.object.filter(nombre="mesa" precio<50).order_by("-precio")

class CategoriaPro(models.Model):
    nombre = models.CharField(max_length=50)
    creado = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaPro, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= 'tienda', null = True, blank=True)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)
    creado = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


    def __str__(self):
        return self.nombre

