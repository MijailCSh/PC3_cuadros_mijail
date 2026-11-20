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
    if len(datos) == 0:
        raise HTTPException(status_code=400, detail="Lista vacía")
    c = 0
    for i in datos:
        c = c + i
    c = c/len(datos)
    return {"promedio": c}

@app.get("/health")
def health():
    return {"status": "ok"}