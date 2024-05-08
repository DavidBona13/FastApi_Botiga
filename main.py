from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/product/")
def getProducts():
    return {"Hello": "World"}