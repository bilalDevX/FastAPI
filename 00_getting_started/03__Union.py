"""
 The Union type from typing 
 is used to specify that a variable can accept multiple types.
"""

# Import necessary modules
from fastapi import FastAPI
from typing import Union

# Create an instance of the FastAPI class
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    """
    Retrieve an item by its ID with an optional query parameter.

    Args:
        item_id (int): The ID of the item (must be an integer).
        q (Union[str, None], optional): An optional query parameter 
                                        that can be a string or None.

    Returns:
        dict: A dictionary containing the item ID and query parameter.
    """
    return {"item_id": item_id, "q": q}

"""
Explanation:

- `item_id` is a required path parameter and must be an integer.
- `q` is an optional query parameter that can either be:
  - A string (`str`) if provided.
  - `None` if not provided.

Example Requests and Responses:

1️⃣ Request:  GET http://localhost:8000/items/5?q=somequery
   Response:  {"item_id": 5, "q": "somequery"}

2️⃣ Request:  GET http://localhost:8000/items/5
   Response:  {"item_id": 5, "q": null}

3️⃣ Request:  GET http://localhost:8000/items/5?q=
   Response:  {"item_id": 5, "q": ""}

4️⃣ Request:  GET http://localhost:8000/items/5?q
   Response:  {"item_id": 5, "q": null}
"""
