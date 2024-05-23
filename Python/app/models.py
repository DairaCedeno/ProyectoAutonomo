from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class Empleado(db.Model):
    __tablename__ = 'empleados'
    id_empleado = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    telefono = db.Column(db.String(15))

    def to_dict(self):
        return {
            'id_empleado': self.id_empleado,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono
        }

# Define una clase Producto 
class Producto(db.Model):
    # Especifica el nombre de la tabla en la base de datos
    __tablename__ = 'productos'
    
    # Define las columnas de la tabla 'productos' con sus respectivos tipos de datos y restricciones
    id_producto = db.Column(db.Integer, primary_key=True)  
    nombre = db.Column(db.String(100))  
    descripcion = db.Column(db.Text) 
    precio = db.Column(db.Float)  
    stock = db.Column(db.Integer)  
    categoria = db.Column(db.String(100))  
    
    # Método para convertir un objeto Producto en un diccionario
    def to_dict(self):
        # Retorna un diccionario con los atributos del producto
        return {
            'id_producto': self.id_producto,  
            'nombre': self.nombre,  
            'descripcion': self.descripcion,  
            'precio': self.precio,  
            'stock': self.stock,  
            'categoria': self.categoria 
        }


class DetalleProducto(db.Model):
    __tablename__ = 'detalle_productos'
    id_detalle = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'))
    id_factura = db.Column(db.Integer, db.ForeignKey('facturas.id_factura'))
    cantidad = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id_detalle': self.id_detalle,
            'id_producto': self.id_producto,
            'id_factura': self.id_factura,
            'cantidad': self.cantidad
        }

class Factura(db.Model):
    __tablename__ = 'facturas'
    id_factura = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'))
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id_empleado'))
    fecha = db.Column(db.Date)
    total = db.Column(db.Float)

    def to_dict(self):
        return {
            'id_factura': self.id_factura,
            'id_cliente': self.id_cliente,
            'id_producto': self.id_producto,
            'id_empleado': self.id_empleado,
            'fecha': self.fecha,
            'total': self.total
        }

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    cedula = db.Column(db.String(20))
    telefono = db.Column(db.String(15))

    def to_dict(self):
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'cedula': self.cedula,
            'telefono': self.telefono
        }
    
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

    # Un diccionario en Python es una estructura de datos que 
    # permite almacenar pares de "llaves" y "valores". 
    # Cada "llave" en un diccionario debe ser única y está asociada 
    # a un "valor". Los diccionarios son extremadamente flexibles 
    # y útiles para organizar y manipular datos de forma eficiente.

