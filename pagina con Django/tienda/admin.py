
from tienda.models import CategoriaPro, Producto
from django.contrib import admin

# Register your models here.
class CatProducto(admin.ModelAdmin):

    list_display = ("nombre", "actualizacion")
    search_fields = ("nombre",)
    readonly_fields = ("creado", "actualizacion")

class Prod(admin.ModelAdmin):

    list_display = ("nombre", "categoria")
    search_fields = ("nombre", "categoria", "disponible")
    search_fields = ("nombre",)
    readonly_fields = ("creado", "actualizacion")


admin.site.register(Producto, Prod)

admin.site.register(CategoriaPro, CatProducto)