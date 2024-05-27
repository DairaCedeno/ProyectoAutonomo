from django.test import TestCase
from .models import Empleado, Producto, DetalleProducto, Factura, Cliente

class EmpleadoModelTest(TestCase):
    def setUp(self):
        self.empleado = Empleado.objects.create(nombre="Juan", apellido="Pérez", telefono="123456789")
        
    def test_empleado_creation(self):
        self.assertEqual(self.empleado.nombre, "Juan")
        self.assertEqual(self.empleado.apellido, "Pérez")
        self.assertEqual(self.empleado.telefono, "123456789")

    def test_empleado_str(self):
        self.assertEqual(str(self.empleado), "Juan Pérez")

class ProductoModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(nombre="Laptop", descripcion="Laptop de alta gama", precio=1500.00, stock=10, categoria="Electrónica")

    def test_producto_creation(self):
        self.assertEqual(self.producto.nombre, "Laptop")
        self.assertEqual(self.producto.descripcion, "Laptop de alta gama")
        self.assertEqual(self.producto.precio, 1500.00)
        self.assertEqual(self.producto.stock, 10)
        self.assertEqual(self.producto.categoria, "Electrónica")

    def test_producto_str(self):
        self.assertEqual(str(self.producto), "Laptop")

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Ana", apellido="García", cedula="123456789", telefono="987654321")

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nombre, "Ana")
        self.assertEqual(self.cliente.apellido, "García")
        self.assertEqual(self.cliente.cedula, "123456789")
        self.assertEqual(self.cliente.telefono, "987654321")

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), "Ana García")


class DetalleProductoModelTest(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(nombre="Laptop", descripcion="Laptop de alta gama", precio=1500.00, stock=10, categoria="Electrónica")
        self.cliente = Cliente.objects.create(nombre="Ana", apellido="García", cedula="123456789", telefono="987654321")
        self.empleado = Empleado.objects.create(nombre="Juan", apellido="Pérez", telefono="123456789")
        self.factura = Factura.objects.create(cliente=self.cliente, empleado=self.empleado, total=2000.00)
        self.detalle = DetalleProducto.objects.create(producto=self.producto, factura=self.factura, cantidad=1)

    def test_detalle_producto_creation(self):
        self.assertEqual(self.detalle.producto, self.producto)
        self.assertEqual(self.detalle.factura, self.factura)
        self.assertEqual(self.detalle.cantidad, 1)

    def test_detalle_producto_str(self):
        self.assertEqual(str(self.detalle), f"Detalle {self.detalle.id} - Producto: Laptop, Cantidad: 1")

class FacturaModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Ana", apellido="García", cedula="123456789", telefono="987654321")
        self.empleado = Empleado.objects.create(nombre="Juan", apellido="Pérez", telefono="123456789")
        self.factura = Factura.objects.create(cliente=self.cliente, empleado=self.empleado, total=2000.00)

    def test_factura_creation(self):
        self.assertEqual(self.factura.cliente, self.cliente)
        self.assertEqual(self.factura.empleado, self.empleado)
        self.assertEqual(self.factura.total, 2000.00)

    def test_factura_str(self):
        self.assertEqual(str(self.factura), f"Factura {self.factura.id} - Total: 2000.00")
