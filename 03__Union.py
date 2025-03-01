# The Union type from typing 
# is used to specify that a variable can accept multiple types.

from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# In this case, the q parameter can be either a str or None.

# """
# Why Union[str, None]?

# - The parameter q can either be:
# - A string (str) if the user provides a query parameter.
# - None if the query parameter is not provided

# """
# If you go to http://
# localhost:8000/items/5?q=somequery
# you will receive:
# {
#     "item_id": 5,
#     "q": "somequery"
# }
# If you go to http://localhost:8000/items/5
# you will receive:
# {
#     "item_id": 5,
#     "q": null
# }
# If you go to http://localhost:8000/items/5?q=
# you will receive:
# {
#     "item_id": 5,
#     "q": ""
# }
# If you go to http://localhost:8000/items/5?q
# you will receive:
# {
#     "item_id": 5,
#     "q": null
# }
