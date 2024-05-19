from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from app.models import Usuario
from app import db, jwt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(username=data['username']).first()
    if usuario and check_password_hash(usuario.password, data['password']):
        access_token = create_access_token(identity=usuario.id)
        return jsonify(access_token=access_token)
    return jsonify({"mensaje": "Credenciales incorrectas"}), 401

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify(logged_in_as=current_user_id), 200
