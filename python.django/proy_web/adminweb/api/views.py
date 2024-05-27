from rest_framework import viewsets
from adminweb.models import Producto, DetalleProducto, Cliente, Empleado, Factura
from adminweb.api.serializer import ProductoSerializer, ClienteSerializer, EmpleadoSerializer, FacturaSerializer, DetalleProductoSerializer
from rest_framework.permissions import IsAuthenticated

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class DetalleProductoViewSet(viewsets.ModelViewSet):
    queryset = DetalleProducto.objects.all()
    serializer_class = DetalleProductoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Estoy usando Django REST Framework (DRF) para manejar 
#diferentes metodos HTTP gracias a ¨ModelViewSet"... 
#Con esto se definen automaticamente los metodos sin tener
#que definirlos uno a uno! 

