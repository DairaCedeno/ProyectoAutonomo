import pytest
from app import app, db
from app.models import Factura

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_mostrar_facturas(client):
    # Crear algunas facturas de prueba en la base de datos
    factura1 = Factura(id_cliente=1, id_producto=1, id_empleado=1, fecha='2024-05-18', total=100.0)
    factura2 = Factura(id_cliente=2, id_producto=2, id_empleado=2, fecha='2024-05-18', total=200.0)
    db.session.add_all([factura1, factura2])
    db.session.commit()

    # Realizar una solicitud GET a la ruta '/facturas'
    rv = client.get('/facturas')

    # Verificar que la respuesta sea exitosa (código de estado 200)
    assert rv.status_code == 200

    # Verificar que la respuesta sea en formato JSON
    assert rv.is_json

    # Verificar que la respuesta contenga las facturas creadas
    json_data = rv.get_json()
    assert len(json_data) == 2
    assert json_data[0]['total'] == 100.0
    assert json_data[1]['total'] == 200.0

def test_crear_factura(client):
    # Realizar una solicitud POST para crear una nueva factura
    rv = client.post('/facturas', json={
        'id_cliente': 1,
        'id_producto': 1,
        'id_empleado': 1,
        'fecha': '2024-05-18',
        'total': 300.0
    })

    # Verificar que la respuesta sea exitosa (código de estado 201)
    assert rv.status_code == 201

    # Verificar el mensaje de respuesta
    json_data = rv.get_json()
    assert json_data['mensaje'] == 'Factura creada exitosamente'
