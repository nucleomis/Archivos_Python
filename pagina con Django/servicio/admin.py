from django.contrib import admin
from servicio.models import *

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    
    readonly_fields = ("fecha_creado", "fecha_actualizado")


admin.site.register(Servicio, ServicioAdmin)