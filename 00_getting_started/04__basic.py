from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read():
    return {"message": "this is syed bilal"}

@app.get("/items/{item_id}")
def read_item(item_id: int , q: Union[str, None] = None):
    return {"item_id of product is": item_id, "q is equal to ": q}


class Item(BaseModel):
    name: str
    price : float
    is_offer : Union[bool, None] = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}