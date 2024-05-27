from django.contrib import admin
from adminweb.models import Producto, DetalleProducto, Cliente, Factura, Empleado


admin.site.register(Producto)
admin.site.register(DetalleProducto)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Empleado)
