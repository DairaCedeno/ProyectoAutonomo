import unittest
from app import app, db
from app.models import Usuario

class TestAuth(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()

        # Crear la base de datos en memoria y agregar un usuario de prueba
        with app.app_context():
            db.create_all()
            usuario = Usuario(username='usuario_prueba', password='contraseña_prueba')
            db.session.add(usuario)
            db.session.commit()

    def tearDown(self):
        # Limpiar la base de datos después de cada prueba
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_autenticacion_credenciales_validas(self):
        # Datos de prueba para la solicitud POST de autenticación
        datos_autenticacion = {'username': 'usuario_prueba', 'password': 'contraseña_prueba'}

        # Realizar la solicitud POST de autenticación
        respuesta = self.app.post('/login', json=datos_autenticacion)

        # Verificar que la solicitud fue exitosa (código de estado 200)
        self.assertEqual(respuesta.status_code, 200)

        # Verificar que se devolvió un token de acceso en la respuesta
        self.assertIn('access_token', respuesta.json)

    def test_autenticacion_credenciales_incorrectas(self):
        # Datos de prueba con credenciales incorrectas
        datos_autenticacion = {'username': 'usuario_invalido', 'password': 'contraseña_invalida'}

        # Realizar la solicitud POST de autenticación
        respuesta = self.app.post('/login', json=datos_autenticacion)

        # Verificar que la solicitud fue rechazada (código de estado 401)
        self.assertEqual(respuesta.status_code, 401)

        # Verificar que se devolvió un mensaje de error en la respuesta
        self.assertEqual(respuesta.json['mensaje'], 'Credenciales incorrectas')

if __name__ == '__main__':
    unittest.main()

