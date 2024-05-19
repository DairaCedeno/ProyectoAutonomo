import pytest
from app import app, db
from app.models import Cliente

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_mostrar_clientes(client):
    # Crear algunos clientes de prueba en la base de datos
    cliente1 = Cliente(nombre='Cliente 1', apellido='Apellido 1', cedula='123456789', telefono='1234567890')
    cliente2 = Cliente(nombre='Cliente 2', apellido='Apellido 2', cedula='987654321', telefono='9876543210')
    db.session.add_all([cliente1, cliente2])
    db.session.commit()

    # Realizar una solicitud GET a la ruta '/clientes'
    rv = client.get('/clientes')

    # Verificar que la respuesta sea exitosa (código de estado 200)
    assert rv.status_code == 200

    # Verificar que la respuesta sea en formato JSON
    assert rv.is_json

    # Verificar que la respuesta contenga los clientes creados
    json_data = rv.get_json()
    assert len(json_data) == 2
    assert json_data[0]['nombre'] == 'Cliente 1'
    assert json_data[1]['nombre'] == 'Cliente 2'

def test_crear_cliente(client):
    # Realizar una solicitud POST para crear un nuevo cliente
    rv = client.post('/clientes', json={
        'nombre': 'Cliente Test',
        'apellido': 'Apellido Test',
        'cedula': '999999999',
        'telefono': '9999999999'
    })

    # Verificar que la respuesta sea exitosa (código de estado 201)
    assert rv.status_code == 201

    # Verificar el mensaje de respuesta
    json_data = rv.get_json()
    assert json_data['mensaje'] == 'Cliente creado exitosamente'

