from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Numeros(BaseModel):
    valores: List[float]

@app.get("/sumar")
def sumar(a: int, b: int):
    return {"suma": a+b}

@app.post("/promedio")
def promedio(datos: Numeros):
    if not datos[0]:
        raise HTTPException(status_code=400, detail="Lista vacía")
    return {"promedio", (a+b)/len(datos)}

@app.get("/health")
def health():
    return {"status": "ok"}