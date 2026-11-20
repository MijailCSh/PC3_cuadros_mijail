from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sumar_integracion():
    respuesta = client.get("/sumar/1/2/")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"suma": a+b}

def test_promedio_lista_valida():
    respuesta = client.post("/promedio", [1, 2, 3])
    assert respuesta.status_code == 200
    assert respuesta.json() == {"promedio": 2}

def test_promedio_lista_vacia():
    respuesta = client.post("/promedio", [])
    assert respuesta.status_code == 400
    assert respuesta.json() == {"detail": "Lista vacía"}