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

#Endpoint per obtenir el productes
@app.get("/product/")
def getProducts():
    return botiga_db.read()

#Endpoint obtenció de productes per id
@app.get("/product/{id}")
def read_product(id: int):
    return botiga_db.read_one(id)

#Endpoint per obtenir 
@app.get("/productAll/")
def read_productAll():
    return botiga_db.readAll()

#Endpoint que permet inserir un nou producte. el async permet que altres operacions treballin en paral·lel.
@app.post("/product/")
async def insert_product(data: product):
    name = data.name
    description = data.description
    company = data.company
    price = data.price
    units = data.units
    subcategory_id = data.subcategory_id
    created_at = data.created_at
    updated_at = data.updated_at
    ins_product = botiga_db.insert_product(name, description, company, price, units, subcategory_id,  created_at, updated_at)
    return {
        "S'ha afegit": "correctament!",
        "id_product": ins_product,
        "Producte": name
        }

#Endpoint que permet modificar el preu d'un producte.
@app.put("/product/producte/{id}")
def update_product(id:int, price:float):
    botiga_db.update_product(id, price)
    return { "S'ha afegit": "correctament!"}

#Endpoint que permet eliminar un producte pel seu id.
@app.delete("/product/{id}")
def delete_product(id:int):
    botiga_db.delete_product(id)
    return {
        "S'ha eliminat": "correctament!"
    }

#Endpoint amb el async() que crida al mètode insert.all de la clase botiga_db i permet inserir o modificar les dades d'un arxiu .csv a la base de dades botiga.
@app.post("/loadProducts")
async def insert_csv():
    inst_all = botiga_db.insert_all()
    return {
        "S'ha afegit": "correctament!"
    }
    