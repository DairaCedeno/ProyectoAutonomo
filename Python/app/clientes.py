from flask import Blueprint, request, jsonify
from app import db
from app.models import Cliente

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes', methods=['GET'])
def mostrar_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes])

@clientes_bp.route('/clientes/<int:id>', methods=['GET'])
def obtener_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify(cliente.to_dict())

@clientes_bp.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.json
    nuevo_cliente = Cliente(
        nombre=data['nombre'],
        apellido=data['apellido'],
        cedula=data['cedula'],
        telefono=data['telefono']
    )
    db.session.add(nuevo_cliente)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente creado exitosamente'}), 201

@clientes_bp.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    data = request.json
    cliente = Cliente.query.get_or_404(id)
    cliente.nombre = data['nombre']
    cliente.apellido = data['apellido']
    cliente.cedula = data['cedula']
    cliente.telefono = data['telefono']
    db.session.commit()
    return jsonify({'mensaje': 'Cliente actualizado exitosamente'})

@clientes_bp.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente eliminado exitosamente'})
