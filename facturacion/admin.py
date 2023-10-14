from django.contrib import admin
from facturacion.models import *

# Register your models here.
admin.site.register(Libro)
admin.site.register(Linea)
admin.site.register(Factura)
admin.site.register(Pedido)