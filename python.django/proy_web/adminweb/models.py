from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class DetalleProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    factura = models.ForeignKey('Factura', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Detalle {self.id} - Producto: {self.producto.nombre}, Cantidad: {self.cantidad}"

class Factura(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id} - Total: {self.total:.2f}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
