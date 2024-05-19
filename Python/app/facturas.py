from flask import Blueprint, request, jsonify
from app import db
from app.models import Factura

facturas_bp = Blueprint('facturas', __name__)

@facturas_bp.route('/facturas', methods=['GET'])
def mostrar_facturas():
    facturas = Factura.query.all()
    return jsonify([factura.to_dict() for factura in facturas])

@facturas_bp.route('/facturas/<int:id>', methods=['GET'])
def obtener_factura(id):
    factura = Factura.query.get_or_404(id)
    return jsonify(factura.to_dict())

@facturas_bp.route('/facturas', methods=['POST'])
def crear_factura():
    data = request.json
    nueva_factura = Factura(
        id_cliente=data['id_cliente'],
        id_producto=data['id_producto'],
        id_empleado=data['id_empleado'],
        fecha=data['fecha'],
        total=data['total']
    )
    db.session.add(nueva_factura)
    db.session.commit()
    return jsonify({'mensaje': 'Factura creada exitosamente'}), 201

@facturas_bp.route('/facturas/<int:id>', methods=['PUT'])
def actualizar_factura(id):
    data = request.json
    factura = Factura.query.get_or_404(id)
    factura.id_cliente = data['id_cliente']
    factura.id_producto = data['id_producto']
    factura.id_empleado = data['id_empleado']
    factura.fecha = data['fecha']
    factura.total = data['total']
    db.session.commit()
    return jsonify({'mensaje': 'Factura actualizada exitosamente'})

@facturas_bp.route('/facturas/<int:id>', methods=['DELETE'])
def eliminar_factura(id):
    factura = Factura.query.get_or_404(id)
    db.session.delete(factura)
    db.session.commit()
    return jsonify({'mensaje': 'Factura eliminada exitosamente'})

