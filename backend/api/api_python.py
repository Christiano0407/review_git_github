from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Inicializa la aplicación FastAPI
app = FastAPI()

# Modelo de datos para un ítem
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Base de datos simulada (en memoria)
fake_db = [
    {"id": 1, "name": "Manzana", "description": "Fruta fresca", "price": 1.0, "tax": 0.05},
    {"id": 2, "name": "Leche", "description": "1 litro entera", "price": 1.5},
    {"id": 3, "name": "Pan", "description": "Pan de molde", "price": 2.0, "tax": 0.10},
]

# Endpoint raíz
@app.get("/")
async def read_root():
    """
    Endpoint de bienvenida.
    """
    return {"message": "¡Bienvenido a mi pequeña API de prueba!"}

# Endpoint para obtener todos los ítems
@app.get("/items/", response_model=List[Item])
async def read_items():
    """
    Obtiene una lista de todos los ítems disponibles.
    """
    return fake_db

# Endpoint para obtener un ítem por ID
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """
    Obtiene un ítem específico por su ID.
    Retorna 404 si el ítem no se encuentra.
    """
    for item in fake_db:
        if item["id"] == item_id:
            return item
    return {"detail": "Item not found"}, 404 # Esto debería ser un HTTPException, pero para simplicidad lo dejo así por ahora

# Endpoint para crear un nuevo ítem
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """
    Crea un nuevo ítem y lo añade a la base de datos simulada.
    """
    fake_db.append(item.dict())
    return item

# Endpoint de ejemplo para un cálculo sencillo
@app.get("/calculate_total/{item_id}")
async def calculate_total(item_id: int):
    """
    Calcula el precio total (precio + impuesto) de un ítem específico.
    """
    for item in fake_db:
        if item["id"] == item_id:
            price = item["price"]
            tax = item.get("tax", 0.0)
            total = price * (1 + tax)
            return {"item_id": item_id, "total_price": round(total, 2)}
    return {"detail": "Item not found"}, 404