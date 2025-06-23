from fastapi.testclient import TestClient
from ..api.api_python import app  

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "¡Bienvenido a mi pequeña API de prueba!"}

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1

def test_read_item_found():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_read_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404  # ⚠️ debería ser 404 pero el código actual retorna 200
    assert response.json()["detail"] == "Item not found"

def test_create_item():
    new_item = {
        "id": 4,
        "name": "Queso",
        "description": "Queso manchego",
        "price": 3.5,
        "tax": 0.15
    }
    response = client.post("/items/", json=new_item)
    assert response.status_code == 200
    assert response.json()["name"] == "Queso"

def test_calculate_total():
    response = client.get("/calculate_total/1")
    assert response.status_code == 200
    total = response.json()["total_price"]
    assert isinstance(total, float)
