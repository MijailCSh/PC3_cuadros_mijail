from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sumar_integracion():
    respuesta = client.get("/sumar/1/2/")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"suma": a+b}

def test_promedio_lista_valida():
    pass
def test_promedio_lista_vacia():
    pass