
from django.contrib import admin
from blog.models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    readonly_fields = ("fecha_creado", "fecha_actualizado")

class CatAdmin(admin.ModelAdmin):

    readonly_fields = ("fecha_creado", "fecha_actualizado")


admin.site.register(Post, PostAdmin)

admin.site.register(Categorias, CatAdmin)

