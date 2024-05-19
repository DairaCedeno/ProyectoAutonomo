import pytest
from app import app, db
from app.models import Producto

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_mostrar_productos(client):
    # Crear algunos productos de prueba en la base de datos
    producto1 = Producto(nombre='Producto 1', descripcion='Descripción del producto 1', precio=10.0, stock=100, categoria='Categoría 1')
    producto2 = Producto(nombre='Producto 2', descripcion='Descripción del producto 2', precio=20.0, stock=200, categoria='Categoría 2')
    db.session.add_all([producto1, producto2])
    db.session.commit()

    # Realizar una solicitud GET a la ruta '/productos'
    rv = client.get('/productos')

    # Verificar que la respuesta sea exitosa (código de estado 200)
    assert rv.status_code == 200

    # Verificar que la respuesta sea en formato JSON
    assert rv.is_json

    # Verificar que la respuesta contenga los productos creados
    json_data = rv.get_json()
    assert len(json_data) == 2
    assert json_data[0]['nombre'] == 'Producto 1'
    assert json_data[1]['nombre'] == 'Producto 2'

def test_crear_producto(client):
    # Realizar una solicitud POST para crear un nuevo producto
    rv = client.post('/productos', json={
        'nombre': 'Producto Test',
        'descripcion': 'Descripción del producto test',
        'precio': 9.99,
        'stock': 100,
        'categoria': 'Test'
    })

    # Verificar que la respuesta sea exitosa (código de estado 201)
    assert rv.status_code == 201

    # Verificar el mensaje de respuesta
    json_data = rv.get_json()
    assert json_data['mensaje'] == 'Producto creado exitosamente'

