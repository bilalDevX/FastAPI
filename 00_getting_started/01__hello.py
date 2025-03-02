# Importing the FastAPI class from the fastapi module
from fastapi import FastAPI

# Creating an instance of the FastAPI class
app = FastAPI()

# Defining a route for the root URL ("/")
@app.get("/")
def read_root():
    # Returning a JSON response with a message
    return {"message": "Hello World"}