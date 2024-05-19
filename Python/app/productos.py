from flask import Blueprint, request, jsonify
from app import db
from app.models import Producto

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos', methods=['GET'])
def mostrar_productos():
    productos = Producto.query.all()
    return jsonify([producto.to_dict() for producto in productos])

@productos_bp.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = Producto.query.get_or_404(id)
    return jsonify(producto.to_dict())

@productos_bp.route('/productos', methods=['POST'])
def crear_producto():
    data = request.json
    nuevo_producto = Producto(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        precio=data['precio'],
        stock=data['stock'],
        categoria=data['categoria']
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto creado exitosamente'}), 201

@productos_bp.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.json
    producto = Producto.query.get_or_404(id)
    producto.nombre = data['nombre']
    producto.descripcion = data['descripcion']
    producto.precio = data['precio']
    producto.stock = data['stock']
    producto.categoria = data['categoria']
    db.session.commit()
    return jsonify({'mensaje': 'Producto actualizado exitosamente'})

@productos_bp.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto eliminado exitosamente'})
