# Import necessary modules
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

@app.get("/")
async def read():
  
    return {"message": "This is Syed Bilal"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    """
    Retrieve an item by its ID with an optional query parameter.

    Args:
        item_id (int): The ID of the item (must be an integer).
        q (Union[str, None], optional): An optional query parameter.

    Returns:
        dict: A dictionary containing the item ID and query parameter.
    """
    return {"item_id": item_id, "query": q}

# Define a Pydantic model for request validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    Update an item by its ID with provided details.

    Args:
        item_id (int): The ID of the item to update.
        item (Item): The updated item data (validated by Pydantic).

    Returns:
        dict: A dictionary containing the updated item details.
    """
    return {"item_name": item.name, "item_id": item_id}
