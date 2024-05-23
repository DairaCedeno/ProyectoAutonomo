from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from app.models import Usuario

# Crea un objeto Blueprint llamado 'auth_bp' para agrupar las rutas relacionadas con la autenticación
auth_bp = Blueprint('auth', __name__)

# Define una ruta para el proceso de inicio de sesión
@auth_bp.route('/login', methods=['POST'])
def login():
    # Obtiene los datos en formato JSON
    data = request.json
    
    # Busca un usuario en la base de datos por su nombre de usuario
    usuario = Usuario.query.filter_by(username=data['username']).first()
    
    # Verifica si el usuario existe y si la contraseña es valida
    if usuario and check_password_hash(usuario.password, data['password']):

        # Se genera un token de acceso JWT
        access_token = create_access_token(identity=usuario.id)

        # Devuelve el token de acceso como respuesta
        return jsonify(access_token=access_token)
    
    # Si las credenciales son incorrectas, devuelve un mensaje de error 
    return jsonify({"mensaje": "Credenciales incorrectas"}), 401



# Define una ruta protegida que requiere un token de acceso JWT válido para acceder
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Obtiene la identidad del usuario del token de acceso JWT
    current_user_id = get_jwt_identity()
    # Devuelve la identidad del usuario como respuesta
    return jsonify(logged_in_as=current_user_id), 200
