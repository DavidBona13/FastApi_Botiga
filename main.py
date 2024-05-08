from typing import Union
from fastapi import FastAPI
import botiga_db

from typing import List
from datetime import datetime

from pydantic import BaseModel

app = FastAPI()

class product(BaseModel):
    name: str
    description: str
    company:  str
    price: float
    units: int
    subcategory_id: int
    created_at: datetime
    updated_at: datetime

@app.get("/product/")
def getProducts():
    return botiga_db.read()

@app.get("/product/{id}")
def read_product(id: int):
    return botiga_db.read_one()

@app.get("/productAll/")
def read_productAll():
    return {}

@app.post("/product/")
def insert_product(data: product):
    return {}

@app.put("/product/producte/{id}")
def update_product(criteri):
    #pelis_db.update_vots(id, criteri)
    return {}

@app.delete("/product/{id}")
def delete_product(id:int):
    pelis_db.delete_peli(id)
    return {
        "msg": "data eliminated!!"
    }